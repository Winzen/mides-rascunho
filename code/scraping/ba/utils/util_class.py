import hashlib
from io import BytesIO
import csv
import os
from io import StringIO
import json
import re
import unicodedata


class BoxFerramentas:

    @staticmethod
    def md5sum(file):
        """Calculate the md5 checksum of a file-like object without reading its
        whole content in memory.
        from io import BytesIO
        md5sum(BytesIO(b'file content to hash'))
        '784406af91dd5a54fbb9c84c2236595a'
        """
        m = hashlib.md5()
        while True:
            d = file.read(8096)
            if not d:
                break
            m.update(d)
        return m.hexdigest()

    def make_checksum(self, path: str) -> str:

        with open(path, 'rb') as csv_binary:
            arquivo = BytesIO(csv_binary.read())
            checksum = self.md5sum(arquivo)
            return checksum

    @staticmethod
    def csv_manager(path: str, rows: list, mode: str, fieldnames: list) -> None:

        with open(path, mode, newline='', encoding='utf-8') as file:
            # Create a CSV writer object
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            # Write the field names
            if mode == 'w':
                writer.writeheader()
            writer.writerows(rows)

    @staticmethod
    def abreviar(full_name: str):
        return ''.join([name[0].upper() for name in full_name.split()])

    @staticmethod
    def create_folders(name_folders: str) -> None:
        try:
            os.makedirs(name_folders)

        except FileExistsError:
            pass

    @staticmethod
    def csv_to_ram(rows: list, mode: str, fieldnames: list) -> str:

        csv_buffer = StringIO()

        writer = csv.DictWriter(csv_buffer, fieldnames=fieldnames)

        # Write the field names
        if mode == 'w':
            writer.writeheader()
        writer.writerows(rows)

        return csv_buffer.getvalue()

    @staticmethod
    def save_json(path: str, data: dict) -> None:
        with open(path, 'w', encoding="utf-8") as json_file:
            json.dump(data, json_file)

    @staticmethod
    def load_json(path: str) -> dict:

        with open(path, 'r', encoding="utf-8") as json_file:
            data = json.load(json_file)
            return data

    @staticmethod
    def register_erro(path: str,  data: dict) -> None:

        with open(path, 'a', newline='', encoding="utf-8") as f:
            # Create a DictWriter object with the field names as the keys of the dictionary
            writer = csv.DictWriter(f, fieldnames=list(data.keys()))

            # Write the dictionary as a row in the CSV file
            writer.writerow(data)

    @staticmethod
    def slugify(s):
        s = s.strip().lower()
        s = unicodedata.normalize("NFD", s)
        s = s.encode("ascii", "ignore")
        s = s.decode("utf-8")
        s = s.lower().strip()
        s = re.sub(r'[^\w\s-]', '', s)
        s = re.sub(r'[\s_-]+', '_', s)
        s = re.sub(r'^-+|-+$', '', s)
        return s

    def checksum_from_string(self, text: str, encoding: str = 'utf-8'):

        csv_bite = text.encode(encoding=encoding)
        checkum = self.md5sum(BytesIO(csv_bite))
        return checkum
