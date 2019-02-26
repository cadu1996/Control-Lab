import ConfigParser
import numpy as np
import nidaqmx
from nidaqmx import stream_writers
import os
from datetime import datetime
import time
from PyQt4 import QtCore
import os

class AutoRun(QtCore.QThread):
    def __init__(self, parent):
        super(AutoRun, self).__init__()
        self.parent = parent
        self.Value_Shot = 0

    def __del__(self):
        self.wait()


    def date_system(self):
        system = []
        arq = open('data/system.txt', 'r')
        texto = arq.readlines()
        for linha in texto:
            system.append(linha.split('\t'))
        arq.close()
        return system


    def verification(self):
        system = self.date_system()
        config = ConfigParser.ConfigParser()
        config.read('data/Parameters/{0}'.format(self.parent.name_file))
        channels = []
        channels_names = []
        for i in range(len(config.items('channels'))):
            channels.append(config.items('channels')[i][0])
            channels_names.append(config.items('channels')[i][1])


        channels_available=[]
        for i in range(len(config.items('channels'))):
            for j in range(len(system)):
                if (channels_names[i]) == system[j][1]:
                    tupla = '{0}'.format(channels[i]), '{0}'.format(system[j][0])
                    channels_available.append(tupla)
                else:
                    pass
        return channels_available


    def sequence(self):
        config = ConfigParser.ConfigParser()
        config.read('data/Parameters/{0}'.format(self.parent.name_file))
        channels = self.verification()
        channels.sort(key=lambda x: x[1])
        processes = config.sections()[2:]

        timestep = config.getfloat('table size', 'timestep(us)')*10**(-6)

        first_step = (config.getfloat('Process 1', 'duration(ms)')*10**(-3))/ timestep

        array = np.array([])
        array = np.resize(array, (1, int(first_step)))

        samples = np.array([])
        samples = np.resize(samples, (len(channels),1))

        for process in processes:
            duration = config.getfloat(process, 'duration(ms)') * 10 ** (-3)
            step = duration / timestep
            array = np.array([])
            array = np.resize(array, (1, int(step)))

            for channel in channels:
                a = config.getfloat(str(process), '{0} Value'.format(channel[0])) * np.ones(int(step))
                a = np.resize(a, (1, int(step)))
                array = np.concatenate((array, a), axis=0)
            samples = np.resize(samples, (np.shape(array)[0], np.shape(samples)[1]))
            samples = np.concatenate((samples, array), axis=1)
        return samples, channels, 1/timestep

    def conversion_month(self):
        now = datetime.now()

        if int(now.month) == 1:
            month = 'January'

        elif int(now.month) == 2:
            month = 'February'

        elif int(now.month) == 3:
            month = 'March'

        elif int(now.month) == 4:
            month = 'April'

        elif int(now.month) == 5:
            month = 'May'

        elif int(now.month) == 6:
            month = 'June'

        elif int(now.month) == 7:
            month = 'July'

        elif int(now.month) == 8:
            month = 'August'

        elif int(now.month) == 9:
            month = 'September'

        elif int(now.month) == 10:
            month = 'October'

        elif int(now.month) == 11:
            month = 'November'

        elif int(now.month) == 12:
            month = 'December'


        return month




    def directory(self):
        now = datetime.now()
        month = self.conversion_month()

        if 'Log' not in os.listdir('.'):
            os.mkdir('Log')
            os.mkdir('Log/{0}'.format(str(now.year)))
            os.mkdir('Log/{0}/{1}'.format(str(now.year), month))
            os.mkdir('log/{0}/{1}/{2}'.format(str(now.year), month, str(now.day)))

        elif str(now.year) not in os.listdir('Log'):
            os.mkdir('Log/{0}'.format(str(now.year)))
            os.mkdir('Log/{0}/{1}'.format(str(now.year), month))
            os.mkdir('log/{0}/{1}/{2}'.format(str(now.year), month, str(now.day)))

        elif month not in os.listdir('Log/{0}'.format(str(now.year))):
            os.mkdir('Log/{0}/{1}'.format(str(now.year), month))
            os.mkdir('log/{0}/{1}/{2}'.format(str(now.year), month, str(now.day)))

        elif str(now.day) not in os.listdir('Log/{0}/{1}'.format(str(now.year), month)):
            os.mkdir('log/{0}/{1}/{2}'.format(str(now.year), month, str(now.day)))

        else:
            pass

    def write_number(self):
        now = datetime.now()
        month = self.conversion_month()
        config = ConfigParser.ConfigParser()
        if 'ShotNumber.ini' not in os.listdir('Log/{0}/{1}/{2}'.format(str(now.year), month, str(now.day))):
            config.add_section("ShotNumber")
            config.set("ShotNumber", "Number", 1)
            self.Value_Shot = 1

        else:
            t = self.read_number()
            self.Value_Shot = 1 + int(t)
            config.add_section("ShotNumber")
            config.set("ShotNumber", "Number", "{0}".format(self.Value_Shot))

        with open('log/{0}/{1}/{2}/ShotNumber.ini'.format(str(now.year), month, str(now.day)), 'w') as configfile:
            config.write(configfile)

        self.save_log()

    def read_number(self):
        self.directory()
        now = datetime.now()
        month = self.conversion_month()
        config = ConfigParser.ConfigParser()
        if 'ShotNumber.ini' not in os.listdir('Log/{0}/{1}/{2}'.format(str(now.year), month, str(now.day))):
            config.add_section("ShotNumber")
            config.set("ShotNumber", "Number", 0)
            self.Value_Shot = 0

            with open('log/{0}/{1}/{2}/ShotNumber.ini'.format(str(now.year), month, str(now.day)), 'w') as configfile:
                config.write(configfile)

        else:
            config.read('log/{0}/{1}/{2}/ShotNumber.ini'.format(str(now.year), month, str(now.day)))
            self.Value_Shot = config.get('ShotNumber', 'Number')
        return config.get('ShotNumber', 'Number')

    def save_log(self):
        now = datetime.now()
        month = self.conversion_month()
        os.popen('copy data\Parameters\{0}.ini log\{1}\{2}\{3}\{0}-{4}.ini'.format(self.parent.name_file[:-4], str(now.year), month, str(now.day), self.Value_Shot))


    def wait_time(self):
        samples, channel, frequency = self.sequence()
        self.parent.wait_time = int((1.0/frequency)*len(samples[0])+1)


    def run(self):
        self.parent.btn_run.setDisabled(True)

        self.directory()
        samples, channels, frequency = self.sequence()

        samples = np.delete(samples, 0, 0)
        samples = np.delete(samples, 0, axis=1)

        if len(samples) == (self.parent.table.columnCount() - 3):

            while self.parent.status_button == True:

                print samples



                self.parent.wait_time = int((1.0/frequency)*len(samples[0])+1)
                print(samples)
                task = nidaqmx.Task()

                for channel in channels:
                    task.ao_channels.add_ao_voltage_chan('{0}'.format(channel[1]))

                task.timing.cfg_samp_clk_timing(rate=frequency, sample_mode=nidaqmx.constants.AcquisitionType.FINITE,
                                                     samps_per_chan=len(samples[0]))

                write = stream_writers.AnalogMultiChannelWriter(task.out_stream, auto_start=True)
                inicio = time.time()


                write.write_many_sample(samples, timeout=self.parent.wait_time)

                task.wait_until_done(timeout=self.parent.wait_time)
                task.stop()
                task.close()
                self.write_number()
                self.parent.shot_number()
                fim = time.time()
                print("elapsed time {0} seconds".format(fim - inicio))
                #print(len(samples[0]))
                self.parent.btn_run.setDisabled(False)

            self.parent.validation = True
            print ('done')
            self.terminate()

        else:
            self.parent.validation = False
            self.parent.btn_run.setDisabled(False)
            self.parent.btn_autorun.setDisabled(False)
            self.terminate()

