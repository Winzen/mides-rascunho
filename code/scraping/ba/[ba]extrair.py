from utils.class_webdrive import MyWebDrive
from utils.call_scripts_js import Scripts
import base64
import pandas as pd
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from urllib3 import PoolManager, disable_warnings, exceptions, Timeout
from time import sleep, time
import concurrent.futures
from bs4 import BeautifulSoup
import re
from utils.util_class import BoxFerramentas
import os
from more_itertools import batched
from typing import Iterable
import asyncio
import aiohttp
from aiohttp.client import ClientSession
from urllib.parse import urlencode, urlunparse


class TokenManage:

    def __init__(self, drive: WebElement, wait: WebDriverWait, script: Scripts):
        self.drive = drive
        self.wait = wait
        self.script = script


class SlotExtration:

    def __init__(self, row: pd.DataFrame, link: str = "", response=None):

        self.row = row
        self.link = link
        self.response = response


def get_html_document(row: pd.DataFrame, token: str) -> SlotExtration:
    base_url = "https://www.tcm.ba.gov.br/controle-social/consulta-de-despesas/detalhe-despesa/?"

    ano = row.dataempenho.split("-")[0]

    fields = {
        "entidade": row.cd_unidade,
        "txtEntidade": row.unidade,
        "ano": ano,
        "orgao": row.cd_orgao,
        "unidOrca": row.cd_unidadeorcamentaria,
        "fase": "E",
        "empenho": row.empenho,
        "nuDocumento": "",
        "valor": row.valor,
        "data": base64.b64encode(row.dataempenho.encode('utf-8')),
        "g-recaptcha-response": token,
        "action": "validate_captcha",
        "pesquisar": row.empenho
    }

    query_string = urlencode(fields)
    url = base_url + query_string

    return SlotExtration(row, url)
   

def wait_tokens(old_value: int | str, tokem_manege: TokenManage) -> bool:
    present_value = tokem_manege.drive.find_element(By.CSS_SELECTOR, '.id_validation21').get_attribute("value")
    return present_value != old_value


def make_list_chunks(values: list | Iterable, chunk_size: int = 2000) -> list:
    resquet_in_chunks = [chunk for chunk in batched(values, chunk_size)]
    return resquet_in_chunks


def try_get_name_tables(suop_html: BeautifulSoup) -> list:
    all_h4 = re.findall(r"<h4>\n(.*?)\n</h4>\n.*\n.*\n<table", suop_html.prettify().replace(" ", ""))
    all_h4 = [BoxFerramentas.slugify(text) for text in all_h4]
    return all_h4


def try_get_dados_geral(suop_html: BeautifulSoup, path: str) -> bool:
    columns = suop_html.select("div.form-group label")
    columns = [column.text.replace(':', '').strip() for column in columns if column is not None]

    values = suop_html.select("div.form-group span")[2:]
    values = [value.text.strip() for value in values if value is not None]

    row = dict(zip(columns, values))
    name_file = os.path.join(path, f"geral.csv")

    if row:
        os.makedirs(path, exist_ok=True)

        BoxFerramentas.csv_manager(name_file, [row], "w", list(row.keys()))

        return True
    
    return False


def try_get_all_table(suop_html: BeautifulSoup,
                      path_output_csv: str) -> None:

    raw_table = suop_html.select("table")
    names_tables = try_get_name_tables(suop_html)
    tables = dict(zip(names_tables, raw_table))
    if tables:
        for names_table, table in tables.items():
            get_table(names_table, table, path_output_csv)


def get_table(name_table: str,
              table: BeautifulSoup,
              path_output_csv: str) -> None:
    row_table = []
    # Extract rows
    rows = table.find_all("tr")[1:]
    columns_names = table.find_all("th")
    columns_names = [column_name.text.lower() for column_name in columns_names]
    # Iterate through each row
    for row in rows:
        # Extract columns (cells)
        cols = row.find_all("td")
        row = [col.text for col in cols]
        row_table.append(dict(zip(columns_names, row)))
        # Extract and print cell text
    name_file = os.path.join(path_output_csv, f"{name_table}.csv")
    BoxFerramentas.csv_manager(name_file, row_table, "w", columns_names)


def extrair(slot_extration: SlotExtration) -> SlotExtration|bool:
    
    try:
        ano, mes, _ = slot_extration.row.dataempenho.split("-")
        base_path = os.path.join(os.getcwd(), "input_test_mult_thread", ano, mes.lstrip("0"),
                                slot_extration.row.id_municipio, slot_extration.row.checksum)

        soup = BeautifulSoup(slot_extration.response, 'html.parser')
        if try_get_dados_geral(soup, base_path):
            try_get_all_table(soup, base_path)

            return slot_extration
        
        return False

    except:
        return False

def get_html_source(slot_extration: SlotExtration) -> SlotExtration|bool:
    
    try:
        base_url = "https://www.tcm.ba.gov.br/controle-social/consulta-de-despesas/detalhe-despesa/"

        response = http.request('GET', slot_extration.link)
        slot_extration.response = response.data.decode(encoding="utf-8")
        
        return slot_extration
    except:
        return False

def get_tokens(token_manage: TokenManage) -> list:
    token_manage.script.carregar_tokens()

    old_value_token = token_manage.drive.find_element(By.CSS_SELECTOR, '.id_validation21').get_attribute('value')
    token_manage.wait.until(lambda x: wait_tokens(old_value_token, token_manage))

    tokens = [token.get_attribute("value")
              for token in token_manage.drive.find_elements(By.CSS_SELECTOR, '.slot_tokens input')]

    return tokens


def create_drive_generation_token(number: int) -> TokenManage|None:

    drive = MyWebDrive(headless=True).drive

    try:
        
        wait = WebDriverWait(drive, 30)
        url = "https://www.tcm.ba.gov.br/controle-social/consulta-de-despesas/"

        scripts = Scripts(drive, wait)

        drive.get(url)

        wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[name="pesquisar"]')))

        scripts.create_slot_tokens()

        sleep(1)
        token_manege = TokenManage(drive, wait, scripts)

        print(f"Gerador de tokens numero {number} criado!")

        return token_manege
    
    except Exception as error:
        print(f"Falha ao criar Gerador de tokens numero {number}")
        drive.quit()
        return None


def quit_all_maneges(token_manage: TokenManage) -> None:
    token_manage.drive.quit()
    return None


def create_token_mult_thread(token_maneges: list) -> list:
    with concurrent.futures.ThreadPoolExecutor() as executor:
        all_tokens = [tokens for tokens in executor.map(get_tokens, token_maneges)]

    all_tokens = [token for row_tokens in all_tokens for token in row_tokens]

    return all_tokens


def quit_all_mult_thread(token_maneges: list) -> None:

    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(quit_all_maneges, token_maneges)

    return None


async def download_link(slot_extration: SlotExtration, session: ClientSession) -> SlotExtration:
    
    # try:
    async with session.get(slot_extration.link, timeout=60) as response:
    
            result = await response.text()
            slot_extration.response = result
            return slot_extration
    
    # except Exception as erro:
    #     return erro

async def download_all(rows: list):
    my_conn = aiohttp.TCPConnector(limit=21, ssl=False)
    # timeout = aiohttp.ClientTimeout(total=10)
    async with aiohttp.ClientSession(connector=my_conn) as session:
        slots = []
        for row in rows:
            slot = asyncio.ensure_future(download_link(slot_extration=row, session=session))
            slots.append(slot)
        await asyncio.gather(*slots, return_exceptions=True)# the await must be nest inside of the session
    return slots


def salvar(df: pd.DataFrame, checksums: list, name_csv: str) -> None:
    
    print("Salvado Coletada...")
    mask = df.checksum.isin(checksums)
    df.loc[mask, ["coletado"]] = "True"
    df.to_csv(name_csv, index=False)
    print(f"Coleta salva!\n{'-' * 30}")


if __name__ == '__main__':

    # name_csv = "anos_extrair/empenhos_2021_coletados.csv"
    name_csv = "anos_extrair/empenhos_2021_coletados_new.csv"

    chuck_size = 21

    timeout = Timeout(total=20)
    http = PoolManager(maxsize=chuck_size, cert_reqs='CERT_NONE', block=True, timeout=timeout)
    disable_warnings(exceptions.InsecureRequestWarning)
    

    checksums = []

    tokens_creates = []

    while True:

        try:

            print(f"Iniciado componentes\n")

            rows = pd.read_csv(name_csv, dtype=str)

            coleta = rows[rows.coletado == "False"]

            with concurrent.futures.ThreadPoolExecutor() as executor:
                tokens_creates = [token_create 
                for token_create in executor.map(create_drive_generation_token, list(range(1)))]

            if None in tokens_creates:
                quit_all_mult_thread(tokens_creates)
                raise Exception("Falha ao criar geradores de tokens")

            try:

                print("Iniciando extração")

                start_time = time()

                chunks = make_list_chunks(coleta.itertuples(), chunk_size=chuck_size)

                for n_chunk, chunk in enumerate(chunks):

                    print(f"{n_chunk}/{len(chunks)}")

                    start_time = time()

                    tokens = create_token_mult_thread(tokens_creates)
                    
                    index_minino = min(len(tokens), len(chunk))

                    slots_extration = [get_html_document(chunk[n], tokens[n])
                                        for n in range(index_minino)]
                    
                    # tasks = asyncio.run(download_all(slots_extration))
                    
                    # tasks_done = [slot.result() for slot in tasks if not slot.exception()]

                    with concurrent.futures.ThreadPoolExecutor() as executor:
                        tasks_done = [slot for slot in executor.map(get_html_source, slots_extration) if slot]
                    
                    print(f"Dados prontos para serem extraidos : {len(tasks_done)}")

                    with concurrent.futures.ThreadPoolExecutor() as executor:
                        tasks_done = [slot for slot in executor.map(extrair, tasks_done) if slot]

                    print(f"Dados extraidos com sucesso : {len(tasks_done)}")
                    
                    print(f"Duração da execução: {(time() - start_time) / 60:.2f}\n{'-' * 30}")
                    
                    checksums += [slot.row.checksum for slot in tasks_done]

                    if (n_chunk + 1) % 20 == 0:
                        
                        salvar(rows, checksums, name_csv)
                        checksums.clear()
               
                break

            finally:

                quit_all_mult_thread(tokens_creates)
                salvar(rows, checksums, name_csv)
                checksums.clear()
                print("Fechei todos os navegadores")

        except Exception as erro:
            print(f"{erro}\nReiniciando..")
