from flask import Flask, jsonify, request

app = Flask(__name__)

users = [
  {
    "username": "test",
    "email": "test@gmail.com"
  }
]

def get_login_response(username):
  response = jsonify({})
  response.headers.add('Access-Control-Allow-Origin', '*')

  user = next((x for x in users if x["username"] == username), None)

  if user is None:
    return response, 401, None
  return response, 200, user


@app.route("/profile/<username>")
def profile(username):
  response, status, user = get_login_response(username)
  if status != 200:
    return response, status

  response = jsonify({"email": user["email"]})
  response.headers.add('Access-Control-Allow-Origin', '*')
  return response, 200


@app.route("/edit", methods=["POST"])
def edit():
  req = request.get_json()
  response, status, user = get_login_response(req["username"])
  if status != 200:
    return response, status
  if "new_email" not in req:
    return response, 400

  user["email"] = req["new_email"]
  return response, 200


if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0')