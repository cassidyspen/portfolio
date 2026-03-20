# Cassidy Spencer — Portfolio

A playing card–themed portfolio built with React + Vite (frontend) and Flask (backend).

---

## Project Structure

```
cassidy-portfolio/
├── backend/
│   ├── app.py              # Flask API
│   └── requirements.txt
└── frontend/
    ├── index.html
    ├── vite.config.js
    ├── package.json
    └── src/
        ├── main.jsx
        ├── App.jsx
        ├── components/
        │   ├── Card.jsx
        │   ├── ProjectCard.jsx
        │   └── DeckCorner.jsx
        ├── data/
        │   └── arts.js         # SVG botanical illustrations
        └── styles/
            └── global.css
```

---

## Running Locally

### 1. Backend (Flask)

```bash
cd backend
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Flask runs on **http://localhost:5000**

### 2. Frontend (React + Vite)

```bash
cd frontend
npm install
npm run dev
```

Vite runs on **http://localhost:5173** and proxies `/api` to Flask.

---

## Building for Production

```bash
cd frontend
npm run build
```

The `dist/` folder can be deployed to AWS S3 / CloudFront.
Flask can be deployed to AWS Elastic Beanstalk.

---

## Updating Content

All portfolio content lives in `backend/app.py` in the `PORTFOLIO_DATA` dict.
Update your experience, projects, tech, and about cards there — no frontend changes needed.

---

## Tech Stack

| Layer    | Tech                        |
|----------|-----------------------------|
| Frontend | React 18, Vite 5            |
| Backend  | Flask 3, Flask-CORS         |
| Deploy   | AWS S3 + CloudFront + EB    |
| Fonts    | Playfair Display, Lora, DM Sans (Google Fonts) |
