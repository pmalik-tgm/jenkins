import unittest

import Model
import View


class Test(unittest.TestCase):

    def setUp(self):
        self.form  = View.Ui_Form()
        self.model = Model.Model()


    def test_csv(self):
        #self.assertEqual(self.form.textBrowser.
        csvstring = self.model.readcsv("Book1.csv")
        self.assertEqual(csvstring,"A1\tB1\tC\t\n","csv cant get read")

    def test_invalid_csv(self):
        pass
        
