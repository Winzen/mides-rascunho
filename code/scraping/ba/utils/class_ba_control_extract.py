from .class_page_ba import Page
from .util_class import BoxFerramentas
from time import sleep
import os


class BaControlExtract(BoxFerramentas):

    def __init__(self, headless=True):

        self.page = Page(headless=headless)
        self.path_json = os.path.join(os.getcwd(), "register", "checkpoint.json")
        self.path_erros = os.path.join(os.getcwd(), "register", "erros.csv")
        self.checkpoint = self.load_json(self.path_json)
        self.check = False

    def try_extract(self) -> None:

        try:

            self.try_extract_all_years()

        finally:

            sleep(5)
            self.page.drive.quit()
            print("Fechado com cuidado")

    def try_get_municipio_anos(self):

        self.page.get_ready()
        return self.page.get_municipios_anos()

    def try_extract_all_years(self):

        municipios, anos = self.try_get_municipio_anos()

        for index_ano in list(anos.keys()):

            if self.checkpoint['index_ano'] != index_ano and not self.check:
                continue

            for index_municipio in municipios.keys():

                if self.checkpoint['index_municipio'] != index_municipio and not self.check:
                    continue

                entidade_count = self.page.get_entidade_count(municipios[index_municipio][1])

                for index_entidade in range(entidade_count):

                    if self.checkpoint['index_entidade'] != index_entidade and not self.check:
                        continue

                    self.check = True

                    self.try_get_full_entidade(municipios,
                                               anos,
                                               index_ano,
                                               index_municipio,
                                               index_entidade)

    def try_extract_page(self, index_ano: int,
                         index_municipio: int,
                         index_entidade: int,
                         page: int) -> bool:

        self.checkpoint = {"index_ano": index_ano,
                           "index_municipio": index_municipio,
                           "index_entidade": index_entidade,
                           "page": page}

        for attempt in range(3):
            try:
                self.page.get_ready()
                self.page.try_pesquisar_js(index_ano, index_municipio, index_entidade, page)
                docs = self.page.extract_row_docs()
                docs = self.page.insert_identification_docs(docs)
                numbes_to_acess = self.page.get_numbers_acess_docs(docs)
                self.page.try_extract_all_page(numbes_to_acess, docs)
                self.save_json(self.path_json, self.checkpoint)
                return True

            except Exception as error:
                print(f"{error}\n\nTentativa de numero: {attempt + 1}/3\nFalhou!")

        self.register_erro(self.path_erros, self.checkpoint)
        return False

    def try_get_full_entidade(self, municipios: dict,
                              anos: dict,
                              index_ano: int,
                              index_municipio: int,
                              index_entidade: int) -> None:

        page = 1

        print(
            f"Tentando pesquisar\nMunicipio: {municipios[index_municipio]} | Ano: {anos[index_ano]} | "
            f"Entidade: {index_entidade}")

        while True:

            next_page = self.try_extract_page(index_ano,
                                              index_municipio,
                                              index_entidade,
                                              page)

            if next_page and self.page.is_there_next_page():

                print(
                    f"Nome: {municipios[index_municipio]} | Pagina: {page} | Entidade: {index_entidade}\nColeta com "
                    f"Sucesso!\n{'--' * 30}")

                page += 1

                self.page.scripts.select_page(page)

            else:

                break
