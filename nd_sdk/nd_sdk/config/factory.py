from ..utils.singleton import singleton
from ..config.data_config import ServiceConfig

@singleton
def get_config(config_data, provider="service"):
    if provider == "service":
        return ServiceConfig(**config_data)
    return None