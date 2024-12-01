from collections import ChainMap

default_connection = {"host": "localhost", "port": 4567}
connection = {"port": 5678}
conn = ChainMap(connection, default_connection)
print(conn)  # ChainMap({'port': 5678}, {'host': 'localhost', 'port': 4567})
print(conn["port"])  # 5678
print(conn["host"])  # localhost
print(conn.maps)  # [{'port': 5678}, {'host': 'localhost', 'port': 4567}]
conn["host"] = "packtpub.com"
print(
    conn.maps
)  # [{'port': 5678, 'host': 'packtpub.com'}, {'host': 'localhost', 'port': 4567}]
del conn["port"]
print(conn.maps)
print(conn["port"])
