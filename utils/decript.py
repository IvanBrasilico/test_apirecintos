import json
import os
from base64 import b64decode
from pprint import pprint
from zipfile import ZipFile

import click
from Crypto.Cipher import AES

KEY = 'MDEyMzQ1Njc4OWFiY2RlZkZFRENCQTk4NzY1NDMyMTA='
FILENAME = 'res-20200200000000058-1.json'
OUTFILENAME = 'decripted.json'


def decrypt(ciphertext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext.rstrip(b"\0")


def decrypt_file(filename, out_filename, key):
    with open(filename, 'rb') as fo:
        ciphertext = fo.read()
    dec = decrypt(ciphertext, key)
    with open(out_filename, 'wb') as fo:
        fo.write(dec)


def unzip_file(filename):
    """Extrai arquivo json do zip e apaga o zip original."""
    with ZipFile(filename, 'r') as zipObj:
        name = zipObj.namelist()[0]
        zipObj.extract(name)
    os.remove(filename)
    json_filename = filename[:-4]
    if os.path.exists(json_filename):
        os.remove(json_filename)
    os.rename(name, json_filename)
    return json_filename


def get_json_file(filename):
    """Coloca conteúdo do arquivo JSON em uma string."""
    with open(filename) as json_in:
        eventos = json.load(json_in)
    return eventos


@click.command()
@click.option('--arquivo', default=FILENAME,
              help='Nome do arquivo de Evento baixado da API')
@click.option('--key', default=KEY,
              help='Chave de criptografia')
@click.option('--saida', default=OUTFILENAME,
              help='Nome do arquivo de Saída. Padrão %s ' % OUTFILENAME)
def decript(arquivo, saida, key):
    key = b64decode(key)
    out_filename = saida + '.zip'  # Gera um zip temporário
    decrypt_file(arquivo, out_filename, key)
    json_filename = unzip_file(out_filename)
    eventos = get_json_file(json_filename)
    pprint(eventos)


if __name__ == '__main__':
    decript()
