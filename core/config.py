import os
from configparser import ConfigParser

from dotenv import load_dotenv


def get_config(key: str) -> str:
    load_dotenv()
    return os.getenv(key)


def get_url():
    return get_config("URL")


def get_yop_mail_url():
    return get_config("YOP_MAIL_URL")


def get_db_config_file_name():
    return get_config("DATABASE_CONFIG")


def get_db_config(db_config_file_name: str, section: str) -> dict[str, str]:
    parser = ConfigParser()
    parser.read(db_config_file_name)
    configs = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            configs[param[0]] = param[1]
    else:
        raise Exception(f"Section {section} is not found in the {db_config_file_name}.")
    return configs


def get_ssh_configs(db_config_file_name: str):
    return get_db_config(db_config_file_name, get_config("SSH_SECTION"))


def get_remote_bind_address(db_config_file_name: str):
    return get_db_config(db_config_file_name, get_config("REMOTE_BIND_ADDRESS_SECTION"))


def get_local_bind_address(db_config_file_name: str):
    return get_db_config(db_config_file_name, get_config("LOCAL_BIND_ADDRESS_SECTION"))


def get_data_base_config(db_config_file_name: str):
    return get_db_config(db_config_file_name, get_config("DATA_BASE_SECTION"))


def get_schemas(db_config_file_name: str):
    return get_db_config(db_config_file_name, get_config("SCHEMA_SECTION"))


def get_schema(db_config_file_name: str, schema_name: str):
    schemas = get_schemas(db_config_file_name)
    return schemas[schema_name]
