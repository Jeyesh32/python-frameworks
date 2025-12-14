import traceback

from flask import Flask, request, jsonify
from .base import WebFrameworkWrapper
from ..observability.factory import get_logger, get_tracer, get_metrics
from ..utils.string_utils import to_snake_case

class FlaskWrapper(WebFrameworkWrapper):

    def __init__(self, app: Flask, service: str):
        self.app = app
        self.logger = get_logger.get()
        # self.tracer = get_tracer()
        # self.metrics = get_metrics()
        self.service = service

    def initialize(self):
        self.register_middlewares()
        self.register_error_handlers()
        self.logger.info("FlaskWrapper initialized")

    # --------------------------
    # Middleware: Before Request
    # --------------------------
    def register_middlewares(self):

        @self.app.route(f"/{to_snake_case(self.service)}/health_check")
        def health_check():
            return "I'm Healthy"

        @self.app.before_request
        def before():
            self.logger.info(f"Incoming request: {request.path}")
            # span = self.tracer.start_span(request.path)
            # request._span = span  # attach to flask request context

        @self.app.after_request
        def after(response):
            self.logger.info(f"Response status: {response.status_code}")
            # self.metrics.record("request.count", 1)
            return response

    # -----------------------
    # Global Error Handling
    # -----------------------
    def register_error_handlers(self):
        @self.app.errorhandler(Exception)
        def handle_exception(e):
            self.logger.error(
                f"""Unhandled error: {type(e).__name__}: {e} "path": {request.path}, "method": {request.method}, "ip": {request.remote_addr}""")

            status_code = getattr(e, 'code', 500)

            # Generic message for production
            return jsonify({
                "error": {
                    "message": traceback.format_exception_only(type(e), e),
                    "type": type(e).__name__,
                    "status_code": status_code
                }
            }), status_code
