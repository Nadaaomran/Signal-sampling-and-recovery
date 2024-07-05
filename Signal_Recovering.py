
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import numpy as np
import pandas as pd
from PyQt5.QtWidgets import QFileDialog , QMenuBar , QMainWindow, QApplication, QSizePolicy, QMessageBox
from numpy import ceil, floor, cos, arange, pi

class Composed_signal:
   def __init__(self):
        self.frequency=[]
        self.amplitude=[]
        self.phase=[]
        self.x_values=[]
        self.y_values=[]

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(764, 569)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        style_sheet = """
    QWidget#centralwidget {
        background-color: #f0f0f0; /* Default off-white background */
        color: black; /* Default text color */
    }

    QPushButton {
        border: 1px solid #888;
        border-radius: 5px;
        background-color: #d3d3d3;
        color: black;
        padding: 5px;
    }
    QPushButton:hover {
        background-color: #c0c0c0;
    }
    QPushButton:pressed {
        background-color: #a9a9a9;
    }

    QComboBox {
        border: 1px solid #888;
        border-radius: 5px;
        background-color: #d3d3d3;
        color: black;
        padding: 1px 18px 1px 3px;
        min-width: 6em;
    }
    QComboBox:editable {
        background: white;
    }
    QComboBox:!editable, QComboBox::drop-down:editable {
        background: #d3d3d3;
    }
    QComboBox:!editable:on, QComboBox::drop-down:editable:on {
        background: #c0c0c0;
    }
    QComboBox::drop-down {
        subcontrol-origin: padding;
        subcontrol-position: top right;
        width: 15px;
        border-left: none;
    }
    QComboBox::down-arrow {
        width: 15px;
        height: 15px;
    }

    QSlider::groove:horizontal, QSlider::groove:vertical {
        border: 1px solid #888;
        background: #d3d3d3;
        border-radius: 5px;
    }
    QSlider::groove:horizontal {
        height: 8px;
        margin: 2px 0;
    }
    QSlider::groove:vertical {
        width: 8px;
        margin: 0 2px;
    }
    QSlider::handle:horizontal, QSlider::handle:vertical {
        background: white;
        border: 1px solid #888;
        border-radius: 5px;
    }
    QSlider::handle:horizontal {
        width: 18px;
        margin: -2px 0;
    }
    QSlider::handle:vertical {
        height: 18px;
        margin: 0 -2px;
    }

    QCheckBox {
        spacing: 5px;
        color: black;
    }
    QCheckBox::indicator {
        width: 15px;
        height: 15px;
        border: 1px solid #888;
        border-radius: 3px;
        background: #d3d3d3;
    }
    QCheckBox::indicator:checked {
        background: #b1b1b1;
    }

    QRadioButton {
        spacing: 5px;
        color: black;
    }
    QRadioButton::indicator {
        width: 15px;
        height: 15px;
        border: 1px solid #888;
        border-radius: 7px;
        background: #d3d3d3;
    }
    QRadioButton::indicator:checked {
        background: #b1b1b1;
    }

    QLabel {
        color: black;
    }

    QGroupBox {
        border: 1px solid #888;
        border-radius: 5px;
        margin-top: 6px;
        background-color: #d3d3d3;
    }
    QGroupBox::title {
        subcontrol-origin: margin;
        subcontrol-position: top left;
        padding: 0 3px;
        color: black;
    }

    PlotWidget {
        background-color: #d3d3d3;
        border: 1px solid #888;
    }
    QTabWidget::pane { 
        border: 1px solid #888;
        background-color: #d3d3d3;
        border-radius: 5px;
    }
    QTabWidget::tab-bar {
        left: 5px; 
    }

    QTabBar::tab {
        background: #d3d3d3;
        border: 1px solid #888;
        padding: 10px;
        border-top-left-radius: 2px;
        border-top-right-radius: 2px;
    }
    QTabBar::tab:selected {
        background: #c0c0c0;
        margin-bottom: -1px;
    }
    QTabBar::tab:!selected {
        background: #d3d3d3;
    }
    QTabBar::tab:hover {
        background: #b1b1b1;
    }
"""
        self.centralwidget.setStyleSheet(style_sheet)
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)

        self.tabWidget.setObjectName("tabWidget")
        self.sampler_tap = QtWidgets.QWidget()
        self.sampler_tap.setObjectName("sampler_tap")
        self.gridLayout_17 = QtWidgets.QGridLayout(self.sampler_tap)
        self.gridLayout_17.setObjectName("gridLayout_17")

        self.original_signal = PlotWidget(self.sampler_tap)
        self.original_signal.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.original_signal.setObjectName("original_signal")
        self.gridLayout_17.addWidget(self.original_signal, 0, 0, 1, 1)

        self.recovered_signal = PlotWidget(self.sampler_tap)
        self.recovered_signal.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.recovered_signal.setObjectName("recovered_signal")
        self.gridLayout_17.addWidget(self.recovered_signal, 1, 0, 1, 1)

        self.error_signal = PlotWidget(self.sampler_tap)
        self.error_signal.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.error_signal.setObjectName("error_signal")
        self.gridLayout_17.addWidget(self.error_signal, 2, 0, 1, 1)

        self.recovered_signal.setYLink(self.original_signal)
        self.error_signal.setYLink(self.original_signal)

        self.frame_5 = QtWidgets.QFrame(self.sampler_tap)
        self.frame_5.setMinimumSize(QtCore.QSize(0, 75))
        self.frame_5.setMaximumSize(QtCore.QSize(16777215, 75))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout_16 = QtWidgets.QGridLayout(self.frame_5)
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")

        self.browse_button = QtWidgets.QPushButton(self.frame_5)
        self.browse_button.setMinimumSize(QtCore.QSize(100, 30))
        self.browse_button.setMaximumSize(QtCore.QSize(100, 30))
        self.browse_button.setObjectName("browse_button")
        self.horizontalLayout_14.addWidget(self.browse_button)
        self.browse_button.clicked.connect(self.get_csv_file)
        # Set the shortcut to Ctrl+B
        self.browse_button.setShortcut("Ctrl+B")
        browse_shortcut = QtWidgets.QShortcut(QtGui.QKeySequence("Ctrl+B"), MainWindow)
        browse_shortcut.activated.connect(self.get_csv_file)

        self.composed_signals_groupbox = QtWidgets.QGroupBox(self.frame_5)
        self.composed_signals_groupbox.setMinimumSize(QtCore.QSize(0, 65))
        self.composed_signals_groupbox.setMaximumSize(QtCore.QSize(16777215, 65))
        self.composed_signals_groupbox.setObjectName("composed_signals_groupbox")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.composed_signals_groupbox)
        self.gridLayout_13.setObjectName("gridLayout_13")

        self.composed_signals_combobox = QtWidgets.QComboBox(self.composed_signals_groupbox)
        self.composed_signals_combobox.setMinimumSize(QtCore.QSize(0, 25))
        self.composed_signals_combobox.setMaximumSize(QtCore.QSize(16777215, 25))
        self.composed_signals_combobox.setObjectName("composed_signals_combobox")
        self.composed_signals_combobox.activated.connect(self.select_composed_signal)
        self.gridLayout_13.addWidget(self.composed_signals_combobox, 0, 0, 1, 1)
        self.horizontalLayout_14.addWidget(self.composed_signals_groupbox)

        self.fs_groupbox = QtWidgets.QGroupBox(self.frame_5)
        self.fs_groupbox.setMinimumSize(QtCore.QSize(400, 65))
        self.fs_groupbox.setMaximumSize(QtCore.QSize(400, 65))
        self.fs_groupbox.setObjectName("fs_groupbox")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.fs_groupbox)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setSpacing(25)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setSpacing(5)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")

        self.fs_slider = QtWidgets.QSlider(self.fs_groupbox)
        self.fs_slider.setOrientation(QtCore.Qt.Horizontal)
        self.fs_slider.setObjectName("fs_slider")
        self.horizontalLayout_11.addWidget(self.fs_slider)
        self.fs_slider.valueChanged.connect(lambda: self.update_fs_slider_value(self.fs_slider.value() / 10.0))
        self.fs_slider.setSingleStep(1)

        self.label_fs_value = QtWidgets.QLabel(self.fs_groupbox)
        self.label_fs_value.setObjectName("label_fs_value")
        self.horizontalLayout_11.addWidget(self.label_fs_value)

        self.label = QtWidgets.QLabel(self.fs_groupbox)
        self.label.setObjectName("label")
        self.horizontalLayout_11.addWidget(self.label)
        self.horizontalLayout_13.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setSpacing(5)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")

        self.fs_normal_slider = QtWidgets.QSlider(self.fs_groupbox)
        self.fs_normal_slider.setOrientation(QtCore.Qt.Horizontal)
        self.fs_normal_slider.setObjectName("fs_normal_slider")
        self.horizontalLayout_12.addWidget(self.fs_normal_slider)
        self.fs_normal_slider.setMinimum(0)  # Set the minimum value to 0
        self.fs_normal_slider.setMaximum(40)  # Set the maximum value to 4
        self.fs_normal_slider.setSingleStep(1)
        self.fs_normal_slider.valueChanged.connect(lambda: self.update_fs_normal_slider_value(self.fs_normal_slider.value() /10.0))
        

        self.label_fs_normal_value = QtWidgets.QLabel(self.fs_groupbox)
        self.label_fs_normal_value.setObjectName("label_fs_normal_value")
        self.horizontalLayout_12.addWidget(self.label_fs_normal_value)

        self.label_2 = QtWidgets.QLabel(self.fs_groupbox)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_12.addWidget(self.label_2)
        self.horizontalLayout_13.addLayout(self.horizontalLayout_12)
        self.gridLayout_14.addLayout(self.horizontalLayout_13, 0, 0, 1, 1)
        self.horizontalLayout_14.addWidget(self.fs_groupbox)

        self.snr_groupbox = QtWidgets.QGroupBox(self.frame_5)
        self.snr_groupbox.setMinimumSize(QtCore.QSize(170, 65))
        self.snr_groupbox.setMaximumSize(QtCore.QSize(170, 65))
        self.snr_groupbox.setObjectName("snr_groupbox")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.snr_groupbox)
        self.gridLayout_15.setObjectName("gridLayout_15")

        self.snr_slider = QtWidgets.QSlider(self.snr_groupbox)
        self.snr_slider.setOrientation(QtCore.Qt.Horizontal)
        self.snr_slider.setObjectName("snr_slider")
        self.snr_slider.valueChanged.connect(self.update_snr_slider_value)

        self.gridLayout_15.addWidget(self.snr_slider, 0, 0, 1, 1)
        self.horizontalLayout_14.addWidget(self.snr_groupbox)
        self.gridLayout_16.addLayout(self.horizontalLayout_14, 0, 0, 1, 1)
        self.gridLayout_17.addWidget(self.frame_5, 3, 0, 1, 1)

        self.tabWidget.addTab(self.sampler_tap, "")
        self.composer_tap = QtWidgets.QWidget()
        self.composer_tap.setObjectName("composer_tap")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.composer_tap)
        self.gridLayout_12.setObjectName("gridLayout_12")

        self.components_graph = PlotWidget(self.composer_tap)
        self.components_graph.setMinimumSize(QtCore.QSize(0, 0))
        self.components_graph.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.components_graph.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.components_graph.setObjectName("components_graph")
        self.gridLayout_12.addWidget(self.components_graph, 0, 0, 1, 1)

        self.components_groupbox = QtWidgets.QGroupBox(self.composer_tap)
        self.components_groupbox.setMinimumSize(QtCore.QSize(0, 150))
        self.components_groupbox.setMaximumSize(QtCore.QSize(16777215, 150))
        self.components_groupbox.setObjectName("components_groupbox")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.components_groupbox)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.frame_4 = QtWidgets.QFrame(self.components_groupbox)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_10.setObjectName("gridLayout_10")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_10.addItem(spacerItem, 0, 0, 1, 1)

        self.save_signal_button = QtWidgets.QPushButton(self.frame_4)
        self.save_signal_button.setMinimumSize(QtCore.QSize(0, 30))
        self.save_signal_button.setMaximumSize(QtCore.QSize(16777215, 30))
        self.save_signal_button.setObjectName("save_signal_button")
        self.save_signal_button.clicked.connect(self.Save_composed_signal)
        # Set the shortcut to Ctrl+S
        self.save_signal_button.setShortcut("Ctrl+S")
        save_shortcut = QtWidgets.QShortcut(QtGui.QKeySequence("Ctrl+S"), MainWindow)
        save_shortcut.activated.connect(self.Save_composed_signal)

        self.gridLayout_10.addWidget(self.save_signal_button, 0, 1, 1, 1)
        self.gridLayout_9.addWidget(self.frame_4, 1, 0, 1, 1)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.frame_3 = QtWidgets.QFrame(self.components_groupbox)
        self.frame_3.setMinimumSize(QtCore.QSize(330, 0))
        self.frame_3.setMaximumSize(QtCore.QSize(330, 16777215))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")

        self.remove_button = QtWidgets.QPushButton(self.frame_3)
        self.remove_button.setMinimumSize(QtCore.QSize(65, 30))
        self.remove_button.setMaximumSize(QtCore.QSize(65, 30))
        self.remove_button.setObjectName("remove_button")
        self.horizontalLayout_9.addWidget(self.remove_button)
        self.remove_button.clicked.connect(self.Remove_selected_component)
        # Set the shortcut to Ctrl+R
        self.remove_button.setShortcut("Ctrl+R")
        remove_shortcut = QtWidgets.QShortcut(QtGui.QKeySequence("Ctrl+R"), MainWindow)
        remove_shortcut.activated.connect(self.Remove_selected_component)

        self.components_combobox = QtWidgets.QComboBox(self.frame_3)
        self.components_combobox.setMinimumSize(QtCore.QSize(0, 25))
        self.components_combobox.setMaximumSize(QtCore.QSize(16777215, 25))
        self.components_combobox.setObjectName("components_combobox")
        self.horizontalLayout_9.addWidget(self.components_combobox)
        self.gridLayout_8.addLayout(self.horizontalLayout_9, 0, 0, 1, 1)
        self.horizontalLayout_10.addWidget(self.frame_3)
        self.frame_2 = QtWidgets.QFrame(self.components_groupbox)
        self.frame_2.setMinimumSize(QtCore.QSize(300, 0))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setSpacing(20)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")

        self.frequency = QtWidgets.QLabel(self.frame_2)
        self.frequency.setObjectName("frequency")
        self.horizontalLayout_5.addWidget(self.frequency)
        self.frequency_spin = QtWidgets.QDoubleSpinBox(self.frame_2)
        self.frequency_spin.setMinimumSize(QtCore.QSize(0, 25))
        self.frequency_spin.setMaximumSize(QtCore.QSize(16777215, 25))
        self.frequency_spin.setObjectName("frequency_spin")
        self.horizontalLayout_5.addWidget(self.frequency_spin)
        self.hz_2 = QtWidgets.QLabel(self.frame_2)
        self.hz_2.setObjectName("hz_2")
        self.horizontalLayout_5.addWidget(self.hz_2)
        self.horizontalLayout_8.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSpacing(5)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.frequency_spin.valueChanged.connect(self.plot_component)

        self.amplitude = QtWidgets.QLabel(self.frame_2)
        self.amplitude.setObjectName("amplitude")
        self.horizontalLayout_6.addWidget(self.amplitude)
        self.amplitude_spin = QtWidgets.QDoubleSpinBox(self.frame_2)
        self.amplitude_spin.setMinimumSize(QtCore.QSize(0, 25))
        self.amplitude_spin.setMaximumSize(QtCore.QSize(16777215, 25))
        self.amplitude_spin.setObjectName("amplitude_spin")
        self.horizontalLayout_6.addWidget(self.amplitude_spin)
        self.horizontalLayout_8.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setSpacing(5)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.amplitude_spin.valueChanged.connect(self.plot_component)

        self.phase = QtWidgets.QLabel(self.frame_2)
        self.phase.setObjectName("phase")
        self.horizontalLayout_7.addWidget(self.phase)
        self.phase_spin = QtWidgets.QSpinBox(self.frame_2)
        self.phase_spin.setMinimumSize(QtCore.QSize(0, 25))
        self.phase_spin.setMaximumSize(QtCore.QSize(16777215, 25))
        self.phase_spin.setObjectName("phase_spin")
        self.horizontalLayout_7.addWidget(self.phase_spin)
        self.phase_spin.valueChanged.connect(self.plot_component)
        

        self.pi = QtWidgets.QLabel(self.frame_2)
        self.pi.setObjectName("pi")
        self.horizontalLayout_7.addWidget(self.pi)
        self.horizontalLayout_8.addLayout(self.horizontalLayout_7)

        self.add_button = QtWidgets.QPushButton(self.frame_2)
        self.add_button.setMinimumSize(QtCore.QSize(0, 30))
        self.add_button.setMaximumSize(QtCore.QSize(16777215, 30))
        self.add_button.setObjectName("add_button")
        self.horizontalLayout_8.addWidget(self.add_button)
        self.add_button.clicked.connect(self.AddComponent)
        # Set the shortcut to Ctrl+A
        self.add_button.setShortcut("Ctrl+A")
        add_shortcut = QtWidgets.QShortcut(QtGui.QKeySequence("Ctrl+A"), MainWindow)
        add_shortcut.activated.connect(self.AddComponent)
        
        self.gridLayout_7.addLayout(self.horizontalLayout_8, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem1, 0, 0, 1, 1)
        self.horizontalLayout_10.addWidget(self.frame_2)
        self.gridLayout_9.addLayout(self.horizontalLayout_10, 0, 0, 1, 1)
        self.gridLayout_12.addWidget(self.components_groupbox, 1, 0, 1, 1)

        self.signals_groupbox = QtWidgets.QGroupBox(self.composer_tap)
        self.signals_groupbox.setMinimumSize(QtCore.QSize(0, 60))
        self.signals_groupbox.setMaximumSize(QtCore.QSize(16777215, 60))
        self.signals_groupbox.setObjectName("signals_groupbox")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.signals_groupbox)
        self.gridLayout_11.setObjectName("gridLayout_11")

        self.signals_combobox = QtWidgets.QComboBox(self.signals_groupbox)
        self.signals_combobox.setObjectName("signals_combobox")
        self.gridLayout_11.addWidget(self.signals_combobox, 0, 0, 1, 1)
        self.gridLayout_12.addWidget(self.signals_groupbox, 2, 0, 1, 1)
        self.signals_combobox.activated.connect(self.Edit_selected_signal)

        self.tabWidget.addTab(self.composer_tap, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        

        #A list to carry all the mixed signals prepared by the composer
        self.Mixed_signals=[]
        self.Current_signal_index= 0
        #Create 3 saved composed signals for test cases 
        self.Current_Signal= Composed_signal()
        self.Current_Signal.frequency.append(2)
        self.Current_Signal.amplitude.append(1)
        self.Current_Signal.phase.append(0)
        #Create a x-axis array
        self.Current_Signal.x_values = np.linspace(0, 10, num=1000)
        #Create an empty y-axis array
        self.Current_Signal.y_values= np.zeros_like(self.Current_Signal.x_values)
        #Calculate the y coordinate of the resulted mixed signal which corresponds to each x coordinate
        for frequency, amplitude, phase in zip(self.Current_Signal.frequency, self.Current_Signal.amplitude, self.Current_Signal.phase):
            y_signal = amplitude * np.sin(2 * np.pi * frequency * self.Current_Signal.x_values + phase * np.pi)
            self.Current_Signal.y_values+= y_signal
        self.Mixed_signals.append(self.Current_Signal)
        self.Current_signal_index= len(self.Mixed_signals)
        self.Current_Signal= Composed_signal()
        self.Current_Signal.frequency.append(4)
        self.Current_Signal.amplitude.append(3)
        self.Current_Signal.phase.append(0)
        self.Current_Signal.frequency.append(1)
        self.Current_Signal.amplitude.append(3)
        self.Current_Signal.phase.append(1)
        #Create a x-axis array
        self.Current_Signal.x_values = np.linspace(0, 10, num=1000)
        #Create an empty y-axis array
        self.Current_Signal.y_values= np.zeros_like(self.Current_Signal.x_values)
        #Calculate the y coordinate of the resulted mixed signal which corresponds to each x coordinate
        for frequency, amplitude, phase in zip(self.Current_Signal.frequency, self.Current_Signal.amplitude, self.Current_Signal.phase):
            y_signal = amplitude * np.sin(2 * np.pi * frequency * self.Current_Signal.x_values + phase * np.pi)
            self.Current_Signal.y_values+= y_signal
        self.Mixed_signals.append(self.Current_Signal)
        self.Current_signal_index= len(self.Mixed_signals)
        self.Current_Signal= Composed_signal()
        for Signal_index in range (len(self.Mixed_signals)):
            self.composed_signals_combobox.addItem(f"Signal {Signal_index}", userData=Signal_index)
            self.signals_combobox.addItem(f"Signal {Signal_index}", userData=Signal_index)
        self.signals_combobox.setCurrentIndex(-1)
        self.composed_signals_combobox.setCurrentIndex(-1)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Set default sampling rate
        self.sampling_rate = 10
        self.fs_slider.setValue(10)
        self.snr_slider.setMinimum(1)  
        self.snr_slider.setMaximum(100)
        self.snr_slider.setValue(100)

    def update_fs_slider_value(self, value):
        formatted_value = "{:.1f}".format(value)
        self.label_fs_value.setText(str(formatted_value))
        if (self.fs_slider.value() == 0):
            self.original_signal.clear()
            self.recovered_signal.clear()
            self.error_signal.clear()
            self.original_signal.plot(self.x_values, self.y_values, pen='w')  # Plot the original signal with white pen color
        else:
            self.sampling_rate = value
            self.sampling()


    def update_fs_normal_slider_value(self, value):
        self.label_fs_normal_value.setText(str(value))
        new_value = value * self.fmax
        self.fs_slider.setValue(int(new_value * 10))
        self.update_fs_slider_value(new_value)

    def update_snr_slider_value(self):
        snr = self.snr_slider.value() /100
        self.add_noise(snr)
        self.sampling()

    #browse to select the csv file
    def get_csv_file(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(None, "Select CSV File", "", "CSV Files (*.csv)")

        if file_path:
            # Load CSV file using pandas
            df = pd.read_csv(file_path)
            self.x_values = df['Time'].values
            self.y_values = df['Voltage'].values
            if (self.snr_slider.value()==100):
                self.y_values_noisy=self.y_values
            else:
                self.add_noise(self.snr_slider.value()/100)
            self.fmax = df['fmax'].values[0]
            self.fmax= int(self.fmax)
            self.fs_slider.setMinimum(0)  # Set the minimum value to 0
            self.fs_slider.setMaximum(40 * self.fmax)
            self.update_fs_slider_value(self.fs_slider.value() / 10.0)
            self.composed_signals_combobox.setCurrentIndex(-1)
            self.original_signal.clear()
            self.sampling()

    def add_noise(self, snr):
        self.noise = np.random.normal(0, self.y_values.std() / snr, len(self.y_values))
        self.y_values_noisy = self.y_values + 0.1 * self.noise


    def sampling(self):
        # Clear the old plot
        self.original_signal.clear()
        self.sampling_interval = 1 / self.sampling_rate

        # Generate the sampling points
        self.sampling_points = np.arange(self.x_values.min(), self.x_values.max(), self.sampling_interval)

        if (self.snr_slider.value()==100):
            self.y_values_noisy=self.y_values

        # Perform sampling by interpolating the original signal at the sampling points
        self.sampled_signal = np.interp(self.sampling_points, self.x_values, self.y_values_noisy)
        
        # Plot the original signal
        self.original_signal.plot(self.x_values, self.y_values_noisy, pen='w')  # Plot the original signal with white pen color
        # Plot the original signal
        self.original_signal.plot(self.sampling_points, self.sampled_signal, pen=None, symbol='o', symbolPen='g', symbolBrush='g', symbolSize=4)  # Plot the sampled signal with green circle markers
        self.sampler_tap.show() 
        self.reconstruct_signal()


    def reconstruct_signal(self):
        # Clear the old plot
        self.recovered_signal.clear()

        self.reconstructed_signal = np.zeros_like(self.x_values)

        for i in range(len(self.sampling_points)):
            reconstruct = self.sampled_signal[i] * np.sinc((self.x_values - self.sampling_points[i]) / self.sampling_interval)
            self.reconstructed_signal+= reconstruct

        # Plot the reconstructed signal
        self.recovered_signal.plot(self.x_values,self.reconstructed_signal, pen='r')
        self.plot_error_signal()
    

    def plot_error_signal(self):
        # Clear the old plot
        self.error_signal.clear()

        # Calculate the difference between original and reconstructed signals
        difference = self.y_values -  self.reconstructed_signal

        # Plot the signal difference
        self.error_signal.plot(self.x_values, difference, pen='b')

        # Show the plot
        self.error_signal.show()


    def plot_component(self):
        self.components_graph.clear()
        x_trial= np.linspace(0, 10, num=1000)
        y_signal = self.amplitude_spin.value() * np.sin(2 * np.pi * self.frequency_spin.value() * x_trial + self.phase_spin.value() * np.pi)
        y_trial= self.Current_Signal.y_values.copy()
        if len(self.Current_Signal.y_values)== 0:
            y_trial= np.zeros_like(x_trial)
        y_trial+= y_signal
        self.components_graph.plot(x_trial,y_trial , pen='w')


     #saves the information of each component then displays it in the components combobox and plots the resulted  mixed signal 
    def AddComponent(self):
        #get the component information and add it to the current signal
        self.Current_Signal.frequency.append(self.frequency_spin.value())
        self.Current_Signal.amplitude.append(self.amplitude_spin.value())
        self.Current_Signal.phase.append(self.phase_spin.value())
        self.components_graph.clear()
        #Create a x-axis array
        self.Current_Signal.x_values = np.linspace(0, 10, num=1000)
        #Create an empty y-axis array
        self.Current_Signal.y_values= np.zeros_like(self.Current_Signal.x_values)
        #Calculate the y coordinate of the resulted mixed signal which corresponds to each x coordinate
        for frequency, amplitude, phase in zip(self.Current_Signal.frequency, self.Current_Signal.amplitude, self.Current_Signal.phase):
            y_signal = amplitude * np.sin(2 * np.pi * frequency * self.Current_Signal.x_values + phase * np.pi)
            self.Current_Signal.y_values+= y_signal
        self.components_graph.plot(self.Current_Signal.x_values, self.Current_Signal.y_values, pen='w')
        #Update the components combobox
        self.components_combobox.clear()
        for Component_index in range (len(self.Current_Signal.frequency)):
            self.components_combobox.addItem(f"frequency= {self.Current_Signal.frequency[Component_index]}, Amplitude= {self.Current_Signal.amplitude[Component_index]}, Phase={self.Current_Signal.phase[Component_index]}", userData=Component_index)

    def Remove_selected_component(self):
        #get the index of the selected component from the components combobox
        selected_component_index = self.components_combobox.currentData()
        #remove the component frequency, amplitude and phase from the mixed signal components 
        self.Current_Signal.frequency.pop(selected_component_index)
        self.Current_Signal.amplitude.pop(selected_component_index)
        self.Current_Signal.phase.pop(selected_component_index)
        #redraw the mixed signal 
        #Clear the graph
        self.components_graph.clear()
        #Create a x-axis array
        self.Current_Signal.x_values = np.linspace(0, 10, num=1000)
        #Create an empty y-axis array
        self.Current_Signal.y_values= np.zeros_like(self.Current_Signal.x_values)
        #Calculate the y coordinate of the resulted mixed signal which corresponds to each x coordinate
        for frequency, amplitude, phase in zip(self.Current_Signal.frequency, self.Current_Signal.amplitude, self.Current_Signal.phase):
            y_signal = amplitude * np.sin(2 * np.pi * frequency * self.Current_Signal.x_values + phase * np.pi)
            self.Current_Signal.y_values+= y_signal
        #if the removed component was the only component empty the x and y lists 
        if (len(self.Current_Signal.frequency)== 0):
            self.Current_Signal.x_values=[]
            self.Current_Signal.y_values=[]
        self.components_graph.plot(self.Current_Signal.x_values, self.Current_Signal.y_values, pen='w')
        #update the combobox
        self.components_combobox.clear()
        for Component_index in range (len(self.Current_Signal.frequency)):
            self.components_combobox.addItem(f"frequency= {self.Current_Signal.frequency[Component_index]}, Amplitude= {self.Current_Signal.amplitude[Component_index]}, Phase={self.Current_Signal.phase[Component_index]}", userData=Component_index)

    def Save_composed_signal(self):
        #if the current signal is not already appended in the mixed signals list, append it
        if self.Current_signal_index== len(self.Mixed_signals):
            self.Mixed_signals.append(self.Current_Signal)
        #set the current signal value to a new empty composed_signal object
        self.Current_Signal= Composed_signal()
        #Update the index value 
        self.Current_signal_index= len(self.Mixed_signals)
        #clear the graph and the components combobox
        self.components_combobox.clear()
        self.components_graph.clear()
         #update the combobox
        self.signals_combobox.clear()
        self.composed_signals_combobox.clear()
        for Signal_index in range (len(self.Mixed_signals)):
            self.signals_combobox.addItem(f"Signal {Signal_index}", userData=Signal_index)
            self.composed_signals_combobox.addItem(f"Signal {Signal_index}", userData=Signal_index)

        #set the default value of the combobox to none 
        self.signals_combobox.setCurrentIndex(-1)
        self.composed_signals_combobox.setCurrentIndex(-1)

    def Edit_selected_signal(self):
        #clear the graph
        self.components_graph.clear()
        #get the index of the selected signal from the signals combobox
        selected_signal_index = self.signals_combobox.currentData()
        self.Current_signal_index= selected_signal_index
        self.Current_Signal= self.Mixed_signals[selected_signal_index]
        #plot the selected signal
        self.components_graph.plot(self.Current_Signal.x_values, self.Current_Signal.y_values, pen='w')
        #update the components combobox
        self.components_combobox.clear()
        for Component_index in range (len(self.Current_Signal.frequency)):
            self.components_combobox.addItem(f"frequency= {self.Current_Signal.frequency[Component_index]}, Amplitude= {self.Current_Signal.amplitude[Component_index]}, Phase={self.Current_Signal.phase[Component_index]}", userData=Component_index)

    def select_composed_signal(self):
        # Get the selected signal from the combobox
        selected_signal = self.composed_signals_combobox.currentData()
        self.Current_Composed_Signal= self.Mixed_signals[selected_signal]
        self.x_values, self.y_values = self.Current_Composed_Signal.x_values, self.Current_Composed_Signal.y_values
        if (self.snr_slider.value()==100):
            self.y_values_noisy=self.y_values
        else:
            self.add_noise(self.snr_slider.value()/100)
        self.fmax= int(max(self.Current_Composed_Signal.frequency,key=lambda x: x))
        self.fs_slider.setMinimum(0)  # Set the minimum value to 0
        self.fs_slider.setMaximum(40 * self.fmax)
        self.sampling()
        


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.browse_button.setText(_translate("MainWindow", "Browse"))
        self.composed_signals_groupbox.setTitle(_translate("MainWindow", "Composed Signals"))
        self.fs_groupbox.setTitle(_translate("MainWindow", "Sampling Frequency"))
        self.label_fs_value.setText(_translate("MainWindow", "10"))
        self.label.setText(_translate("MainWindow", "Hz"))
        self.label_fs_value.setText(_translate("MainWindow", "0"))
        self.label_2.setText(_translate("MainWindow", "fmax"))
        self.snr_groupbox.setTitle(_translate("MainWindow", "SNR"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.sampler_tap), _translate("MainWindow", "Sampler"))
        self.components_groupbox.setTitle(_translate("MainWindow", "Components"))
        self.save_signal_button.setText(_translate("MainWindow", "Save Signal"))
        self.remove_button.setText(_translate("MainWindow", "Remove"))
        self.frequency.setText(_translate("MainWindow", "Frequency"))
        self.hz_2.setText(_translate("MainWindow", "Hz"))
        self.amplitude.setText(_translate("MainWindow", "Amplitude"))
        self.phase.setText(_translate("MainWindow", "Phase"))
        self.pi.setText(_translate("MainWindow", "π"))
        self.add_button.setText(_translate("MainWindow", "Add"))
        self.signals_groupbox.setTitle(_translate("MainWindow", "Signals"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.composer_tap), _translate("MainWindow", "Composer"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
