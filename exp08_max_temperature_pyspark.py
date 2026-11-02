"""
EXP 08 - Maximum temperature per weather station using Apache Spark (PySpark)
Install:  pip install pyspark
Input  :  temperature.txt  (StationID,Date,Temperature)
"""
from pyspark import SparkContext

# Create Spark Context
sc = SparkContext("local", "Maximum Temperature")

# Load input file
lines = sc.textFile("temperature.txt")

# Create (StationID, Temperature) pairs
temperature = lines.map(lambda x: x.split(",")) \
                   .map(lambda x: (x[0], int(x[2])))

# Find maximum temperature
maxTemp = temperature.reduceByKey(lambda x, y: max(x, y))

# Display output
print("Maximum Temperature of Each Station")
for station, temp in sorted(maxTemp.collect()):
    print(station, ":", temp, "°C")

# Stop Spark
sc.stop()
