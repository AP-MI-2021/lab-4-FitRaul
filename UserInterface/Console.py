from Service.produs_service import ProdusService
from Service.depozit_service import DepozitService


class Console:
    def __init__(self,
                 produs_service: ProdusService,
                 depozit_service: DepozitService):
        self.produs_service = produs_service
        self.depozit_service = depozit_service

    def show_menu(self):
        print('1. Adauga produs')
        print('2. Adauga depozit')
        print('3 Afisare produse cu text in nume')
        print('4 Afisare valoare produse dintr-un depozit')
        print('5 Export JSON')

    def run_console(self):

        while True:
            self.show_menu()
            opt = input('Optiunea: ')

            if opt == '1':
                self.handle_add_produs()
                self.handle_show_all(self.produs_service.get_all())
            elif opt == '2':
                self.handle_add_depozit()
                self.handle_show_all(self.depozit_service.get_all())
            elif opt == '3':
                self.handle_show_all(
                    self.produs_service.get_produse_with_text())
            elif opt == '4':
                self.handle_show_all(self.depozit_service.get_produse_depozit())
            elif opt == '5':
                self.handle_export()
            elif opt == 'x':
                break
            else:
                print('Optiune invalida.')

    def handle_add_produs(self):
        try:
            id_produs = input('Id-ul produsului: ')
            nume = input('Numele produsului: ')
            pret = int(input('Pretul produsului: '))


            self.produs_service.add_produs(id_produs, nume, pret)
        except ValueError as ve:
            print('Eroare validare:', ve)
        except KeyError as ke:
            print('Eroare ID:', ke)
        except Exception as ex:
            print('Eroare:', ex)

    def handle_show_all(self, entities):
        for entity in entities:
            print(entity)


    def handle_add_depozit(self):
        try:
            id_depozit = input('Id-ul depozitului: ')
            locatie = input('Locatia depozitului: ')
            produse = list(input('Id-urile produselor din depozit: '))



            self.depozit_service.add_depozit(id_depozit, locatie, produse)
        except ValueError as ve:
            print('Eroare validare:', ve)
        except KeyError as ke:
            print('Eroare ID:', ke)
        except Exception as ex:
            print('Eroare:', ex)


    def handle_export(self):
        try:
            filename = input('Numele fisierului pentru export: ')
            self.depozit_service.export_json(filename)
        except Exception as ex:
            print('Eroare:', ex)