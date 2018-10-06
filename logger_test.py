import unittest
from logger import Logger

class LoggerTest(unittest.TestCase):

    def setUp(self):
        self.filename = "first_line.txt"
        self.file = open(self.filename)
        self.ref = self.file.readline()

    def test_metadata_function(self):
        new_log = Logger("test.txt")
        new_log.write_metadata(10000, 0.20, 0.90, 'Ebola', 0.25)

        file_created = open("test.txt")

        assert file_created.readline() == self.ref
