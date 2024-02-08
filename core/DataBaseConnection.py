import psycopg2
from sshtunnel import SSHTunnelForwarder

from core import Logger, config


def create_ssh_tunnel(db_config_file_name: str):
    ssh = config.get_ssh_configs(db_config_file_name)
    remote_bind_address = config.get_remote_bind_address(db_config_file_name)
    local_bind_address = config.get_local_bind_address(db_config_file_name)

    try:
        ssh_tunnel = SSHTunnelForwarder(
            ssh_address_or_host=(ssh['ssh_host'], int(ssh['ssh_port'])),
            ssh_username=ssh['ssh_username'],
            ssh_password=ssh['ssh_password'],
            remote_bind_address=(remote_bind_address['remote_bind_host'], int(remote_bind_address['remote_bind_port'])),
            local_bind_address=(local_bind_address['local_bind_host'], int(local_bind_address['local_bind_port']))
        )
        Logger.info("SSH Tunnel is - CREATED")
        return ssh_tunnel
    except Exception as e:
        Logger.db_error("SSH Tunnel Server", e)
        return None


def create_connection(ssh_tunnel: SSHTunnelForwarder, db_config_file_name: str, schema_name: str):
    data_base = config.get_data_base_config(db_config_file_name)
    schema = config.get_schema(db_config_file_name, schema_name)
    try:
        ssh_tunnel.start()
        connection = psycopg2.connect(
            database=data_base['database_name'],
            user=data_base['user'],
            password=data_base['password'],
            host=data_base['host'],
            port=ssh_tunnel.local_bind_port,
            options=f'-c search_path={schema}'
        )
        Logger.info("Connection is - CREATED")
        return connection
    except Exception as e:
        Logger.db_error("Connection to DataBase", e)


def select(connection, query: str):
    cursor = connection.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    return rows


def close(connection, ssh_tunnel):
    connection.close()
    ssh_tunnel.stop()


def debug_query_print_all(rows):
    """
    To print all data from query result
    Query example: SELECT column_1, column_2, column_3 FROM table_name limit 5;
    Select query returns data from DB in tuple style:
    Example output:
    (Decimal('6831071406'), Decimal('25552023'), 'REAL_SALE')
    (Decimal('6831176026'), Decimal('25554642'), 'DEACTIVATION_BILLING')
    (Decimal('6831217866'), Decimal('25615022'), 'REAL_SALE')
    (Decimal('6831228546'), Decimal('25619242'), 'REAL_SALE')
    (Decimal('6831238266'), Decimal('25615162'), 'REAL_SALE')
    :param rows: all data returned from executed query
    """
    print("\nAll rows: ")
    for row in rows:
        print(row)


def debug_query_print_by_column_index(rows, column_index: int):
    """
    To print column data by index

    Example output: column_index = 0
    (Decimal('6831071406')
    (Decimal('6831176026')
    (Decimal('6831217866')
    (Decimal('6831228546')
    (Decimal('6831238266')

    :param rows: all data from executed query
    :param column_index: index of column you want to print
    :return:
    """
    print(f"\nColumn {column_index}: ")
    for row in rows:
        print(row[column_index])


def debug_query_print_by_column_index_by_data_index(rows, column_index, row_index):
    """
    To print one value

    Example output: column_index = 0, data_index = 0
    6831071406

    :param rows: all data from executed query
    :param column_index: index of column you want to print
    :param row_index: index of data from column you want to print
    :return:
    """
    print(f"\nColumn {column_index}, Row {row_index}: ")
    data = []
    for row in rows:
        data.append(row[column_index])
    print(data[row_index])
