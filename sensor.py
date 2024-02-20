from datetime import datetime
import random
import time
import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='fertiliser'
)

cursor = conn.cursor()

while True:
    for sensor_id in range(1, 4):  # Iterate through sensors 1 to 3
        # Generate a random number from 1 to 10
        measurement_value = random.randint(1, 100)

        # Create a tuple to insert into the table
        data = (datetime.now(), sensor_id, measurement_value)  # Update process ID

        # Insert the data into the table
        insert_query = """
        INSERT INTO sensor_data (timestamp, sensor_id, measurement_value) 
        VALUES (%s, %s, %s)
        """
        cursor.execute(insert_query, data)
        conn.commit()

        print("Sensor data stored successfully in the database:")
        print("Timestamp:", data[0])
        print("Sensor ID:", data[1])
        print("Measurement Value:", data[2])
        print()

    # Wait for one second before generating the next data value
    time.sleep(1)

# Close connection
cursor.close()
conn.close()
