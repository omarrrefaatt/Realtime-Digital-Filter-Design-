import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QCheckBox, QComboBox,QFileDialog
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
from scipy.signal import freqz, convolve
from scipy.signal import zpk2tf, tf2zpk, freqz
from scipy import signal
import numpy as np
from numpy import abs, angle, pi,log10 
from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene, QGraphicsEllipseItem, QGraphicsSimpleTextItem, QGridLayout, QFrame
from PyQt5.QtCore import  pyqtSignal
from PyQt5.QtCore import Qt
import pyqtgraph as pg
from PyQt5.QtCore import QPointF
import pandas as pd

class CustomGraphicsView(QtWidgets.QGraphicsView):
    dragged =pyqtSignal(object) # Custom signal to emit mouse click events with coordinates

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.prev_pos = None
        self.pressed = False

    def mousePressEvent (self, event):
        self.prev_pos = event.pos()
        self.pressed=True 

    def mouseMoveEvent (self, event):
        global xLoc 
        global yloc
        if self.prev_pos and self.pressed:
            self.dragged.emit (event)
            self.prev_pos = event.pos()

    def mouseReleaseEvent (self,event):
        self.prev_pos = None
        self.pressed=False 

class MyPlotWidget(pg.PlotWidget):
    dragged =pyqtSignal(object) # Custom signal to emit mouse click events with coordinates
    select =pyqtSignal(object)
    released =pyqtSignal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.prev_pos = None
        self.pressed = False

    def mousePressEvent (self, event):
        self.prev_pos = event.pos()
        self.pressed=True 
        self.select.emit(event)

    def mouseMoveEvent (self, event):
        global xLoc 
        global yloc
        if self.prev_pos and self.pressed:
            self.dragged.emit (event)
            self.prev_pos = event.pos()
    def mouseReleaseEvent (self,event):
        self.prev_pos = None
        self.pressed=False 
        self.released. emit()
    def update_plot(self, x_values):
        # Assuming x_values is a list of x-coordinates
        # You need to adapt this part based on the actual plotting method used
        self.clear()  # Clear the previous plot
        self.plot(x_values, pen='b')
    


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1201, 841)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1201, 781))
        self.tabWidget.setObjectName("tabWidget")
        self.zPoleTab = QtWidgets.QWidget()
        self.zPoleTab.setObjectName("zPoleTab")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.zPoleTab)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 591, 341))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.zPoleLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.zPoleLayout.setContentsMargins(0, 0, 0, 0)
        self.zPoleLayout.setObjectName("zPoleLayout")
        self.groupBox = QtWidgets.QGroupBox(self.zPoleTab)
        self.groupBox.setGeometry(QtCore.QRect(600, 0, 581, 341))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.zerosRadioButton = QtWidgets.QRadioButton(self.groupBox)
        self.zerosRadioButton.setGeometry(QtCore.QRect(70, 60, 95, 20))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.zerosRadioButton.setFont(font)
        self.zerosRadioButton.setObjectName("zerosRadioButton")
        self.polesRadioButton = QtWidgets.QRadioButton(self.groupBox)
        self.polesRadioButton.setGeometry(QtCore.QRect(190, 60, 95, 20))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.polesRadioButton.setFont(font)
        self.polesRadioButton.setObjectName("polesRadioButton")
        self.clearButton = QtWidgets.QPushButton(self.groupBox)
        self.clearButton.setGeometry(QtCore.QRect(360, 50, 181, 28))
        self.clearButton.setObjectName("clearButton")
        self.conjugateCheckBox = QtWidgets.QCheckBox(self.groupBox)
        self.conjugateCheckBox.setGeometry(QtCore.QRect(60, 230, 121, 20))
        self.conjugateCheckBox.setObjectName("conjugateCheckBox")
        self.clearAllButton = QtWidgets.QPushButton(self.groupBox)
        self.clearAllButton.setGeometry(QtCore.QRect(60, 150, 481, 28))
        self.clearAllButton.setObjectName("clearAllButton")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.zPoleTab)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 350, 591, 401))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.magnitudeLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.magnitudeLayout.setContentsMargins(0, 0, 0, 0)
        self.magnitudeLayout.setObjectName("magnitudeLayout")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.zPoleTab)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(600, 350, 591, 401))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.phaseLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.phaseLayout.setContentsMargins(0, 0, 0, 0)
        self.phaseLayout.setObjectName("phaseLayout")
        self.tabWidget.addTab(self.zPoleTab, "")
        self.filterTab = QtWidgets.QWidget()
        self.filterTab.setObjectName("filterTab")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.filterTab)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(0, 0, 1191, 371))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.zPoleLayout2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.zPoleLayout2.setContentsMargins(0, 0, 0, 0)
        self.zPoleLayout2.setObjectName("zPoleLayout2")
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.filterTab)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(0, 380, 391, 371))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.originalPhaseLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.originalPhaseLayout.setContentsMargins(0, 0, 0, 0)
        self.originalPhaseLayout.setObjectName("originalPhaseLayout")
        self.verticalLayoutWidget_6 = QtWidgets.QWidget(self.filterTab)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(810, 380, 391, 371))
        self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")
        self.correctedPhaseLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_6)
        self.correctedPhaseLayout.setContentsMargins(0, 0, 0, 0)
        self.correctedPhaseLayout.setObjectName("correctedPhaseLayout")
        self.filterComboBox = QtWidgets.QComboBox(self.filterTab)
        self.filterComboBox.setGeometry(QtCore.QRect(490, 400, 251, 22))
        self.filterComboBox.setObjectName("filterComboBox")
        self.label = QtWidgets.QLabel(self.filterTab)
        self.label.setGeometry(QtCore.QRect(430, 400, 51, 21))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.groupBox_2 = QtWidgets.QGroupBox(self.filterTab)
        self.groupBox_2.setGeometry(QtCore.QRect(400, 380, 401, 161))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.applyfilterbutton = QtWidgets.QPushButton(self.groupBox_2)
        self.applyfilterbutton.setGeometry(QtCore.QRect(20, 70, 161, 28))
        self.applyfilterbutton.setObjectName("applyfilterbutton")
        self.removeFilterButton = QtWidgets.QPushButton(self.groupBox_2)
        self.removeFilterButton.setGeometry(QtCore.QRect(210, 70, 161, 28))
        self.removeFilterButton.setObjectName("removeFilterButton")
        self.groupBox_3 = QtWidgets.QGroupBox(self.filterTab)
        self.groupBox_3.setGeometry(QtCore.QRect(400, 550, 401, 201))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 81, 16))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit.setGeometry(QtCore.QRect(90, 80, 131, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.addfilterbutton = QtWidgets.QPushButton(self.groupBox_3)
        self.addfilterbutton.setGeometry(QtCore.QRect(230, 80, 151, 31))
        self.addfilterbutton.setObjectName("addfilterbutton")
        self.groupBox_2.raise_()
        self.verticalLayoutWidget_4.raise_()
        self.verticalLayoutWidget_5.raise_()
        self.verticalLayoutWidget_6.raise_()
        self.filterComboBox.raise_()
        self.label.raise_()
        self.groupBox_3.raise_()
        self.tabWidget.addTab(self.filterTab, "")
        self.signalTab = QtWidgets.QWidget()
        self.signalTab.setObjectName("signalTab")
        self.verticalLayoutWidget_7 = QtWidgets.QWidget(self.signalTab)
        self.verticalLayoutWidget_7.setGeometry(QtCore.QRect(0, 0, 1191, 211))
        self.verticalLayoutWidget_7.setObjectName("verticalLayoutWidget_7")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_7)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayoutWidget_8 = QtWidgets.QWidget(self.signalTab)
        self.verticalLayoutWidget_8.setGeometry(QtCore.QRect(0, 230, 1191, 211))
        self.verticalLayoutWidget_8.setObjectName("verticalLayoutWidget_8")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_8)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox_4 = QtWidgets.QGroupBox(self.signalTab)
        self.groupBox_4.setGeometry(QtCore.QRect(0, 450, 1191, 291))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox_4)
        self.radioButton.setGeometry(QtCore.QRect(200, 20, 101, 20))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox_4)
        self.radioButton_2.setGeometry(QtCore.QRect(460, 20, 95, 20))
        self.radioButton_2.setObjectName("radioButton_2")
        self.pushButton = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton.setGeometry(QtCore.QRect(720, 10, 131, 31))
        self.pushButton.setObjectName("pushButton")
        self.graphicsView = CustomGraphicsView(self.groupBox_4)
        self.graphicsView.setGeometry(QtCore.QRect(10, 61, 1171, 221))
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView.dragged.connect(self.generate_signal)
        self.tabWidget.addTab(self.signalTab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1201, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.filterComboBox.addItem("")
        self.filterComboBox.addItem("")
        self.filterComboBox.addItem("")
        self.filterComboBox.addItem("")

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.applyfilterbutton.clicked.connect(self.apply_allpass)
        self.zeros = []
        self.poles = []
        self.adjustedzeros = []
        self.adjustedpoles = []
        self.lastallpass = {
            1:(0,0),
            2:(0,0)
        }
        self.alllist =[]
        self.show_conjugates = False
        self.selected_element = 'Zero'
        self.plot_widget_zplane = MyPlotWidget(self.centralwidget)
        self.plot_widget_zplane.showGrid(x=True, y=True)
        self.plot_widget_zplane.setAspectLocked()
        self.plot_widget_zplane.setXRange(-2, 2)
        self.plot_widget_zplane.setYRange(-1.5, 1.5)
        self.plot_widget_zplane.setAspectLocked(lock=True, ratio=1)
        self.plot_widget_zplane.setTitle('Z-plane')
        self.plot_widget_zplane.setLabel('left', 'Imaginary')
        self.plot_widget_zplane.setLabel('bottom', 'Real')
        self.plot_widget_zplane.addLegend()
        self.plot_widget_zplane.select.connect(self.select)
        self.plot_widget_zplane.dragged.connect(self.drag)
        self.plot_widget_zplane.released.connect(self.clear_selection)
        self.zPoleLayout.addWidget(self.plot_widget_zplane)

        self.allpasswidget = MyPlotWidget(self.centralwidget)
        self.allpasswidget.showGrid(x=True, y=True)
        self.allpasswidget.setAspectLocked()
        self.zPoleLayout2.addWidget(self.allpasswidget)

        self.loadwidget = MyPlotWidget(self.centralwidget)
        self.loadwidget.showGrid(x=True, y=True)
        self.loadwidget.setAspectLocked()
        self.verticalLayout.addWidget(self.loadwidget)
        
        self.filteredwidget = MyPlotWidget(self.centralwidget)
        self.filteredwidget.showGrid(x=True, y=True)
        self.filteredwidget.setAspectLocked()
        self.verticalLayout_2.addWidget(self.filteredwidget)

        # Magnitude Response Plot
        self.fig_magnitude, self.ax_magnitude = plt.subplots(figsize=(8, 3))
        self.canvas_magnitude = FigureCanvas(self.fig_magnitude)
        self.magnitudeLayout.addWidget(self.canvas_magnitude)
        self.ax_magnitude.set_title('Magnitude Response')
        self.ax_magnitude.set_xlabel('Frequency')
        self.ax_magnitude.set_ylabel('Magnitude (dB)')

        # Phase Response Plot
        self.fig_phase, self.ax_phase = plt.subplots(figsize=(8, 3))
        self.canvas_phase = FigureCanvas(self.fig_phase)
        self.phaseLayout.addWidget(self.canvas_phase)
        self.ax_phase.set_title('Phase Response')
        self.ax_phase.set_xlabel('Frequency')
        self.ax_phase.set_ylabel('Phase (degrees)')

        self.fig_orgphase, self.ax_orgphase = plt.subplots(figsize=(8, 3))
        self.canvas_orgphase = FigureCanvas(self.fig_orgphase)
        self.originalPhaseLayout.addWidget(self.canvas_orgphase)
        self.ax_orgphase.set_title('original Phase Response')
        self.ax_orgphase.set_xlabel('Frequency')
        self.ax_orgphase.set_ylabel('Phase (degrees)')


        self.fig_newphase, self.ax_newphase = plt.subplots(figsize=(8, 3))
        self.canvas_newphase = FigureCanvas(self.fig_newphase)
        self.correctedPhaseLayout.addWidget(self.canvas_newphase)
        self.ax_newphase.set_title('corrected Phase Response')
        self.ax_newphase.set_xlabel('Frequency')
        self.ax_newphase.set_ylabel('Phase (degrees)')
        self.pushButton.clicked.connect(self.open_csv_file)
    


        self.update_plot()

        self.clearButton.clicked.connect(self.clear)
        self.clearAllButton.clicked.connect(self.clear_all)
        self.conjugateCheckBox.stateChanged.connect(self.toggle_conjugates)
        self.tabWidget.currentChanged.connect(self.update_plot)
        self.selected=None
        self.addfilterbutton.clicked.connect(self.add_filter_button_clicked)
        self.removeFilterButton.clicked.connect(self.remove_selected_item)

        self.allPassOptions=[ complex(0.5,0.5) ,complex(1,0.5),complex(1,1),complex(1,2),complex(2,0.5)]
        self.generated_signal_array=[]
        self.update_combo_box()


    def add_filter_button_clicked(self):
        # Get the text from the QLineEdit
        input_text = self.lineEdit.text()

        # Split the input into real and imaginary parts
        parts = input_text.split("+")
        if len(parts) != 2:
            print("Invalid complex number format")
            return

        real_part = parts[0].strip()
        imaginary_part = parts[1].strip("j").strip()

        try:
            # Convert the parts to floats and create a complex number
            real_part = float(real_part)
            imaginary_part = float(imaginary_part)
            complex_form = complex(real_part, imaginary_part)

            # Append the complex number to the array
            self.allPassOptions.append(complex_form)

            # Clear the QLineEdit
            self.lineEdit.clear()

            # Update the contents of the ComboBox with the new array
            self.update_combo_box()
        except ValueError:
            print("Invalid complex number format")
    
    def remove_selected_item(self):
        # Get the currently selected item index
        current_index = self.filterComboBox.currentIndex()
        print("wasalt")

        if current_index != -1:
            # Remove the selected item from the array
            del self.allPassOptions[current_index]

            # Update the contents of the ComboBox with the new array
            self.update_combo_box()

    def update_combo_box(self):
        # Clear the current items in the ComboBox
        self.filterComboBox.clear()

        # Add the items from the array to the ComboBox
        self.filterComboBox.addItems(map(str, self.allPassOptions))



    def generate_signal(self, event):
        if self.radioButton_2.isChecked():
            # Get the x position from the mouse event
            y_position = event.pos().y()

            # Append the x position to the array
            self.generated_signal_array.append(y_position)

            # Update the MyPlotWidget with the new x values
            self.loadwidget.update_plot(self.generated_signal_array)

            self.apply_filter(self.generated_signal_array)

    def open_csv_file(self):
        if self.radioButton.isChecked():
            file_dialog = QFileDialog()
            file_path, _ = file_dialog.getOpenFileName(caption='Open CSV File', filter='CSV Files (*.csv)')
            if file_path:
                df = pd.read_csv(file_path)

                # Assuming your CSV file has two columns: time and magnitude
                time = df.iloc[:, 0]
                magnitude = df.iloc[:, 1]
                self.loadwidget.update_plot(magnitude)
                self.apply_filter(magnitude)
            
            

    def apply_filter(self, input_signal):
        # Convert the coordinates of zeros and poles to complex numbers
        zeros_complex = [complex(z[0], z[1]) for z in self.zeros]
        poles_complex = [complex(p[0], p[1]) for p in self.poles]

        # Create the transfer function using zeros and poles
        num, den = signal.zpk2tf(zeros_complex, poles_complex, 1)
        
        # Apply the filter to the input signal
        output_signal = signal.lfilter(num, den, input_signal)

        self.filteredwidget.update_plot(np.real(output_signal))
 

    def clear_selection(self):
       self.selected = None

    def clear(self):
        if  self.zerosRadioButton.isChecked(): 
            self.zeros = []
        elif self.polesRadioButton.isChecked():
            self.poles = []
        self.update_plot()

    def clear_all(self):
        self.zeros = []
        self.poles = []
        self.alllist
        self.update_plot()

    def toggle_conjugates(self, state):
        self.show_conjugates = state == 2
        self.compute_frequency_response()
        self.update_plot()

    def getXY(self,widget, event):
        pos = event.pos()
        view_coords = widget.plotItem.vb.mapSceneToView(pos)
        x, y = view_coords.x(), view_coords.y()
        return x, y


    def get_zero_or_pole_at_coordinates(self, coordinates):
        selected_zero=None
        selected_pole=None
        for zero in self.zeros:
            if zero[0] == coordinates[0] and zero[1] == coordinates[1]:
                selected_zero = zero
        for pole in self.poles:
            if pole[0] == coordinates[0] and pole[1] == coordinates[1]:
                selected_pole = pole
        return selected_zero, selected_pole

    def drag(self, event):
        if self.selected:
            x, y = self.getXY(self.plot_widget_zplane, event)
            # Check if the dragged point is close to any existing zeros
            selected_zero,selected_pole = self.get_zero_or_pole_at_coordinates(self.selected)
            new = (x,y)
            if selected_zero:
                selected_zero = list(selected_zero)
                self.remove_zero_or_pole_at_coordinates(selected_zero)
                self.zeros.append(new)
            elif selected_pole:
                selected_pole = list(selected_pole)
                self.remove_zero_or_pole_at_coordinates(selected_pole)
                self.poles.append(new)
            self.alllist.append(new)
            self.selected=new
            self.update_plot()

    


    def select(self,event):
        x,y = self.getXY(self.plot_widget_zplane,event)
        for i in range(len(self.alllist)):
            if((self.alllist[i][0]-0.1<x<self.alllist[i][0]+0.1) and (self.alllist[i][1]-0.1<y<self.alllist[i][1]+0.1)):
                if event.button() == Qt.LeftButton:
                    self.selected = (self.alllist[i][0],self.alllist[i][1])
                    return
                elif event.button() == Qt.RightButton:
                    self.remove_zero_or_pole_at_coordinates((self.alllist[i][0],self.alllist[i][1]))
                    return

        if self.zerosRadioButton.isChecked():
                self.zeros.append((x, y))
                self.alllist.append((x,y))
        elif self.polesRadioButton.isChecked():
                self.poles.append((x, y))
                self.alllist.append((x,y))
        self.update_plot()
    
    def remove_zero_or_pole_at_coordinates(self, coordinates):
        x, y = coordinates
        # Remove zero if exists at the given coordinates
        self.zeros = [zero for zero in self.zeros if (zero[0], zero[1]) != (x, y)]
        # Remove pole if exists at the given coordinates
        self.poles = [pole for pole in self.poles if (pole[0], pole[1]) != (x, y)]

        self.alllist = [point for point in self.alllist if (point[0], point[1]) != (x, y)]
        # Update the plot after removing the zero or pole
        self.update_plot()


    def update_plot(self):
        if self.tabWidget.currentIndex() == 0:
        
            self.plot_widget_zplane.clear()
            # Plot unit circle
            unit_circle = pg.EllipseROI(pos=(-1, -1), size=(2, 2), pen=pg.mkPen('white'))
            self.plot_widget_zplane.addItem(unit_circle)

            # Plot zeros and poles
            self.plot_widget_zplane.scatterPlot([z[0] for z in self.zeros], [z[1] for z in self.zeros],
                                                symbol='o', pen='b', name='Zeros')
            self.plot_widget_zplane.scatterPlot([p[0] for p in self.poles], [p[1] for p in self.poles],
                                                symbol='x', pen='r', name='Poles')

            if self.show_conjugates:
                # Plot conjugates
                for zero in self.zeros:
                    if zero[1] != 0:
                        self.plot_widget_zplane.scatterPlot([zero[0]], [-zero[1]],
                                                            symbol='o', pen='white', alpha=0.5)
                for pole in self.poles:
                    if pole[0] != 0:
                        self.plot_widget_zplane.scatterPlot([pole[0]], [-pole[1]],
                                                            symbol='x', pen='white', alpha=0.5)
            # Update frequency response plots
            self.ax_magnitude.clear()
            self.ax_phase.clear()

            # Compute frequency response
            frequencies, response = self.compute_frequency_response()
            # Plot magnitude response
            self.ax_magnitude.plot(frequencies, 20 * log10(abs(response)))
            self.ax_magnitude.set_title('Magnitude Response')
            self.ax_magnitude.set_xlabel('Frequency')
            self.ax_magnitude.set_ylabel('Magnitude (dB)')

            # Plot phase response
            self.ax_phase.plot(frequencies, angle(response, deg=True))
            self.ax_phase.set_title('Phase Response')
            self.ax_phase.set_xlabel('Frequency')
            self.ax_phase.set_ylabel('Phase (degrees)')
            self.canvas_magnitude.draw()
            self.canvas_phase.draw()





    def compute_frequency_response(self):
        # Compute frequency response using zeros and poles
        system = [1]  # Numerator coefficients
        den = [1]  # Denominator coefficients

        for zero in self.zeros:
            complexzero =(zero[0] + 1j * zero[1])
            system = convolve(system, [1, -complexzero])
            if zero[1] != 0 and self.show_conjugates:
                    conjugate_zero = np.conjugate(complexzero)
                    system = convolve(system, [1, -conjugate_zero])

        for pole in self.poles:
            complexpole =(pole[0] + 1j * pole[1])
            den = convolve(den, [1, -complexpole])
            # Include conjugate poles
            if pole[1] != 0 and self.show_conjugates:
                conjugate_pole = np.conjugate(complexpole)
                den = convolve(den, [1, -conjugate_pole])

        frequencies, response = freqz(system, den)
        return frequencies, response
    
    def apply_allpass(self):

        # Assuming allPassOptions is a list of complex numbers, e.g., [a + bj, c + dj, ...]
        selected_option = self.allPassOptions[self.filterComboBox.currentIndex()]

        # Create the transfer function based on the selected complex number
        num = [-selected_option,1]
        den = [1, -selected_option]
        # Get zeros and poles
        zeros, poles, _ = tf2zpk(num, den)
        self.zeros.append((zeros[0].real,zeros[0].imag))
        self.poles.append((poles[0].real,poles[0].imag))
   
        self.remove_zero_or_pole_at_coordinates(self.lastallpass[1])
        self.remove_zero_or_pole_at_coordinates(self.lastallpass[2])
        frequencies, response = self.compute_frequency_response()
 
        # Plot phase response
        self.ax_newphase.clear()
        self.ax_newphase.plot(frequencies, angle(response, deg=True))
        self.ax_newphase.set_title('corrected Phase Response')
        self.ax_newphase.set_xlabel('Frequency')
        self.ax_newphase.set_ylabel('Phase (degrees)')
        self.canvas_newphase.draw()

        self.allpasswidget.clear()
        unit_circle = pg.EllipseROI(pos=(-1, -1), size=(2, 2), pen=pg.mkPen('white'))
        self.allpasswidget.addItem(unit_circle)
        # Plot zeros and poles
        self.allpasswidget.scatterPlot(x=zeros.real, y=zeros.imag, symbol='o', pen='b', name='Zeros')
        self.allpasswidget.scatterPlot(x=poles.real, y=poles.imag, symbol='x', pen='r', name='Poles')
        # Compute the frequency response
        w, FreqResp = freqz(num, den)
        phase_response = np.angle(FreqResp)

        # Plot phase response on ax_newphase
        self.ax_orgphase.clear()  # Clear existing plot
        self.ax_orgphase.plot(w, phase_response, label='All-pass filter')
        self.ax_orgphase.set_title('Phase Response of All-pass Filter')
        self.ax_orgphase.set_xlabel('Frequency (radians/sample)')
        self.ax_orgphase.set_ylabel('Phase (radians)')
        self.ax_orgphase.legend()
        self.ax_orgphase.grid(True)
        self.canvas_orgphase.draw()

        self.lastallpass[1] =(zeros[0].real,zeros[0].imag)
        self.lastallpass[2] =(poles[0].real,poles[0].imag)

    
    def get_zero_or_pole_at_coordinates(self, coordinates):
        x, y = coordinates
        # Find the zero with the specified coordinates
        selected_zero = next((zero for zero in self.zeros if (zero[0], zero[1]) == (x, y)), None)
        # Find the pole with the specified coordinates
        selected_pole = next((pole for pole in self.poles if (pole[0], pole[1]) == (x, y)), None)

        return selected_zero, selected_pole
    
    

        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Zeros & Poles"))
        self.zerosRadioButton.setText(_translate("MainWindow", "Zeros"))
        self.polesRadioButton.setText(_translate("MainWindow", "Poles"))
        self.clearButton.setText(_translate("MainWindow", "Clear"))
        self.conjugateCheckBox.setText(_translate("MainWindow", "Add Conjugate"))
        self.clearAllButton.setText(_translate("MainWindow", "Clear All"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.zPoleTab), _translate("MainWindow", "Z-Pole plot"))
        self.label.setText(_translate("MainWindow", "Filter:"))
        self.groupBox_2.setTitle(_translate("MainWindow", "My Filters"))
        self.applyfilterbutton.setText(_translate("MainWindow", "apply changes"))
        self.removeFilterButton.setText(_translate("MainWindow", "Remove"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Add Filter"))
        self.label_2.setText(_translate("MainWindow", "Coordinates:"))
        self.addfilterbutton.setText(_translate("MainWindow", "Add"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.filterTab), _translate("MainWindow", "Filter"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Controls"))
        self.radioButton.setText(_translate("MainWindow", "Load Signal"))
        self.radioButton_2.setText(_translate("MainWindow", "Touch Pad"))
        self.pushButton.setText(_translate("MainWindow", "Load"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.signalTab), _translate("MainWindow", "Signal"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
