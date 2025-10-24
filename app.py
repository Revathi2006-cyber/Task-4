from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory data store
users = {}

# Home route
@app.route("/")
def home():
    return "User API is running!"

# Create User (POST)
@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    user_id = str(data["id"])
    users[user_id] = data
    return jsonify({"message": "User Created", "user": data})

# Get All Users (GET)
@app.route("/users", methods=["GET"])
def get_all_users():
    return jsonify(users)

# Get Single User (GET)
@app.route("/users/<user_id>", methods=["GET"])
def get_user(user_id):
    if user_id in users:
        return jsonify(users[user_id])
    return jsonify({"message": "User Not Found"})

# Update User (PUT)
@app.route("/users/<user_id>", methods=["PUT"])
def update_user(user_id):
    if user_id in users:
        data = request.get_json()
        users[user_id].update(data)
        return jsonify({"message": "User Updated", "user": users[user_id]})
    return jsonify({"message": "User Not Found"})

# Delete User (DELETE)
@app.route("/users/<user_id>", methods=["DELETE"])
def delete_user(user_id):
    if user_id in users:
        deleted_user = users.pop(user_id)
        return jsonify({"message": "User Deleted", "user": deleted_user})
    return jsonify({"message": "User Not Found"})

if __name__ == "__main__":
    app.run(debug=True)