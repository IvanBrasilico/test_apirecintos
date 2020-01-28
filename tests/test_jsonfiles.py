import json
import os
import unittest
from tests.test_base import BaseTestCase

JSONDIR = 'json'

POST_URL = 'https://tes-pucomex-rcnt-priv.estaleiro.serpro/recintos-ext/api/ext/'


class JsonTestCase(BaseTestCase):

    def get_json_filenames(self):
        return [os.path.join(JSONDIR, filename)
                for filename in os.listdir(JSONDIR)
                if '.json' in filename]

    def test_post(self):
        tokens = self.get_tokens(self.autenticar())
        for json_filename in self.get_json_filenames():
            with open(json_filename) as infile:
                payload = json.load(infile)
            evento_url = POST_URL + json_filename[len(JSONDIR) + 1:-5]
            r = self._post(evento_url,
                           tokens=tokens,
                           cnpj='92772821010712',
                           payload=payload
                           )
            print(evento_url)
            print(tokens)
            print(payload)
            print(r.status_code)
            print(r.text)
            for k, v in r.headers.items():
                print('%s: %s' % (k, v))
            assert r.status_code == 201


if __name__ == '__main__':
    unittest.main()
