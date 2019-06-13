from PyQt4 import QtGui, QtCore
import sys
import ConfigParser
import os





class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.parent = parent
        self.setWindowIcon(QtGui.QIcon("laser.png"))
        self.setWindowTitle("Select Sequence")
        self.setFixedWidth(1000)
        self.setWindowModified(False)
        self.move(0, 0)

        self.system = []


    def initialize(self):
        if 'system.txt' in os.listdir("data/"):
            self.read()

        else:
            arq = open('data/system.txt', 'a')
            write = []

            for i in range(32):
                write.append('AO6723/ao{0}\tChannel AO {0}\tAnalog\tyes\t5\n'.format(i))
            arq.writelines(write)
            arq.close()

            self.read()


        self.control = self.parent
        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create("cleanlooks"))

        wid = QtGui.QWidget(self)
        self.setCentralWidget(wid)
        self.grid_layout = QtGui.QGridLayout()
        self.grid_layout.setSpacing(10)

        # Buttons
        self.Button_Update = QtGui.QPushButton('Update System File')
        self.Button_Update.setFixedWidth(150)
        self.Button_Update.setFixedHeight(100)
        self.Button_Update.clicked.connect(self.write)

        self.Button_Default = QtGui.QPushButton("Default Names")
        self.Button_Default.setFixedWidth(150)
        self.Button_Default.setFixedHeight(100)
        self.Button_Default.clicked.connect(self.default)


        #labels
        self.Physical_Name = QtGui.QLabel()
        self.Physical_Name.setText('Physical Name')

        self.Name = QtGui.QLabel()
        self.Name.setText('Name')

        self.Conversion = QtGui.QLabel()
        self.Conversion.setText("Conversion/Logics")

        self.Function = QtGui.QLabel()
        self.Function.setText("Function")

        self.AO6723_ao0 = QtGui.QLabel()
        self.AO6723_ao0.setText('AO6723/ao0')

        self.AO6723_ao1 = QtGui.QLabel()
        self.AO6723_ao1.setText('AO6723/ao1')

        self.AO6723_ao2 = QtGui.QLabel()
        self.AO6723_ao2.setText('AO6723/ao2')

        self.AO6723_ao3 = QtGui.QLabel()
        self.AO6723_ao3.setText('AO6723/ao3')

        self.AO6723_ao4 = QtGui.QLabel()
        self.AO6723_ao4.setText('AO6723/ao4')

        self.AO6723_ao5 = QtGui.QLabel()
        self.AO6723_ao5.setText('AO6723/ao5')

        self.AO6723_ao6 = QtGui.QLabel()
        self.AO6723_ao6.setText('AO6723/ao6')

        self.AO6723_ao7 = QtGui.QLabel()
        self.AO6723_ao7.setText('AO6723/ao7')

        self.AO6723_ao8 = QtGui.QLabel()
        self.AO6723_ao8.setText('AO6723/ao8')

        self.AO6723_ao9 = QtGui.QLabel()
        self.AO6723_ao9.setText('AO6723/ao9')

        self.AO6723_ao10 = QtGui.QLabel()
        self.AO6723_ao10.setText('AO6723/ao10')

        self.AO6723_ao11 = QtGui.QLabel()
        self.AO6723_ao11.setText('AO6723/ao11')

        self.AO6723_ao12 = QtGui.QLabel()
        self.AO6723_ao12.setText('AO6723/ao12')

        self.AO6723_ao13 = QtGui.QLabel()
        self.AO6723_ao13.setText('AO6723/ao13')

        self.AO6723_ao14 = QtGui.QLabel()
        self.AO6723_ao14.setText('AO6723/ao14')

        self.AO6723_ao15 = QtGui.QLabel()
        self.AO6723_ao15.setText('AO6723/ao15')

        self.AO6723_ao16 = QtGui.QLabel()
        self.AO6723_ao16.setText('AO6723/ao16')

        self.AO6723_ao17 = QtGui.QLabel()
        self.AO6723_ao17.setText('AO6723/ao17')

        self.AO6723_ao18 = QtGui.QLabel()
        self.AO6723_ao18.setText('AO6723/ao18')

        self.AO6723_ao19 = QtGui.QLabel()
        self.AO6723_ao19.setText('AO6723/ao19')

        self.AO6723_ao20 = QtGui.QLabel()
        self.AO6723_ao20.setText('AO6723/ao20')

        self.AO6723_ao21 = QtGui.QLabel()
        self.AO6723_ao21.setText('AO6723/ao21')

        self.AO6723_ao22 = QtGui.QLabel()
        self.AO6723_ao22.setText('AO6723/ao22')

        self.AO6723_ao23 = QtGui.QLabel()
        self.AO6723_ao23.setText('AO6723/ao23')

        self.AO6723_ao24 = QtGui.QLabel()
        self.AO6723_ao24.setText('AO6723/ao24')

        self.AO6723_ao25 = QtGui.QLabel()
        self.AO6723_ao25.setText('AO6723/ao25')

        self.AO6723_ao26 = QtGui.QLabel()
        self.AO6723_ao26.setText('AO6723/ao26')

        self.AO6723_ao27 = QtGui.QLabel()
        self.AO6723_ao27.setText('AO6723/ao27')

        self.AO6723_ao28 = QtGui.QLabel()
        self.AO6723_ao28.setText('AO6723/ao28')

        self.AO6723_ao29 = QtGui.QLabel()
        self.AO6723_ao29.setText('AO6723/ao29')

        self.AO6723_ao30 = QtGui.QLabel()
        self.AO6723_ao30.setText('AO6723/ao30')

        self.AO6723_ao31 = QtGui.QLabel()
        self.AO6723_ao31.setText('AO6723/ao31')

        #Line Edit Name

        self.LineEdit_AO6723_ao0 = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao0.setFixedWidth(150)
        self.LineEdit_AO6723_ao0.setText(self.system[0][1])


        self.LineEdit_AO6723_ao1 = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao1.setFixedWidth(150)
        self.LineEdit_AO6723_ao1.setText(self.system[1][1])

        self.LineEdit_AO6723_ao2 = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao2.setFixedWidth(150)
        self.LineEdit_AO6723_ao2.setText(self.system[2][1])

        self.LineEdit_AO6723_ao3 = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao3.setFixedWidth(150)
        self.LineEdit_AO6723_ao3.setText(self.system[3][1])

        self.LineEdit_AO6723_ao4 = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao4.setFixedWidth(150)
        self.LineEdit_AO6723_ao4.setText(self.system[4][1])

        self.LineEdit_AO6723_ao5 = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao5.setFixedWidth(150)
        self.LineEdit_AO6723_ao5.setText(self.system[5][1])

        self.LineEdit_AO6723_ao6 = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao6.setFixedWidth(150)
        self.LineEdit_AO6723_ao6.setText(self.system[6][1])

        self.LineEdit_AO6723_ao7 = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao7.setFixedWidth(150)
        self.LineEdit_AO6723_ao7.setText(self.system[7][1])

        self.LineEdit_AO6723_ao8 = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao8.setFixedWidth(150)
        self.LineEdit_AO6723_ao8.setText(self.system[8][1])

        self.LineEdit_AO6723_ao9 = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao9.setFixedWidth(150)
        self.LineEdit_AO6723_ao9.setText(self.system[9][1])

        self.LineEdit_AO6723_ao10 = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao10.setFixedWidth(150)
        self.LineEdit_AO6723_ao10.setText(self.system[10][1])

        self.LineEdit_AO6723_ao11 = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao11.setFixedWidth(150)
        self.LineEdit_AO6723_ao11.setText(self.system[11][1])

        self.LineEdit_AO6723_ao12 = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao12.setFixedWidth(150)
        self.LineEdit_AO6723_ao12.setText(self.system[12][1])

        self.LineEdit_AO6723_ao13 = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao13.setFixedWidth(150)
        self.LineEdit_AO6723_ao13.setText(self.system[13][1])

        self.LineEdit_AO6723_ao14 = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao14.setFixedWidth(150)
        self.LineEdit_AO6723_ao14.setText(self.system[14][1])

        self.LineEdit_AO6723_ao15 = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao15.setFixedWidth(150)
        self.LineEdit_AO6723_ao15.setText(self.system[15][1])

        self.LineEdit_AO6723_ao16 = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao16.setFixedWidth(150)
        self.LineEdit_AO6723_ao16.setText(self.system[16][1])

        self.LineEdit_AO6723_ao17 = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao17.setFixedWidth(150)
        self.LineEdit_AO6723_ao17.setText(self.system[17][1])

        self.LineEdit_AO6723_ao18 = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao18.setFixedWidth(150)
        self.LineEdit_AO6723_ao18.setText(self.system[18][1])

        self.LineEdit_AO6723_ao19 = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao19.setFixedWidth(150)
        self.LineEdit_AO6723_ao19.setText(self.system[19][1])

        self.LineEdit_AO6723_ao20 = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao20.setFixedWidth(150)
        self.LineEdit_AO6723_ao20.setText(self.system[20][1])

        self.LineEdit_AO6723_ao21 = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao21.setFixedWidth(150)
        self.LineEdit_AO6723_ao21.setText(self.system[21][1])

        self.LineEdit_AO6723_ao22 = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao22.setFixedWidth(150)
        self.LineEdit_AO6723_ao22.setText(self.system[22][1])

        self.LineEdit_AO6723_ao23 = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao23.setFixedWidth(150)
        self.LineEdit_AO6723_ao23.setText(self.system[23][1])

        self.LineEdit_AO6723_ao24 = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao24.setFixedWidth(150)
        self.LineEdit_AO6723_ao24.setText(self.system[24][1])

        self.LineEdit_AO6723_ao25 = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao25.setFixedWidth(150)
        self.LineEdit_AO6723_ao25.setText(self.system[25][1])

        self.LineEdit_AO6723_ao26 = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao26.setFixedWidth(150)
        self.LineEdit_AO6723_ao26.setText(self.system[26][1])

        self.LineEdit_AO6723_ao27 = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao27.setFixedWidth(150)
        self.LineEdit_AO6723_ao27.setText(self.system[27][1])

        self.LineEdit_AO6723_ao28 = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao28.setFixedWidth(150)
        self.LineEdit_AO6723_ao28.setText(self.system[28][1])

        self.LineEdit_AO6723_ao29 = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao29.setFixedWidth(150)
        self.LineEdit_AO6723_ao29.setText(self.system[29][1])

        self.LineEdit_AO6723_ao30 = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao30.setFixedWidth(150)
        self.LineEdit_AO6723_ao30.setText(self.system[30][1])

        self.LineEdit_AO6723_ao31 = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao31.setFixedWidth(150)
        self.LineEdit_AO6723_ao31.setText(self.system[31][1])


        #Line Edit Function

        self.LineEdit_AO6723_ao0_Function = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao0_Function.setFixedWidth(150)
        self.LineEdit_AO6723_ao0_Function.setText(self.system[0][2])

        self.LineEdit_AO6723_ao1_Function = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao1_Function.setFixedWidth(150)
        self.LineEdit_AO6723_ao1_Function.setText(self.system[1][2])

        self.LineEdit_AO6723_ao2_Function = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao2_Function.setFixedWidth(150)
        self.LineEdit_AO6723_ao2_Function.setText(self.system[2][2])

        self.LineEdit_AO6723_ao3_Function = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao3_Function.setFixedWidth(150)
        self.LineEdit_AO6723_ao3_Function.setText(self.system[3][2])

        self.LineEdit_AO6723_ao4_Function = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao4_Function.setFixedWidth(150)
        self.LineEdit_AO6723_ao4_Function.setText(self.system[4][2])

        self.LineEdit_AO6723_ao5_Function = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao5_Function.setFixedWidth(150)
        self.LineEdit_AO6723_ao5_Function.setText(self.system[5][2])

        self.LineEdit_AO6723_ao6_Function = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao6_Function.setFixedWidth(150)
        self.LineEdit_AO6723_ao6_Function.setText(self.system[6][2])

        self.LineEdit_AO6723_ao7_Function = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao7_Function.setFixedWidth(150)
        self.LineEdit_AO6723_ao7_Function.setText(self.system[7][2])

        self.LineEdit_AO6723_ao8_Function = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao8_Function.setFixedWidth(150)
        self.LineEdit_AO6723_ao8_Function.setText(self.system[8][2])

        self.LineEdit_AO6723_ao9_Function = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao9_Function.setFixedWidth(150)
        self.LineEdit_AO6723_ao9_Function.setText(self.system[9][2])

        self.LineEdit_AO6723_ao10_Function = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao10_Function.setFixedWidth(150)
        self.LineEdit_AO6723_ao10_Function.setText(self.system[10][2])

        self.LineEdit_AO6723_ao11_Function = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao11_Function.setFixedWidth(150)
        self.LineEdit_AO6723_ao11_Function.setText(self.system[11][2])

        self.LineEdit_AO6723_ao12_Function = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao12_Function.setFixedWidth(150)
        self.LineEdit_AO6723_ao12_Function.setText(self.system[12][2])

        self.LineEdit_AO6723_ao13_Function = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao13_Function.setFixedWidth(150)
        self.LineEdit_AO6723_ao13_Function.setText(self.system[13][2])

        self.LineEdit_AO6723_ao14_Function = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao14_Function.setFixedWidth(150)
        self.LineEdit_AO6723_ao14_Function.setText(self.system[14][2])

        self.LineEdit_AO6723_ao15_Function = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao15_Function.setFixedWidth(150)
        self.LineEdit_AO6723_ao15_Function.setText(self.system[15][2])

        self.LineEdit_AO6723_ao16_Function = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao16_Function.setFixedWidth(150)
        self.LineEdit_AO6723_ao16_Function.setText(self.system[16][2])

        self.LineEdit_AO6723_ao17_Function = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao17_Function.setFixedWidth(150)
        self.LineEdit_AO6723_ao17_Function.setText(self.system[17][2])

        self.LineEdit_AO6723_ao18_Function = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao18_Function.setFixedWidth(150)
        self.LineEdit_AO6723_ao18_Function.setText(self.system[18][2])

        self.LineEdit_AO6723_ao19_Function = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao19_Function.setFixedWidth(150)
        self.LineEdit_AO6723_ao19_Function.setText(self.system[19][2])

        self.LineEdit_AO6723_ao20_Function = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao20_Function.setFixedWidth(150)
        self.LineEdit_AO6723_ao20_Function.setText(self.system[20][2])

        self.LineEdit_AO6723_ao21_Function = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao21_Function.setFixedWidth(150)
        self.LineEdit_AO6723_ao21_Function.setText(self.system[21][2])

        self.LineEdit_AO6723_ao22_Function = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao22_Function.setFixedWidth(150)
        self.LineEdit_AO6723_ao22_Function.setText(self.system[22][2])

        self.LineEdit_AO6723_ao23_Function = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao23_Function.setFixedWidth(150)
        self.LineEdit_AO6723_ao23_Function.setText(self.system[23][2])

        self.LineEdit_AO6723_ao24_Function = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao24_Function.setFixedWidth(150)
        self.LineEdit_AO6723_ao24_Function.setText(self.system[24][2])

        self.LineEdit_AO6723_ao25_Function = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao25_Function.setFixedWidth(150)
        self.LineEdit_AO6723_ao25_Function.setText(self.system[25][2])

        self.LineEdit_AO6723_ao26_Function = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao26_Function.setFixedWidth(150)
        self.LineEdit_AO6723_ao26_Function.setText(self.system[26][2])

        self.LineEdit_AO6723_ao27_Function = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao27_Function.setFixedWidth(150)
        self.LineEdit_AO6723_ao27_Function.setText(self.system[27][2])

        self.LineEdit_AO6723_ao28_Function = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao28_Function.setFixedWidth(150)
        self.LineEdit_AO6723_ao28_Function.setText(self.system[28][2])

        self.LineEdit_AO6723_ao29_Function = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao29_Function.setFixedWidth(150)
        self.LineEdit_AO6723_ao29_Function.setText(self.system[29][2])

        self.LineEdit_AO6723_ao30_Function = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao30_Function.setFixedWidth(150)
        self.LineEdit_AO6723_ao30_Function.setText(self.system[30][2])

        self.LineEdit_AO6723_ao31_Function = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao31_Function.setFixedWidth(150)
        self.LineEdit_AO6723_ao31_Function.setText(self.system[31][2])

        #Line Edit Conversion

        self.LineEdit_AO6723_ao0_Conversion = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao0_Conversion .setFixedWidth(150)
        self.LineEdit_AO6723_ao0_Conversion.setText(self.system[0][3])

        self.LineEdit_AO6723_ao1_Conversion  = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao1_Conversion .setFixedWidth(150)
        self.LineEdit_AO6723_ao1_Conversion.setText(self.system[1][3])

        self.LineEdit_AO6723_ao2_Conversion  = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao2_Conversion .setFixedWidth(150)
        self.LineEdit_AO6723_ao2_Conversion.setText(self.system[2][3])

        self.LineEdit_AO6723_ao3_Conversion  = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao3_Conversion .setFixedWidth(150)
        self.LineEdit_AO6723_ao3_Conversion.setText(self.system[3][3])

        self.LineEdit_AO6723_ao4_Conversion  = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao4_Conversion .setFixedWidth(150)
        self.LineEdit_AO6723_ao4_Conversion.setText(self.system[4][3])

        self.LineEdit_AO6723_ao5_Conversion  = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao5_Conversion .setFixedWidth(150)
        self.LineEdit_AO6723_ao5_Conversion.setText(self.system[5][3])

        self.LineEdit_AO6723_ao6_Conversion  = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao6_Conversion .setFixedWidth(150)
        self.LineEdit_AO6723_ao6_Conversion.setText(self.system[6][3])

        self.LineEdit_AO6723_ao7_Conversion  = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao7_Conversion .setFixedWidth(150)
        self.LineEdit_AO6723_ao7_Conversion.setText(self.system[7][3])

        self.LineEdit_AO6723_ao8_Conversion  = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao8_Conversion .setFixedWidth(150)
        self.LineEdit_AO6723_ao8_Conversion.setText(self.system[8][3])

        self.LineEdit_AO6723_ao9_Conversion  = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao9_Conversion .setFixedWidth(150)
        self.LineEdit_AO6723_ao9_Conversion.setText(self.system[9][3])

        self.LineEdit_AO6723_ao10_Conversion  = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao10_Conversion .setFixedWidth(150)
        self.LineEdit_AO6723_ao10_Conversion.setText(self.system[10][3])

        self.LineEdit_AO6723_ao11_Conversion  = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao11_Conversion .setFixedWidth(150)
        self.LineEdit_AO6723_ao11_Conversion.setText(self.system[11][3])

        self.LineEdit_AO6723_ao12_Conversion  = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao12_Conversion .setFixedWidth(150)
        self.LineEdit_AO6723_ao12_Conversion.setText(self.system[12][3])

        self.LineEdit_AO6723_ao13_Conversion  = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao13_Conversion .setFixedWidth(150)
        self.LineEdit_AO6723_ao13_Conversion.setText(self.system[13][3])

        self.LineEdit_AO6723_ao14_Conversion  = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao14_Conversion .setFixedWidth(150)
        self.LineEdit_AO6723_ao14_Conversion.setText(self.system[14][3])

        self.LineEdit_AO6723_ao15_Conversion  = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao15_Conversion .setFixedWidth(150)
        self.LineEdit_AO6723_ao15_Conversion.setText(self.system[15][3])

        self.LineEdit_AO6723_ao16_Conversion  = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao16_Conversion .setFixedWidth(150)
        self.LineEdit_AO6723_ao16_Conversion.setText(self.system[16][3])

        self.LineEdit_AO6723_ao17_Conversion  = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao17_Conversion .setFixedWidth(150)
        self.LineEdit_AO6723_ao17_Conversion.setText(self.system[17][3])

        self.LineEdit_AO6723_ao18_Conversion  = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao18_Conversion .setFixedWidth(150)
        self.LineEdit_AO6723_ao18_Conversion.setText(self.system[18][3])

        self.LineEdit_AO6723_ao19_Conversion  = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao19_Conversion .setFixedWidth(150)
        self.LineEdit_AO6723_ao19_Conversion.setText(self.system[19][3])

        self.LineEdit_AO6723_ao20_Conversion  = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao20_Conversion .setFixedWidth(150)
        self.LineEdit_AO6723_ao20_Conversion.setText(self.system[20][3])

        self.LineEdit_AO6723_ao21_Conversion  = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao21_Conversion .setFixedWidth(150)
        self.LineEdit_AO6723_ao21_Conversion.setText(self.system[21][3])

        self.LineEdit_AO6723_ao22_Conversion  = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao22_Conversion .setFixedWidth(150)
        self.LineEdit_AO6723_ao22_Conversion.setText(self.system[22][3])

        self.LineEdit_AO6723_ao23_Conversion  = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao23_Conversion .setFixedWidth(150)
        self.LineEdit_AO6723_ao23_Conversion.setText(self.system[23][3])

        self.LineEdit_AO6723_ao24_Conversion  = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao24_Conversion .setFixedWidth(150)
        self.LineEdit_AO6723_ao24_Conversion.setText(self.system[24][3])

        self.LineEdit_AO6723_ao25_Conversion  = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao25_Conversion .setFixedWidth(150)
        self.LineEdit_AO6723_ao25_Conversion.setText(self.system[25][3])

        self.LineEdit_AO6723_ao26_Conversion  = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao26_Conversion .setFixedWidth(150)
        self.LineEdit_AO6723_ao26_Conversion.setText(self.system[26][3])

        self.LineEdit_AO6723_ao27_Conversion  = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao27_Conversion .setFixedWidth(150)
        self.LineEdit_AO6723_ao27_Conversion.setText(self.system[27][3])

        self.LineEdit_AO6723_ao28_Conversion  = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao28_Conversion .setFixedWidth(150)
        self.LineEdit_AO6723_ao28_Conversion.setText(self.system[28][3])

        self.LineEdit_AO6723_ao29_Conversion  = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao29_Conversion .setFixedWidth(150)
        self.LineEdit_AO6723_ao29_Conversion.setText(self.system[29][3])

        self.LineEdit_AO6723_ao30_Conversion  = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao30_Conversion .setFixedWidth(150)
        self.LineEdit_AO6723_ao30_Conversion.setText(self.system[30][3])

        self.LineEdit_AO6723_ao31_Conversion  = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao31_Conversion .setFixedWidth(150)
        self.LineEdit_AO6723_ao31_Conversion.setText(self.system[31][3])

        # Line Edit Default

        self.LineEdit_AO6723_ao0_Default = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao0_Default.setFixedWidth(150)
        self.LineEdit_AO6723_ao0_Default.setText(self.system[0][4])

        self.LineEdit_AO6723_ao1_Default = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao1_Default.setFixedWidth(150)
        self.LineEdit_AO6723_ao1_Default.setText(self.system[1][4])

        self.LineEdit_AO6723_ao2_Default = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao2_Default.setFixedWidth(150)
        self.LineEdit_AO6723_ao2_Default.setText(self.system[2][4])

        self.LineEdit_AO6723_ao3_Default = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao3_Default.setFixedWidth(150)
        self.LineEdit_AO6723_ao3_Default.setText(self.system[3][4])

        self.LineEdit_AO6723_ao4_Default = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao4_Default.setFixedWidth(150)
        self.LineEdit_AO6723_ao4_Default.setText(self.system[4][4])

        self.LineEdit_AO6723_ao5_Default = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao5_Default.setFixedWidth(150)
        self.LineEdit_AO6723_ao5_Default.setText(self.system[5][4])

        self.LineEdit_AO6723_ao6_Default = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao6_Default.setFixedWidth(150)
        self.LineEdit_AO6723_ao6_Default.setText(self.system[6][4])

        self.LineEdit_AO6723_ao7_Default = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao7_Default.setFixedWidth(150)
        self.LineEdit_AO6723_ao7_Default.setText(self.system[7][4])

        self.LineEdit_AO6723_ao8_Default = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao8_Default.setFixedWidth(150)
        self.LineEdit_AO6723_ao8_Default.setText(self.system[8][4])

        self.LineEdit_AO6723_ao9_Default = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao9_Default.setFixedWidth(150)
        self.LineEdit_AO6723_ao9_Default.setText(self.system[9][4])

        self.LineEdit_AO6723_ao10_Default = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao10_Default.setFixedWidth(150)
        self.LineEdit_AO6723_ao10_Default.setText(self.system[10][4])

        self.LineEdit_AO6723_ao11_Default = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao11_Default.setFixedWidth(150)
        self.LineEdit_AO6723_ao11_Default.setText(self.system[11][4])

        self.LineEdit_AO6723_ao12_Default = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao12_Default.setFixedWidth(150)
        self.LineEdit_AO6723_ao12_Default.setText(self.system[12][4])

        self.LineEdit_AO6723_ao13_Default = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao13_Default.setFixedWidth(150)
        self.LineEdit_AO6723_ao13_Default.setText(self.system[13][4])

        self.LineEdit_AO6723_ao14_Default = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao14_Default.setFixedWidth(150)
        self.LineEdit_AO6723_ao14_Default.setText(self.system[14][4])

        self.LineEdit_AO6723_ao15_Default = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao15_Default.setFixedWidth(150)
        self.LineEdit_AO6723_ao15_Default.setText(self.system[15][4])

        self.LineEdit_AO6723_ao16_Default = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao16_Default.setFixedWidth(150)
        self.LineEdit_AO6723_ao16_Default.setText(self.system[16][4])

        self.LineEdit_AO6723_ao17_Default = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao17_Default.setFixedWidth(150)
        self.LineEdit_AO6723_ao17_Default.setText(self.system[17][4])

        self.LineEdit_AO6723_ao18_Default = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao18_Default.setFixedWidth(150)
        self.LineEdit_AO6723_ao18_Default.setText(self.system[18][4])

        self.LineEdit_AO6723_ao19_Default = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao19_Default.setFixedWidth(150)
        self.LineEdit_AO6723_ao19_Default.setText(self.system[19][4])

        self.LineEdit_AO6723_ao20_Default = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao20_Default.setFixedWidth(150)
        self.LineEdit_AO6723_ao20_Default.setText(self.system[20][4])

        self.LineEdit_AO6723_ao21_Default = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao21_Default.setFixedWidth(150)
        self.LineEdit_AO6723_ao21_Default.setText(self.system[21][4])

        self.LineEdit_AO6723_ao22_Default = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao22_Default.setFixedWidth(150)
        self.LineEdit_AO6723_ao22_Default.setText(self.system[22][4])

        self.LineEdit_AO6723_ao23_Default = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao23_Default.setFixedWidth(150)
        self.LineEdit_AO6723_ao23_Default.setText(self.system[23][4])

        self.LineEdit_AO6723_ao24_Default = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao24_Default.setFixedWidth(150)
        self.LineEdit_AO6723_ao24_Default.setText(self.system[24][4])

        self.LineEdit_AO6723_ao25_Default = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao25_Default.setFixedWidth(150)
        self.LineEdit_AO6723_ao25_Default.setText(self.system[25][4])

        self.LineEdit_AO6723_ao26_Default = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao26_Default.setFixedWidth(150)
        self.LineEdit_AO6723_ao26_Default.setText(self.system[26][4])

        self.LineEdit_AO6723_ao27_Default = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao27_Default.setFixedWidth(150)
        self.LineEdit_AO6723_ao27_Default.setText(self.system[27][4])

        self.LineEdit_AO6723_ao28_Default = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao28_Default.setFixedWidth(150)
        self.LineEdit_AO6723_ao28_Default.setText(self.system[28][4])

        self.LineEdit_AO6723_ao29_Default = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao29_Default.setFixedWidth(150)
        self.LineEdit_AO6723_ao29_Default.setText(self.system[29][4])

        self.LineEdit_AO6723_ao30_Default = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao30_Default.setFixedWidth(150)
        self.LineEdit_AO6723_ao30_Default.setText(self.system[30][4])

        self.LineEdit_AO6723_ao31_Default = QtGui.QLineEdit()
        self.LineEdit_AO6723_ao31_Default.setFixedWidth(150)
        self.LineEdit_AO6723_ao31_Default.setText(self.system[31][4])



        self.layout()




    def layout(self):
        wid = QtGui.QWidget(self)
        self.setCentralWidget(wid)
        self.grid_layout = QtGui.QGridLayout()
        self.grid_layout.setSpacing(3)

        #buttons
        self.grid_layout.addWidget(self.Button_Update, 2, 5, 4, 5)
        self.grid_layout.addWidget(self.Button_Default, 3, 5, 9, 5)

        #labels
        self.grid_layout.addWidget(self.Physical_Name, 0, 0)
        self.grid_layout.addWidget(self.Name, 0, 1)
        self.grid_layout.addWidget(self.Function, 0, 2)
        self.grid_layout.addWidget(self.Conversion, 0, 3)
        self.grid_layout.addWidget(self.AO6723_ao0, 1, 0)
        self.grid_layout.addWidget(self.AO6723_ao1, 2, 0)
        self.grid_layout.addWidget(self.AO6723_ao2, 3, 0)
        self.grid_layout.addWidget(self.AO6723_ao3, 4, 0)
        self.grid_layout.addWidget(self.AO6723_ao4, 5, 0)
        self.grid_layout.addWidget(self.AO6723_ao5, 6, 0)
        self.grid_layout.addWidget(self.AO6723_ao6, 7, 0)
        self.grid_layout.addWidget(self.AO6723_ao7, 8, 0)
        self.grid_layout.addWidget(self.AO6723_ao8, 9, 0)
        self.grid_layout.addWidget(self.AO6723_ao9, 10, 0)
        self.grid_layout.addWidget(self.AO6723_ao10, 11, 0)
        self.grid_layout.addWidget(self.AO6723_ao11, 12, 0)
        self.grid_layout.addWidget(self.AO6723_ao12, 13, 0)
        self.grid_layout.addWidget(self.AO6723_ao13, 14, 0)
        self.grid_layout.addWidget(self.AO6723_ao14, 15, 0)
        self.grid_layout.addWidget(self.AO6723_ao15, 16, 0)
        self.grid_layout.addWidget(self.AO6723_ao16, 17, 0)
        self.grid_layout.addWidget(self.AO6723_ao17, 18, 0)
        self.grid_layout.addWidget(self.AO6723_ao18, 19, 0)
        self.grid_layout.addWidget(self.AO6723_ao19, 20, 0)
        self.grid_layout.addWidget(self.AO6723_ao20, 21, 0)
        self.grid_layout.addWidget(self.AO6723_ao21, 22, 0)
        self.grid_layout.addWidget(self.AO6723_ao22, 23, 0)
        self.grid_layout.addWidget(self.AO6723_ao23, 24, 0)
        self.grid_layout.addWidget(self.AO6723_ao24, 25, 0)
        self.grid_layout.addWidget(self.AO6723_ao25, 26, 0)
        self.grid_layout.addWidget(self.AO6723_ao26, 27, 0)
        self.grid_layout.addWidget(self.AO6723_ao27, 28, 0)
        self.grid_layout.addWidget(self.AO6723_ao28, 29, 0)
        self.grid_layout.addWidget(self.AO6723_ao29, 30, 0)
        self.grid_layout.addWidget(self.AO6723_ao30, 31, 0)
        self.grid_layout.addWidget(self.AO6723_ao31, 32, 0)

        #Line Edit Name
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao0, 1, 1)
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao1, 2, 1)
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao2, 3, 1)
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao3, 4, 1)
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao4, 5, 1)
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao5, 6, 1)
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao6, 7, 1)
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao7, 8, 1)
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao8, 9, 1)
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao9, 10, 1)
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao10, 11, 1)
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao11, 12, 1)
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao12, 13, 1)
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao13, 14, 1)
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao14, 15, 1)
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao15, 16, 1)
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao16, 17, 1)
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao17, 18, 1)
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao18, 19, 1)
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao19, 20, 1)
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao20, 21, 1)
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao21, 22, 1)
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao22, 23, 1)
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao23, 24, 1)
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao24, 25, 1)
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao25, 26, 1)
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao26, 27, 1)
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao27, 28, 1)
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao28, 29, 1)
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao29, 30, 1)
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao30, 31, 1)
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao31, 32, 1)


        #Line Edit Function
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao0_Function, 1, 2)
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao1_Function, 2, 2)
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao2_Function, 3, 2)
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao3_Function, 4, 2)
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao4_Function, 5, 2)
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao5_Function, 6, 2)
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao6_Function, 7, 2)
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao7_Function, 8, 2)
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao8_Function, 9, 2)
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao9_Function, 10, 2)
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao10_Function, 11, 2)
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao11_Function, 12, 2)
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao12_Function, 13, 2)
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao13_Function, 14, 2)
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao14_Function, 15, 2)
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao15_Function, 16, 2)
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao16_Function, 17, 2)
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao17_Function, 18, 2)
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao18_Function, 19, 2)
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao19_Function, 20, 2)
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao20_Function, 21, 2)
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao21_Function, 22, 2)
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao22_Function, 23, 2)
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao23_Function, 24, 2)
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao24_Function, 25, 2)
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao25_Function, 26, 2)
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao26_Function, 27, 2)
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao27_Function, 28, 2)
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao28_Function, 29, 2)
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao29_Function, 30, 2)
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao30_Function, 31, 2)
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao31_Function, 32, 2)

        # Line Edit Conversion
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao0_Conversion, 1, 3)
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao1_Conversion, 2, 3)
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao2_Conversion, 3, 3)
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao3_Conversion, 4, 3)
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao4_Conversion, 5, 3)
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao5_Conversion, 6, 3)
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao6_Conversion, 7, 3)
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao7_Conversion, 8, 3)
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao8_Conversion, 9, 3)
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao9_Conversion, 10, 3)
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao10_Conversion, 11, 3)
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao11_Conversion, 12, 3)
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao12_Conversion, 13, 3)
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao13_Conversion, 14, 3)
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao14_Conversion, 15, 3)
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao15_Conversion, 16, 3)
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao16_Conversion, 17, 3)
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao17_Conversion, 18, 3)
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao18_Conversion, 19, 3)
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao19_Conversion, 20, 3)
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao20_Conversion, 21, 3)
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao21_Conversion, 22, 3)
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao22_Conversion, 23, 3)
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao23_Conversion, 24, 3)
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao24_Conversion, 25, 3)
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao25_Conversion, 26, 3)
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao26_Conversion, 27, 3)
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao27_Conversion, 28, 3)
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao28_Conversion, 29, 3)
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao29_Conversion, 30, 3)
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao30_Conversion, 31, 3)
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao31_Conversion, 32, 3)

        # Line Edit Default
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao0_Default, 1, 4)
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao1_Default, 2, 4)
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao2_Default, 3, 4)
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao3_Default, 4, 4)
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao4_Default, 5, 4)
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao5_Default, 6, 4)
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao6_Default, 7, 4)
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao7_Default, 8, 4)
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao8_Default, 9, 4)
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao9_Default, 10, 4)
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao10_Default, 11, 4)
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao11_Default, 12, 4)
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao12_Default, 13, 4)
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao13_Default, 14, 4)
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao14_Default, 15, 4)
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao15_Default, 16, 4)
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao16_Default, 17, 4)
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao17_Default, 18, 4)
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao18_Default, 19, 4)
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao19_Default, 20, 4)
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao20_Default, 21, 4)
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao21_Default, 22, 4)
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao22_Default, 23, 4)
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao23_Default, 24, 4)
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao24_Default, 25, 4)
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao25_Default, 26, 4)
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao26_Default, 27, 4)
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao27_Default, 28, 4)
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao28_Default, 29, 4)
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao29_Default, 30, 4)
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao30_Default, 31, 4)
        self.grid_layout.addWidget(self.LineEdit_AO6723_ao31_Default, 32, 4)





        wid.setLayout(self.grid_layout)

        if 'system.txt' in os.listdir("data/"):
            pass
        else:
            self.write()


    def read(self):
        arq = open('data/system.txt', 'r')
        texto = arq.readlines()
        for linha in texto:
            self.system.append(linha.split('\t'))
            if len(self.system[-1]) > 5:
                self.system[-1].remove('')
                self.system[-1].remove('')
                self.system[-1].remove('')
                print(self.system[0])
            else:
                pass
        for linha in texto:
            self.system.append(linha.replace('\n', ''))

        arq.close()



    def write(self):
        arq = open('data/system.txt', 'w')
        write =[]

        write.append('{0}\t{1}\t{2}\t{3}\t{4}\n' .format(self.AO6723_ao0.text(),
                                                         self.LineEdit_AO6723_ao0.text(),
                                                         self.LineEdit_AO6723_ao0_Function.text(),
                                                         self.LineEdit_AO6723_ao0_Conversion.text(),
                                                         self.LineEdit_AO6723_ao0_Default.text()))

        write.append('{0}\t{1}\t{2}\t{3}\t{4}\n'.format(self.AO6723_ao1.text(),
                                                        self.LineEdit_AO6723_ao1.text(),
                                                        self.LineEdit_AO6723_ao1_Function.text(),
                                                        self.LineEdit_AO6723_ao1_Conversion.text(),
                                                        self.LineEdit_AO6723_ao1_Default.text()))

        write.append('{0}\t{1}\t{2}\t{3}\t{4}\n'.format(self.AO6723_ao2.text(),
                                                        self.LineEdit_AO6723_ao2.text(),
                                                        self.LineEdit_AO6723_ao2_Function.text(),
                                                        self.LineEdit_AO6723_ao2_Conversion.text(),
                                                        self.LineEdit_AO6723_ao2_Default.text()))

        write.append('{0}\t{1}\t{2}\t{3}\t{4}\n'.format(self.AO6723_ao3.text(),
                                                        self.LineEdit_AO6723_ao3.text(),
                                                        self.LineEdit_AO6723_ao3_Function.text(),
                                                        self.LineEdit_AO6723_ao3_Conversion.text(),
                                                        self.LineEdit_AO6723_ao3_Default.text()))

        write.append('{0}\t{1}\t{2}\t{3}\t{4}\n'.format(self.AO6723_ao4.text(),
                                                        self.LineEdit_AO6723_ao4.text(),
                                                        self.LineEdit_AO6723_ao4_Function.text(),
                                                        self.LineEdit_AO6723_ao4_Conversion.text(),
                                                        self.LineEdit_AO6723_ao4_Default.text()))

        write.append('{0}\t{1}\t{2}\t{3}\t{4}\n'.format(self.AO6723_ao5.text(),
                                                        self.LineEdit_AO6723_ao5.text(),
                                                        self.LineEdit_AO6723_ao5_Function.text(),
                                                        self.LineEdit_AO6723_ao5_Conversion.text(),
                                                        self.LineEdit_AO6723_ao5_Default.text()))

        write.append('{0}\t{1}\t{2}\t{3}\t{4}\n'.format(self.AO6723_ao6.text(),
                                                      self.LineEdit_AO6723_ao6.text(),
                                                      self.LineEdit_AO6723_ao6_Function.text(),
                                                      self.LineEdit_AO6723_ao6_Conversion.text(),
                                                      self.LineEdit_AO6723_ao6_Default.text()))

        write.append('{0}\t{1}\t{2}\t{3}\t{4}\n'.format(self.AO6723_ao7.text(),
                                                      self.LineEdit_AO6723_ao7.text(),
                                                      self.LineEdit_AO6723_ao7_Function.text(),
                                                      self.LineEdit_AO6723_ao7_Conversion.text(),
                                                      self.LineEdit_AO6723_ao7_Default.text()))

        write.append('{0}\t{1}\t{2}\t{3}\t{4}\n'.format(self.AO6723_ao8.text(),
                                                      self.LineEdit_AO6723_ao8.text(),
                                                      self.LineEdit_AO6723_ao8_Function.text(),
                                                      self.LineEdit_AO6723_ao8_Conversion.text(),
                                                      self.LineEdit_AO6723_ao8_Default.text()))

        write.append('{0}\t{1}\t{2}\t{3}\t{4}\n'.format(self.AO6723_ao9.text(),
                                                      self.LineEdit_AO6723_ao9.text(),
                                                      self.LineEdit_AO6723_ao9_Function.text(),
                                                      self.LineEdit_AO6723_ao9_Conversion.text(),
                                                      self.LineEdit_AO6723_ao9_Default.text()))

        write.append('{0}\t{1}\t{2}\t{3}\t{4}\n'.format(self.AO6723_ao10.text(),
                                                      self.LineEdit_AO6723_ao10.text(),
                                                      self.LineEdit_AO6723_ao10_Function.text(),
                                                      self.LineEdit_AO6723_ao10_Conversion.text(),
                                                      self.LineEdit_AO6723_ao10_Default.text()))

        write.append('{0}\t{1}\t{2}\t{3}\t{4}\n'.format(self.AO6723_ao11.text(),
                                                      self.LineEdit_AO6723_ao11.text(),
                                                      self.LineEdit_AO6723_ao11_Function.text(),
                                                      self.LineEdit_AO6723_ao11_Conversion.text(),
                                                      self.LineEdit_AO6723_ao11_Default.text()))

        write.append('{0}\t{1}\t{2}\t{3}\t{4}\n'.format(self.AO6723_ao12.text(),
                                                      self.LineEdit_AO6723_ao12.text(),
                                                      self.LineEdit_AO6723_ao12_Function.text(),
                                                      self.LineEdit_AO6723_ao12_Conversion.text(),
                                                      self.LineEdit_AO6723_ao12_Default.text()))

        write.append('{0}\t{1}\t{2}\t{3}\t{4}\n'.format(self.AO6723_ao13.text(),
                                                      self.LineEdit_AO6723_ao13.text(),
                                                      self.LineEdit_AO6723_ao13_Function.text(),
                                                      self.LineEdit_AO6723_ao13_Conversion.text(),
                                                      self.LineEdit_AO6723_ao13_Default.text()))

        write.append('{0}\t{1}\t{2}\t{3}\t{4}\n'.format(self.AO6723_ao14.text(),
                                                      self.LineEdit_AO6723_ao14.text(),
                                                      self.LineEdit_AO6723_ao14_Function.text(),
                                                      self.LineEdit_AO6723_ao14_Conversion.text(),
                                                      self.LineEdit_AO6723_ao14_Default.text()))

        write.append('{0}\t{1}\t{2}\t{3}\t{4}\n'.format(self.AO6723_ao15.text(),
                                                      self.LineEdit_AO6723_ao15.text(),
                                                      self.LineEdit_AO6723_ao15_Function.text(),
                                                      self.LineEdit_AO6723_ao15_Conversion.text(),
                                                      self.LineEdit_AO6723_ao15_Default.text()))

        write.append('{0}\t{1}\t{2}\t{3}\t{4}\n'.format(self.AO6723_ao16.text(),
                                                      self.LineEdit_AO6723_ao16.text(),
                                                      self.LineEdit_AO6723_ao16_Function.text(),
                                                      self.LineEdit_AO6723_ao16_Conversion.text(),
                                                      self.LineEdit_AO6723_ao16_Default.text()))

        write.append('{0}\t{1}\t{2}\t{3}\t{4}\n'.format(self.AO6723_ao17.text(),
                                                      self.LineEdit_AO6723_ao17.text(),
                                                      self.LineEdit_AO6723_ao17_Function.text(),
                                                      self.LineEdit_AO6723_ao17_Conversion.text(),
                                                      self.LineEdit_AO6723_ao17_Default.text()))

        write.append('{0}\t{1}\t{2}\t{3}\t{4}\n'.format(self.AO6723_ao18.text(),
                                                      self.LineEdit_AO6723_ao18.text(),
                                                      self.LineEdit_AO6723_ao18_Function.text(),
                                                      self.LineEdit_AO6723_ao18_Conversion.text(),
                                                      self.LineEdit_AO6723_ao18_Default.text()))

        write.append('{0}\t{1}\t{2}\t{3}\t{4}\n'.format(self.AO6723_ao19.text(),
                                                      self.LineEdit_AO6723_ao19.text(),
                                                      self.LineEdit_AO6723_ao19_Function.text(),
                                                      self.LineEdit_AO6723_ao19_Conversion.text(),
                                                      self.LineEdit_AO6723_ao19_Default.text()))

        write.append('{0}\t{1}\t{2}\t{3}\t{4}\n'.format(self.AO6723_ao20.text(),
                                                      self.LineEdit_AO6723_ao20.text(),
                                                      self.LineEdit_AO6723_ao20_Function.text(),
                                                      self.LineEdit_AO6723_ao20_Conversion.text(),
                                                      self.LineEdit_AO6723_ao20_Default.text()))

        write.append('{0}\t{1}\t{2}\t{3}\t{4}\n'.format(self.AO6723_ao21.text(),
                                                      self.LineEdit_AO6723_ao21.text(),
                                                      self.LineEdit_AO6723_ao21_Function.text(),
                                                      self.LineEdit_AO6723_ao21_Conversion.text(),
                                                      self.LineEdit_AO6723_ao21_Default.text()))

        write.append('{0}\t{1}\t{2}\t{3}\t{4}\n'.format(self.AO6723_ao22.text(),
                                                      self.LineEdit_AO6723_ao22.text(),
                                                      self.LineEdit_AO6723_ao22_Function.text(),
                                                      self.LineEdit_AO6723_ao22_Conversion.text(),
                                                      self.LineEdit_AO6723_ao22_Default.text()))

        write.append('{0}\t{1}\t{2}\t{3}\t{4}\n'.format(self.AO6723_ao23.text(),
                                                      self.LineEdit_AO6723_ao23.text(),
                                                      self.LineEdit_AO6723_ao23_Function.text(),
                                                      self.LineEdit_AO6723_ao23_Conversion.text(),
                                                      self.LineEdit_AO6723_ao23_Default.text()))

        write.append('{0}\t{1}\t{2}\t{3}\t{4}\n'.format(self.AO6723_ao24.text(),
                                                      self.LineEdit_AO6723_ao24.text(),
                                                      self.LineEdit_AO6723_ao24_Function.text(),
                                                      self.LineEdit_AO6723_ao24_Conversion.text(),
                                                      self.LineEdit_AO6723_ao24_Default.text()))

        write.append('{0}\t{1}\t{2}\t{3}\t{4}\n'.format(self.AO6723_ao25.text(),
                                                      self.LineEdit_AO6723_ao25.text(),
                                                      self.LineEdit_AO6723_ao25_Function.text(),
                                                      self.LineEdit_AO6723_ao25_Conversion.text(),
                                                      self.LineEdit_AO6723_ao25_Default.text()))

        write.append('{0}\t{1}\t{2}\t{3}\t{4}\n'.format(self.AO6723_ao26.text(),
                                                      self.LineEdit_AO6723_ao26.text(),
                                                      self.LineEdit_AO6723_ao26_Function.text(),
                                                      self.LineEdit_AO6723_ao26_Conversion.text(),
                                                      self.LineEdit_AO6723_ao26_Default.text()))

        write.append('{0}\t{1}\t{2}\t{3}\t{4}\n'.format(self.AO6723_ao27.text(),
                                                      self.LineEdit_AO6723_ao27.text(),
                                                      self.LineEdit_AO6723_ao27_Function.text(),
                                                      self.LineEdit_AO6723_ao27_Conversion.text(),
                                                      self.LineEdit_AO6723_ao27_Default.text()))

        write.append('{0}\t{1}\t{2}\t{3}\t{4}\n'.format(self.AO6723_ao28.text(),
                                                      self.LineEdit_AO6723_ao28.text(),
                                                      self.LineEdit_AO6723_ao28_Function.text(),
                                                      self.LineEdit_AO6723_ao28_Conversion.text(),
                                                      self.LineEdit_AO6723_ao28_Default.text()))

        write.append('{0}\t{1}\t{2}\t{3}\t{4}\n'.format(self.AO6723_ao29.text(),
                                                      self.LineEdit_AO6723_ao29.text(),
                                                      self.LineEdit_AO6723_ao29_Function.text(),
                                                      self.LineEdit_AO6723_ao29_Conversion.text(),
                                                      self.LineEdit_AO6723_ao29_Default.text()))

        write.append('{0}\t{1}\t{2}\t{3}\t{4}\n'.format(self.AO6723_ao30.text(),
                                                      self.LineEdit_AO6723_ao30.text(),
                                                      self.LineEdit_AO6723_ao30_Function.text(),
                                                      self.LineEdit_AO6723_ao30_Conversion.text(),
                                                      self.LineEdit_AO6723_ao30_Default.text()))

        write.append('{0}\t{1}\t{2}\t{3}\t{4}\n'.format(self.AO6723_ao31.text(),
                                                      self.LineEdit_AO6723_ao31.text(),
                                                      self.LineEdit_AO6723_ao31_Function.text(),
                                                      self.LineEdit_AO6723_ao31_Conversion.text(),
                                                      self.LineEdit_AO6723_ao31_Default.text()))

        text = []
        for linha in write:
            text.append(linha.replace('\n\n', '\n'))
        arq.writelines(text)
        arq.close()



    def default(self):
        self.LineEdit_AO6723_ao0.setText("Channel AO 0")
        self.LineEdit_AO6723_ao1.setText("Channel AO 1")
        self.LineEdit_AO6723_ao2.setText("Channel AO 2")
        self.LineEdit_AO6723_ao3.setText("Channel AO 3")
        self.LineEdit_AO6723_ao4.setText("Channel AO 4")
        self.LineEdit_AO6723_ao5.setText("Channel AO 5")
        self.LineEdit_AO6723_ao6.setText("Channel AO 6")
        self.LineEdit_AO6723_ao7.setText("Channel AO 7")
        self.LineEdit_AO6723_ao8.setText("Channel AO 8")
        self.LineEdit_AO6723_ao9.setText("Channel AO 9")
        self.LineEdit_AO6723_ao10.setText("Channel AO 10")
        self.LineEdit_AO6723_ao11.setText("Channel AO 11")
        self.LineEdit_AO6723_ao12.setText("Channel AO 12")
        self.LineEdit_AO6723_ao13.setText("Channel AO 13")
        self.LineEdit_AO6723_ao14.setText("Channel AO 14")
        self.LineEdit_AO6723_ao15.setText("Channel AO 15")
        self.LineEdit_AO6723_ao16.setText("Channel AO 16")
        self.LineEdit_AO6723_ao17.setText("Channel AO 17")
        self.LineEdit_AO6723_ao18.setText("Channel AO 18")
        self.LineEdit_AO6723_ao19.setText("Channel AO 19")
        self.LineEdit_AO6723_ao20.setText("Channel AO 20")
        self.LineEdit_AO6723_ao21.setText("Channel AO 21")
        self.LineEdit_AO6723_ao22.setText("Channel AO 22")
        self.LineEdit_AO6723_ao23.setText("Channel AO 23")
        self.LineEdit_AO6723_ao24.setText("Channel AO 24")
        self.LineEdit_AO6723_ao25.setText("Channel AO 25")
        self.LineEdit_AO6723_ao26.setText("Channel AO 26")
        self.LineEdit_AO6723_ao27.setText("Channel AO 27")
        self.LineEdit_AO6723_ao28.setText("Channel AO 28")
        self.LineEdit_AO6723_ao29.setText("Channel AO 29")
        self.LineEdit_AO6723_ao30.setText("Channel AO 30")
        self.LineEdit_AO6723_ao31.setText("Channel AO 31")
