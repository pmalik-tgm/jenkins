import os
import sys
import View, Model

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget


class Controller(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.form = View.Ui_Form()
        self.form.setupUi(self);
        self.button = self.form.pushButton
        self.model = Model.Model()
        self.text = "Press convert to get the content of the given csv file"
        self.connect_button()

    def connect_button(self):
        self.button.clicked.connect(self.button_listener)

    def button_listener(self):
        filename = self.form.lineEdit.text()
        self.text = self.model.readcsv(filename)
        self.update()

    def update(self):
        self.form.textBrowser.setText(self.text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    c = Controller()
    c.show()
    sys.exit(app.exec_())
