import sys
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QGridLayout, QLineEdit, QPushButton, QComboBox


class SpeedCalculator(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Average Speed Calculator")
        grid = QGridLayout()

        distance_label = QLabel("Distance:")
        self.distance_input = QLineEdit()

        time_label = QLabel("Time(hours): ")
        self.time_input = QLineEdit()

        self.unit_combo = QComboBox()
        self.unit_combo.addItems(["Metric (km)", "Imperial (miles)"])

        calculate = QPushButton("Calculate")
        calculate.clicked.connect(self.calculate)

        self.result_label = QLabel("")

        grid.addWidget(distance_label, 0, 0)
        grid.addWidget(self.distance_input, 0, 1)
        grid.addWidget(self.unit_combo, 0, 2)
        grid.addWidget(time_label, 1, 0)
        grid.addWidget(self.time_input, 1, 1)
        grid.addWidget(calculate, 2, 1)
        grid.addWidget(self.result_label, 3, 0, 1, 2)

        self.setLayout(grid)

    def calculate(self):
        distance = float(self.distance_input.text())
        time = float(self.time_input.text())

        speed = distance / time
        if self.unit_combo.currentText() == "Metric (km)":
            speed = round(speed, 2)
            units = "km/h"
        elif self.unit_combo.currentText() == "Imperial (miles)":
            speed = round(speed*0.621371, 2)
            units = "mph"
        self.result_label.setText(f"Average speed: {speed} {units}")

app = QApplication(sys.argv)
speed_calculator = SpeedCalculator()
speed_calculator.show()
sys.exit(app.exec())