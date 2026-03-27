# Cassidy Spencer — Portfolio

A playing card–themed portfolio built with React + Vite (frontend) and Python (backend), deployed on Vercel.

---

## Project Structure

```
portfolio/
├── api/
│   ├── portfolio.py        # Python serverless API handler
│   └── models.py           # Card, Contact, Portfolio dataclasses
├── public/
│   ├── flowers/            # Flower PNG images for card backs
│   └── suits/              # Suit icon PNGs (Club, Diamond, Heart, Spade)
├── src/
│   ├── App.jsx
│   ├── components/
│   │   ├── Card.jsx        # Card + Spread components
│   │   └── DeckCorner.jsx
│   ├── data/
│   │   └── arts.js         # Flower image mappings + card back SVG pattern
│   └── styles/
│       └── global.css
├── index.html
├── vite.config.js
└── vercel.json
```

---

## Running Locally

### 1. Backend (Python)

```bash
cd api
python portfolio.py
```

Runs on **http://localhost:5000** (or use `vercel dev` to run the full stack locally).

### 2. Frontend (React + Vite)

```bash
npm install
npm run dev
```

Vite runs on **http://localhost:5173** and proxies `/api` to the Python handler.

---

## Deployment

Deployed on **Vercel**. The `api/` directory is served as Vercel serverless functions. Pushing to `main` triggers an automatic deploy.

```bash
vercel --prod
```

---

## Updating Content

All portfolio content lives in `api/portfolio.py` in the `_portfolio` object. Update experience, projects, tech, and about cards there — no frontend changes needed. Each card has an `art` field that maps to a flower PNG in `public/flowers/`.

---

## Tech Stack

| Layer    | Tech                                           |
|----------|------------------------------------------------|
| Frontend | React 18, Vite                                 |
| Backend  | Python (`http.server`), Vercel serverless      |
| Deploy   | Vercel                                         |
| Fonts    | Playfair Display, Lora, DM Sans (Google Fonts) |
