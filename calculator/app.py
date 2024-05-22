import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
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


class AveragingCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Set up the main window
        self.setWindowTitle("Professional Averaging Calculator")
        self.setFixedSize(600, 500)

        # Main layout setup
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(20, 20, 20, 20)
        self.layout.setAlignment(Qt.AlignCenter)

        self.num_spinboxes = []

        # Header label
        header_label = QLabel("Averaging Calculator")
        header_label.setAlignment(Qt.AlignCenter)
        header_label.setStyleSheet(
            "font-weight: bold; font-size: 24px; color: #FFFFFF;"
        )
        header_label.setFont(QFont("Arial", 24, QFont.Bold))

        # Label for number count selection
        label_num_count = QLabel("Select the number of numbers to average:")
        label_num_count.setAlignment(Qt.AlignCenter)
        label_num_count.setStyleSheet("font-size: 16px; color: #FFFFFF;")
        label_num_count.setFont(QFont("Arial", 16, QFont.Bold))

        # ComboBox for selecting number count
        self.number_count_combo = QComboBox()
        self.number_count_combo.addItems(["2", "3", "4", "5"])
        self.number_count_combo.setFixedSize(300, 40)
        self.number_count_combo.setStyleSheet(
            "background-color: #444444; color: #FFFFFF; border: 1px solid #777777; border-radius: 5px; font-size: 16px;"
        )
        self.number_count_combo.setFont(QFont("Arial", 14))
        self.number_count_combo.currentIndexChanged.connect(self.update_spinboxes)

        # Add combo box and label to a vertical layout
        combo_layout = QVBoxLayout()
        combo_layout.addWidget(label_num_count)
        combo_layout.addWidget(self.number_count_combo)
        combo_layout.setAlignment(Qt.AlignCenter)

        # Add header and combo layout to the main layout
        self.layout.addWidget(header_label)
        self.layout.addLayout(combo_layout)

        # Label for displaying result
        self.result_label = QLabel()
        self.result_label.setAlignment(Qt.AlignCenter)
        self.result_label.setStyleSheet(
            "font-size: 18pt; font-weight: bold; color: #FF0000;"
        )
        self.result_label.setFont(QFont("Arial", 18, QFont.Bold))

        self.layout.addWidget(self.result_label)

        # Create default number of spin boxes
        self.spinbox_layout = QVBoxLayout()
        self.layout.addLayout(self.spinbox_layout)
        self.create_spinboxes(2)

        # Spacer item
        self.layout.addItem(
            QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        )

        # Layout for buttons
        self.button_layout = QHBoxLayout()
        self.button_layout.setAlignment(Qt.AlignCenter)

        # Button for calculating average
        self.calculate_button = QPushButton("Calculate", clicked=self.calculate_average)
        self.calculate_button.setStyleSheet(
            "background-color: #4CAF50; color: white; border: none; border-radius: 5px; padding: 10px 20px; font-size: 16px;"
        )
        self.calculate_button.setFont(QFont("Arial", 16, QFont.Bold))

        # Button for resetting spinboxes
        self.reset_button = QPushButton("Reset", clicked=self.reset_spinboxes)
        self.reset_button.setStyleSheet(
            "background-color: #f44336; color: white; border: none; border-radius: 5px; padding: 10px 20px; font-size: 16px;"
        )
        self.reset_button.setFont(QFont("Arial", 16, QFont.Bold))

        # Add buttons to the button layout
        self.button_layout.addWidget(self.calculate_button)
        self.button_layout.addWidget(self.reset_button)
        self.layout.addLayout(self.button_layout)

        # Apply style sheet to set dark background
        self.setStyleSheet("QWidget { background-color: #2D2D2D; }")

    def create_spinboxes(self, count):
        # Clear existing spin boxes and labels
        for label, spinbox in self.num_spinboxes:
            label.deleteLater()
            spinbox.deleteLater()
        self.num_spinboxes.clear()
        self.spinbox_layout.setParent(None)
        self.spinbox_layout = QVBoxLayout()
        self.layout.insertLayout(4, self.spinbox_layout)

        # Create spin boxes and labels based on the given count
        for i in range(count):
            label = QLabel(f"Number {i + 1}:")
            label.setAlignment(Qt.AlignCenter)
            label.setStyleSheet("font-size: 20px; color: #FFFFFF; font-weight: bold;")
            label.setFont(QFont("Arial", 20, QFont.Bold))
            spinbox = QDoubleSpinBox()
            spinbox.setStyleSheet(
                "background-color: #444444; color: white; border: 1px solid #777777; border-radius: 5px; font-size: 20px; font-weight: bold;"
            )
            spinbox.setFont(QFont("Arial", 20, QFont.Bold))
            spinbox.setDecimals(2)
            spinbox.setRange(-10000, 10000)
            spinbox.setFixedSize(200, 40)
            spinbox.setButtonSymbols(QDoubleSpinBox.NoButtons)

            # Add spin boxes and labels to a vertical layout
            label_layout = QVBoxLayout()
            label_layout.addWidget(label)
            label_layout.addWidget(spinbox)
            label_layout.setAlignment(Qt.AlignCenter)
            self.spinbox_layout.addLayout(label_layout)

            self.num_spinboxes.append((label, spinbox))

        # Resize window based on the number of spin boxes
        new_height = 350 + count * 60
        self.setFixedSize(600, new_height)

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

    def reset_spinboxes(self):
        # Reset all spinboxes to 0 and clear the result label
        for label, spinbox in self.num_spinboxes:
            spinbox.setValue(0)
        self.result_label.setText("")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AveragingCalculator()
    window.show()
    sys.exit(app.exec_())
