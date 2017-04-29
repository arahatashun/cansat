

import serial
import csv
import pynmea2
import io


class Gps():

    def __init__(self):
        self.latitude = ''
        self.longitude = ''
        self.speed = ''
        self.altitude = ''
        self.course = ''
        try:
            self.ser = serial.Serial("/dev/ttyS0",
                                     baudrate=9600,
                                     bytesize=serial.EIGHTBITS,
                                     parity=serial.PARITY_NONE,
                                     stopbits=serial.STOPBITS_ONE,
                                     timeout=1)
        except serial.SerialException:
            print("could not open port")

    def create_file(self, filename="gps.csv"):
        with open(filename, 'a') as csvfile:
            csvwriter = csv.writer(csvfile, dialect='excel')
            csvwriter.writerow(['latitude',
                                'longitude',
                                'speed',
                                'altitude',
                                'course'])

    def write_data(self, filename="gps.csv"):
        with open(filename, 'a') as csvfile:
            csvwriter = csv.writer(csvfile, dialect='excel')
            csvwriter.writerow(self.return_results())

    def return_results(self):
        return [self.latitude,
                self.longitude,
                self.speed,
                self.altitude,
                self.course]

    def read_data(self):
        self.ser.reset_input_buffer()
        flag = 0
        while flag != 2:
            sio1 = io.BufferedRWPair(self.ser, self.ser, 1)
            sio2 = io.TextIOWrapper(sio1,
                                    newline='\r',
                                    line_buffering=True)

            self_id = sio2.readline()
            msg = pynmea2.parse(self_id)

            if msg.sentence_type == 'GGA':
                self.latitude = msg.latitude
                self.longitude = msg.longitude
                self.altitude = msg.altitude
                flag = 1

            if msg.sentence_type == 'RMC':
                self.speed = msg.spd_over_grnd
                self.course = msg.true_course
                if flag == 1:
                    flag = 2


if __name__ == "__main__":
    mygps = Gps()
    mygps.create_file()
    mygps.read_data()
    mygps.write_data()
