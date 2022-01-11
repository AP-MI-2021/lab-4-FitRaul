from Repository.json_repository import JsonRepository
from Service.produs_service import ProdusService
from Service.depozit_service import DepozitService

from UserInterface.Console import Console


def main():
    produs_repository = JsonRepository('produse.json')
    depozit_repository = JsonRepository('depozite.json')

    produs_service = ProdusService(produs_repository)
    depozit_service = DepozitService(depozit_repository, produs_repository)

    console = Console(produs_service, depozit_service)
    console.run_console()



if __name__ == '__main__':
    main()