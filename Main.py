from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import pyqtSlot
import sys
import ConfigParser
import os, fnmatch
from time import sleep

from windows import system
from windows import sequence
from task import AutoRun
from task import Run


class MainWindow(QtGui.QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        # variables
        self.parameters_files = []
        self.name_process = ['', '', '']
        self.name_channels = ['', '', '', '']
        self.selectSequence = ''
        self.name_file = ''
        self.wait_time = 0
        self.validation = True

        self.buildMainWindow()

    def buildMainWindow(self):
        self.setWindowIcon(QtGui.QIcon("laser.png"))
        self.setWindowTitle("Control")
        self.setFixedHeight(500)
        self.setFixedWidth(1000)
        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create("Plastique"))

        exit = QtGui.QAction("Exit", self)
        exit.setShortcut("Ctrl+Q")
        exit.setStatusTip('Leave The App')
        exit.triggered.connect(self.close_application)

        new = QtGui.QAction("New", self)
        new.setShortcut("Ctrl+N")
        new.setStatusTip("New window")
        new.triggered.connect(self.new_windows)

        save_as = QtGui.QAction("Save As", self)
        save_as.setShortcut("Ctrl+S")
        save_as.setStatusTip('Save File')
        save_as.triggered.connect(self.file_save)

        open_sequence = QtGui.QAction("Open Sequence", self)
        open_sequence.setShortcut("Ctrl+O")
        open_sequence.setStatusTip("opens a window with the sequences")
        open_sequence.triggered.connect(self.select_sequence)

        plain = QtGui.QAction("Plain", self)
        plain.setStatusTip("clean the table")
        plain.triggered.connect(self.plain)

        self.statusBar()

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&Sequence')
        fileMenu.addAction(new)
        fileMenu.addAction(plain)
        fileMenu.addAction(open_sequence)
        fileMenu.addAction(exit)

        open_system = QtGui.QAction("System Window", self)
        open_system.setShortcut("Ctrl+w")
        open_system.triggered.connect(self.open_system_window)

        view = mainMenu.addMenu("&View")
        view.addAction(open_system)

        # Buttons
        self.btn_addProcess = QtGui.QPushButton('Add Process', self)
        self.btn_addProcess.setFixedWidth(150)

        self.btn_addChannel = QtGui.QPushButton('Add Channel', self)
        self.btn_addChannel.setFixedWidth(150)

        self.btn_Save = QtGui.QPushButton("Save", self)
        self.btn_Save.setFixedWidth(100)

        self.btn_removeProcess = QtGui.QPushButton("Remove Process")
        self.btn_removeProcess.setFixedWidth(150)

        self.btn_removeChannel = QtGui.QPushButton("Remove Channel")
        self.btn_removeChannel.setFixedWidth(150)

        self.btn_run = QtGui.QPushButton("Run")
        self.btn_run.setFixedWidth(100)
        self.btn_run.setFixedHeight(100)

        self.btn_autorun = QtGui.QPushButton("Auto Run")
        self.btn_autorun.setFixedWidth(100)
        self.btn_autorun.setFixedHeight(100)
        self.btn_autorun.setCheckable(True)
        self.btn_autorun.setChecked(True)
        self.btn_autorun.setDown(False)
        self.btn_autorun.toggle()
        self.btn_autorun.setAutoRepeat(True)
        # self.btn_autorun.setAutoRepeatInterval(3000)

        # Action Buttons
        self.btn_addProcess.clicked.connect(self.addProcess)
        self.btn_addChannel.clicked.connect(self.addChanell)
        self.btn_Save.clicked.connect(self.writeParameters)
        self.btn_removeProcess.clicked.connect(self.removeProcess)
        self.btn_removeChannel.clicked.connect(self.removeChannel)
        self.btn_run.clicked.connect(self.run_sequence)
        self.btn_autorun.toggled.connect(self.status_button_pressed)
        self.btn_autorun.toggled.connect(self.started_auto_run)

        # LineEdit
        self.text_save = QtGui.QLineEdit()
        self.text_save.setFixedWidth(150)

        self.text_timestep = QtGui.QLineEdit()
        self.text_timestep.setText('10')
        self.text_timestep.setFixedWidth(50)

        # label
        self.label_save = QtGui.QLabel('File name')
        self.label_timestep = QtGui.QLabel('Timestep(us)')
        self.label_name_sequence = QtGui.QLabel("")

        # Table
        self.table = QtGui.QTableWidget(self)
        self.table_item = QtGui.QTableWidgetItem()
        self.table_item.setFlags(QtCore.Qt.ItemIsEditable)
        self.table.resize(100, 100)

        self.table.setRowCount(2)
        self.table.setVerticalHeaderLabels(['', ''])

        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(['', '', '', ''])

        self.table.setItem(0, 0, QtGui.QTableWidgetItem('Processes'))
        self.table.setItem(0, 1, QtGui.QTableWidgetItem('Duration(ms)'))
        self.table.setItem(0, 3, QtGui.QTableWidgetItem('Channel AO 0'))
        self.table.setItem(1, 0, QtGui.QTableWidgetItem('Process 1'))

        for i in range(2):
            self.table_item = QtGui.QTableWidgetItem()
            self.table_item.setFlags(QtCore.Qt.ItemIsEditable)
            self.table.setItem(i, 2, self.table_item)
            self.table.item(i, 2).setBackground(QtGui.QColor(0, 0, 0))

        # Table Process action
        self.table.cellClicked.connect(self.removeProcess)
        self.table.cellClicked.connect(self.removeChannel)
        self.table.cellClicked.connect(self.change_color_background)

        # LCD Number
        self.shotnumber = QtGui.QLCDNumber()
        self.shotnumber.setNumDigits(5)
        self.shotnumber.display(0)
        self.shotnumber.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.shot_number()

        # change colors of LCD
        palette = self.shotnumber.palette()
        # foreground color
        palette.setColor(palette.WindowText, QtGui.QColor(0, 0, 0))
        # background color
        palette.setColor(palette.Background, QtGui.QColor(0, 0, 0))
        # "light" border
        palette.setColor(palette.Light, QtGui.QColor(0, 0, 0))
        # "dark" border
        palette.setColor(palette.Dark, QtGui.QColor(0, 0, 0))
        # set the palette
        self.shotnumber.setPalette(palette)

        # List of files
        self.layout()
        self.initialization()
        self.verifying_that_the_system_ini_exists()
        self.window


    def layout(self):
        wid = QtGui.QWidget(self)
        self.setCentralWidget(wid)
        self.grid_layout = QtGui.QGridLayout()
        self.grid_layout.setSpacing(10)

        # Tables
        self.grid_layout.addWidget(self.table, 2, 0, 4, 4)

        # Buttons
        self.grid_layout.addWidget(self.btn_addProcess, 7, 0, 1, 1)
        self.grid_layout.addWidget(self.btn_addChannel, 7, 1, 1, 1)
        self.grid_layout.addWidget(self.btn_Save, 9, 2, 1, 1)

        self.grid_layout.addWidget(self.btn_removeProcess, 8, 0, 1, 1)
        self.grid_layout.addWidget(self.btn_removeChannel, 8, 1, 1, 1)
        self.grid_layout.addWidget(self.btn_run, 2, 4, 1, 1)
        self.grid_layout.addWidget(self.btn_autorun, 4, 4, 1, 1)

        # LineEdit
        self.grid_layout.addWidget(self.text_save, 9, 1, 1, 1)
        self.grid_layout.addWidget(self.text_timestep, 1, 0)

        # label
        self.grid_layout.addWidget(self.label_save, 9, 0, 1, 1)
        self.label_save.setAlignment(QtCore.Qt.AlignRight)
        self.grid_layout.addWidget(self.label_timestep, 0, 0)
        self.grid_layout.addWidget(self.label_name_sequence, 1, 1)

        # LCD_Number
        self.grid_layout.addWidget(self.shotnumber, 0, 4)

        wid.setLayout(self.grid_layout)

    # def addProcess(self):
    # self.name_process.append('')
    # i = self.table.rowCount()
    # self.table.insertRow(i)
    # self.table.setVerticalHeaderLabels(self.name_process)
    # self.table.setItem(i, 0, QtGui.QTableWidgetItem('Process %s' % (i)))

    def addChanell(self):
        self.name_channels.append('')
        j = self.table.columnCount()
        self.table.insertColumn(j)
        self.table.setHorizontalHeaderLabels(self.name_channels)
        self.table.setItem(0, j, QtGui.QTableWidgetItem('Channel AO %s' % (j - 3)))

    def addProcess(self):
        self.name_process.append('')
        i = self.table.rowCount()
        self.table.insertRow(i)
        self.table.setVerticalHeaderLabels(self.name_process)
        self.table.setItem(i, 0, QtGui.QTableWidgetItem('Process %s' % (i)))
        self.table_item = QtGui.QTableWidgetItem()
        self.table_item.setFlags(QtCore.Qt.ItemIsEditable)
        self.table.setItem(i, 2, self.table_item)
        self.table.item(i, 2).setBackground(QtGui.QColor(0, 0, 0))

    def removeProcess(self, i, j=None):
        try:
            if j != None:
                self.row = i
            elif j == None:
                if self.table.rowCount() > 2:
                    choice = QtGui.QMessageBox.question(self, 'Delete!',
                                                        "Are you sure you want to delete the Process?",
                                                        QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
                    if choice == QtGui.QMessageBox.Yes:
                        self.table.removeRow(self.row)
                        self.name_process.remove(self.name_process[self.row])
                    else:
                        pass
                else:
                    pass
        except AttributeError:
            pass

    def removeChannel(self, i, j=None):
        try:
            if j != None:
                self.column = j
            elif j == None:
                if self.table.columnCount() > 4:
                    choice = QtGui.QMessageBox.question(self, 'Delete!',
                                                        "Are you sure you want to delete the channel?",
                                                        QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
                    if choice == QtGui.QMessageBox.Yes:
                        self.table.removeColumn(self.column)
                        self.name_channels.remove(self.name_channels[self.column])


                    else:
                        pass
                else:
                    pass
        except AttributeError:
            pass

    def close_application(self):
        sys.exit()

    def writeParameters(self):
        if 'data' not in os.listdir('.'):
            os.mkdir('data')
            os.mkdir('data/Parameters')
        elif 'Parameters' not in os.listdir('data/'):
            os.mkdir('data/Parameters')
        else:
            pass
        try:
            if self.text_timestep.text() != '':
                if self.text_save.text() != '':
                    if '{0}.ini'.format(self.text_save.text()) not in os.listdir('data/Parameters'):
                        config = ConfigParser.ConfigParser()
                        i = self.table.rowCount()
                        j = self.table.columnCount()
                        config.add_section("table size")
                        config.set("table size", "NChannel", "{0}".format(j - 3))
                        config.set("table size", "NProcess", "{0}".format(i - 1))
                        config.set('table size', 'TimeStep(us)', '{0}'.format(self.text_timestep.text()))

                        config.add_section("channels")
                        for n in range(j - 3):
                            config.set('channels', 'Channel AO {0}'.format(n),
                                       '{0}'.format(self.table.item(0, 3 + n).text()))

                        for m in range(i - 1):
                            config.add_section('Process {0}'.format(m + 1))
                            config.set('Process {0}'.format(m + 1), 'name',
                                       '{0}'.format(self.table.item(m + 1, 0).text()))
                            config.set('Process {0}'.format(m + 1), 'Duration(ms)',
                                       '{0}'.format(self.table.item(m + 1, 1).text()))
                            for p in range(j - 3):
                                config.set('Process {0}'.format(m + 1), 'Channel AO {0} value'.format(p),
                                           '{0}'.format(float(self.table.item(m + 1, p + 3).text())))
                        with open('data/Parameters/{0}.ini'.format(self.text_save.text()), 'w') as configfile:

                            config.write(configfile)



                    # self.list_parameters()

                    else:
                        choice = QtGui.QMessageBox.question(self, 'warning',
                                                            "Are you sure you want to open another file? "
                                                            "Data that has not been saved will be lost?",
                                                            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
                        if choice == QtGui.QMessageBox.Yes:
                            config = ConfigParser.ConfigParser()
                            i = self.table.rowCount()
                            j = self.table.columnCount()
                            config.add_section("table size")
                            config.set("table size", "NChannel", "{0}".format(j - 3))
                            config.set("table size", "NProcess", "{0}".format(i - 1))
                            config.set('table size', 'TimeStep(us)', '{0}'.format(float(self.text_timestep.text())))

                            config.add_section("channels")
                            for n in range(j - 3):
                                config.set('channels', 'Channel AO {0}'.format(n),
                                           '{0}'.format(self.table.item(0, 3 + n).text()))

                            for m in range(i - 1):
                                config.add_section('Process {0}'.format(m + 1))
                                config.set('Process {0}'.format(m + 1), 'name',
                                           '{0}'.format(self.table.item(m + 1, 0).text()))
                                config.set('Process {0}'.format(m + 1), 'Duration(ms)',
                                           '{0}'.format(self.table.item(m + 1, 1).text()))
                                for p in range(j - 3):
                                    config.set('Process {0}'.format(m + 1), 'Channel AO {0} value'.format(p),
                                               '{0}'.format(float(self.table.item(m + 1, p + 3).text())))
                            with open('data/Parameters/{0}.ini'.format(self.text_save.text()), 'w') as configfile:

                                config.write(configfile)
                    self.write_settings(self.text_save.text())

                else:
                    choice = QtGui.QMessageBox.question(self, 'warning!',
                                                        "Unnamed sequence, put a name!",
                                                        QtGui.QMessageBox.Ok)

            else:
                choice = QtGui.QMessageBox.question(self, 'warning!',
                                                    "empty timestep!",
                                                    QtGui.QMessageBox.Ok)

        except ValueError:
            choice = QtGui.QMessageBox.question(self, 'warning!',
                                                "you used characters or there are empty cells:"
                                                " Only use numbers in cells.\n"
                                                "Note: Never use \" , \" in numbers only \" . \" , make"
                                                " sure Timestep has only numbers",
                                                QtGui.QMessageBox.Ok)

        self.setWindowTitle("Control - {0}".format(self.text_save.text()))
        self.name_sequence_save()

    def select_sequence(self):
        self.child_window = sequence.SelectSequence(self)
        self.child_window.buildMainWindow()
        self.child_window.show()

    def open_system_window(self):
        self.child_window_system = system.MainWindow(self)
        self.child_window_system.initialize()
        self.child_window_system.show()

    def run_sequence(self):
        self.child_run_sequence = Run.Run(self)
        self.btn_run.setDisabled(True)
        self.btn_autorun.setDisabled(True)
        self.child_run_sequence.start()
        self.child_run_sequence.wait_time()
        sleep(1)
        if self.validation == True:

            # self.child_run_sequence.wait_time()
            self.child_run_sequence.write_number()
            self.shot_number()

        else:
            self.irregular_channels()
            self.validation = True

    def status_button_pressed(self, status):
        print(status)
        self.status_button = status

    def started_auto_run(self, status):
        if status == True:
            self.child_run_sequence = AutoRun.AutoRun(self)
            self.child_run_sequence.start()
            self.child_run_sequence.wait_time()
            sleep(1)
            if self.validation == True:

                self.child_run_sequence.write_number()
                self.shot_number()

            else:
                self.irregular_channels()
                self.validation = True
                self.btn_autorun.setChecked(False)


        else:
            pass

    def new_windows(self):
        choice = QtGui.QMessageBox.question(self, 'warning!',
                                            "Are you sure you want to open a new window? "
                                            "unsaved data will be lost",
                                            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:
            self.table.setRowCount(2)
            self.table.setColumnCount(4)
            self.table.setItem(0, 0, QtGui.QTableWidgetItem('Process'))
            self.table.setItem(0, 1, QtGui.QTableWidgetItem('Duration(ms)'))
            self.table.setItem(0, 3, QtGui.QTableWidgetItem('Channel AO 0'))
            self.table.setItem(1, 0, QtGui.QTableWidgetItem('Process 1'))
            self.table.setItem(1, 1, QtGui.QTableWidgetItem(''))
            self.table.setItem(1, 3, QtGui.QTableWidgetItem(''))

            for i in range(2):
                self.table_item = QtGui.QTableWidgetItem()
                self.table_item.setFlags(QtCore.Qt.ItemIsEditable)
                self.table.setItem(i, 2, self.table_item)
                self.table.item(i, 2).setBackground(QtGui.QColor(0, 0, 0))
        else:
            pass

    def file_save(self):
        name = QtGui.QFileDialog.getSaveFileName(self, 'Save File', 'Parameters', 'file(*.ini)')
        # print (name)
        # file = open(name, 'w')
        if name:
            config = ConfigParser.ConfigParser()
            i = self.table.rowCount()
            j = self.table.columnCount()
            config.add_section("table size")
            config.set("table size", "NChannel", "{0}".format(j - 3))
            config.set("table size", "NProcess", "{0}".format(i - 1))
            config.add_section("channels")
            for n in range(len(self.name_channels) - 2):
                config.set('channels', 'Channel {0}'.format(n + 1), '{0}'.format(self.table.item(0, 3 + n).text()))

            for m in range(len(self.name_process) - 2):
                config.add_section('Process {0}'.format(m + 1))
                config.set('Process {0}'.format(m + 1), 'name', '{0}'.format(self.table.item(m + 1, 0).text()))
                for p in range(len(self.name_channels) - 2):
                    print(float(self.table.item(m + 1, p + 3).text()))
                    config.set('Process {0}'.format(m + 1), 'Channel {0} value'.format(p + 1),
                               '{0}'.format(float(self.table.item(m + 1, p + 3).text())))
            with open('Parameters/{0}.ini'.format(self.text_save.text()), 'w') as configfile:

                config.write(configfile)
            with open('%s' % name, 'w') as configfile:

                config.write(configfile)

            self.list_parameters()
        else:
            pass

    def name_sequence_save(self):
        self.name_file = str(self.text_save.text()) + '.ini'
        n = len(self.name_file) - 4
        self.write_settings(self.name_file[0:len(self.name_file) - 4])

    def name_sequence(self):
        n = len(self.name_file) - 4
        self.text_save.setText(self.name_file[0:n])
        self.setWindowTitle("Control - {0}".format(self.name_file[0:n]))
        self.write_settings(self.name_file[0:len(self.name_file) - 4])

    def change_color_background(self, row, column):
        # print ('teste {0}'.format(self.table.item(1, 1).text()))
        for i in range(2):
            try:
                self.table_item = QtGui.QTableWidgetItem()
                self.table.item(int(row), i).setBackground(QtGui.QColor(153, 204, 255))
                if row == 0:
                    for l in range(1, self.table.rowCount() + 1):
                        try:
                            self.table.item(l, i).setBackground(QtGui.QColor(255, 255, 255))
                        except AttributeError:
                            self.table_item = QtGui.QTableWidgetItem()
                            self.table_item.setBackground(QtGui.QColor(255, 255, 255))
                            self.table.setItem(l, i, self.table_item)

                else:
                    for l in range(row):
                        try:
                            self.table.item(l, i).setBackground(QtGui.QColor(255, 255, 255))

                        except AttributeError:
                            self.table_item = QtGui.QTableWidgetItem()
                            self.table_item.setBackground(QtGui.QColor(255, 255, 255))
                            self.table.setItem(l, i, self.table_item)
                    for l in range(1 + row, self.table.rowCount()):
                        try:
                            self.table.item(l, i).setBackground(QtGui.QColor(255, 255, 255))
                        except AttributeError:
                            self.table_item = QtGui.QTableWidgetItem()
                            self.table_item.setBackground(QtGui.QColor(255, 255, 255))
                            self.table.setItem(l, i, self.table_item)

            except AttributeError:
                self.table_item = QtGui.QTableWidgetItem()
                self.table_item.setBackground(QtGui.QColor(153, 204, 255))
                self.table.setItem(int(row), i, self.table_item)

        for j in range(3, self.table.columnCount()):
            try:
                self.table_item = QtGui.QTableWidgetItem()
                self.table.item(int(row), j).setBackground(QtGui.QColor(153, 204, 255))
                if row == 0:
                    for l in range(1, self.table.rowCount() + 1):
                        try:
                            self.table.item(l, j).setBackground(QtGui.QColor(255, 255, 255))
                        except AttributeError:
                            self.table_item = QtGui.QTableWidgetItem()
                            self.table_item.setBackground(QtGui.QColor(255, 255, 255))
                            self.table.setItem(l, j, self.table_item)

                else:
                    for l in range(row):
                        try:
                            self.table.item(l, j).setBackground(QtGui.QColor(255, 255, 255))

                        except AttributeError:
                            self.table_item = QtGui.QTableWidgetItem()
                            self.table_item.setBackground(QtGui.QColor(255, 255, 255))
                            self.table.setItem(l, j, self.table_item)
                    for l in range(1 + row, self.table.rowCount()):
                        try:
                            self.table.item(l, j).setBackground(QtGui.QColor(255, 255, 255))
                        except AttributeError:
                            self.table_item = QtGui.QTableWidgetItem()
                            self.table_item.setBackground(QtGui.QColor(255, 255, 255))
                            self.table.setItem(l, j, self.table_item)

            except AttributeError:
                self.table_item = QtGui.QTableWidgetItem()
                self.table_item.setBackground(QtGui.QColor(153, 204, 255))
                self.table.setItem(int(row), j, self.table_item)

    def write_settings(self, name):
        config = ConfigParser.ConfigParser()
        config.add_section("initialization")
        config.set("initialization", "Last Sequence", "{0}".format(name))
        with open('settings.ini', 'w') as configfile:
            config.write(configfile)

    def initialization(self):
        if 'settings.ini' in os.listdir('.'):
            config = ConfigParser.ConfigParser()
            config.read('settings.ini')
            name = config.get("initialization", 'Last Sequence')
            self.text_save.setText(name)
            self.name_file = name + ".ini"
            self.setWindowTitle('Control - {0}'.format(name))

            config = ConfigParser.ConfigParser()
            config.read('data/Parameters/%s.ini' % name)
            section = config.sections()

            try:
                # build table
                j = int(config.get('%s' % (section[0]), 'nchannel'))
                i = int(config.get('%s' % (section[0]), 'nprocess'))
                self.table.setRowCount(i + 1)
                self.table.setColumnCount(j + 3)
                self.table.setItem(0, 0, QtGui.QTableWidgetItem('Process'))
                self.table.setItem(0, 1, QtGui.QTableWidgetItem('Duration(ms)'))
                self.text_timestep.setText(config.get('table size', 'timestep(us)'))
                for i in range(i + 1):
                    self.table_item = QtGui.QTableWidgetItem()
                    self.table_item.setFlags(QtCore.Qt.ItemIsEditable)
                    self.table.setItem(i, 2, self.table_item)
                    self.table.item(i, 2).setBackground(QtGui.QColor(0, 0, 0))
                for n in range(j + 3):
                    self.name_channels.append('')
                self.table.setHorizontalHeaderLabels(self.name_channels)

                for m in range(i + 1):
                    self.name_process.append('')
                self.table.setVerticalHeaderLabels(self.name_process)

                # get channels
                for p in range(1, i + 1):
                    # get Durations
                    self.table.setItem(p, 1,
                                       QtGui.QTableWidgetItem(config.get('Process {0}'.format(p), 'duration(ms)')))
                    for q in range(3, j + 3):
                        # get channels
                        self.table.setItem(p, q, QtGui.QTableWidgetItem(config.get('Process %i' % (p),
                                                                                   'channel AO %i value' % (q - 3))))

                        # name of channels and process
                        self.table.setItem(p, 0, QtGui.QTableWidgetItem(config.get('Process {0}'.format(p), 'name')))
                        self.table.setItem(0, q, QtGui.QTableWidgetItem(
                            config.get('channels', 'channel AO {0}'.format(q - 3))))
            except IndexError:
                pass
        else:
            pass

    def plain(self):
        choice = QtGui.QMessageBox.question(self, 'warning!',
                                            "Are you sure you want to open a new window? "
                                            "unsaved data will be lost",
                                            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:
            self.table.setItem(0, 0, QtGui.QTableWidgetItem('Process'))
            self.table.setItem(0, 1, QtGui.QTableWidgetItem('Duration(ms)'))
            self.table.setItem(0, 3, QtGui.QTableWidgetItem('Channel AO 0'))
            self.table.setItem(1, 0, QtGui.QTableWidgetItem('Process 1'))
            self.table.setItem(1, 1, QtGui.QTableWidgetItem(''))
            self.table.setItem(1, 3, QtGui.QTableWidgetItem(''))

            for i in range(1, self.table.rowCount()):
                self.table.setItem(i, 1, QtGui.QTableWidgetItem(''))
                for j in range(3, self.table.columnCount()):
                    self.table.setItem(i, j, QtGui.QTableWidgetItem(''))







        else:
            pass

    def shot_number(self):
        self.child_run_sequence = Run.Run(self)
        number = int(self.child_run_sequence.read_number())
        self.shotnumber.display(number)

    def irregular_channels(self):
        choice = QtGui.QMessageBox.question(self, 'warning!',
                                            "One of the channels was not defined in the system:"
                                            " View >> system window (Ctrl + W)",
                                            QtGui.QMessageBox.Ok)

    def verifying_that_the_system_ini_exists(self):
        if 'data' not in os.listdir('.'):
            os.mkdir('data')

            arq = open('data/system.txt', 'a')
            write = []

            for i in range(32):
                write.append('AO6723/ao{0}\tChannel AO {0}\tAnalog\tyes\t5\n'.format(i))
            arq.writelines(write)
            arq.close()

        elif 'system.txt' not in os.listdir('data/'):
            arq = open('data/system.txt', 'a')
            write = []

            for i in range(32):
                write.append('AO6723/ao{0}\tChannel AO {0}\tAnalog\tyes\t5\n'.format(i))
            arq.writelines(write)
            arq.close()
        else:
            pass


def main():
    app_1 = QtGui.QApplication(sys.argv)
    win_1 = MainWindow()
    win_1.show()
    sys.exit(app_1.exec_())


if __name__ == '__main__':
    main()
