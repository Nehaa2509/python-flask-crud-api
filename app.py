from flask import Flask, request, jsonify

app = Flask(__name__)

users = []

@app.route("/")
def home():
    return "Flask API Running"

@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users), 200

@app.route("/users", methods=["POST"])
def add_user():
    data = request.json
    users.append(data)
    return jsonify({"message": "User added"}), 201

@app.route("/users/<int:index>", methods=["PUT"])
def update_user(index):
    data = request.json
    users[index] = data
    return jsonify({"message": "User updated"}), 200

@app.route("/users/<int:index>", methods=["DELETE"])
def delete_user(index):
    users.pop(index)
    return jsonify({"message": "User deleted"}), 200

if __name__ == "__main__":
    app.run(debug=True)

