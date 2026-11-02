"""
EXP 07 (c) - Hive create/insert/query using PyHive
Install:  pip install pyhive
Needs HiveServer2 running on localhost:10000.
"""
from pyhive import hive

# Connect to Hive
conn = hive.connect(host='localhost', port=10000, auth='NONE', database='default')

# Create a table in Hive
with conn.cursor() as cursor:
    cursor.execute("CREATE TABLE IF NOT EXISTS test_table (id INT, name STRING, age INT)")

# Insert data into the table
with conn.cursor() as cursor:
    cursor.execute("INSERT INTO test_table VALUES (1, 'John Doe', 30)")
    cursor.execute("INSERT INTO test_table VALUES (2, 'Jane Smith', 25)")

# Query data from the table
with conn.cursor() as cursor:
    cursor.execute("SELECT * FROM test_table")
    results = cursor.fetchall()
    for row in results:
        print(row)

# Close the connection
conn.close()
