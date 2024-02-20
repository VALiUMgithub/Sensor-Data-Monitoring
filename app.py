from flask import Flask, jsonify, render_template,request
import mysql.connector
from datetime import datetime

app = Flask(__name__)




@app.route('/index')
def index():
     # Connect to the database
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='fertiliser'
    )
    cursor = conn.cursor()
   
    # Fetch data from the database
    cursor.execute("SELECT * FROM sensor_data WHERE sensor_id=1 ORDER BY process_id DESC LIMIT 15")
    data = cursor.fetchall()

    # Convert data to a list of dictionaries
    data_list = []
    for row in data:
        data_list.append({'process_id': row[0], 'sensor_id': row[1], 'measurement_value': row[2], 'timestamp': row[3]})
    cursor.close()
    conn.close()
    
    # Return the data as JSON
    return jsonify(data_list)
    #return render_template('index.html')

@app.route('/index_tabledata')
def index_tabledata():
     # Connect to the database
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='fertiliser'
    )
    cursor = conn.cursor()

    # Fetch data from the database
    cursor.execute("SELECT * FROM sensor_data ORDER BY process_id DESC LIMIT 10")
    data = cursor.fetchall()

    # Convert data to a list of dictionaries
    data_list = []
    for row in data:
        data_list.append({'process_id': row[0], 'sensor_id': row[1], 'measurement_value': row[2], 'timestamp': row[3]})
    cursor.close()
    conn.close()
    
    # Return the data as JSON
    return jsonify(data_list)
    #return render_template('index.html')

@app.route('/previous-index')
def previous_index():
    start = request.args.get('start_timestamp')
    start_timestamp = datetime.strptime(start, '%Y-%m-%dT%H:%M')
    end = request.args.get('end_timestamp')
    end_timestamp = datetime.strptime(end, '%Y-%m-%dT%H:%M')

    try:
        # Connect to the database
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='fertiliser'
        )
        cursor = conn.cursor()

        # Fetch data from the database
        query = "SELECT * FROM sensor_data WHERE timestamp BETWEEN %s AND %s ORDER BY process_id DESC"
        cursor.execute(query, (start_timestamp, end_timestamp))
        data = cursor.fetchall()

        # Convert data to a list of dictionaries
        data_list = []
        for row in data:
            data_list.append({'process_id': row[0], 'sensor_id': row[1], 'measurement_value': row[2], 'timestamp': row[3]})

        cursor.close()
        conn.close()

        # Return the data as JSON
        return jsonify(data_list)

    except Exception as e:
        print("Error:", e)
        return jsonify({'error': str(e)}), 500


@app.route('/')
def index1():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
