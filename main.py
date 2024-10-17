import sys
import pandas as pd
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt


def tracer_csv(filepath):
    data = pd.read_csv(filepath)
    x = data['X']
    y = data['Y']

    plt.figure()
    plt.plot(x, y)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title("Tracé sans régression")
    plt.show()


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Régression Polynomiale")

        self.main_layout = QHBoxLayout()

        # Variables

        # Ajouter les widgets au main layout.
        self.parameters_widget = QWidget()
        self.main_layout.addWidget(self.parameters_widget, stretch=1)

        self.affichage_widget = QWidget()
        self.affichage_widget.setStyleSheet("background-color: #d6dadc;")
        self.main_layout.addWidget(self.affichage_widget, stretch=3)

        # Remplir le parameters_widget

        self.parameters_layout = QVBoxLayout()
        self.parameters_widget.setLayout(self.parameters_layout)

        self.spacer1 = QSpacerItem(20, 20, QSizePolicy.Maximum, QSizePolicy.Expanding)
        self.parameters_layout.addItem(self.spacer1)

        self.input_group = QGroupBox("Entrez vos données")
        self.form_layout_input = QFormLayout()
        self.parameters_layout.addWidget(self.input_group)

        # Ajouter au Form Layout
        self.import_label = QLabel("Importer Fichier:")
        self.filepath_line = QLineEdit()
        self.filepath_line.setReadOnly(True)

        self.import_btn = QPushButton("Importer")
        self.import_btn.clicked.connect(self.select_csv)

        self.import_layout = QHBoxLayout()
        self.import_layout.addWidget(self.filepath_line)
        self.import_layout.addWidget(self.import_btn)
        self.form_layout_input.addRow(self.import_label, self.import_layout)

        self.degre_label = QLabel("Degré:")
        self.degre_spinB = QSpinBox()
        self.degre_spinB.setMinimum(2)
        self.form_layout_input.addRow(self.degre_label, self.degre_spinB)

        self.show_btn = QPushButton("Tracer")
        self.show_btn.setMaximumWidth(80)
        self.show_btn.clicked.connect(lambda: tracer_csv(self.filepath_line.text()))
        self.form_layout_input.addRow(self.show_btn)
        self.form_layout_input.setAlignment(self.show_btn, Qt.AlignRight)

        self.input_group.setLayout(self.form_layout_input)

        self.spacer2 = QSpacerItem(10, 70, QSizePolicy.Maximum, QSizePolicy.Maximum)
        self.parameters_layout.addItem(self.spacer2)

        # Ajouter l'output
        self.output_group = QGroupBox("Données de sortie")
        self.form_layout_output = QFormLayout()
        self.output_group.setLayout(self.form_layout_output)
        self.parameters_layout.addWidget(self.output_group)

        self.polynome_label = QLabel("Polynôme:")
        self.polynome_sortie = QPlainTextEdit()
        self.polynome_sortie.setReadOnly(True)
        self.polynome_sortie.setMaximumHeight(70)
        self.form_layout_output.addRow(self.polynome_label, self.polynome_sortie)

        self.regression_btn = QPushButton("Tracer")
        self.form_layout_output.addRow(self.regression_btn)
        self.form_layout_output.setAlignment(self.regression_btn, Qt.AlignRight)

        self.parameters_layout.addItem(self.spacer1)

        self.setLayout(self.main_layout)



    # Méthodes:
    def select_csv(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select File", "", "CSV Files (*.csv)")
        if file_path != "":
            self.filepath = file_path
            self.filepath_line.setText(file_path)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    win = MainWindow()
    win.show()

    sys.exit(app.exec_())