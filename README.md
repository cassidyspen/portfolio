# Cassidy Spencer — Portfolio

A single-page interactive portfolio built as a table of playing cards. Each card represents a part of my experience, projects, or personal life. Click a card to flip and expand it.

**Live:** _coming soon_

---

## Project Structure

```
portfolio/
├── frontend/          # React + Vite
│   ├── src/
│   │   ├── components/   # Card, CardModal, Hand, CardTable, TableHeader
│   │   ├── data/         # cards.js — all card content
│   │   └── styles/       # CSS modules
│   ├── index.html
│   └── vite.config.js
├── backend/           # Flask API
│   ├── app.py
│   ├── requirements.txt
│   └── Procfile
└── docs/
    └── architecture.md
```

---

## Local Development

### Frontend

```bash
cd frontend
npm install
npm run dev
```

Visit `http://localhost:5173`

### Backend

```bash
cd backend
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

API runs at `http://localhost:5000`

---

## Customizing Content

All card content lives in `frontend/src/data/cards.js`. Edit the `hands` array to update:

- Work experience (contributions, technologies, dates)
- Personal cards (body text)
- Tech stack categories
- Project links and descriptions
- Cat names and photos (replace `emoji` with `photoUrl` for real photos)

The Flask backend mirrors this data in `backend/app.py` for the API layer.

---

## Deployment

### Frontend → AWS S3 + CloudFront

```bash
cd frontend
npm run build
# Upload dist/ to S3 bucket configured for static hosting
# Point CloudFront distribution to S3 bucket origin
```

### Backend → AWS Elastic Beanstalk

```bash
cd backend
# Initialize EB application
eb init -p python-3.11 portfolio-api
eb create portfolio-api-env
eb deploy
```

---

## Tech Stack

| Layer    | Technology                     |
|----------|-------------------------------|
| Frontend | React 18, Vite 5              |
| Styles   | Vanilla CSS, CSS Variables    |
| Backend  | Python, Flask, Flask-CORS     |
| Server   | Gunicorn                      |
| Hosting  | AWS S3 + CloudFront, Elastic Beanstalk |

---

## Roadmap

- [ ] AWS deployment
- [ ] Cat photo gallery (real photos)
- [ ] Contact / reach out card
- [ ] AI assistant for exploring the portfolio
- [ ] Blog post cards
- [ ] GitHub activity visualization
