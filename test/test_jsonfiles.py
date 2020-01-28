import json
import os
from .test_endpoints import BaseTestCase


JSONDIR = '../json'

urls_eventos = {
    'pesagem-veiculos-cargas.json': ''
}


class JsonTestCase(BaseTestCase):

    def get_json_filenames(self):
        return [filename for filename in
                      os.listdir(JSONDIR)
                      if '.json' in filename]

    def test_post(self):
        for json_filename in self.get_json_files():
            with open(json_filename) as infile:
                payload = json.loads(infile)

            self._post(evento_url, )



