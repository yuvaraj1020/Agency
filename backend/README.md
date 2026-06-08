# Backend Folder 📁

This folder contains all the backend code for the Digital Marketing Agency Website.

## 📂 Structure

```
backend/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── render.yaml           # Render.io deployment config
├── Dockerfile            # Docker containerization
├── DEPLOYMENT.md         # Deployment guide
├── models/               # Database models
│   ├── database.py       # Database initialization
│   ├── client_model.py
│   ├── portfolio_model.py
│   └── service_request_model.py
├── routes/               # API endpoints
│   ├── admin.py
│   ├── auth.py
│   ├── contact_routes.py
│   ├── leads.py
│   ├── marketing_routes.py
│   ├── public.py
│   ├── service_routes.py
│   └── video_edit_routes.py
├── auth/                 # Authentication
│   ├── middleware.py
│   └── __init__.py
├── utils/                # Utility functions
│   ├── email_service.py
│   ├── email.py
│   └── validation.py
├── docs/                 # Documentation
│   └── generate_prompt_pdf.py
└── .env                  # Environment variables (create from template)
```

## 🚀 Quick Start

### Local Development
```bash
pip install -r requirements.txt
python app.py
```

Server will run on `http://localhost:5000`

### Production Deployment

Read **DEPLOYMENT.md** for detailed instructions on:
- Render deployment (recommended)
- Heroku deployment
- Docker deployment
- Manual VPS deployment

## 📋 Environment Variables

Create a `.env` file with:
```
SECRET_KEY=your-secure-key-here
DEBUG=False (for production)
ENV=production
ALLOWED_ORIGINS=https://your-frontend-domain.com
PORT=5000
```

## 🔑 Key Endpoints

- `GET  /api/quotes/random` - Get random quote
- `POST /auth/login` - Admin login
- `GET  /api/leads` - Get all leads
- `POST /api/leads` - Create new lead

## 📦 Dependencies

All dependencies are listed in `requirements.txt`:
- Flask 3.0.3
- Flask-CORS 4.0.1
- Gunicorn 22.0.0
- SQLAlchemy (for database)

## 🐳 Docker

Build and run with Docker:
```bash
docker build -t dma-backend .
docker run -p 5000:5000 -e DEBUG=False dma-backend
```

## 📝 Notes

- Database auto-initializes on first run
- SQLite used for storage (agency.db)
- All API endpoints require CORS headers from frontend

## ❓ Need Help?

1. Read DEPLOYMENT.md for deployment help
2. Check logs for errors
3. Verify .env variables are set correctly
4. Ensure frontend ALLOWED_ORIGINS are configured

---

**Status: ✅ READY FOR PRODUCTION**
