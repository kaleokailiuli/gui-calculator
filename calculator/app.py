import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QLabel,
    QDoubleSpinBox,
    QPushButton,
    QComboBox,
    QSpacerItem,
    QSizePolicy,
)
from PyQt5 import QtCore


class AveragingCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Set up the main window
        self.setWindowTitle("Averaging Calculator")  # Window title
        self.setStyleSheet("background-color: #444444; color: white; border-radius: 10px;")  # Set main background color to darker grey

        # Main layout setup
        self.layout = QVBoxLayout(self)  # Main layout
        self.layout.setContentsMargins(10, 10, 10, 10)  # Set layout margins

        self.num_spinboxes = []  # List to store spin boxes and labels

        # Label for number count selection
        label_num_count = QLabel("Select the number of numbers to average:")
        label_num_count.setAlignment(QtCore.Qt.AlignCenter)
        self.layout.addWidget(label_num_count)

        # ComboBox for selecting number count
        self.number_count_combo = QComboBox()
        self.number_count_combo.addItems(["2", "3", "4", "5"])

        # Make the dropdown menu taller and wider
        self.number_count_combo.setFixedSize(300, 40)  # Set size
        self.number_count_combo.setStyleSheet("background-color: white; color: black;")  # Set background color to white and text color to black

        # Set the drop-down arrow to be transparent
        self.number_count_combo.view().setStyleSheet("QListView{selection-background-color: transparent;}")

        self.layout.addWidget(self.number_count_combo, alignment=QtCore.Qt.AlignCenter)

        self.layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))  # Add vertical spacer

        # Create default number of spin boxes
        self.create_spinboxes(2)

        self.layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))  # Add vertical spacer

        # Button for calculating average
        self.calculate_button = QPushButton("Solve", clicked=self.calculate_average)
        self.calculate_button.setStyleSheet("background-color: #4CAF50; color: white; border: none; border-radius: 5px; padding: 20px;")  # Increase padding
        self.calculate_button.setFixedSize(350, 70)  # Increase size
        self.layout.addWidget(self.calculate_button, alignment=QtCore.Qt.AlignCenter)

        # Label for displaying result
        self.result_label = QLabel()
        self.result_label.setAlignment(QtCore.Qt.AlignCenter)
        self.result_label.setStyleSheet("font-size: 18pt; font-weight: bold;")
        self.layout.addWidget(self.result_label, alignment=QtCore.Qt.AlignCenter)

    def create_spinboxes(self, count):
        # Create spin boxes and labels based on the given count
        for i in range(count):
            label = QLabel(f"Number {i+1}:")
            label.setAlignment(QtCore.Qt.AlignCenter)
            spinbox = QDoubleSpinBox()
            spinbox.setStyleSheet("background-color: white; color: black;")  # Set background color to white and text color to black
            spinbox.setDecimals(2)
            spinbox.setRange(-10000, 10000)
            spinbox.setFixedHeight(40)  # Set height of the spin box

            # Remove up and down arrows from the spin box
            spinbox.setButtonSymbols(QDoubleSpinBox.NoButtons)

            self.layout.addWidget(label)
            self.layout.addWidget(spinbox)
            self.num_spinboxes.append((label, spinbox))

    def clear_spinboxes(self):
        # Remove existing spin boxes and labels
        for label, spinbox in self.num_spinboxes:
            label.deleteLater()
            spinbox.deleteLater()
        self.num_spinboxes.clear()

    def update_spinboxes(self):
        # Update number of spin boxes based on ComboBox selection
        count = int(self.number_count_combo.currentText())
        self.clear_spinboxes()
        self.create_spinboxes(count)

    def calculate_average(self):
        # Calculate the average of numbers entered
        numbers = [spinbox.value() for label, spinbox in self.num_spinboxes]
        if numbers:
            average = sum(numbers) / len(numbers)
            self.result_label.setText(f"Average: {average:.2f}")
        else:
            self.result_label.setText("Please enter numbers.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AveragingCalculator()
    window.setFixedSize(600, 800)  # Set window size
    window.show()
    sys.exit(app.exec_())
