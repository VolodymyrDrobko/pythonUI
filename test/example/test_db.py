import pytest

from core import DataBaseConnection, config


@pytest.mark.db
def test_db():
    DB_CONFIG = config.get_db_config_file_name()
    query = "SELECT cust_ord_id, cust_id, extra_field1 FROM cust_ord limit 5;"
    ssh_tunnel = DataBaseConnection.create_ssh_tunnel(DB_CONFIG)
    db_connection = DataBaseConnection.create_connection(ssh_tunnel, DB_CONFIG, "schema_name")
    rows = DataBaseConnection.select(db_connection, query)
    DataBaseConnection.debug_query_print_all(rows)
    DataBaseConnection.debug_query_print_by_column_index(rows, 0)
    DataBaseConnection.debug_query_print_by_column_index_by_data_index(rows, 0, 0)
    DataBaseConnection.close(db_connection, ssh_tunnel)
