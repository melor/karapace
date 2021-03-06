"""
karapace - configuration validation

Copyright (c) 2019 Aiven Ltd
See LICENSE for details
"""
import socket


def set_config_defaults(config):
    config.setdefault("advertised_hostname", socket.gethostname())
    config.setdefault("bootstrap_uri", "127.0.0.1:9092")
    config.setdefault("client_id", "sr-1")
    config.setdefault("compatibility", "BACKWARD")
    config.setdefault("group_id", "schema-registry")
    config.setdefault("host", "127.0.0.1")
    config.setdefault("log_level", "DEBUG")
    config.setdefault("port", 8081)
    config.setdefault("master_eligibility", True)
    config.setdefault("replication_factor", 1)
    config.setdefault("security_protocol", "PLAINTEXT")
    config.setdefault("ssl_cafile", None)
    config.setdefault("ssl_certfile", None)
    config.setdefault("ssl_keyfile", None)
    config.setdefault("topic_name", "_schemas")
    return config
