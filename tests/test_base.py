import unittest
import warnings

from requests_pkcs12 import post

warnings.simplefilter('ignore')

AUTENTICA_URL = 'https://tes.pucomex.serpro/portal/api/autenticar'
PKCS12_FILENAME = 'C:\\Users\\25052288840\\Downloads\\132656_CERTIFICADO_TESTES_INTEGRADOS.p12'
PKCS12_PASSWORD = '123456'


class BaseTestCase(unittest.TestCase):

    def autenticar(self,
                   url=AUTENTICA_URL,
                   certificate=PKCS12_FILENAME,
                   password=PKCS12_PASSWORD,
                   headers={'Role-Type': 'DEPOSIT'}):
        return post(AUTENTICA_URL,
                    headers=headers,
                    pkcs12_filename=certificate,
                    pkcs12_password=password,
                    verify=False)

    def get_tokens(self, response):
        tokens = {}
        tokens['xcsrftoken'] = response.headers['X-CSRF-Token']
        tokens['authorization'] = response.headers['Set-Token']
        return tokens

    def _post(self,
              url: str,
              tokens: dict,
              cnpj: str,
              payload: dict,
              certificate=PKCS12_FILENAME,
              password=PKCS12_PASSWORD,
              ):
        headers = {'X-CSRF-Token': tokens['xcsrftoken'],
                   'authorization': tokens['authorization'],
                   'Cnpj-Representante': cnpj}
        r = post(url,
                 headers=headers,
                 json=payload,
                 pkcs12_filename=certificate,
                 pkcs12_password=password,
                 verify=False)
        return r


if __name__ == '__main__':
    unittest.main()
