import json
from http.server import BaseHTTPRequestHandler

PORTFOLIO_DATA = {
    "name": "Cassidy Spencer",
    "title": "Software Engineer",
    "location": "Pittsburgh",
    "contact": {
        "linkedin": "https://linkedin.com/in/cassidy-spencer-cs",
        "github": "https://github.com/cassidyspen",
        "email": "cassidyspencer.dev@gmail.com"
    },
    "experience": [
        {
            "pip": "A", "suit": "♠",
            "backTitle": "PNC Software Engingineer",
            "art": "flower",
            "faceTitle": "Software Engineer",
            "faceSub": "PNC Bank · Pittsburgh",
            "faceDesc": "Nov 2024 - Present: Built python FastAPI RESTful microservices and SQL solutions to automate internal audit workflows for 400+ users. Led deployments, failover events, and security remediation, delivering 20+ releases and resolving 100+ vulnerabilities.",
            "tags": ["Python", "SQL Server", "OpenShift", "Jenkins", "FastAPI"]
        },
        {
            "pip": "K", "suit": "♠",
            "backTitle": "CGI Software Developer",
            "art": "rose",
            "faceTitle": "Software Developer",
            "faceSub": "CGI · Pittsburgh",
            "faceDesc": "June 2024 - Nov 2025: Built full-stack features for a pro bono Flutter/Python app supporting children with autism, including an Angular admin dashboard. Completed training in Java, SpringBoot, Docker, PostgreSQL, and RESTful API development.",
            "tags": ["Full-stack", "Python", "Java", "Angular", "Flutter"]
        },
        {
            "pip": "Q", "suit": "♠",
            "backTitle": "CGI Internships",
            "art": "daisy",
            "faceTitle": "Dev Intern ×2",
            "faceSub": "CGI Federal",
            "faceDesc": "Back-end & front-end rotations — shipped real features in both stacks.",
            "tags": ["Back-end", "Front-end", "CGI"]
        },
        {
            "pip": "J", "suit": "♠",
            "backTitle": "Senior Capstone",
            "art": "leaf",
            "faceTitle": "Obstacle Avoidance App",
            "faceSub": "USD Senior Capstone",
            "faceDesc": "iPhone app for users with visual impairments built with Swift, Xcode & Core ML.",
            "tags": ["Swift", "Core ML", "iOS"]
        }
    ],
    "projects": [
        {
            "pip": "10", "suit": "♣",
            "backTitle": "re·locate",
            "art": "leaf",
            "faceTitle": "re·locate",
            "faceSub": "relocatecost.com",
            "faceDesc": "Compare cost of living across all 50 states + DC with a full 2025 tax engine.",
            "tags": ["Vanilla JS", "Vercel", "Serverless", "RapidAPI"]
        },
        {
            "pip": "9", "suit": "♣",
            "backTitle": "This Portfolio",
            "art": "rose",
            "faceTitle": "This Portfolio",
            "faceSub": "React · Vite · Python",
            "faceDesc": "Playing card themed portfolio with a Vercel serverless API backend.",
            "tags": ["React", "Vite", "Python", "Vercel"]
        }
    ],
    "tech": [
        {
            "pip": "8", "suit": "♦",
            "backTitle": "Languages & Stack",
            "art": "clover",
            "faceTitle": "Languages & Stack",
            "faceSub": "Full-Stack",
            "faceDesc": "Python · JS · Swift · React · Vite · SQL Server · PostgreSQL · AWS · OpenShift · Vercel",
            "tags": ["Python", "React", "Vercel"]
        },
        {
            "pip": "7", "suit": "♦",
            "backTitle": "Coding Style",
            "art": "tulip",
            "faceTitle": "Coding Style",
            "faceSub": "Philosophy",
            "faceDesc": "Functional components, clean separation of concerns. Plain JS over TypeScript. Flask blueprints, no fuss.",
            "tags": ["Functional", "Plain JS"]
        },
        {
            "pip": "6", "suit": "♦",
            "backTitle": "Why I Code",
            "art": "leaf",
            "faceTitle": "Why I Code",
            "faceSub": "Mission",
            "faceDesc": "Building things that actually help people — from accessibility apps to cost-of-living tools.",
            "tags": ["Impact", "Accessibility"]
        }
    ],
    "about": [
        {
            "pip": "5", "suit": "♥",
            "backTitle": "Passions",
            "art": "tulip",
            "faceTitle": "Passions",
            "faceSub": "Music · Travel · Language",
            "faceDesc": "Spanish minor — love connecting across cultures. Always planning the next trip.",
            "tags": ["Music", "Travel", "Spanish"]
        },
        {
            "pip": "4", "suit": "♥",
            "backTitle": "Hobbies",
            "art": "music",
            "faceTitle": "Hobbies",
            "faceSub": "Off the Clock",
            "faceDesc": "Concert-going, exploring new cities, building side projects that start as \"just an idea\".",
            "tags": ["Concerts", "Building"]
        },
        {
            "pip": "3", "suit": "♥",
            "backTitle": "Cats",
            "art": "cat",
            "faceTitle": "Cats",
            "faceSub": "Chief Supervisors",
            "faceDesc": "Proudly owned by cats. They supervise all coding sessions and have strong opinions.",
            "tags": ["Important", "Supervisors"]
        },
        {
            "pip": "2", "suit": "♥",
            "backTitle": "Volunteer",
            "art": "sunflower",
            "faceTitle": "Volunteer",
            "faceSub": "Community & Accessibility",
            "faceDesc": "Giving time to causes that matter — community and accessibility close to my heart.",
            "tags": ["Community", "Accessibility"]
        }
    ]
}


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(json.dumps(PORTFOLIO_DATA).encode())

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()
