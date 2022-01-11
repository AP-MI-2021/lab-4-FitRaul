from typing import List
from Domain.produs import Produs
from Repository.repository import Repository


class ProdusService:
    def __init__(self,
                 produs_repository: Repository
                 ):
        self.produs_repository = produs_repository

    def add_produs(self, id_produs: str, nume: str, pret: int):

        produs = Produs(id_produs, nume, pret)
        self.produs_repository.create(produs)

    def get_all(self) -> List[Produs]:

        return self.produs_repository.read()

    def get_produse_with_text(self):
        text = input('Introduceti textul din nume: ')
        a='Nu exista produse pentru textul cautat'
        ok = 0
        result = []
        produse = self.produs_repository.read()
        for produs in produse:
            if text.lower() in produs.nume.lower():
                ok = ok + 1
                result.append(produs)
        if ok == 0:
            result.append(a)

        return result

