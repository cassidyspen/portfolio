import json
from dataclasses import dataclass, field
from typing import List


@dataclass
class Contact:
    linkedin: str
    github: str
    email: str
    resume: str = ""

    def to_dict(self) -> dict:
        return {
            "linkedin": self.linkedin,
            "github": self.github,
            "email": self.email,
            "resume": self.resume,
        }


@dataclass
class Card:
    pip: str
    suit: str
    back_title: str
    art: str
    face_title: str
    face_sub: str
    face_desc: str
    tags: List[str]
    face_sub2: str = ""
    link: str = ""
    link_label: str = ""
    images: List[str] = field(default_factory=list)

    def to_dict(self) -> dict:
        return {
            "pip": self.pip,
            "suit": self.suit,
            "backTitle": self.back_title,
            "art": self.art,
            "faceTitle": self.face_title,
            "faceSub": self.face_sub,
            "faceSub2": self.face_sub2,
            "faceDesc": self.face_desc,
            "tags": self.tags,
            "link": self.link,
            "linkLabel": self.link_label,
            "images": self.images,
        }


class Portfolio:
    def __init__(self, name: str, title: str, location: str, contact: Contact,
                 experience: List[Card], projects: List[Card],
                 tech: List[Card], about: List[Card]):
        self.name = name
        self.title = title
        self.location = location
        self.contact = contact
        self.experience = experience
        self.projects = projects
        self.tech = tech
        self.about = about

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "title": self.title,
            "location": self.location,
            "contact": self.contact.to_dict(),
            "experience": [c.to_dict() for c in self.experience],
            "projects": [c.to_dict() for c in self.projects],
            "tech": [c.to_dict() for c in self.tech],
            "about": [c.to_dict() for c in self.about],
        }

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), ensure_ascii=False)
