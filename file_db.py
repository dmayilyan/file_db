from utils import load_sql_script, get_cursor
from datetime import datetime
from time import time

DB_NAME = "file.db"


def main():
    table_create = load_sql_script("./sql/create_table.sql")
    insert_query = load_sql_script("./sql/insert.sql")

    cur = get_cursor(DB_NAME)
    cur.executescript(table_create)
    cam_name = "cam32"
    timestamp = int(time())  # adapt
    cur.execute(insert_query, (f"./wrwer/{cam_name}", cam_name, timestamp))


if __name__ == "__main__":
    main()
