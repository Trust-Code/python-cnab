
import unittest

from cnab240 import Cnab240
from cnab240 import errors


class TestCnab240(unittest.TestCase):
    def setUp(self):
        pass

    def test_escrita_vazia(self):
        cnab240 = Cnab240()
        with self.assertRaises(Exception):
            unicode(cnab240)

if __name__ == '__main__':
    unittest.main()
