import os, sys
sys.path.insert(0, os.path.dirname(__file__))

from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'dev-secret-change-in-production')

# Cross-domain session cookies (needed when frontend on Vercel, backend on Render)
app.config.update(
    SESSION_COOKIE_SAMESITE='None',
    SESSION_COOKIE_SECURE=True,      # Required for SameSite=None
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_DOMAIN=None,      # Let Flask auto-detect
)

from datetime import timedelta
app.permanent_session_lifetime = timedelta(hours=8)

# CORS
allowed_origins = os.getenv(
    'ALLOWED_ORIGINS',
    'http://localhost:8000,http://127.0.0.1:8000,http://localhost:3000,http://localhost:5000'
).split(',')

CORS(app,
     origins=[o.strip() for o in allowed_origins],
     supports_credentials=True,
     allow_headers=["Content-Type", "Authorization"],
     methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"])

from models.database import init_db
init_db()

from routes.public import public_bp
from routes.leads import leads_bp
from routes.auth import auth_bp
from routes.admin import admin_bp
from routes.contact_routes import contact_bp

app.register_blueprint(public_bp)
app.register_blueprint(leads_bp, url_prefix='/api')
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(admin_bp, url_prefix='/admin')
app.register_blueprint(contact_bp, url_prefix='/api')

@app.route('/health')
def health():
    return jsonify({'status': 'ok', 'service': 'Digital Marketing Agency API'})

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    print(f"[START] Running on http://localhost:{port}")
    print(f"[INFO] Admin login -> admin@digitalmarketingagency.com / Admin@123")
    app.run(host='0.0.0.0', port=port, debug=os.getenv('DEBUG', 'True') == 'True')
