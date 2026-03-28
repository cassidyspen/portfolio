Product Requirements Document (PRD)
Project Name: Personal Portfolio – Card Table Interface

1. Overview
A single-page personal portfolio designed as a table of playing cards. Each card represents a part of my professional experience, technical skills, projects, or personal life. Visitors explore the portfolio by interacting with cards that flip to reveal details and can be expanded into a zoom view.

The goal is a memorable, interactive portfolio that demonstrates frontend engineering, backend API design, and thoughtful UI design.

2. Goals
Primary Goals
- Showcase professional experience and technical projects
- Demonstrate full-stack engineering skills
- Build a unique, memorable portfolio experience
- Deploy on Vercel with a Python serverless backend

Secondary Goals
- Demonstrate UI/UX design thinking
- Present engineering philosophy and personal interests
- Build a platform that can support future AI features

3. Target Audience
Primary: engineering hiring managers, technical recruiters, software engineers
Secondary: friends, collaborators, general visitors

4. Core Concept
The portfolio appears as a table of cards laid out in four hands, each representing a category of content. Cards start face down showing a decorative back with a unique flower illustration. Clicking a card flips it to reveal the front. Double-clicking (or double-tapping) opens the card in a zoomed modal.

5. Visual Design

Color Palette
- Cream/off-white — card background
- Sage and emerald green — accents, typography, borders
- Gold/olive — decorative accents
- Light tan/wood — page background

Card Back
- Cream background with a repeating diamond/circle SVG pattern
- A unique flower PNG illustration centered on each card (from public/flowers/)
- Card title displayed below the flower
- "Tap to reveal" hint text

Card Front
- Pip and suit icon in the top-left and bottom-right corners
- Suit icons are PNG images (Club, Diamond, Heart, Spade) from public/suits/
- Title, subtitle, description, tags
- Optional: link button, photo gallery (cats card)

6. Page Layout
Four hands of cards, each corresponding to a suit:

Experience (♣)
- A♣ PNC Software Developer
- K♣ CGI Software Developer
- Q♣ CGI Internships
- J♣ Computer Science Tutor and Lab Assistant

Projects (♦)
- 10♦ re·locate
- 9♦ This Portfolio

Tech (♠)
- 8♠ Languages & Stack
- 7♠ Coding Style
- 6♠ Why I Code

About (♥)
- 5♥ Passions
- 4♥ Hobbies
- 3♥ Cats
- 2♥ Volunteer

7. Card Interaction Design

Default State
Cards appear face down in a fanned arc under each section heading.

Hover
Cards lift slightly upward with a shadow increase.

Single Click / Tap
Card flips on the Y-axis to reveal the front. Clicking again flips it back.

Double Click / Double Tap
Card opens in a full zoomed modal overlay. Close by clicking outside, clicking ✕, or pressing Escape.

Keyboard
Tab to focus a card, Enter/Space to flip, Escape to close.

8. Card Content Structure
Each card has:
- pip — card rank (A, K, Q, J, 10–2)
- suit — ♣ ♦ ♥ ♠
- back_title — label shown on card back
- art — flower key mapping to a PNG in public/flowers/
- face_title, face_sub, face_sub2 — title and subtitles
- face_desc — main description text
- tags — list of tag chips
- link / link_label — optional external link
- images — optional photo gallery (used on cats card)

9. Technical Architecture

Frontend
- React 18 + Vite
- Single component: Card.jsx (handles flip, zoom, hover, keyboard)
- arts.js maps art names to flower PNG image HTML strings and exports the card back SVG pattern generator
- Suit icons rendered as <img> tags via SUIT_IMGS map in Card.jsx

Backend
- Python serverless function (api/portfolio.py) using http.server.BaseHTTPRequestHandler
- Single endpoint: GET /api/portfolio
- Returns full portfolio JSON including all card data
- Strawberry GraphQL schema (api/schema.py) used as an internal data layer — resolvers query the database and return typed Card objects
- psycopg (v3) handles PostgreSQL connections via a module-level cached connection

Data
- Portfolio card data stored in a PostgreSQL `cards` table hosted on Supabase
- Columns: id, pip, suit, section, sort_order, back_title, art, face_title, face_sub, face_sub2, face_desc, link, link_label, images (text[]), tags (text[])
- Cards are grouped by `section` (experience, projects, tech, about) and ordered by `sort_order`
- DATABASE_URL environment variable connects the serverless function to the database

Deployment
- Hosted on Vercel
- api/ directory served as serverless functions
- Frontend built with npm run build → dist/
- DATABASE_URL set in Vercel project environment variables

10. Flower Art System
Each card has a unique flower PNG from public/flowers/:
- hibiscus, rose, daisy, lavender, cosmos, peony, iris, tulip, jasmine, forget_me_not, buttercup, anemone, sunflower
- Rendered with mix-blend-mode: multiply so white backgrounds are transparent against the card

11. MVP Scope (Delivered)
- Single homepage with four card hands
- Cards starting face down with flower art
- Card flip animation (single click)
- Card zoom modal (double click)
- Hover lift animation
- Fanned arc layout per hand
- Python serverless API on Vercel
- Suit PNG icons in card corners
- Responsive mobile layout

12. Future Enhancements
- AI assistant for exploring the portfolio
- Blog posts
- Interactive architecture diagrams
- GitHub activity visualization
- Project deep dives

13. Success Criteria
- Visitors quickly understand my experience
- The design is memorable and polished
- The site demonstrates full-stack engineering ability
- Recruiters can easily explore projects and skills
- The codebase is clean and well-documented
