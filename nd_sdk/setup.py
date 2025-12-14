from setuptools import setup, find_packages

setup(
    name="nd-sdk",
    version="1.1.13",
    description="Unified SDK for Observability, Caching and Storage",
    author="Jeyesh Vishnu",
    author_email="jeyesh.vishnu@novacisdigital.com",
    python_requires=">=3.8",
    packages=find_packages(where=".", include=["nd_sdk*"]),
    install_requires=[
        "azure-storage-blob~=12.16.0",
        "azure-core~=1.29.5",
        "Flask~=2.1.2",
        "redis~=6.1.1",
        "Werkzeug~=2.2.2",
        "opentelemetry-api>=1.20.0",
        "opentelemetry-sdk>=1.20.0",
        "opentelemetry-exporter-otlp-proto-http>=1.20.0",
        "aiohttp>=3.8.0"
    ],
)