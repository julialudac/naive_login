from flask import Flask, jsonify, request

app = Flask(__name__)

users = [
  {
    "username": "test",
    "password": "testp",
    "email": "test@gmail.com"
  }
]

@app.route("/login", methods=['POST'])
def index():
  response = jsonify({})
  response.headers.add('Access-Control-Allow-Origin', '*')

  req = request.get_json()
  user = next((x for x in users if x["username"] == req["username"]), None)

  if user is None or user["password"] != req["password"]:
    return response, 401
  return response, 200


if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0')