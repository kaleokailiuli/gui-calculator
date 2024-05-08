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
    QHBoxLayout,
    QSizePolicy,
)
from PyQt5.QtCore import Qt


class AveragingCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Set up the main window
        self.setWindowTitle("Averaging Calculator")
        self.setFixedSize(600, 600)  # Set window size with fixed dimensions

        # Main layout setup
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(10, 10, 10, 10)
        self.layout.setAlignment(Qt.AlignCenter)  # Center align the layout

        self.num_spinboxes = []

        # Label for number count selection
        label_num_count = QLabel("Select the number of numbers to average:")
        label_num_count.setAlignment(Qt.AlignCenter)
        label_num_count.setStyleSheet("font-weight: bold;")

        # ComboBox for selecting number count
        self.number_count_combo = QComboBox()
        self.number_count_combo.addItems(["2", "3", "4", "5"])
        self.number_count_combo.setFixedSize(300, 40)
        self.number_count_combo.setStyleSheet(
            "background-color: white; color: black; border-radius: 5px;"
        )
        self.number_count_combo.currentIndexChanged.connect(self.update_spinboxes)

        # Add combo box label and combo box to a horizontal layout
        combo_layout = QVBoxLayout()
        combo_layout.addWidget(label_num_count)
        combo_layout.addWidget(self.number_count_combo)
        combo_layout.setAlignment(Qt.AlignCenter)

        # Add the horizontal layout to the main layout
        self.layout.addLayout(combo_layout)

        # Spacer item
        self.layout.addItem(
            QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        )

        # Create default number of spin boxes
        self.create_spinboxes(2)

        # Button for calculating average
        self.calculate_button = QPushButton("Solve", clicked=self.calculate_average)
        self.calculate_button.setStyleSheet(
            "background-color: #4CAF50; color: white; border: none; border-radius: 5px; padding: 10px;"
        )
        self.calculate_button.setFixedSize(300, 80)  # Set button size

        # Add solve button to the layout with center alignment
        self.layout.addWidget(self.calculate_button, alignment=Qt.AlignCenter)

        # Spacer item
        self.layout.addItem(
            QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        )

        # Label for displaying result
        self.result_label = QLabel()
        self.result_label.setAlignment(Qt.AlignCenter)
        self.result_label.setStyleSheet("font-size: 18pt; font-weight: bold;")

        # Add result label to the layout
        self.layout.addWidget(self.result_label)

        # Apply style sheet to round the window edges
        self.setStyleSheet(
            "border-radius: 10px; background-color: #444444; color: white;"
        )

    def create_spinboxes(self, count):
        # Clear existing spin boxes and labels
        for label, spinbox in self.num_spinboxes:
            label.deleteLater()
            spinbox.deleteLater()
        self.num_spinboxes.clear()

        # Create spin boxes and labels based on the given count
        for i in range(count):
            label = QLabel(f"Number {i+1}:")
            label.setAlignment(Qt.AlignCenter)
            label.setStyleSheet(
                "font-weight: bold; font-size: 14pt;"
            )  # Adjust font size
            spinbox = QDoubleSpinBox()
            spinbox.setStyleSheet(
                "background-color: white; color: black; border-radius: 5px; font-size: 14pt; text-align: center;"
            )  # Adjust font size and alignment
            spinbox.setDecimals(2)
            spinbox.setRange(-10000, 10000)
            spinbox.setFixedSize(400, 40)  # Set spinbox size
            spinbox.setButtonSymbols(QDoubleSpinBox.NoButtons)

            # Add spin boxes and labels to the main layout with center alignment
            label_layout = QVBoxLayout()
            label_layout.addWidget(label)
            label_layout.addWidget(spinbox)
            label_layout.setAlignment(Qt.AlignCenter)
            self.layout.addLayout(label_layout)

            self.num_spinboxes.append((label, spinbox))

    def update_spinboxes(self):
        # Update number of spin boxes based on ComboBox selection
        count = int(self.number_count_combo.currentText())
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
    window.show()
    sys.exit(app.exec_())
