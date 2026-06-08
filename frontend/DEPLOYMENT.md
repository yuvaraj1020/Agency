🚀 FRONTEND DEPLOYMENT GUIDE - INDEPENDENT DEPLOYMENT
═══════════════════════════════════════════════════════════════

✅ STATUS: READY TO DEPLOY

═══════════════════════════════════════════════════════════════
FRONTEND DEPLOYMENT CHECKLIST
═══════════════════════════════════════════════════════════════

BEFORE DEPLOYING:
  ☐ Get backend URL from backend deployment
  ☐ Update vercel.json with backend URL
  ☐ Test locally with: npm start or python dev_server.py
  ☐ Verify all pages load correctly
  ☐ Test forms work (they'll call backend)
  ☐ Check admin dashboard loads
  ☐ Verify no console errors
  ☐ Update BACKEND_URL environment variable

═══════════════════════════════════════════════════════════════
FRONTEND DEPLOYMENT OPTIONS
═══════════════════════════════════════════════════════════════

OPTION 1: VERCEL (Recommended - Free & Easy)
──────────────────────────────────────────────────────────────
1. Go to: https://vercel.com
2. Sign up with GitHub
3. Click "Import Project"
4. Select your repository
5. Settings:
   • Root Directory: Digital-Marketing-Agency-Website-main/frontend
   • Framework: "Other"
   • Build Command: Leave blank (no build needed)
   • Output Directory: ./
6. Environment Variables:
   • BACKEND_URL=[your-backend-url]
     Example: https://dma-backend.onrender.com
7. Click "Deploy"
8. Wait 2-3 minutes
9. Get your frontend URL
10. Share with users

vercel.json is already configured in this folder!

═══════════════════════════════════════════════════════════════

OPTION 2: NETLIFY
──────────────────────────────────────────────────────────────
1. Go to: https://www.netlify.com
2. Sign up with GitHub
3. Click "Add new site"
4. Import from Git
5. Select repository
6. Settings:
   • Base directory: Digital-Marketing-Agency-Website-main/frontend
   • Build command: (leave empty)
   • Publish directory: .
7. Set Environment Variables:
   BACKEND_URL=https://your-backend-url.com

═══════════════════════════════════════════════════════════════

OPTION 3: DOCKER
──────────────────────────────────────────────────────────────
Frontend Dockerfile exists in this folder!

Docker Commands:
  # Build image
  docker build -t dma-frontend .
  
  # Run locally
  docker run -p 8000:8000 \
    -e BACKEND_URL=http://your-backend-url:5000 \
    dma-frontend

═══════════════════════════════════════════════════════════════

OPTION 4: GITHUB PAGES
──────────────────────────────────────────────────────────────
GitHub Pages serves static files (HTML, CSS, JS)

1. Push frontend files to repo
2. Go to Settings → Pages
3. Select main branch
4. Save
5. Wait 2-3 minutes
6. Access at: https://your-username.github.io/repo-name

Note: This is static hosting only. BACKEND_URL must point to your backend.

═══════════════════════════════════════════════════════════════

OPTION 5: MANUAL VPS/WEBSERVER
──────────────────────────────────────────────────────────────
Using Nginx:

1. SSH into your server
2. Install Nginx
3. Copy frontend files to /var/www/html/
4. Create Nginx config with proxy rules
5. Enable and restart Nginx
6. Access at your domain

═══════════════════════════════════════════════════════════════
FRONTEND CONFIGURATION FOR PRODUCTION
═══════════════════════════════════════════════════════════════

Location: vercel.json (in this folder)

Update these values:

Before deployment, update BACKEND_URL in:
  1. vercel.json (for Vercel)
  2. Environment variables (for deployment platform)

Example production values:
  BACKEND_URL=https://dma-backend.onrender.com

This URL will be used by frontend to:
  • Proxy /api/* requests
  • Proxy /auth/* requests
  • Proxy /admin/* requests

═══════════════════════════════════════════════════════════════
ENVIRONMENT VARIABLES NEEDED
═══════════════════════════════════════════════════════════════

Required:
  BACKEND_URL=https://your-backend-url.com    [CRITICAL]
    • Must match your backend deployment URL
    • Example: https://dma-backend.onrender.com

Optional:
  PORT=8000 (default, usually don't change)

═══════════════════════════════════════════════════════════════
HOW TO UPDATE BACKEND URL IN VERCEL.JSON
═══════════════════════════════════════════════════════════════

Current vercel.json:
  "destination": "https://YOUR_BACKEND_URL.onrender.com/api/:path*"

Update Steps:
  1. Open: vercel.json (in this folder)
  2. Replace: YOUR_BACKEND_URL with your actual backend URL
  3. Examples:
     • If backend is dma-backend.onrender.com
       → "destination": "https://dma-backend.onrender.com/api/:path*"
  4. Update ALL THREE rewrites:
     - /api/:path*
     - /auth/:path*
     - /admin/api/:path*
  5. Save and commit to Git

═══════════════════════════════════════════════════════════════
PAGES THAT WILL BE SERVED
═══════════════════════════════════════════════════════════════

Static Pages:
  ✅ index.html              → Homepage
  ✅ about.html              → About page
  ✅ services.html           → Services page
  ✅ portfolio.html          → Portfolio page
  ✅ contact.html            → Contact page
  ✅ pricing.html            → Pricing page

Admin:
  ✅ admin-login.html        → Admin login
  ✅ admin-dashboard/dashboard.html
  ✅ admin-dashboard/clients.html

═══════════════════════════════════════════════════════════════
FILES IN THIS FOLDER
═══════════════════════════════════════════════════════════════

✅ vercel.json              - Vercel configuration with proxies
✅ Dockerfile               - Docker container setup
✅ package.json             - Frontend manifest
✅ index.html               - Homepage
✅ *.html files            - All pages
✅ static/css/             - Stylesheets
✅ static/js/              - JavaScript files
✅ admin-dashboard/        - Admin pages

═══════════════════════════════════════════════════════════════
STEP-BY-STEP VERCEL DEPLOYMENT
═══════════════════════════════════════════════════════════════

1. Update vercel.json with backend URL
   File: vercel.json (in this folder)
   
   Change: YOUR_BACKEND_URL → your-actual-backend-url
   
   Example: dma-backend.onrender.com

2. Commit and push:
   git add .
   git commit -m "Update backend URL"
   git push origin main

3. Go to vercel.com
4. Click "Add New" → "Project"
5. Import your GitHub repository
6. Configure:
   • Root Directory: Digital-Marketing-Agency-Website-main/frontend
   • Framework: Other
   • Build Command: (leave empty)

7. Environment Variables:
   BACKEND_URL=https://your-backend-url.com

8. Click "Deploy"
9. Wait 2-3 minutes
10. Get your live URL: https://your-project.vercel.app

═══════════════════════════════════════════════════════════════
TROUBLESHOOTING
═══════════════════════════════════════════════════════════════

Issue: CORS error when submitting form
Fix: Backend ALLOWED_ORIGINS must include your frontend domain

Issue: Form submission shows 404
Fix: Check BACKEND_URL in vercel.json is correct

Issue: "Backend URL not found"
Fix: Ensure BACKEND_URL environment variable is set

Issue: Admin login page shows but won't login
Fix: Ensure backend is running and accessible

Issue: Pages not loading
Fix: Check HTML files are in correct location

═══════════════════════════════════════════════════════════════
✅ FRONTEND READY TO DEPLOY
═══════════════════════════════════════════════════════════════

Your frontend is production-ready!

Steps to complete:
1. Get backend URL from backend deployment
2. Update vercel.json with backend URL
3. Deploy frontend to Vercel/Netlify
4. Test frontend → backend connection

═══════════════════════════════════════════════════════════════
