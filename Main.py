from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QPushButton, QLabel, QStackedWidget, \
    QHBoxLayout
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import sys
import math


class KalkulyatorUI(QWidget):
    def __init__(self):
        super().__init__()
        self.tekushchee_znachenie = "0"  # тек число на экране
        self.operator = None  # тек оператор
        self.pervyy_operand = None  # первый операнд
        self.ozhidanie_vtorogo = False  # флаг ожидания второго операнда
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Калькулятор")
        self.setGeometry(100, 100, 320, 420)
        vert_raskladka = QVBoxLayout()
        knopki_rezhimov = QHBoxLayout()  # блок кнопок для переключения режимов

        # кнопки выбора режима
        self.knopka_obychnyy = QPushButton("Обычный")
        self.knopka_trigonometriya = QPushButton("Тригонометрия")

        # стили для активного и неактивного режима
        self.aktivniy_stil = "background-color: #4A90E2; color: white; border-radius: 5px;"
        self.neaktivniy_stil = "background-color: lightgray; color: black; border-radius: 5px;"

        # начальный стиль
        self.knopka_obychnyy.setStyleSheet(self.aktivniy_stil)
        self.knopka_trigonometriya.setStyleSheet(self.neaktivniy_stil)

        # подключение сигналов
        self.knopka_obychnyy.clicked.connect(self.perekluchit_na_obychnyy)
        self.knopka_trigonometriya.clicked.connect(self.perekluchit_na_trigonometriyu)

        knopki_rezhimov.addWidget(self.knopka_obychnyy)
        knopki_rezhimov.addWidget(self.knopka_trigonometriya)
        vert_raskladka.addLayout(knopki_rezhimov)

        # дисплей калькулятора
        self.displey = QLabel("0")
        self.displey.setFont(QFont("Arial", 24))  # шрифт для дисплея
        self.displey.setStyleSheet("border: 2px solid black; min-height: 50px; background: white;")
        self.displey.setAlignment(Qt.AlignRight)
        vert_raskladka.addWidget(self.displey)

        # стек для переключения между режимами
        self.stek = QStackedWidget()
        vert_raskladka.addWidget(self.stek)

        # вкладки
        self.vkladka_obychnyy = QWidget()
        self.vkladka_trigonometriya = QWidget()
        self.stek.addWidget(self.vkladka_obychnyy)
        self.stek.addWidget(self.vkladka_trigonometriya)

        # инициализация интерфейса
        self.init_obychnyy()
        self.init_trigonometriya()

        # по умолчанию выбираем "Обычный"
        self.stek.setCurrentWidget(self.vkladka_obychnyy)

        self.setLayout(vert_raskladka)

    def perekluchit_na_obychnyy(self):
        self.stek.setCurrentWidget(self.vkladka_obychnyy)
        self.sbor_kalkulyatora()
        self.knopka_obychnyy.setStyleSheet(self.aktivniy_stil)
        self.knopka_trigonometriya.setStyleSheet(self.neaktivniy_stil)

    def perekluchit_na_trigonometriyu(self):
        self.stek.setCurrentWidget(self.vkladka_trigonometriya)
        self.sbor_kalkulyatora()
        self.knopka_trigonometriya.setStyleSheet(self.aktivniy_stil)
        self.knopka_obychnyy.setStyleSheet(self.neaktivniy_stil)

    def sbor_kalkulyatora(self):
        self.tekushchee_znachenie = "0"
        self.operator = None
        self.pervyy_operand = None
        self.ozhidanie_vtorogo = False
        self.obnovit_displey()

    def obnovit_displey(self):
        self.displey.setText(self.tekushchee_znachenie)

    def dobavit_chislo(self, chislo):
        if self.ozhidanie_vtorogo:
            self.tekushchee_znachenie = chislo
            self.ozhidanie_vtorogo = False
        elif self.tekushchee_znachenie == "0":
            self.tekushchee_znachenie = chislo
        else:
            self.tekushchee_znachenie += chislo
        self.obnovit_displey()

    def dobavit_operator(self, operator):
        if self.pervyy_operand is None:
            self.pervyy_operand = float(self.tekushchee_znachenie)
        else:
            self.vychislit_rezultat()
            self.pervyy_operand = float(self.tekushchee_znachenie)
        self.operator = operator
        self.ozhidanie_vtorogo = True

    def vychislit_rezultat(self):
        if self.pervyy_operand is not None and self.operator is not None:
            vtoroy_operand = float(self.tekushchee_znachenie)
            if self.operator == "+":
                rezultat = self.pervyy_operand + vtoroy_operand
            elif self.operator == "-":
                rezultat = self.pervyy_operand - vtoroy_operand
            elif self.operator == "×":
                rezultat = self.pervyy_operand * vtoroy_operand
            elif self.operator == "÷":
                if vtoroy_operand != 0:
                    rezultat = self.pervyy_operand / vtoroy_operand
                else:
                    rezultat = "Ошибка"
            self.tekushchee_znachenie = str(rezultat)
            self.obnovit_displey()
            self.pervyy_operand = None
            self.operator = None

    def ochistit_vsyo(self):
        self.sbor_kalkulyatora()

    def ochistit_poslednee(self):
        if self.ozhidanie_vtorogo:
            # если ждем второй операнд, сбрасываем только его
            self.tekushchee_znachenie = "0"
            self.ozhidanie_vtorogo = False
        else:
            # просто очищаем текущее число
            self.tekushchee_znachenie = "0"
        self.obnovit_displey()

    def smenit_znak(self):
        if self.tekushchee_znachenie != "0":
            if self.tekushchee_znachenie.startswith("-"):
                self.tekushchee_znachenie = self.tekushchee_znachenie[1:]
            else:
                self.tekushchee_znachenie = "-" + self.tekushchee_znachenie
            self.obnovit_displey()

    def dobavit_tochku(self):
        if "." not in self.tekushchee_znachenie:
            self.tekushchee_znachenie += "."
            self.obnovit_displey()

    def obratnoe_chislo(self):
        try:
            self.tekushchee_znachenie = str(1 / float(self.tekushchee_znachenie))
            self.obnovit_displey()
        except ZeroDivisionError:
            self.tekushchee_znachenie = "Ошибка"
            self.obnovit_displey()

    def kvadrat(self):
        self.tekushchee_znachenie = str(float(self.tekushchee_znachenie) ** 2)
        self.obnovit_displey()

    def koren(self):
        self.tekushchee_znachenie = str(math.sqrt(float(self.tekushchee_znachenie)))
        self.obnovit_displey()

    def procent(self):
        try:
            self.tekushchee_znachenie = str(float(self.tekushchee_znachenie) / 100)
            self.obnovit_displey()
        except Exception as e:
            self.tekushchee_znachenie = "Ошибка"
            self.obnovit_displey()

    def trigonometricheskaya_funkciya(self, func):
        try:
            znachenie = float(self.tekushchee_znachenie)
            if func == "sin":
                self.tekushchee_znachenie = str(math.sin(math.radians(znachenie)))
            elif func == "cos":
                self.tekushchee_znachenie = str(math.cos(math.radians(znachenie)))
            elif func == "tan":
                self.tekushchee_znachenie = str(math.tan(math.radians(znachenie)))
            elif func == "asin":
                self.tekushchee_znachenie = str(math.degrees(math.asin(znachenie)))
            elif func == "acos":
                self.tekushchee_znachenie = str(math.degrees(math.acos(znachenie)))
            elif func == "atan":
                self.tekushchee_znachenie = str(math.degrees(math.atan(znachenie)))
            self.obnovit_displey()
        except Exception as e:
            self.tekushchee_znachenie = "Ошибка"
            self.obnovit_displey()

    def init_obychnyy(self):
        setka_knopok = QGridLayout()
        knopki = [
            ('%', 0, 0), ('CE', 0, 1), ('C', 0, 2), ('⌫', 0, 3),
            ('1/x', 1, 0), ('x²', 1, 1), ('√x', 1, 2), ('÷', 1, 3),
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('×', 2, 3),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('+', 4, 3),
            ('+/-', 5, 0), ('0', 5, 1), ('.', 5, 2), ('=', 5, 3)
        ]
        self.dobavit_knopki(setka_knopok, knopki, rezhim="obychnyy")
        self.vkladka_obychnyy.setLayout(setka_knopok)

    def init_trigonometriya(self):
        setka_knopok = QGridLayout()
        knopki = [
            ('sin', 0, 0), ('cos', 0, 1), ('tan', 0, 2), ('C', 0, 3),
            ('asin', 1, 0), ('acos', 1, 1), ('atan', 1, 2), ('÷', 1, 3),
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('×', 2, 3),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('+', 4, 3),
            ('+/-', 5, 0), ('0', 5, 1), ('.', 5, 2), ('=', 5, 3)
        ]
        self.dobavit_knopki(setka_knopok, knopki, rezhim="trigonometriya")
        self.vkladka_trigonometriya.setLayout(setka_knopok)

    def dobavit_knopki(self, layout, knopki, rezhim):
        for tekst, stroka, stolbec in knopki:
            knopka = QPushButton(tekst)
            knopka.setFont(QFont("Arial", 18))  # шрифт для кнопок
            knopka.setFixedSize(60, 60)

            # стили для кнопок
            normal_style = "background-color: lightgray; border-radius: 5px;"
            hover_style = "background-color: #4A90E2; color: white; border-radius: 5px;"
            knopka.setStyleSheet(f"{normal_style} QPushButton:hover {{ {hover_style} }}")

            if tekst.isdigit():
                knopka.clicked.connect(lambda _, t=tekst: self.dobavit_chislo(t))
                knopka.setStyleSheet("background-color: #444; color: white; border-radius: 5px;")
            elif tekst in ["+", "-", "×", "÷"]:
                knopka.clicked.connect(lambda _, t=tekst: self.dobavit_operator(t))
            elif tekst == "=":
                knopka.clicked.connect(self.vychislit_rezultat)
                knopka.setStyleSheet("background-color: #4A90E2; color: white; border-radius: 5px;")
            elif tekst == "C":
                knopka.clicked.connect(self.ochistit_vsyo)
            elif tekst == "CE":
                knopka.clicked.connect(self.ochistit_poslednee)
            elif tekst == "⌫":
                knopka.clicked.connect(self.ochistit_poslednee)
            elif tekst == "+/-":
                knopka.clicked.connect(self.smenit_znak)
            elif tekst == ".":
                knopka.clicked.connect(self.dobavit_tochku)
            elif tekst == "1/x":
                knopka.clicked.connect(self.obratnoe_chislo)
            elif tekst == "x²":
                knopka.clicked.connect(self.kvadrat)
            elif tekst == "√x":
                knopka.clicked.connect(self.koren)
            elif tekst == "%":
                knopka.clicked.connect(self.procent)
            elif rezhim == "trigonometriya" and tekst in ["sin", "cos", "tan", "asin", "acos", "atan"]:
                knopka.clicked.connect(lambda _, t=tekst: self.trigonometricheskaya_funkciya(t))
            layout.addWidget(knopka, stroka, stolbec)


if __name__ == "__main__":
    prilozhenie = QApplication(sys.argv)
    okno = KalkulyatorUI()
    okno.show()
    sys.exit(prilozhenie.exec_())