"""
EXP 07 (a) - Cassandra import/export using cassandra-driver
Install:  pip install cassandra-driver
Needs a running Cassandra server on localhost.
"""
from cassandra.cluster import Cluster

# Connect to Cassandra cluster
cluster = Cluster(['localhost'])
session = cluster.connect()

# Create a keyspace and table
session.execute("CREATE KEYSPACE IF NOT EXISTS test WITH REPLICATION = "
                "{'class': 'SimpleStrategy', 'replication_factor': 1}")
session.execute("CREATE TABLE IF NOT EXISTS test.users (id UUID PRIMARY KEY, name TEXT, age INT)")

# Insert data into the table
session.execute("INSERT INTO test.users (id, name, age) VALUES (uuid(), 'John Doe', 30)")
session.execute("INSERT INTO test.users (id, name, age) VALUES (uuid(), 'Jane Smith', 25)")

# Query data from the table
rows = session.execute("SELECT * FROM test.users")
for row in rows:
    print(row.id, row.name, row.age)

# Close the connection
session.shutdown()
cluster.shutdown()
