# Frontend — BhAAi Fans Digital AA

**Frontend for Web, Marketing & Creative Solutions**

---

## 📂 Folder Structure

This folder contains all the frontend code for the Digital Marketing Agency Website.

```
frontend/
├── index.html            # Homepage
├── about.html            # About page
├── contact.html          # Contact page
├── services.html         # Services page
├── portfolio.html        # Portfolio page
├── pricing.html          # Pricing page
├── admin-login.html      # Admin login
├── package.json          # NPM manifest
├── vercel.json          # Vercel deployment config
├── dev_server.py        # Development server
├── Dockerfile           # Docker containerization
├── DEPLOYMENT.md        # Deployment guide ⭐
├── README.md            # This file
├── admin-dashboard/
│   ├── dashboard.html
│   ├── dashboard.js
│   ├── clients.html
│   └── requests.html
├── services/
│   ├── web-development.html
│   ├── graphic-design.html
│   ├── social-media-marketing.html
│   ├── video-editing.html
│   ├── marketing-strategy.html
│   └── ads-management.html
├── static/
│   ├── css/
│   │   ├── style.css
│   │   ├── responsive.css
│   │   └── services.css
│   ├── js/
│   │   ├── main.js
│   │   ├── animations.js
│   │   ├── form.js
│   │   └── firebase-config.js
│   └── images/
│       └── portfolio/
└── scripts/
    └── utility scripts
```

---

## 🚀 Quick Start

### Local Development
```bash
python dev_server.py
```
Server runs on `http://localhost:8000`

### Production Deployment

**👉 Read DEPLOYMENT.md for detailed deployment instructions!**

Options:
- **Vercel** (recommended)
- **Netlify**
- **GitHub Pages**
- **Docker**
- **Manual Nginx**

---

## 📋 Configuration

### Backend URL Configuration (vercel.json)
Update your backend URL in `vercel.json`:

```json
"destination": "https://your-backend-url.com/api/:path*"
```

Replace `your-backend-url.com` with your actual deployed backend URL.

### Environment Variables
When deploying, set:
```
BACKEND_URL=https://your-backend-url.com
```

---

## 📱 Features

- ✅ Responsive design (mobile-friendly)
- ✅ Contact form (submits to backend API)
- ✅ Portfolio showcase
- ✅ Service listings
- ✅ Admin dashboard
- ✅ API proxy (Vercel/dev_server)
- ✅ Production-ready

---

## 🧪 Testing

### Local Testing
1. Start backend: Run `RUN_BACKEND.bat` (from root)
2. Start frontend: `python dev_server.py`
3. Open `http://localhost:8000` in browser
4. Test forms and navigation

---

## 🐳 Docker

Build and run with Docker:
```bash
docker build -t dma-frontend .
docker run -p 8000:8000 -e BACKEND_URL=http://backend:5000 dma-frontend
```

---

## 🔧 Customization

- **Colors:** Edit CSS variables in `static/css/style.css`
- **Content:** Edit HTML files directly
- **Pricing:** Modify pricing cards in `pricing.html`
- **Images:** Add to `static/images/`

---

## 🌐 Services Offered

1. Web Development
2. Social Media Marketing
3. Ads Management
4. Video Editing
5. Graphic Design
6. Marketing Strategy

---

## 📚 Tech Stack

- **Frontend:** HTML5, CSS3, Vanilla JavaScript
- **Deployment:** Vercel, Netlify, Docker, or manual hosting
- **Fonts:** Google Fonts (Bebas Neue, DM Sans, DM Mono)
- **Backend:** Python Flask (separate deployment)

---

## ❓ Need Help?

1. **Deployment Help:** Read `DEPLOYMENT.md`
2. **Backend Issues:** Check backend folder README
3. **Console Errors:** Open browser console (F12)
4. **Proxy Not Working:** Verify `BACKEND_URL` is set correctly

---

## 📝 Status

**✅ READY FOR PRODUCTION**

All files organized and deployment-ready!

---

© 2025 BhAAi Fans Digital AA · Hyderabad, Telangana, India
