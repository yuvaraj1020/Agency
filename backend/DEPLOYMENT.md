🚀 BACKEND DEPLOYMENT GUIDE - INDEPENDENT DEPLOYMENT
═══════════════════════════════════════════════════════════════

✅ STATUS: READY TO DEPLOY

═══════════════════════════════════════════════════════════════
BACKEND DEPLOYMENT CHECKLIST
═══════════════════════════════════════════════════════════════

BEFORE DEPLOYING:
  ☐ Update SECRET_KEY in .env (generate new secure key)
  ☐ Set DEBUG=False in .env
  ☐ Update ALLOWED_ORIGINS to include your frontend domain
  ☐ Configure EMAIL settings if needed
  ☐ Test locally with: RUN_BACKEND.bat
  ☐ Verify database initializes correctly
  ☐ Test all API endpoints locally

═══════════════════════════════════════════════════════════════
BACKEND DEPLOYMENT OPTIONS
═══════════════════════════════════════════════════════════════

OPTION 1: RENDER (Recommended - Free & Easy)
──────────────────────────────────────────────────────────────
1. Go to: https://render.com
2. Sign up with GitHub
3. Click: "New" → "Web Service"
4. Connect to your repository
5. Select branch: main
6. Settings:
   • Name: dma-backend (or your choice)
   • Environment: Python
   • Build Command: pip install -r requirements.txt
   • Start Command: gunicorn app:app --bind 0.0.0.0:$PORT
   • Region: Choose closest to your users
7. Add Environment Variables:
   • DEBUG=False
   • ENV=production
   • SECRET_KEY=[generate new random key]
   • ALLOWED_ORIGINS=https://your-frontend-domain.com
8. Click: "Create Web Service"
9. Wait 5-10 minutes for deployment
10. Copy the URL (e.g., https://dma-backend.onrender.com)
11. Give this URL to your frontend team

render.yaml is already configured in this folder!

═══════════════════════════════════════════════════════════════

OPTION 2: HEROKU
──────────────────────────────────────────────────────────────
1. Go to: https://www.heroku.com
2. Sign up
3. Create new app: dma-backend
4. Connect GitHub repository
5. Enable automatic deployments
6. Add Procfile:
   web: gunicorn app:app --bind 0.0.0.0:$PORT
7. Set Config Variables:
   • DEBUG=False
   • ENV=production
   • SECRET_KEY=[new key]
   • ALLOWED_ORIGINS=[your frontend domain]
8. Deploy from GitHub

═══════════════════════════════════════════════════════════════

OPTION 3: DOCKER
──────────────────────────────────────────────────────────────
Backend Dockerfile exists in this folder!

Docker Commands:
  # Build image
  docker build -t dma-backend .
  
  # Run locally
  docker run -p 5000:5000 \
    -e DEBUG=False \
    -e SECRET_KEY=your-key \
    -e ALLOWED_ORIGINS=your-domain \
    dma-backend

═══════════════════════════════════════════════════════════════

OPTION 4: MANUAL VPS/SERVER
──────────────────────────────────────────────────────────────
1. SSH into your server
2. Install Python 3.11+
3. Clone repository
4. cd backend
5. Create .env file with production settings
6. pip install -r requirements.txt
7. Run with gunicorn:
   gunicorn app:app --bind 0.0.0.0:5000 --workers 4

═══════════════════════════════════════════════════════════════
BACKEND CONFIGURATION FOR PRODUCTION
═══════════════════════════════════════════════════════════════

Location: .env (in this folder)

Update these values:
  
  SECRET_KEY=generate-a-new-random-key-here
    • Use: python -c "import secrets; print(secrets.token_hex(32))"
  
  DEBUG=False
    • CRITICAL: Must be False in production
  
  ENV=production
    • Set to 'production'
  
  ALLOWED_ORIGINS=https://your-frontend-domain.com,https://www.your-frontend-domain.com
    • CRITICAL: Update to your frontend URL
  
  PORT=5000
    • Usually don't change this

═══════════════════════════════════════════════════════════════
ENVIRONMENT VARIABLES NEEDED
═══════════════════════════════════════════════════════════════

Required:
  SECRET_KEY=<generate-new>           [CRITICAL]
  DEBUG=False                         [CRITICAL]
  ENV=production                      [CRITICAL]
  ALLOWED_ORIGINS=<your-frontend>    [CRITICAL]

Optional but Recommended:
  PORT=5000
  DATABASE_PATH=../database/agency.db
  EMAIL_HOST=smtp.gmail.com           [if using email]
  EMAIL_PORT=587                      [if using email]
  EMAIL_USER=your-email@gmail.com     [if using email]
  EMAIL_PASSWORD=app-password         [if using email]

═══════════════════════════════════════════════════════════════
API ENDPOINTS THAT WILL BE AVAILABLE
═══════════════════════════════════════════════════════════════

Public Endpoints:
  GET  /api/quotes/random                 → Random marketing quote

Authentication:
  POST /auth/login                        → Admin login
  POST /auth/register                     → Register user
  GET  /auth/logout                       → Logout

Leads (Contact Form):
  GET  /api/leads                         → Get all leads
  POST /api/leads                         → Create new lead
  GET  /api/leads/<id>                    → Get lead by ID
  PUT  /api/leads/<id>                    → Update lead
  DELETE /api/leads/<id>                  → Delete lead

Admin:
  POST /admin/api/users                   → Manage users
  GET  /admin/api/stats                   → Get statistics

═══════════════════════════════════════════════════════════════
FILES IN THIS FOLDER
═══════════════════════════════════════════════════════════════

✅ render.yaml              - Render.io configuration
✅ Dockerfile               - Docker container setup
✅ requirements.txt         - Python dependencies
✅ app.py                   - Main Flask application
✅ models/database.py       - Database initialization
✅ routes/                  - API endpoints
✅ .env (template)         - Environment variables template

═══════════════════════════════════════════════════════════════
QUICK START FOR RENDER
═══════════════════════════════════════════════════════════════

1. Go to render.com
2. Sign up / Login with GitHub
3. Click "New" → "Web Service"
4. Connect GitHub repo
5. Settings:
   Name: dma-backend
   Environment: Python
   Build: pip install -r requirements.txt
   Start: gunicorn app:app --bind 0.0.0.0:$PORT

6. Environment Variables:
   DEBUG=False
   ENV=production
   SECRET_KEY=<generate>
   ALLOWED_ORIGINS=https://your-frontend-url.com

7. Click "Create"
8. Wait 5-10 minutes
9. Copy backend URL
10. Share with frontend team

═══════════════════════════════════════════════════════════════
TROUBLESHOOTING
═══════════════════════════════════════════════════════════════

Issue: CORS errors in frontend console
Fix: Update ALLOWED_ORIGINS in .env to include frontend domain

Issue: 500 errors in logs
Fix: Check logs, ensure SECRET_KEY is set, DEBUG=False

Issue: Database errors
Fix: Ensure write permissions on database folder

Issue: "Module not found" errors
Fix: Ensure pip install -r requirements.txt ran successfully

═══════════════════════════════════════════════════════════════
✅ BACKEND READY TO DEPLOY
═══════════════════════════════════════════════════════════════

Your backend is production-ready!

Next: Deploy to your chosen platform using steps above.
Then: Share the backend URL with your frontend team.

═══════════════════════════════════════════════════════════════
