import sys
import pandas as pd
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import Qt
from functions import plot_scatter, plot_stem, plot_poly


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Régression Polynomiale")
        self.setMinimumSize(1200, 500)

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

        self.mode_label = QLabel("Mode de tracé:")
        self.modes_combo = QComboBox()
        self.modes_combo.addItem("Points")
        self.modes_combo.addItem("Bâtons")
        self.form_layout_input.addRow(self.mode_label, self.modes_combo)

        self.show_btn = QPushButton("Tracer")
        self.show_btn.setMaximumWidth(80)
        self.show_btn.clicked.connect(lambda: self.plot_csv(self.filepath_line.text()))
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

        self.degre_label = QLabel("Degré:")
        self.degre_spinB = QSpinBox()
        self.degre_spinB.setMinimum(2)
        self.form_layout_output.addRow(self.degre_label, self.degre_spinB)

        self.polynome_label = QLabel("Polynôme:")
        self.polynome_sortie = QPlainTextEdit()
        self.polynome_sortie.setReadOnly(True)
        self.polynome_sortie.setMaximumHeight(70)
        self.form_layout_output.addRow(self.polynome_label, self.polynome_sortie)

        self.regression_btn = QPushButton("Tracer")
        self.regression_btn.clicked.connect(lambda: self.plot_regression(self.filepath_line.text(), self.degre_spinB.value()))
        self.form_layout_output.addRow(self.regression_btn)
        self.form_layout_output.setAlignment(self.regression_btn, Qt.AlignRight)

        self.parameters_layout.addItem(self.spacer1)

        # -------------------------------
        # Plotting Widget

        self.affichage_layout = QHBoxLayout()
        self.affichage_widget.setLayout(self.affichage_layout)

        self.spacer3 = QSpacerItem(20, 40, QSizePolicy.Expanding, QSizePolicy.Maximum)
        self.affichage_layout.addItem(self.spacer3)

        self.vlayout = QVBoxLayout()
        self.affichage_layout.addLayout(self.vlayout)

        self.vlayout.addItem(self.spacer1)

        self.image_label = QLabel(self)
        self.image_label.setScaledContents(True)
        self.vlayout.addWidget(self.image_label)

        self.vlayout.addItem(self.spacer1)

        self.affichage_layout.addItem(self.spacer3)

        self.setLayout(self.main_layout)

    # Méthodes:
    def select_csv(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select File", "", "CSV Files (*.csv)")
        if file_path != "":
            self.filepath_line.setText(file_path)

    def plot_csv(self, filepath):
        match self.modes_combo.currentIndex():
            case 0:
                plot_scatter(filepath)
                self.image_label.setPixmap(QPixmap("points_plot.png"))
            case 1:
                plot_stem(filepath)
                self.image_label.setPixmap(QPixmap("batons_plot.png"))

    def plot_regression(self, filepath, degre):
        coeffs = plot_poly(filepath, degre)
        self.image_label.setPixmap(QPixmap("regression.png"))
        polynome = ""
        for i in range(len(coeffs)):
            polynome = f"{coeffs[i]} x^{i} + " + polynome

        self.polynome_sortie.setPlainText(polynome)


if __name__ == '__main__':
    plt.ion()  # Enable interactive mode for Matplotlib
    app = QApplication(sys.argv)

    win = MainWindow()
    win.show()

    sys.exit(app.exec_())
