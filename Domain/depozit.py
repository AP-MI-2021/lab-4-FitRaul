from dataclasses import dataclass

from Domain.entity import Entity


@dataclass
class Depozit(Entity):
    locatie: str
    produse: list
