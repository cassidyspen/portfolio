# Architecture Overview

## Frontend

- **Framework**: React 18 + Vite
- **Styling**: Plain CSS with CSS variables (no Tailwind/CSS-in-JS)
- **Fonts**: Google Fonts — Cinzel (display), Playfair Display (headings), EB Garamond (body)
- **State**: Local React state (useState) — no external state library needed at this scale
- **Build output**: Static files in `frontend/dist/` → deployed to S3

### Component Tree

```
App
└── CardTable
    ├── CardHand (×4)   — face-down fanned cards per category
    └── CardModal       — overlay with flipped cards
        └── CardFront (×N)  — individual revealed card faces
```

### Key design decisions

- CSS-only animations (no animation library dependency)
- Cards use CSS `transform: rotate()` + `translateY()` for the fan effect
- Flip-in is achieved with `rotateY` keyframes per card, staggered with `animation-delay`
- Wood texture is layered `linear-gradient` + `radial-gradient` (no image assets required)

## Backend

- **Framework**: Flask 3
- **Served via**: Gunicorn (production) / Flask dev server (local)
- **CORS**: flask-cors allows requests from the frontend origin

### API Endpoints

| Method | Path                       | Description            |
|--------|----------------------------|------------------------|
| GET    | `/`                        | Health check           |
| GET    | `/cards`                   | All hands and cards    |
| GET    | `/cards/<hand_id>`         | One hand's cards       |
| GET    | `/cards/<hand_id>/<card_id>` | Single card          |

## Cloud Infrastructure (AWS)

```
                    ┌─────────────────┐
                    │   User Browser  │
                    └────────┬────────┘
                             │ HTTPS
                    ┌────────▼────────┐
                    │  CloudFront CDN │
                    └────────┬────────┘
                      ┌──────┴──────┐
                      │             │
             ┌────────▼──────┐  ┌───▼──────────────────┐
             │  S3 Bucket    │  │  Elastic Beanstalk    │
             │  (React app)  │  │  (Flask API)          │
             └───────────────┘  └──────────────────────┘
```
