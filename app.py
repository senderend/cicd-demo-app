from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def index():
    return jsonify({"message": "Welcome to the SpecterOps CI/CD Demo API", "status": "ok"})


@app.route("/health")
def health():
    return jsonify({"status": "healthy"})


@app.route("/items", methods=["GET"])
def get_items():
    items = [
        {"id": 1, "name": "Widget A", "price": 9.99},
        {"id": 2, "name": "Widget B", "price": 19.99},
        {"id": 3, "name": "Widget C", "price": 29.99},
    ]
    return jsonify({"items": items, "count": len(items)})


@app.route("/items/<int:item_id>", methods=["GET"])
def get_item(item_id):
    items = {
        1: {"id": 1, "name": "Widget A", "price": 9.99},
        2: {"id": 2, "name": "Widget B", "price": 19.99},
        3: {"id": 3, "name": "Widget C", "price": 29.99},
    }
    item = items.get(item_id)
    if item is None:
        return jsonify({"error": "Item not found"}), 404
    return jsonify(item)


if __name__ == "__main__":
    # nosemgrep: python.flask.security.audit.app-run-param-config.avoid_app_run_with_bad_host
    app.run(host="0.0.0.0", port=5000)