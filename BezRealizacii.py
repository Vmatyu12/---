from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QPushButton, QLabel
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

        # добавление кнопок без функционала
        for tekst, stroka, stolbec in knopki:
            knopka = QPushButton(tekst)
            knopka.setFont(QFont("Arial", 18))  # шрифт для кнопок
            knopka.setFixedSize(60, 60)

            # единый стиль для всех кнопок
            knopka.setStyleSheet("background-color: lightgray; border-radius: 5px;")

            setka_knopok.addWidget(knopka, stroka, stolbec)

        vert_raskladka.addLayout(setka_knopok)
        self.setLayout(vert_raskladka)


if __name__ == "__main__":
    prilozhenie = QApplication(sys.argv)
    okno = KalkulyatorUI()
    okno.show()
    sys.exit(prilozhenie.exec_())