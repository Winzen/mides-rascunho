from .class_page_ba import Page
from .util_class import BoxFerramentas
from time import sleep, time
import os


class BaControlExtract2(BoxFerramentas):

    def __init__(self, headless=True):

        self.page = Page(headless=headless)
        self.path_json = os.path.join(os.getcwd(), "register", "checkpoint.json")
        self.path_erros = os.path.join(os.getcwd(), "register", "erros.csv")
        self.checkpoint = self.load_json(self.path_json)
        self.check = False

    def mult_tab(self, index_docs):

        windons_number = len(index_docs)
        for x in range(windons_number - 1):
            self.page.drive.execute_script("window.open('');")

        comandos = [self.entrar_site,
                    lambda: self.page.try_pesquisar_js(1, 0, 0, 1),
                    lambda index: self.page.scripts.acessar_dados(index)]

        for n_comando, comando in enumerate(comandos):

            for x in range(windons_number):
                self.page.drive.switch_to.window(self.page.drive.window_handles[x])

                if n_comando in [2]:
                    comando(index_docs[x])
                else:
                    comando()
        # for tab in range(1, 6):
        #     self.page.drive.get("https://www.tcm.ba.gov.br/controle-social/consulta-de-despesas/")
        #     self.page.drive.switch_to.window(self.page.drive.window_handles[tab])
        #     # self.page.drive.get("https://www.tcm.ba.gov.br/controle-social/consulta-de-despesas/")
        #     sleep(2)
        # sleep(2)
        print("Sucesso")

    def entrar_site(self):

        self.page.drive.get("https://www.tcm.ba.gov.br/controle-social/consulta-de-despesas/")

    def try_extract(self, index_docs) -> None:

        try:

            self.mult_tab(index_docs)


        finally:

            sleep(2)
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
