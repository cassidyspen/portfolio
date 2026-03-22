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
            pip="A", suit="♠", back_title="PNC Software Developer", art="flower",
            face_title="Software Developer", face_sub="PNC Bank · Pittsburgh",
            face_sub2="Nov 2024 - Present",
            face_desc="Eliminated manual audit workflows by building FastAPI microservices and SQL pipelines used by 400+ employees. Delivered 20+ releases and resolved 100+ security vulnerabilities.",
            tags=["Python", "SQL Server", "OpenShift", "Jenkins", "FastAPI"],
        ),
        Card(
            pip="K", suit="♠", back_title="CGI Software Developer", art="rose",
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
            pip="J", suit="♠", back_title="Computer Science Tutor and Lab Assistant", art="leaf",
            face_title="CS Tutor + Lab Assistant", face_sub="University of San Diego",
            face_sub2="Feb 2022 - May 2023",
            face_desc="Assisted undergraduate students with coursework and programming assignments by helping them break down complex problems and develop effective solutions. ",
            tags=["Python", "Operating Systems", "Networking", "Algorithms", "VS Code"],
        ),
    ],
    projects=[
        Card(
            pip="10", suit="♣", back_title="re·locate", art="leaf",
            face_title="re·locate", face_sub="relocatecost.com",
            face_desc="Built a cost of living calculator by using prompt engineering with Anthropic Claude and ChatGPT to compare living costs with 8000+ cities.",
            tags=["Vanilla JS", "Vercel", "CSS", "RapidAPI", "HTML"],
            link="https://relocatecost.com",
        ),
        Card(
            pip="9", suit="♣", back_title="This Portfolio", art="rose",
            face_title="This Portfolio", face_sub="cassidyspencer.dev",
            face_desc="You're looking at it! Playing card themed portfolio hosted on Vercel with Python and React",
            tags=["React", "Vite", "Python", "Vercel"],
            link="https://github.com/cassidyspen/portfolio",
            link_label="View Source ↗",
        ),
    ],
    tech=[
        Card(
            pip="8", suit="♦", back_title="Languages & Stack", art="clover",
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
            pip="6", suit="♦", back_title="Why I Code", art="leaf",
            face_title="Why I Code", face_sub="Mission",
            face_desc="Development has always stood out to me because I love problem solving, and I am passionate in learning how we can use technology to make the world a better place.",
            tags=["Impact", "Challenge", "Innovation"],
        ),
    ],
    about=[
        Card(
            pip="5", suit="♥", back_title="Passions", art="tulip",
            face_title="Passions", face_sub="Music · Travel · Language",
            face_desc="Spanish minor — love connecting across cultures. Always planning the next trip.",
            tags=["Music", "Travel", "Spanish"],
        ),
        Card(
            pip="4", suit="♥", back_title="Hobbies", art="music",
            face_title="Hobbies", face_sub="Off the Clock",
            face_desc='Concert-going, exploring new cities, building side projects that start as "just an idea".',
            tags=["Concerts", "Building"],
        ),
        Card(
            pip="3", suit="♥", back_title="Cats", art="cat",
            face_title="Cats", face_sub="Chief Supervisors",
            face_desc="Proudly owned by cats. They supervise all coding sessions and have strong opinions.",
            tags=["Important", "Supervisors"],
        ),
        Card(
            pip="2", suit="♥", back_title="Volunteer", art="sunflower",
            face_title="Volunteer", face_sub="Community & Accessibility",
            face_desc="Giving time to causes that matter — community and accessibility close to my heart.",
            tags=["Community", "Accessibility"],
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
