import sys
from PyQt5.QtWidgets import QDialog, QApplication
from dialogo_repartir import *

class DialogoReparticionBilletes(QDialog):
    def __init__(self):
        super().__init__()

        self.dialogoVentana = Ui_dialogo()
        self.dialogoVentana.setupUi(self)

        self.dialogoVentana.repartirButton.clicked.connect(self.hacer_reparticion)
        self.dialogoVentana.exitButton.clicked.connect(self.salir)

        self.show()

    def hacer_reparticion(self):
        valor_efectivo = [1, 2, 5, 10, 20, 50, 100]
        cantidad_efectivo = [0, 0, 0, 0, 0, 0, 0]

        cantidad = int(self.dialogoVentana.cantidadInput.text())
        dif_operable = cantidad

        while (dif_operable != 0):
            for i in range(0,7):
                if dif_operable - valor_efectivo[i] >= 0:
                    dif_operable -= valor_efectivo[i]
                    cantidad_efectivo[i] += 1

        cant1 = cantidad_efectivo[0]
        cant2 = cantidad_efectivo[1]
        cant5 = cantidad_efectivo[2]
        cant10 = cantidad_efectivo[3]
        cant20 = cantidad_efectivo[4]
        cant50 = cantidad_efectivo[5]
        cant100 = cantidad_efectivo[6]

        self.dialogoVentana.lcd_1.display(cant1)
        self.dialogoVentana.lcd_2.display(cant2)
        self.dialogoVentana.lcd_5.display(cant5)
        self.dialogoVentana.lcd_10.display(cant10)
        self.dialogoVentana.lcd_20.display(cant20)
        self.dialogoVentana.lcd_50.display(cant50)
        self.dialogoVentana.lcd_100.display(cant100)

    def salir(self):
        sys.exit(0)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialogo = DialogoReparticionBilletes()
    dialogo.show()
    sys.exit(app.exec_())
