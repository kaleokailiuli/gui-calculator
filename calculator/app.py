import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QLabel,
    QDoubleSpinBox,
    QPushButton,
    QComboBox,
    QStackedLayout,
    QMainWindow,
)
from PyQt5 import QtCore


class AveragingCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # name of app at the top of the window
        self.setWindowTitle("Averaging Calculator")

        # sets the style
        self.setStyleSheet(
            "QWidget { background-color: #e0f2f1; }"
            "QDoubleSpinBox { background-color: #f0f0f0; border: 2px solid #ccc; border-radius: 5px; padding: 5px; }"
            "QPushButton { background-color: #4CAF50; color: white; border: none; border-radius: 5px; padding: 10px; }"
            "QPushButton:hover { background-color: #45a049; }"
        )

        # Creates a vertical layout for arranging widgets vertically
        self.layout = QVBoxLayout()

        self.num_spinboxes = []

        # Testing
        self.spinbox_layouts = QStackedLayout()
        self.input_boxes2 = InputLayout(2)
        self.input_boxes3 = InputLayout(3)
        self.spinbox_layouts.addWidget(self.input_boxes2)
        self.spinbox_layouts.addWidget(self.input_boxes3)


        # Makes a label for the averages
        self.result_label = QLabel()
        self.result_label.setAlignment(QtCore.Qt.AlignCenter)  # Align text to center
        self.result_label.setStyleSheet("font-size: 18pt; font-weight: bold;")  # Larger and bold text

        # Makes a combobox to select the number of numbers to average
        self.number_count_combo = QComboBox()
        self.number_count_combo.addItems(["2", "3", "4", "5"])
        self.number_count_combo.currentIndexChanged.connect(self.update_spinboxes)

        # Adds a label and the combo box to the layout
        self.layout.addWidget(QLabel("Select the number of numbers to average:"))
        self.layout.addWidget(self.number_count_combo)

        # Makes a default amount of numbers (2)
        self.create_spinboxes(2)

        self.layout.addStretch()

        # Makes the button for getting the average
        self.calculate_button = QPushButton("Solve")  # Sets text label
        self.calculate_button.clicked.connect(self.calculate_average)

        self.layout.addWidget(self.calculate_button)

        self.layout.addWidget(self.result_label)

        # Set the layout of the widget
        self.setLayout(self.layout)

        # Size and center the window on the screen
        self.resize(600, 400)  # Set width to 600 and height to 400

    def create_spinboxes(self, count):
        # Create spin boxes and labels based on the given count
        for i in range(count):
            label = QLabel(f"Number {i+1}:")
            spinbox = QDoubleSpinBox()
            spinbox.setDecimals(2)
            spinbox.setRange(-10000, 10000)

            # Add the label and spin box to the layout
            self.layout.addWidget(label)
            self.layout.addWidget(spinbox)

            self.num_spinboxes.append((label, spinbox))

    def clear_spinboxes(self):
        # Remove existing spin boxes and labels
        for label, spinbox in self.num_spinboxes:
            self.layout.removeWidget(label)
            self.layout.removeWidget(spinbox)
            label.deleteLater()
            spinbox.deleteLater()
        self.num_spinboxes.clear()

    def update_spinboxes(self):
        # Updates amount of spinboxes
        count = int(self.number_count_combo.currentText())
        self.clear_spinboxes()
        self.create_spinboxes(count)

    def calculate_average(self):
        # Formula
        numbers = [spinbox.value() for label, spinbox in self.num_spinboxes]
        if numbers:
            average = sum(numbers) / len(numbers)
            self.result_label.setText(f"Average: {average:.2f}")
        else:
            self.result_label.setText("Please enter numbers.")

class InputLayout(QWidget):
    def __init__(self, num: int) -> None:
        super().__init__()
        self.layout = QVBoxLayout()
        self.input_boxes = []

        # Labels and spinboxes
        for i in range(num):
            input_layout = QVBoxLayout()
            label = QLabel(f"Number {i+1}:")
            spinbox = QDoubleSpinBox()
            spinbox.setDecimals(2)
            spinbox.setRange(-10000, 10000)

            # Add the label and spin box to the layout
            input_layout.addWidget(label)
            input_layout.addWidget(spinbox)

            self.input_boxes.append((label, spinbox))


            


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AveragingCalculator()
    window.show()
    sys.exit(app.exec_())
