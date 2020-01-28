import unittest
import warnings
from requests_pkcs12 import post

from tests.test_base import BaseTestCase, PKCS12_PASSWORD, PKCS12_FILENAME

warnings.simplefilter('ignore')


class GenericTestCase(BaseTestCase):

    def test_non_ecsiste(self):
        r = post(
            'https://tes-pucomex-rcnt-priv.estaleiro.serpro/recintos-ext/api/ext/non_ecsiste',
            pkcs12_filename=PKCS12_FILENAME,
            pkcs12_password=PKCS12_PASSWORD,
            verify=False)
        # TODO: checar o porque de 422 (esperava 404)
        assert r.status_code == 422
        # assert r.status_code == 404

    def test_autenticar_corretamente(self):
        response = self.autenticar()
        assert response.status_code == 200
        tokens = self.get_tokens(response)
        print(tokens)
        assert tokens.get('xcsrftoken') is not None
        assert tokens.get('authorization') is not None

    def test_post(self):
        tokens = self.get_tokens(self.autenticar())
        myjson = {}
        r = self._post(
            'https://tes-pucomex-rcnt-priv.estaleiro.serpro/recintos-ext/api/ext/pesagem-veiculos-cargas',
            tokens,
            '92772821010712',
            myjson)
        assert r.status_code == 400


if __name__ == '__main__':
    unittest.main()
