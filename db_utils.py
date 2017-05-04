from sqlalchemy import create_engine


def get_engine(db_name="eq_stress_test.db", username=None, pswd=None, port=None,
               db_type="sqlite", hostname="localhost"):
    """
    
    :param db_name: Database name to be used default: eq_stress_test.db for a sqlite3 db 
    :param username: Username (str)
    :param pswd: Password (str)
    :param port: Port (int) 
    :param db_type: Database server type
    :param hostname: Servername
    :return: SQLAlchemy DB Engine
    :raise NameError: when db_type or db_name is None
    """
    conn_str = "<db_type>://<username>:<pswd>@<hostname>:<port>/<db_name>"

    if (username is None and port is None):
        conn_str = "<db_type>://<hostname>:<port>/<db_name>"

    if port is None:
        conn_str = "<db_type>://<hostname>/<db_name>"
    else:
        conn_str = conn_str.replace("<port>", port)

    if hostname is None:
        conn_str = conn_str.replace("<hostname>","")
    elif hostname == "localhost" and db_type == "sqlite":
        conn_str = conn_str.replace("<hostname>", "")
    else:
        conn_str = conn_str.replace("<hostname>", hostname)

    if db_type is None:
        raise NameError("db_type cannot be None")
    else:
        conn_str = conn_str.replace("<db_type>", db_type)

    if db_name is None:
        raise NameError("db_name cannot be None")
    else:
        conn_str = conn_str.replace("<db_name>", db_name)

    return create_engine(conn_str)