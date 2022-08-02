from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://ayomi:ayomi@localhost:81/ayomi"

db = SQLAlchemy(app)

class User(db.Model):
  __tablename__="users"
  _id = db.Column("id", db.Integer, primary_key=True)
  username = db.Column(db.String(100))
  email = db.Column(db.String(100))

  def __init__(self, username, email):
    self.username = username
    self.email = email

def get_login_response(username):
  response = jsonify({})
  response.headers.add('Access-Control-Allow-Origin', '*')

  user = User.query.filter_by(username=username).first()

  if user is None:
    return response, 401, None
  return response, 200, user


@app.route("/profile/<username>")
def profile(username):
  response, status, user = get_login_response(username)
  if status != 200:
    return response, status

  response = jsonify({"email": user.email})
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

  user.email = req["new_email"]
  return response, 200


if __name__ == "__main__":
  db.create_all()
  app.run(debug=True, host='0.0.0.0')