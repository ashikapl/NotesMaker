from flask import Flask
from app.api.notes import notes_bp
from app.api.user import user_bp
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app, supports_credentials=True)
    # CORS(app, resources={r"/*": {"origins": ["http://localhost:8501", "http://127.0.0.1:8501"]}})
    app.register_blueprint(user_bp, url_prefix="/user")
    app.register_blueprint(notes_bp, url_prefix="/user/notes")
    return app