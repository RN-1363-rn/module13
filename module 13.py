# from flask import Flask, jsonify
#
# app = Flask(__name__)
#
# # Function to check if a number is prime
# def is_prime(n):
#     if n <= 1:
#         return False
#     if n == 2:
#         return True
#     if n % 2 == 0:
#         return False
#     for i in range(3, int(n**0.5) + 1, 2):
#         if n % i == 0:
#             return False
#     return True
#
#
# @app.route('/')
# def home():
#     return "Welcome! Use /prime_number/<number> to check primes."
#
# # Route to check prime number
# @app.route('/prime_number/<int:number>', methods=['GET'])
# def check_prime(number):
#     result = {
#         "Number": number,
#         "isPrime": is_prime(number)
#     }
#     return jsonify(result)
#
#
# if __name__ == '__main__':
#     app.run(debug=True)


#################################    2     ##################################

from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)


def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="RN1363rn1363",
        database="flight_game"
    )

@app.route('/airport/<icao>', methods=['GET'])
def get_airport(icao):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    query = """
        SELECT ident, name, municipality
        FROM airport
        WHERE ident = %s
    """
    cursor.execute(query, (icao,))
    result = cursor.fetchone()

    cursor.close()
    conn.close()

    if result:
        return jsonify({
            "ICAO": result["ident"],
            "Name": result["name"],
            "Location": result["municipality"]
        })
    else:
        return jsonify({"error": "Airport not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)