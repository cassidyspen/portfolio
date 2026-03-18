from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Card data – in production this could be fetched from a DB or CMS
CARDS = {
    "work": [
        {
            "id": "pnc",
            "rank": "A",
            "suit": "spades",
            "title": "Software Engineer",
            "subtitle": "PNC Bank",
            "dates": "2023 – Present",
            "contributions": [
                "Designed and built internal tooling used by 200+ analysts across the bank",
                "Led migration of legacy data pipelines to a modern Python-based ETL architecture",
                "Collaborated with product and compliance teams to ship features on tight regulatory deadlines",
                "Mentored two junior engineers through onboarding and first feature delivery",
            ],
            "technologies": ["Python", "React", "PostgreSQL", "REST APIs", "AWS", "Jenkins"],
        },
        {
            "id": "cgi-dev",
            "rank": "K",
            "suit": "spades",
            "title": "CGI Software Developer",
            "subtitle": "CGI Federal",
            "dates": "2022 – 2023",
            "contributions": [
                "Developed and maintained full-stack features for a government client portal",
                "Reduced page load time by 40% through frontend optimization and caching strategies",
                "Participated in agile ceremonies and contributed to sprint planning",
                "Wrote comprehensive unit and integration tests using Jest and pytest",
            ],
            "technologies": ["React", "Python", "SQL", "REST APIs", "Jenkins"],
        },
        {
            "id": "cgi-intern-dev",
            "rank": "Q",
            "suit": "spades",
            "title": "CGI Software Development Intern",
            "subtitle": "CGI Federal",
            "dates": "Summer 2021",
            "contributions": [
                "Built a data visualization dashboard consumed by internal stakeholders",
                "Collaborated with senior engineers on RESTful API design",
                "Participated in code reviews and contributed to internal documentation",
            ],
            "technologies": ["React", "Python", "SQL APIs"],
        },
        {
            "id": "cgi-intern",
            "rank": "J",
            "suit": "spades",
            "title": "CGI Software Development Intern",
            "subtitle": "CGI Federal",
            "dates": "Summer 2020",
            "contributions": [
                "Assisted in designing and prototyping a new internal workflow tool",
                "Gained hands-on experience with agile development processes",
                "Delivered a working prototype by end of internship",
            ],
            "technologies": ["JavaScript", "HTML/CSS", "Python"],
        },
    ],
    "personal": [
        {"id": "passions", "rank": "A", "suit": "hearts", "title": "Passions"},
        {"id": "hobbies",  "rank": "K", "suit": "hearts", "title": "Hobbies"},
        {"id": "cats",     "rank": "Q", "suit": "hearts", "title": "Cats", "is_gallery": True},
        {"id": "volunteer","rank": "J", "suit": "hearts", "title": "Volunteer"},
    ],
    "tech": [
        {
            "id": "stack",
            "rank": "A",
            "suit": "diamonds",
            "title": "Languages & Stack",
            "technologies": ["Python", "JavaScript", "TypeScript", "React", "Flask",
                             "PostgreSQL", "AWS", "Docker", "Git", "Jenkins", "REST APIs", "SQL"],
        },
        {"id": "style", "rank": "K", "suit": "diamonds", "title": "Coding Style"},
        {"id": "why",   "rank": "Q", "suit": "diamonds", "title": "Why I Code"},
    ],
    "projects": [
        {
            "id": "portfolio",
            "rank": "A",
            "suit": "clubs",
            "title": "This Portfolio",
            "live_url": "#",
            "github_url": "https://github.com/cassidyspen",
            "technologies": ["React", "Vite", "AWS S3", "CloudFront", "Flask"],
        },
        {
            "id": "cost-of-living",
            "rank": "K",
            "suit": "clubs",
            "title": "Cost of Living",
            "subtitle": "re·locate",
            "live_url": "https://cost-of-living-ruddy.vercel.app",
            "github_url": "https://github.com/cassidyspen/cost-of-living",
            "technologies": ["HTML", "CSS", "JavaScript", "Vercel", "REST APIs"],
        },
    ],
}


@app.route("/", methods=["GET"])
def index():
    return jsonify({"status": "ok", "message": "Cassidy Spencer Portfolio API"})


@app.route("/cards", methods=["GET"])
def get_all_cards():
    return jsonify(CARDS)


@app.route("/cards/<hand_id>", methods=["GET"])
def get_hand(hand_id):
    hand = CARDS.get(hand_id)
    if not hand:
        return jsonify({"error": "Hand not found"}), 404
    return jsonify(hand)


@app.route("/cards/<hand_id>/<card_id>", methods=["GET"])
def get_card(hand_id, card_id):
    hand = CARDS.get(hand_id)
    if not hand:
        return jsonify({"error": "Hand not found"}), 404
    card = next((c for c in hand if c["id"] == card_id), None)
    if not card:
        return jsonify({"error": "Card not found"}), 404
    return jsonify(card)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
