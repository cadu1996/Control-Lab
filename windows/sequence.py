from PyQt4 import QtGui, QtCore
import sys
import ConfigParser
import os, fnmatch
#from Control import MainWindow



class SelectSequence(QtGui.QMainWindow):

    def __init__(self, parent):
        super(SelectSequence, self).__init__()
        self.parent = parent
        self.name_sequence = ''


        self.buildMainWindow()

    def buildMainWindow(self):
        self.setWindowIcon(QtGui.QIcon("laser.png"))
        self.setWindowTitle("Select Sequence")

        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create("cleanlooks"))

        wid = QtGui.QWidget(self)
        self.setCentralWidget(wid)
        self.grid_layout = QtGui.QGridLayout()
        self.grid_layout.setSpacing(10)

        # Buttons
        self.btn_delete = QtGui.QPushButton("Delete")
        self.btn_delete.setFixedWidth(100)

        self.btn_Open = QtGui.QPushButton("Open", self)
        self.btn_Open.setFixedWidth(100)

        # Action Buttons
        self.btn_Open.clicked.connect(self.readSequence)
        self.btn_delete.clicked.connect(self.delete_parameters)
        self.btn_Open.clicked.connect(self.change_file)


        # list Box
        self.list = QtGui.QListWidget(self)
        self.list.resize(400, 400)
        self.list_parameters()

        # List Action
        self.list.itemClicked.connect(self.select_name_sequence)

        self.layout()



    def layout(self):
        wid = QtGui.QWidget(self)
        self.setCentralWidget(wid)
        self.grid_layout = QtGui.QGridLayout()
        self.grid_layout.setSpacing(10)

        # Buttons
        self.grid_layout.addWidget(self.btn_Open, 0, 5)
        self.grid_layout.addWidget(self.btn_delete, 0, 6)

        # list
        self.grid_layout.addWidget(self.list, 0, 4)

        wid.setLayout(self.grid_layout)

    # def readSequence(self,name):
    #     if name == False:
    #         read = Control.SelectSequence()
    #         read.readSequence(self.name)
    #
    #     else:
    #         self.name = name.text()


    def select_name_sequence(self, name):
        self.name_sequence = name.text()
        #self.parent.name_sequence = name.text()



    def readSequence(self):
        self.control = self.parent

        choice = QtGui.QMessageBox.question(self, 'warning',
                                            "Are you sure you want to open another file? "
                                            "Data that has not been saved will be lost?",
                                            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)

        self.name_channels = []
        self.name_process = []
        try:

            if choice == QtGui.QMessageBox.Yes:
                config = ConfigParser.ConfigParser()
                config.read('data/Parameters/%s' % (self.name_sequence))
                section = config.sections()

                # build table
                j = int(config.get('%s' % (section[0]), 'nchannel'))
                i = int(config.get('%s' % (section[0]), 'nprocess'))
                self.control.table.setRowCount(i+1)
                self.control.table.setColumnCount(j+3)
                self.control.table.setItem(0, 0, QtGui.QTableWidgetItem('Process'))
                self.control.table.setItem(0, 1, QtGui.QTableWidgetItem('Duration(ms)'))
                self.control.text_timestep.setText(config.get('table size', 'timestep(us)'))
                for i in range(i+1):
                    self.table_item = QtGui.QTableWidgetItem()
                    self.table_item.setFlags(QtCore.Qt.ItemIsEditable)
                    self.control.table.setItem(i, 2, self.table_item)
                    self.control.table.item(i, 2).setBackground(QtGui.QColor(0, 0, 0))
                for n in range(j+3):
                    self.name_channels.append('')
                self.control.table.setHorizontalHeaderLabels(self.name_channels)

                for m in range(i+1):
                    self.name_process.append('')
                self.control.table.setVerticalHeaderLabels(self.name_process)


                # get channels
                for p in range(1, i+1):
                    #get Durations
                    self.control.table.setItem(p, 1, QtGui.QTableWidgetItem(config.get('Process {0}'.format(p), 'duration(ms)')))
                    for q in range(3, j+3):
                        #get channels
                        self.control.table.setItem(p, q, QtGui.QTableWidgetItem(config.get('Process %i' % (p),
                                                                                   'channel AO %i value' % (q-3))))

                        #name of channels and process
                        self.control.table.setItem(p, 0, QtGui.QTableWidgetItem(config.get('Process {0}'.format(p), 'name')))
                        self.control.table.setItem(0, q, QtGui.QTableWidgetItem(config.get('channels', 'channel AO {0}'.format(q-3))))
                self.control.show()
                self.parent.name_file = self.name_sequence
            else:
                pass

        except IndexError:
            pass



    def list_parameters(self):
        self.list.clear()
        if 'Parameters' in os.listdir('data/'):
            pass
        else:
            os.mkdir('data/Parameters')

        self.parameters_files = []
        listOfFiles = os.listdir('data/Parameters')
        pattern = "*.ini"
        for entry in listOfFiles:
            if fnmatch.fnmatch(entry, pattern):
                self.list.addItem('%s' % (entry))
                self.parameters_files.append(entry)

    def delete_parameters(self,response):
        if response != False:
            self.name = response.text()

        else:
            choice = QtGui.QMessageBox.question(self, 'warning!',
                                                "Are you sure you want to delete this file?"
                                                " it will be deleted permanently",
                                                QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
            try:

                if choice == QtGui.QMessageBox.Yes:
                    os.remove('data/Parameters/%s' % self.name_sequence)
                    self.list_parameters()

                else:
                    pass

            except WindowsError:
                pass

    def change_file(self):
        self.parent.name_sequence()

