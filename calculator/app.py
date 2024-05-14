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
        
        # Main layout setup
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(20, 20, 20, 20)
        self.layout.setAlignment(Qt.AlignCenter)

        self.num_spinboxes = []

        # Header label
        header_label = QLabel("Averaging Calculator")
        header_label.setAlignment(Qt.AlignCenter)
        header_label.setStyleSheet("font-weight: bold; font-size: 24px; color: #FFFFFF;")
        header_label.setFont(QFont('Arial', 24))

        # Add header to the main layout
        self.layout.addWidget(header_label)

        # Create default number of spin boxes (2)
        self.create_spinboxes(2)

        # Label for displaying result
        self.result_label = QLabel()
        self.result_label.setAlignment(Qt.AlignCenter)
        self.result_label.setStyleSheet("font-size: 18pt; font-weight: bold; color: #FFFFFF;")

        # Add result label to the layout
        self.layout.addWidget(self.result_label)

        # Spacer item
        self.layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Layout for buttons
        self.button_layout = QHBoxLayout()
        self.button_layout.setAlignment(Qt.AlignCenter)

        # Button for calculating average
        self.calculate_button = QPushButton("Calculate", clicked=self.calculate_average)
        self.calculate_button.setStyleSheet(
            "background-color: #4CAF50; color: white; border: none; border-radius: 5px; padding: 20px 40px; font-size: 18px;"
        )
        self.calculate_button.setFont(QFont('Arial', 18))
        self.calculate_button.setFixedSize(200, 80)  # Bigger size for Calculate button

        # Button for resetting spinboxes
        self.reset_button = QPushButton("Reset", clicked=self.reset_spinboxes)
        self.reset_button.setStyleSheet(
            "background-color: #f44336; color: white; border: none; border-radius: 5px; padding: 20px 40px; font-size: 18px;"
        )
        self.reset_button.setFont(QFont('Arial', 18))
        self.reset_button.setFixedSize(200, 80)  # Bigger size for Reset button

        # Add buttons to the button layout
        self.button_layout.addWidget(self.calculate_button)
        self.button_layout.addWidget(self.reset_button)

        # Add button layout to main layout
        self.layout.addLayout(self.button_layout)

        # Apply style sheet to set dark background
        self.setStyleSheet(
            """
            QWidget {
                background-color: #2D2D2D;
            }
            """
        )

    def create_spinboxes(self, count):
        # Clear existing spin boxes and labels
        for label, spinbox in self.num_spinboxes:
            label.deleteLater()
            spinbox.deleteLater()
        self.num_spinboxes.clear()

        # Create a vertical layout for spin boxes
        spinbox_layout = QVBoxLayout()
        spinbox_layout.setAlignment(Qt.AlignCenter)

        # Create spin boxes and labels based on the given count
        for i in range(count):
            label = QLabel(f"Number {i+1}:")
            label.setAlignment(Qt.AlignCenter)
            label.setStyleSheet("font-size: 14px; color: #FFFFFF;")
            label.setFont(QFont('Arial', 14))
            spinbox = QDoubleSpinBox()
            spinbox.setStyleSheet(
                "background-color: #444444; color: white; border: 1px solid #777777; border-radius: 5px; font-size: 14px; font-weight: bold;"
            )
            spinbox.setFont(QFont('Arial', 14, QFont.Bold))
            spinbox.setDecimals(2)
            spinbox.setRange(-10000, 10000)
            spinbox.setFixedSize(300, 50)  # Slightly shorter spin boxes
            spinbox.setButtonSymbols(QDoubleSpinBox.NoButtons)

            # Add spin boxes and labels to a vertical layout
            label_layout = QVBoxLayout()
            label_layout.addWidget(label)
            label_layout.addWidget(spinbox)
            label_layout.setAlignment(Qt.AlignCenter)
            spinbox_layout.addLayout(label_layout)

            self.num_spinboxes.append((label, spinbox))

        # Add the spinbox layout to the main layout
        self.layout.addLayout(spinbox_layout)

        # Resize window based on the number of spin boxes
        new_height = 400 + count * 80
        self.resize(600, new_height)

    def calculate_average(self):
        # Calculate the average of numbers entered
        numbers = [spinbox.value() for label, spinbox in self.num_spinboxes]
        if numbers:
            average = sum(numbers) / len(numbers)
            self.result_label.setText(f"Average: {average:.2f}")
        else:
            self.result_label.setText("Please enter numbers.")

    def reset_spinboxes(self):
        # Reset all spinboxes to 0
        for label, spinbox in self.num_spinboxes:
            spinbox.setValue(0)
        self.result_label.setText("")  # Clear the result label


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AveragingCalculator()
    window.show()
    sys.exit(app.exec_())
