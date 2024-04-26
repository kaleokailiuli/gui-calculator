import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QDoubleSpinBox, QPushButton, QComboBox

class AveragingCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle('Averaging Calculator')
        
        self.layout = QVBoxLayout()
        
        self.num_spinboxes = []
        self.result_label = QLabel()
        
        self.number_count_combo = QComboBox()
        self.number_count_combo.addItems(['2', '3', '4', '5'])
        self.number_count_combo.currentIndexChanged.connect(self.update_spinboxes)
        self.layout.addWidget(QLabel('Select the number of numbers to average:'))
        self.layout.addWidget(self.number_count_combo)
        
        self.create_spinboxes(2)  # Default to 2 spinboxes
        
        self.calculate_button = QPushButton('Calculate Average')
        self.calculate_button.clicked.connect(self.calculate_average)
        self.layout.addWidget(self.calculate_button)
        
        self.layout.addWidget(self.result_label)
        
        self.setLayout(self.layout)
    
    def create_spinboxes(self, count):
        self.clear_spinboxes()
        for i in range(count):
            label = QLabel(f'Number {i+1}:')
            spinbox = QDoubleSpinBox()
            spinbox.setDecimals(2)
            spinbox.setRange(-10000, 10000)
            self.layout.addWidget(label)
            self.layout.addWidget(spinbox)
            self.num_spinboxes.append(spinbox)
    
    def clear_spinboxes(self):
        for spinbox in self.num_spinboxes:
            self.layout.removeWidget(spinbox)
            spinbox.deleteLater()
        self.num_spinboxes.clear()
    
    def update_spinboxes(self):
        count = int(self.number_count_combo.currentText())
        self.create_spinboxes(count)
    
    def calculate_average(self):
        numbers = [spinbox.value() for spinbox in self.num_spinboxes]
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
