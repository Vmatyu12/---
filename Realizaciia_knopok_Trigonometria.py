from PyQt5.QtWidgets import QWidget, QVBoxLayout, QGridLayout, QPushButton, QLabel, QApplication
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import sys
import math

class TrigonometryUI(QWidget):
    def __init__(self):
        super().__init__()
        self.init_trigonometriya()

    def init_trigonometriya(self):
        self.setWindowTitle("Тригонометрический калькулятор")
        self.setGeometry(100, 100, 320, 420)
        vert_raskladka = QVBoxLayout()

        # Название раздела
        self.section_label = QLabel("Тригонометрия")
        self.section_label.setFont(QFont("Arial", 20))
        self.section_label.setAlignment(Qt.AlignCenter)
        vert_raskladka.addWidget(self.section_label)

        # Дисплей калькулятора
        self.displey = QLabel("0")
        self.displey.setFont(QFont("Arial", 24))
        self.displey.setStyleSheet("border: 2px solid black; min-height: 50px; background: white;")
        self.displey.setAlignment(Qt.AlignRight)
        vert_raskladka.addWidget(self.displey)

        # Сетка кнопок
        setka_knopok = QGridLayout()
        knopki = [
            ('sin', 0, 0), ('cos', 0, 1), ('tan', 0, 2), ('C', 0, 3),
            ('asin', 1, 0), ('acos', 1, 1), ('atan', 1, 2), ('÷', 1, 3),
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('×', 2, 3),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('+', 4, 3),
            ('+/-', 5, 0), ('0', 5, 1), ('.', 5, 2), ('=', 5, 3)
        ]
        self.dobavit_knopki(setka_knopok, knopki)
        vert_raskladka.addLayout(setka_knopok)
        self.setLayout(vert_raskladka)

    def dobavit_knopki(self, layout, knopki):
        for tekst, stroka, stolbec in knopki:
            knopka = QPushButton(tekst)
            knopka.setFont(QFont("Arial", 18))
            knopka.setFixedSize(60, 60)
            knopka.clicked.connect(lambda checked, t=tekst: self.nazhat_knopku(t))
            layout.addWidget(knopka, stroka, stolbec)

    def nazhat_knopku(self, tekst):
        tekushchee_znachenie = self.displey.text()
        try:
            if tekst == "C":
                self.displey.setText("0")
            elif tekst == "=":
                self.displey.setText(str(eval(tekushchee_znachenie)))
            elif tekst == "+/-":
                self.displey.setText(str(-float(tekushchee_znachenie)))
            elif tekst in ["sin", "cos", "tan", "asin", "acos", "atan"]:
                chislo = float(tekushchee_znachenie)
                if tekst == "sin":
                    self.displey.setText(str(math.sin(math.radians(chislo))))
                elif tekst == "cos":
                    self.displey.setText(str(math.cos(math.radians(chislo))))
                elif tekst == "tan":
                    self.displey.setText(str(math.tan(math.radians(chislo))))
                elif tekst == "asin":
                    self.displey.setText(str(math.degrees(math.asin(chislo))))
                elif tekst == "acos":
                    self.displey.setText(str(math.degrees(math.acos(chislo))))
                elif tekst == "atan":
                    self.displey.setText(str(math.degrees(math.atan(chislo))))
            else:
                if tekushchee_znachenie == "0":
                    self.displey.setText(tekst)
                else:
                    self.displey.setText(tekushchee_znachenie + tekst)
        except Exception:
            self.displey.setText("Ошибка")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TrigonometryUI()
    window.show()
    sys.exit(app.exec_())
