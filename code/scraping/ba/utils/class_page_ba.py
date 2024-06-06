from .class_webdrive import MyWebDrive
from .call_scripts_js import Scripts
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import os
import requests
import re
from test_scraper.extraction_BA.utils.util_class import BoxFerramentas


class Page(MyWebDrive, BoxFerramentas):

    def __init__(self, headless=False):
        super().__init__(headless=headless)

        # Waits
        self.wait = self.create_wait(60)
        self.scripts = Scripts(self.drive, self.wait)

        self.page_info = {
            "index_ano": int,
            "index_municipio": int,
            "index_entidade": int,
            "page": int
        }

    def create_wait(self, deplay: int):
        return WebDriverWait(self.drive, deplay)

    def update_page_info(self, index_ano: int,
                         index_municipio: int,
                         index_entidade: int,
                         page: int) -> None:

        self.page_info = {
            "index_ano": index_ano,
            "index_municipio": index_municipio,
            "index_entidade": index_entidade,
            "page": page
        }

    def get_ready(self):

        url = "https://www.tcm.ba.gov.br/controle-social/consulta-de-despesas/"
        self.drive.get(url)
        self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[name="pesquisar"]')))

    def try_pesquisar_js(self, index_ano: int,
                         index_municipio: int,
                         index_entidade: int,
                         page: int) -> bool:

        self.update_page_info(index_ano, index_municipio, index_entidade, page)

        for attempt in range(2):
            try:

                self.scripts.pesquisar_js(index_ano, index_municipio, index_entidade)
                self.wait.until(EC.visibility_of_element_located((By.ID, 'form_id')))
                if page > 1:
                    sleep(3)
                    self.scripts.select_page(page)

                return True

            except Exception as error:

                print(f"Falha ao Pesquisar\n{error}")
                sleep(2)
                continue

        return False

    def extract_row_docs(self) -> list[dict]:

        columns = ['data', 'município', 'id_empenho',
                   'entidade', 'orgão', 'unidade_orçamentaria', 'favorecido',
                   'elemento_despesa', 'fonte_recurso', 'valor']

        sleep(2)
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'table#tabelaResultado th')))
        elements = self.drive.find_elements(By.CSS_SELECTOR, 'table#tabelaResultado th')[1:]
        headers = [element.text.title().replace(' De ', ' de ') for element in elements]
        row_data = [self.get_elemnet_header(heade) for heade in headers]
        empenho_ids = self.get_atribute_from_elements(By.CSS_SELECTOR, 'form#form_id input.btn')
        row_data.insert(2, empenho_ids.copy())
        row_data = [list(row) for row in zip(*row_data)]

        rows = [dict(zip(columns, row)) for row in row_data]

        return rows

    def get_elemnet_header(self, column: str) -> list:
        elements = self.drive.find_elements(By.CSS_SELECTOR, f'table#tabelaResultado td[data-title="{column}:"]')
        elements_text = [element.text for element in elements]
        return elements_text

    def get_atribute_from_elements(self, by: By, selector: str, atribute: str = 'value') -> list:

        elements = self.drive.find_elements(by, selector)
        values_elements = [element.get_attribute(atribute) for element in elements]
        return values_elements

    def insert_identification_docs(self, docs: list) -> dict:

        identifications = [self.make_identification_path(row.values(), [row], list(row.keys())) for row in docs]
        docs = dict(zip(identifications, docs))
        return docs

    def make_identification_path(self, row_data: list, csv_rows: list, fieldnames: list) -> str:

        mescle = "-".join(row_data)
        checkum1 = self.checksum_from_string(mescle)
        csv_ram = self.csv_to_ram(csv_rows, "w", fieldnames)
        checkum2 = self.checksum_from_string(csv_ram)

        return f"{checkum1}-{checkum2}"

    def get_numbers_acess_docs(self, docs: dict):

        entrys = [list(docs.keys()).index(key) for key, value in docs.items() if
                  not self.make_entry_path_and_verify(value.values(), key)]
        sleep(2)
        return entrys

    def make_path_output_csv_and_entry(self, row_data: list, identification: str) -> list:

        row_data = list(row_data)
        data = row_data[0].split('/')
        row_path = [data[-1], data[1].lstrip("0"), row_data[1], identification]

        path_output_csv = os.path.join(self.path_input, *row_path)

        entry_csv = os.path.join(path_output_csv,
                                 f'entry_{row_data[2]}_{identification}.csv')

        geral_csv = os.path.join(path_output_csv,
                                 f'geral_{row_data[2]}_{identification}.csv')

        return [path_output_csv, entry_csv, geral_csv]

    def make_entry_path_and_verify(self, row_data: list, identification: str):

        path_output_csv, entry_csv, _ = self.make_path_output_csv_and_entry(row_data, identification)

        return os.path.exists(entry_csv)

    def try_extract_all_page(self, indexes: list, data: dict):

        docs_coletados = 0

        for index in indexes:
            # Esperar resultado da pesquisa
            self.wait.until(EC.visibility_of_element_located((By.ID, 'form_id')))
            # Acessar Dado
            self.try_acess_and_extract(index, data)
            sleep(2)

            if docs_coletados == 3:
                self.get_ready()
                self.try_pesquisar_js(**self.page_info)
                sleep(2)
                docs_coletados = 0

            docs_coletados += 1

    def try_acess_and_extract(self, index_doc: int, datas: dict):

        identifications = list(datas.keys())
        identification = identifications[index_doc]
        row = datas[identification]
        path_output_csv, entry_csv, geral_csv = self.make_path_output_csv_and_entry(row.values(),
                                                                                    identification)
        self.create_folders(path_output_csv)

        self.scripts.acessar_dados(index_doc)

        geral_data = self.get_geral_data()

        if len(geral_data):

            print("Coletando")

            self.csv_manager(geral_csv, [geral_data], 'w', list(geral_data.keys()))
            self.try_get_all_table(path_output_csv, identification)
            self.csv_manager(entry_csv, [row], 'w',  list(row.keys()))

            self.drive.execute_script("document.getElementById('btn-voltar ').click();")

            print("Voltando...")
            self.wait.until(EC.visibility_of_element_located((By.ID, 'form_id')))
            sleep(2)

    def get_geral_data(self) -> dict:

        columns = self.get_atribute_from_elements(By.CSS_SELECTOR, 'div.form-group label',
                                                  atribute='innerText')
        columns = [column.replace(':', '') for column in columns]

        values = self.get_atribute_from_elements(By.CSS_SELECTOR, 'div.form-group span',
                                                 atribute='innerText')[2:]

        row = dict(zip(columns, values))

        return row

    def try_get_all_table(self,
                          path_output_csv: str,
                          identification: str) -> None:

        raw_table = self.drive.find_elements(By.CSS_SELECTOR, "table")
        names_tables = self.try_get_name_tables()
        tables = dict(zip(names_tables, raw_table))
        if tables:
            for names_table, table in tables.items():
                self.get_table(names_table, table, path_output_csv, identification)

    def try_get_name_tables(self) -> list:

        html = self.drive.page_source
        all_h4 = re.findall(r"<h4>(.*?)</h4>\n.*\n.*<table", html)
        all_h4 = [self.slugify(text) for text in all_h4]
        return all_h4

    def get_table(self, name_table: str,
                  table: WebElement,
                  path_output_csv: str,
                  identification: str) -> None:

        row_table = []
        # Extract rows

        rows = table.find_elements(By.TAG_NAME, "tr")[1:]
        columns_names = table.find_elements(By.TAG_NAME, "th")
        columns_names = [column_name.text.lower() for column_name in columns_names]
        # Iterate through each row
        for row in rows:
            # Extract columns (cells)
            cols = row.find_elements(By.TAG_NAME, "td")
            row = [col.text for col in cols]
            row_table.append(dict(zip(columns_names, row)))
            # Extract and print cell text
        name_file = os.path.join(path_output_csv, f"{name_table}_{identification}.csv")
        self.csv_manager(name_file, row_table, "w", columns_names)

    def get_municipios_anos(self) -> list:

        municipios = self.get_texts_from_options('select#municipio > option')
        anos = self.get_texts_from_options('select#ano > option')

        return [municipios, anos]

    def get_texts_from_options(self, select: str) -> dict:

        options = self.drive.find_elements(By.CSS_SELECTOR, select)[1:]
        options = {n: [text.text, text.get_attribute('value').strip()] for n, text in enumerate(options)}
        return options

    @staticmethod
    def get_entidade_count(id_municipio: str) -> int:

        api_link = f'https://webservice.tcm.ba.gov.br/despesas/entidade?muni={id_municipio}'
        json = requests.get(api_link, verify=False).json()
        return len(json)

    def is_there_next_page(self):

        next_buttons = self.wait.until(EC.visibility_of_all_elements_located(
            (By.CSS_SELECTOR, 'form[class="form-page-numbers float-left"]')))

        return len(next_buttons) > 1
