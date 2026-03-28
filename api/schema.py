import os, sys
sys.path.insert(0, os.path.dirname(__file__))

import strawberry
from strawberry.schema.config import StrawberryConfig
from typing import Optional
from db import get_connection


@strawberry.type
class CardType:
    id: int
    pip: str
    suit: str
    section: str
    sort_order: int
    back_title: str
    art: str
    face_title: str
    face_sub: str
    face_sub2: Optional[str]
    face_desc: str
    link: Optional[str]
    link_label: Optional[str]
    images: Optional[list[str]]
    tags: Optional[list[str]]


@strawberry.type
class Query:
    @strawberry.field
    def cards(self, section: Optional[str] = None) -> list[CardType]:
        conn = get_connection()
        with conn.cursor() as cur:
            if section:
                cur.execute(
                    "SELECT * FROM cards WHERE section = %s ORDER BY sort_order",
                    (section,),
                )
            else:
                cur.execute("SELECT * FROM cards ORDER BY section, sort_order")
            rows = cur.fetchall()
        return [CardType(**row) for row in rows]


schema = strawberry.Schema(
    query=Query,
    config=StrawberryConfig(auto_camel_case=False),
)
