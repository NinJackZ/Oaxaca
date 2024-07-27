from driver import *
from app.login import hash
import unittest

class TestStringMethods(unittest.TestCase):
    
    def test_get_data(self):
        with app.app_context():
            Menu.query.get(1)

    def test_hash(self):
        assert hash("password") == "c0067d4af4e87f00dbac63b6156828237059172d1bbeac67427345d6a9fda484"

if __name__ == '__main__':
    unittest.main()