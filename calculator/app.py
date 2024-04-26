import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QDoubleSpinBox, QPushButton, QComboBox

class AveragingCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        # Set the window title
        self.setWindowTitle('Averaging Calculator')
        
        # Set the stylesheet for styling the widgets
        self.setStyleSheet("QWidget { background-color: #e0f2f1; }"
                           "QDoubleSpinBox { background-color: #f0f0f0; border: 2px solid #ccc; border-radius: 5px; padding: 5px; }"
                           "QPushButton { background-color: #4CAF50; color: white; border: none; border-radius: 5px; padding: 10px; }"
                           "QPushButton:hover { background-color: #45a049; }")
        
        # Create a vertical layout for arranging widgets vertically
        self.layout = QVBoxLayout()
        
        # Initialize a list to store spin boxes and labels
        self.num_spinboxes = []
        
        # Create a label for displaying the average result
        self.result_label = QLabel()
        
        # Create a combo box for selecting the number of numbers to average
        self.number_count_combo = QComboBox()
        self.number_count_combo.addItems(['2', '3', '4', '5'])
        self.number_count_combo.currentIndexChanged.connect(self.update_spinboxes)
        
        # Add a label and the combo box to the layout
        self.layout.addWidget(QLabel('Select the number of numbers to average:'))
        self.layout.addWidget(self.number_count_combo)
        
        # Create spin boxes based on the default value (2)
        self.create_spinboxes(2)
        
        # Add a stretch to push widgets to the top and the button to the bottom
        self.layout.addStretch()

        # Create a button for calculating the average
        self.calculate_button = QPushButton('Calculate Average')
        self.calculate_button.clicked.connect(self.calculate_average)
        
        # Add the button to the layout
        self.layout.addWidget(self.calculate_button)
        
        # Add the result label to the layout
        self.layout.addWidget(self.result_label)
        
        # Set the layout of the widget
        self.setLayout(self.layout)
        
        # Set the initial size of the window
        self.resize(600, 400)  # Set width to 600 and height to 400

    def create_spinboxes(self, count):
        # Create spin boxes and labels based on the given count
        for i in range(count):
            label = QLabel(f'Number {i+1}:')
            spinbox = QDoubleSpinBox()
            spinbox.setDecimals(2)
            spinbox.setRange(-10000, 10000)
            
            # Add the label and spin box to the layout
            self.layout.addWidget(label)
            self.layout.addWidget(spinbox)
            
            # Append the label and spin box to the list
            self.num_spinboxes.append((label, spinbox))
    
    def clear_spinboxes(self):
        # Remove and delete all spin boxes and labels from the layout and clear the list
        for label, spinbox in self.num_spinboxes:
            self.layout.removeWidget(label)
            self.layout.removeWidget(spinbox)
            label.deleteLater()
            spinbox.deleteLater()
        self.num_spinboxes.clear()
    
    def update_spinboxes(self):
        # Update the number of spin boxes based on the selected count
        count = int(self.number_count_combo.currentText())
        self.clear_spinboxes()
        self.create_spinboxes(count)
    
    def calculate_average(self):
        # Calculate the average of the entered numbers
        numbers = [spinbox.value() for label, spinbox in self.num_spinboxes]
        if numbers:
            average = sum(numbers) / len(numbers)
            self.result_label.setText(f'Average: {average:.2f}')
        else:
            self.result_label.setText('Please enter numbers.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AveragingCalculator()
    window.show()
    sys.exit(app.exec_())
