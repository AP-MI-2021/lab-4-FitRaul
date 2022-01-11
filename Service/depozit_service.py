from typing import List
import json
from Domain.depozit import Depozit
from Repository.repository import Repository



class DepozitService:
    def __init__(self,
                 depozit_repository: Repository,
                 produs_repository: Repository):
        self.depozit_repository = depozit_repository
        self.produs_repository = produs_repository


    def add_depozit(self,
                  id_depozit: str,
                  locatie: str,
                  produse: list
                  ):

        depozit = Depozit(id_depozit, locatie, produse)
        self.depozit_repository.create(depozit)

    def get_all(self) -> List[Depozit]:
        """
        :return: o lista cu toti colaboratorii
        """
        return self.depozit_repository.read()

    def get_produse_depozit(self):
        result=[]
        id=input('Introduceti id-ul depozitului: ')
        valoare = 0
        produse = self.produs_repository.read()
        depozite = self.depozit_repository.read()
        for depozit in depozite:
            if depozit.id_entity == id:
                for produs in produse:
                    nr = 0
                    if produs.id_entity in depozit.produse:
                        nr = depozit.produse.count(produs.id_entity)
                        valoare = valoare + nr * produs.pret
        result.append(valoare)
        return result

    def export_json(self, export_filename):
        result = {}
        produse = self.produs_repository.read()
        depozite = self.depozit_repository.read()
        for produs in produse:
            product_locations = [depozit.id_entity for depozit in depozite if produs.id_entity in depozit.produse]
            result[produs.nume] = [self.depozit_repository.read(id_entity).locatie for id_entity in product_locations]

        with open(export_filename, 'w') as f:
            json.dump(result, f, indent=2)






















