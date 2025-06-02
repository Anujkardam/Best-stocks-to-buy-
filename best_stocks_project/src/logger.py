import logging
import yaml

def setup_logger(name, config_path="config/logging.yaml"):
    with open(config_path, 'r') as f:
        config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)
    return logging.getLogger(name)
