import unittest
from classes.parser import Parser

class TestParser(unittest.TestCase):
    def setUp(self):
        self.command = "your_app --log log.txt --verbose 3 --script ascript.scr --debug true --format JSON"
        self.parser = Parser()
        self.arrForm = ['-', '-', 'l', 'o', 'g', ' ', 'l', 'o', 'g', '.', 't', 'x', 't', ' ', '-', '-', 'v', 'e', 'r', 'b', 'o', 's', 'e', ' ', '3', ' ', '-', '-', 's', 'c', 'r', 'i', 'p', 't', ' ', 'a', 's', 'c', 'r', 'i', 'p', 't', '.', 's', 'c', 'r', ' ', '-', '-', 'd', 'e', 'b', 'u', 'g', ' ', 't', 'r', 'u', 'e', ' ', '-', '-', 'f', 'o', 'r', 'm', 'a', 't', ' ', 'J', 'S', 'O', 'N']
        self.jsonObject = {
            "log": str, 
            "verbose": int,
            "script": str,
            "debug": bool,
            "format": str,
            }

    def test_can_extract_app_name(self):
        result = self.parser.getApp(self.command)
        self.assertEqual(result, "your_app")

    def test_can_populate_data_structure(self):
        result = self.parser.getArrForm(self.command)
        self.assertEqual(result, self.arrForm)

    def test_can_make_sub_arrays(self):
        step1 = self.parser.getArrForm(self.command)
        result = self.parser.makeJSON(step1)
        self.assertEqual(result, self.jsonObject)