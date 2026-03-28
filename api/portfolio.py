import os, sys
sys.path.insert(0, os.path.dirname(__file__))

from http.server import BaseHTTPRequestHandler, HTTPServer
from models import Card, Contact, Portfolio
from schema import schema


# ── Static contact / header data ─────────────────────────────────────────────

_CONTACT = Contact(
    linkedin="https://linkedin.com/in/cassidy-spencer-cs",
    github="https://github.com/cassidyspen",
    email="cassidyspencer.dev@gmail.com",
    resume="https://docs.google.com/document/d/1HammHRgfye52DshjDyQpzzXeRrq_Pykq/edit?usp=sharing&ouid=102317221848885023723&rtpof=true&sd=true",
)

_CARDS_QUERY = """
{
    cards {
        pip suit section sort_order back_title art
        face_title face_sub face_sub2 face_desc
        link link_label images tags
    }
}
"""


def _build_portfolio() -> Portfolio:
    result = schema.execute_sync(_CARDS_QUERY)
    if result.errors:
        raise RuntimeError(f"GraphQL errors: {result.errors}")

    sections: dict[str, list[Card]] = {
        "experience": [], "projects": [], "tech": [], "about": []
    }
    for c in result.data["cards"]:
        card = Card(
            pip=c["pip"],
            suit=c["suit"],
            back_title=c["back_title"],
            art=c["art"],
            face_title=c["face_title"],
            face_sub=c["face_sub"],
            face_sub2=c["face_sub2"] or "",
            face_desc=c["face_desc"],
            tags=c["tags"] or [],
            link=c["link"] or "",
            link_label=c["link_label"] or "",
            images=c["images"] or [],
        )
        if c["section"] in sections:
            sections[c["section"]].append(card)

    return Portfolio(
        name="Cassidy Spencer",
        title="Software Engineer",
        location="Pittsburgh",
        contact=_CONTACT,
        experience=sections["experience"],
        projects=sections["projects"],
        tech=sections["tech"],
        about=sections["about"],
    )


# ── Vercel serverless handler ─────────────────────────────────────────────────

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        body = _build_portfolio().to_json().encode("utf-8")
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
