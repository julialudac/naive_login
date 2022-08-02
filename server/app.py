from flask import Flask, jsonify, request

app = Flask(__name__)

users = [
  {
    "username": "test",
    "password": "testp",
    "email": "test@gmail.com"
  }
]

def get_login_response(req):
  response = jsonify({})
  response.headers.add('Access-Control-Allow-Origin', '*')

  user = next((x for x in users if x["username"] == req["username"]), None)

  if user is None or user["password"] != req["password"]:
    return response, 401, None
  return response, 200, user


@app.route("/login", methods=['POST'])
def index():
  return get_login_response(request.get_json())


@app.route("/profile", methods=['POST'])
def profile():
  response, status, user = get_login_response(request.get_json())
  if status != 200:
    return response, status

  response = jsonify({"email": user["email"]})
  response.headers.add('Access-Control-Allow-Origin', '*')
  return response, 200


@app.route("/edit", methods=["POST"])
def edit():
  req = request.get_json()
  response, status, user = get_login_response(req)
  if status != 200:
    return response, status
  if "new_email" not in req:
    return response, 400

  user["email"] = req["new_email"]
  return response, 200


if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0')