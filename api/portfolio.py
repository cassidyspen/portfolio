import os, sys
sys.path.insert(0, os.path.dirname(__file__))

from http.server import BaseHTTPRequestHandler, HTTPServer
from models import Card, Contact, Portfolio


# ── Portfolio data ─────────────────────────────────────────────────────────────

_portfolio = Portfolio(
    name="Cassidy Spencer",
    title="Software Engineer",
    location="Pittsburgh",
    contact=Contact(
        linkedin="https://linkedin.com/in/cassidy-spencer-cs",
        github="https://github.com/cassidyspen",
        email="cassidyspencer.dev@gmail.com",
        resume="https://docs.google.com/document/d/1HammHRgfye52DshjDyQpzzXeRrq_Pykq/edit?usp=sharing&ouid=102317221848885023723&rtpof=true&sd=true",
    ),
    experience=[
        Card(
            pip="A", suit="♠", back_title="PNC Software Developer", art="hibiscus",
            face_title="Software Developer", face_sub="PNC Bank · Pittsburgh",
            face_sub2="Nov 2024 - Present",
            face_desc="Eliminated manual audit workflows by building FastAPI microservices and SQL pipelines used by 400+ employees. Delivered 20+ releases and resolved 100+ security vulnerabilities.",
            tags=["Python", "SQL Server", "OpenShift", "Jenkins", "FastAPI"],
        ),
        Card(
            pip="K", suit="♠", back_title="CGI Software Developer", art="sunflower",
            face_title="Software Developer", face_sub="CGI · Pittsburgh",
            face_sub2="June 2024 - Nov 2025",
            face_desc="Developed features for a Flutter/Python app supporting children with autism, including an Angular admin dashboard. Completed training in Java, SpringBoot, Docker, PostgreSQL, and REST API development.",
            tags=["Python", "Java", "Angular", "Flutter", "PostgreSQL"],
        ),
        Card(
            pip="Q", suit="♠", back_title="CGI Internships", art="daisy",
            face_title="Software Development Intern", face_sub="CGI · Pittsburgh",
            face_sub2="Summer 2022 + Summer 2023",
            face_desc="Built an API health dashboard using Java and Spring Boot and developed Angular web components. Led Scrum ceremonies, presented deliverables, and raised $950 for local teachers as Intern Lead.",
            tags=["Java", "SpringBoot", "Angular", "Figma", "Agile"],
        ),
        Card(
            pip="J", suit="♠", back_title="Computer Science Tutor and Lab Assistant", art="lavender",
            face_title="CS Tutor + Lab Assistant", face_sub="University of San Diego",
            face_sub2="Feb 2022 - May 2023",
            face_desc="Assisted undergraduate students with coursework and programming assignments by helping them break down complex problems and develop effective solutions. ",
            tags=["Python", "Operating Systems", "Networking", "Algorithms", "VS Code"],
        ),
    ],
    projects=[
        Card(
            pip="10", suit="♣", back_title="re·locate", art="cosmos",
            face_title="re·locate", face_sub="relocatecost.com",
            face_desc="Built a cost of living calculator by using prompt engineering with Anthropic Claude and ChatGPT to compare living costs with 8000+ cities.",
            tags=["Vanilla JS", "Vercel", "CSS", "RapidAPI", "HTML"],
            link="https://relocatecost.com",
        ),
        Card(
            pip="9", suit="♣", back_title="This Portfolio", art="peony",
            face_title="This Portfolio", face_sub="cassidyspencer.dev",
            face_desc="You're looking at it! Playing card themed portfolio hosted on Vercel with Python and React",
            tags=["React", "Vite", "Python", "Vercel"],
            link="https://github.com/cassidyspen/portfolio",
            link_label="View Source ↗",
        ),
    ],
    tech=[
        Card(
            pip="8", suit="♦", back_title="Languages & Stack", art="iris",
            face_title="Languages & Stack", face_sub="My Specialties",
            face_desc="Back End:\nPython · FastAPI · Java JS · SpringBoot\nFront End:\nReact · Vite · Angular\nDB:\nSQL Server · PostgreSQL\nCI/CD:\nJenkins · OpenShift · Git",
            tags=["Front End","+","Back End"]
        ),
        Card(
            pip="7", suit="♦", back_title="Coding Style", art="tulip",
            face_title="Coding Style", face_sub="Philosophy",
            face_desc="I write clean, maintainable code with an emphasis on clarity and consistency. I rely on unit testing and often use test-driven development to ensure quality and catch issues early.",
            tags=["Clean Formatting", "Test Driven Development", "Engineering Best Practices", "Teamwork"],
        ),
        Card(
            pip="6", suit="♦", back_title="Why I Code", art="jasmine",
            face_title="Why I Code", face_sub="Mission",
            face_desc="Development has always stood out to me because I love problem solving, and I am passionate in learning how we can use technology to make the world a better place.",
            tags=["Impact", "Challenge", "Innovation"],
        ),
    ],
    about=[
        Card(
            pip="5", suit="♥", back_title="Passions", art="forget_me_not",
            face_title="Passions", face_sub="Music · Travel · Language",
            face_desc="Inspired by the natural world and by the ways people connect across cultures, through travel, language, and music. I care deeply about making spaces more accessible and inclusive, especially for disabled and immigrant communities.",
            tags=["Environment", "Nature", "Accessibility", "Connection"],
        ),
        Card(
            pip="4", suit="♥", back_title="Hobbies", art="buttercup",
            face_title="Hobbies", face_sub="Off the Clock",
            face_desc='· Playing cards and board games with friends (if you couldn\'t tell)\n\n· Going to farmers markets\n\n· Hiking and finding new trails\n\n· Attempting to play guitar',
            tags=["Concerts", "Building"],
        ),
        Card(
            pip="3", suit="♥", back_title="Cats", art="anemone",
            face_title="Cats", face_sub="My Two Joys",
            face_desc="I could not make a portfolio without showing my cats, hope you enjoy :)",
            tags=["Nino", "Habanero"],
            images=["/cats/nino.jpg", "/cats/habanero.jpg"],
        ),
        Card(
            pip="2", suit="♥", back_title="Volunteer", art="rose",
            face_title="Volunteer", face_sub="Community",
            face_desc="I enjoy giving back to my community by volunteering with Casa San Jose to teach ESL Pittsburgh, and serving with Northway Christian Community on their production team and in outreach efforts. ",
            tags=["ESL", "Teaching", "Music", "Outreach"],
        ),
    ],
)


# ── Vercel serverless handler ─────────────────────────────────────────────────

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        body = _portfolio.to_json().encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def log_message(self, *_):
        pass  # suppress default request logging


# ── Local dev server ──────────────────────────────────────────────────────────

if __name__ == "__main__":
    port = 8000
    server = HTTPServer(("localhost", port), handler)
    print(f"Running on http://localhost:{port}/api/portfolio")
    server.serve_forever()
