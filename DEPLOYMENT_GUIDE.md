# Digital Marketing Agency — Deployment Guide
## Architecture
- **Frontend**: Static HTML/CSS/JS → Deploy to **Vercel**
- **Backend**: Python Flask → Deploy to **Render** (free tier)

---

## Step 1: Deploy Backend on Render

1. Go to [render.com](https://render.com) → New Web Service
2. Connect your GitHub repo (push the `backend/` folder)
3. Settings:
   - **Root Directory**: `backend`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app --bind 0.0.0.0:$PORT --workers 2`
4. Add Environment Variables on Render:
   | Key | Value |
   |-----|-------|
   | `SECRET_KEY` | Generate a strong random string |
   | `FLASK_ENV` | `production` |
   | `DEBUG` | `False` |
   | `ALLOWED_ORIGINS` | (Add after Step 2, e.g. `https://your-app.vercel.app`) |

5. Deploy → Copy your Render URL (e.g. `https://dma-backend.onrender.com`)

---

## Step 2: Update vercel.json with your Render URL

Open `frontend/vercel.json` and replace `https://your-backend.onrender.com` with your actual Render URL:

```json
{
  "rewrites": [
    {
      "source": "/api/:path*",
      "destination": "https://YOUR-ACTUAL-RENDER-URL.onrender.com/api/:path*"
    },
    {
      "source": "/auth/:path*",
      "destination": "https://YOUR-ACTUAL-RENDER-URL.onrender.com/auth/:path*"
    },
    {
      "source": "/admin/api/:path*",
      "destination": "https://YOUR-ACTUAL-RENDER-URL.onrender.com/admin/api/:path*"
    }
  ],
  "cleanUrls": true
}
```

---

## Step 3: Deploy Frontend on Vercel

1. Go to [vercel.com](https://vercel.com) → New Project
2. Import your GitHub repo
3. Settings:
   - **Root Directory**: `frontend`
   - **Framework**: Other (Static)
   - No build command needed
4. Deploy → Your site is live!

---

## Step 4: Update ALLOWED_ORIGINS on Render

Go back to Render → Environment Variables → Set:
```
ALLOWED_ORIGINS=https://your-actual-vercel-url.vercel.app
```
Redeploy the backend.

---

## Admin Access
- URL: `https://your-site.vercel.app/admin-login.html`
- Email: `admin@digitalmarketingagency.com`
- Password: `Admin@123`
- **⚠️ Change the password after first login!**

---

## Local Development
```bash
# Start backend
cd backend
pip install -r requirements.txt
python app.py
# Runs on http://localhost:5000

# Start frontend
cd frontend
python3 -m http.server 8000
# Open http://localhost:8000
```
