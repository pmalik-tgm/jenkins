import unittest

import Model
import View


class Test(unittest.TestCase):
    def setUp(self):
        self.form = View.Ui_Form()
        self.model = Model.Model()

    def test_csv(self):
        # self.assertEqual(self.form.textBrowser.
        csvstring = self.model.readcsv("Book1.csv")
        self.assertEqual(csvstring, "A1\tB1\tC\t\n", "csv cant get read")

    def test_file_doesnt_end_with_csv(self):
        csvstring = self.model.readcsv("123.exe")
        self.assertEqual(csvstring, "The given Name is no valid csv file")

    def test_file_doesnt_end_with_anything(self):
        csvstring = self.model.readcsv("123")
        self.assertEqual(csvstring, "The given Name is no valid csv file")


    def test_file_doesnt_exist_but_ends_with_csv(self):
        csvstring = self.model.readcsv("Book.csv")
        self.assertEqual(csvstring, "The given Name is no valid csv file")

    def test_Hello_World(self):
        """
        Check if Tests work ;)
        :return:
        """
        self.assertEqual("Hello World","Hello World")
