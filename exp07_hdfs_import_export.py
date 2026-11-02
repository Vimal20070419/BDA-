"""
EXP 07 (b) - HDFS import/export using the hdfs library
Install:  pip install hdfs
Needs HDFS running (WebHDFS on port 50070 for Hadoop 2.x, 9870 for Hadoop 3.x).
"""
from hdfs import InsecureClient

# Connect to HDFS
hdfs_client = InsecureClient('http://localhost:50070', user='your_username')

# Upload a file to HDFS
hdfs_client.upload('/user/your_username/data', 'local_file.txt')

# Download a file from HDFS
hdfs_client.download('/user/your_username/data/local_file.txt', 'downloaded_file.txt')

# List files in a directory on HDFS
files = hdfs_client.list('/user/your_username/data')
print(files)
