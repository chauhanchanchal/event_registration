from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import mysql.connector

# Initialize app
app = Flask(__name__)
CORS(app)

# ================= DATABASE CONFIG =================

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Chanchal55Pass.',  
    'database': 'event_db'
}

# ================= HOME ROUTE =================

@app.route('/')
def home():
    return render_template('index.html')

# ================= REGISTER API =================

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    full_name = data.get('full_name')
    email = data.get('email')
    event_name = data.get('event_name')

    if not full_name or not email or not event_name:
        return jsonify({'message': 'All fields are required'}), 400

    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Check duplicate
        cursor.execute(
            "SELECT * FROM registrations WHERE email=%s AND event_name=%s",
            (email, event_name)
        )

        if cursor.fetchone():
            return jsonify({'message': 'Already registered for this event!'}), 409

        # Insert data
        cursor.execute(
            "INSERT INTO registrations (full_name, email, event_name) VALUES (%s, %s, %s)",
            (full_name, email, event_name)
        )

        conn.commit()

        return jsonify({'message': 'Registration successful!'}), 200

    except Exception as e:
        print("Error:", e)
        return jsonify({'message': 'Database error'}), 500

    finally:
        try:
            cursor.close()
            conn.close()
        except:
            pass

# ================= ADMIN DATA =================

@app.route('/api/registrations', methods=['GET'])
def get_data():
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT * FROM registrations ORDER BY registered_at DESC")
        rows = cursor.fetchall()

        return jsonify(rows), 200

    except Exception as e:
        print("Error:", e)
        return jsonify({'message': 'Database error'}), 500

    finally:
        try:
            cursor.close()
            conn.close()
        except:
            pass

# ================= RUN APP =================

if __name__ == '__main__':
    app.run(debug=True)