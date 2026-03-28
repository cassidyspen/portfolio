import os
import psycopg
from psycopg.rows import dict_row

_conn: psycopg.Connection | None = None


def get_connection() -> psycopg.Connection:
    global _conn
    if _conn is None or _conn.closed:
        url = os.environ.get("DATABASE_URL")
        if not url:
            raise RuntimeError("DATABASE_URL environment variable not set")
        _conn = psycopg.connect(url, row_factory=dict_row, sslmode="require")
    return _conn
