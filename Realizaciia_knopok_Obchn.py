from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QPushButton, QLabel, QHBoxLayout
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import sys


class KalkulyatorUI(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # настройка окна
        self.setWindowTitle("Калькулятор")
        self.setGeometry(100, 100, 320, 420)
        vert_raskladka = QVBoxLayout()

        # Название раздела "Обычный"
        self.section_label = QLabel("Обычный")
        self.section_label.setFont(QFont("Arial", 14, QFont.Bold))
        self.section_label.setAlignment(Qt.AlignCenter)
        vert_raskladka.addWidget(self.section_label)

        # дисплей калькулятора
        self.displey = QLabel("0")
        self.displey.setFont(QFont("Arial", 24))  # шрифт для дисплея
        self.displey.setStyleSheet("border: 2px solid black; min-height: 50px; background: white;")
        self.displey.setAlignment(Qt.AlignRight)
        vert_raskladka.addWidget(self.displey)

        # сетка кнопок
        setka_knopok = QGridLayout()
        knopki = [
            ('%', 0, 0), ('CE', 0, 1), ('C', 0, 2), ('⌫', 0, 3),
            ('1/x', 1, 0), ('x²', 1, 1), ('√x', 1, 2), ('÷', 1, 3),
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('×', 2, 3),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('+', 4, 3),
            ('+/-', 5, 0), ('0', 5, 1), ('.', 5, 2), ('=', 5, 3)
        ]

        self.knopki_dict = {}
        for tekst, stroka, stolbec in knopki:
            knopka = QPushButton(tekst)
            knopka.setFont(QFont("Arial", 18))
            knopka.setFixedSize(60, 60)
            knopka.clicked.connect(self.nazhat_knopku)
            self.knopki_dict[tekst] = knopka
            setka_knopok.addWidget(knopka, stroka, stolbec)

        vert_raskladka.addLayout(setka_knopok)
        self.setLayout(vert_raskladka)
        self.last_input = ""

    def nazhat_knopku(self):
        knopka = self.sender()
        tekst = knopka.text()

        if tekst.isdigit() or tekst == '.':
            if self.displey.text() == "0":
                self.displey.setText(tekst)
            else:
                self.displey.setText(self.displey.text() + tekst)
        elif tekst in ['+', '-', '×', '÷']:
            self.last_input = self.displey.text()
            self.displey.setText(self.displey.text() + f' {tekst} ')
        elif tekst == '=':
            try:
                vyrazhenie = self.displey.text().replace('×', '*').replace('÷', '/')
                rezultat = eval(vyrazhenie)
                self.displey.setText(str(rezultat))
            except:
                self.displey.setText("Ошибка")
        elif tekst == 'C':
            self.displey.setText("0")
        elif tekst == 'CE':
            self.displey.setText(self.last_input if self.last_input else "0")
        elif tekst == '⌫':
            self.displey.setText(self.displey.text()[:-1] or "0")
        elif tekst == '+/-':
            if self.displey.text().startswith('-'):
                self.displey.setText(self.displey.text()[1:])
            else:
                self.displey.setText('-' + self.displey.text())
        elif tekst == 'x²':
            self.displey.setText(str(float(self.displey.text()) ** 2))
        elif tekst == '√x':
            self.displey.setText(str(float(self.displey.text()) ** 0.5))
        elif tekst == '1/x':
            try:
                self.displey.setText(str(1 / float(self.displey.text())))
            except:
                self.displey.setText("Ошибка")
        elif tekst == '%':
            try:
                self.displey.setText(str(float(self.displey.text()) / 100))
            except:
                self.displey.setText("Ошибка")


if __name__ == "__main__":
    prilozhenie = QApplication(sys.argv)
    okno = KalkulyatorUI()
    okno.show()
    sys.exit(prilozhenie.exec_())
