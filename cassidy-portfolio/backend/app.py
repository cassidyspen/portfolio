from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/api/*": {
    "origins": ["http://localhost:5173", "http://127.0.0.1:5173", "http://localhost:3000"],
    "methods": ["GET", "OPTIONS"],
    "allow_headers": ["Content-Type"]
}})

PORTFOLIO_DATA = {
    "name": "Cassidy Spencer",
    "title": "Software Engineer",
    "location": "Pittsburgh",
    "contact": {
        "linkedin": "https://linkedin.com/in/cassidyspencer",
        "github": "https://github.com/cassidyspencer",
        "email": "hello@cassidyspencer.dev"
    },
    "experience": [
        {
            "pip": "A", "suit": "♣",
            "backTitle": "Software Engineer",
            "art": "flower",
            "faceTitle": "Software Engineer",
            "faceDetail": ["PNC Bank · Pittsburgh", "Python pipelines &", "RESTful APIs", "OpenShift · Jenkins CI/CD"],
            "tags": ["Python", "SQL Server", "OpenShift"]
        },
        {
            "pip": "K", "suit": "♠",
            "backTitle": "CGI Developer",
            "art": "rose",
            "faceTitle": "Software Developer",
            "faceDetail": ["CGI Federal · Consultant", "Full-stack development", "across federal client", "engagements"],
            "tags": ["Full-stack", "Federal", "Consulting"]
        },
        {
            "pip": "J", "suit": "♦",
            "backTitle": "Internships ×2",
            "art": "daisy",
            "faceTitle": "Dev Intern ×2",
            "faceDetail": ["CGI Federal", "Back-end & Front-end", "rotations — real features", "in both stacks"],
            "tags": ["Back-end", "Front-end", "CGI"]
        },
        {
            "pip": "10", "suit": "♥",
            "backTitle": "Senior Capstone",
            "art": "leaf",
            "faceTitle": "Obstacle Avoidance App",
            "faceDetail": ["USD Senior Capstone", "iPhone app for users", "with visual impairments", "Swift · Xcode · Core ML"],
            "tags": ["Swift", "Core ML", "iOS"]
        }
    ],
    "projects": [
        {
            "pip": "Q", "suit": "♥",
            "backTitle": "re·locate",
            "backSub": "Cost of living tool",
            "art": "leaf",
            "title": "re·locate",
            "url": "https://relocatecost.com",
            "meta": "relocatecost.com",
            "desc": "Compare cost of living between cities. Full 2025 tax engine — federal brackets, all 50 states + DC, FICA, healthcare.",
            "tags": ["Vanilla JS", "Vercel", "Serverless", "RapidAPI"]
        },
        {
            "pip": "Q", "suit": "♠",
            "backTitle": "This Portfolio",
            "backSub": "Playing card theme",
            "art": "rose",
            "title": "This Portfolio",
            "url": "#",
            "meta": "React · Vite · Flask · AWS",
            "desc": "Playing card–themed portfolio. React + Vite frontend, Flask backend, deployed on AWS S3, CloudFront & Elastic Beanstalk.",
            "tags": ["React", "Vite", "Flask", "AWS"]
        }
    ],
    "tech": [
        {
            "pip": "9", "suit": "♣",
            "backTitle": "Languages & Stack",
            "art": "clover",
            "faceTitle": "Languages & Stack",
            "faceDetail": ["Python · JS · Swift", "React · Flask · Vite", "SQL Server · PostgreSQL", "AWS · OpenShift · Vercel"],
            "tags": ["Python", "React", "Flask"]
        },
        {
            "pip": "8", "suit": "♥",
            "backTitle": "Coding Style",
            "art": "tulip",
            "faceTitle": "Coding Style",
            "faceDetail": ["Functional components,", "clean separation of concerns", "Plain JS over TypeScript", "Flask blueprints, no fuss"],
            "tags": ["Functional", "Plain JS"]
        },
        {
            "pip": "7", "suit": "♦",
            "backTitle": "Why I Code",
            "art": "leaf",
            "faceTitle": "Why I Code",
            "faceDetail": ["Building things that", "actually help people —", "from accessibility apps", "to cost-of-living tools"],
            "tags": ["Impact", "Accessibility"]
        }
    ],
    "about": [
        {
            "pip": "5", "suit": "♥",
            "backTitle": "Passions",
            "art": "tulip",
            "faceTitle": "Passions",
            "faceDetail": ["Music, travel, language", "Spanish minor — love", "connecting across cultures", "Always planning next trip"],
            "tags": ["Music", "Travel", "Spanish"]
        },
        {
            "pip": "5", "suit": "♣",
            "backTitle": "Hobbies",
            "art": "music",
            "faceTitle": "Hobbies",
            "faceDetail": ["Concert-going, exploring", "new cities, building", "side projects that start", "as \"just an idea\""],
            "tags": ["Concerts", "Building"]
        },
        {
            "pip": "5", "suit": "♠",
            "backTitle": "Cats",
            "art": "cat",
            "faceTitle": "Cats",
            "faceDetail": ["Proudly owned by cats", "They supervise all", "coding sessions and", "have strong opinions"],
            "tags": ["Important", "Supervisors"]
        },
        {
            "pip": "5", "suit": "♦",
            "backTitle": "Volunteer",
            "art": "sunflower",
            "faceTitle": "Volunteer",
            "faceDetail": ["Giving time to causes", "that matter — community", "and accessibility close", "to my heart"],
            "tags": ["Community", "Accessibility"]
        }
    ]
}


@app.route("/api/portfolio", methods=["GET", "OPTIONS"])
def get_portfolio():
    return jsonify(PORTFOLIO_DATA)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
