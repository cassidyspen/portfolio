# ============================================================
# FLASK APP — commented out, preserved for future reference
# ============================================================
#
# from flask import Flask, jsonify
# from flask_cors import CORS
#
# app = Flask(__name__)
# CORS(app, resources={r"/api/*": {
#     "origins": ["http://localhost:5173", "http://127.0.0.1:5173", "http://localhost:3000"],
#     "methods": ["GET", "OPTIONS"],
#     "allow_headers": ["Content-Type"]
# }})
#
# PORTFOLIO_DATA = { ... }  # see api/portfolio.py for the data
#
# @app.route("/api/portfolio", methods=["GET", "OPTIONS"])
# def get_portfolio():
#     return jsonify(PORTFOLIO_DATA)
#
# if __name__ == "__main__":
#     app.run(debug=True, host="0.0.0.0", port=5000)
# ============================================================
