import csv
import serial
import time
import os

PORT = 'COM40'  # port initialization
BAUD_RATE = '115200'  # Number of sent/received bits per second
ser = serial.Serial(PORT, BAUD_RATE, timeout=0.1)  # create a serial object
time.sleep(3)  # wait for the serial port to initialise

datafile_name = "data.csv"
if os.path.isfile(datafile_name):
    os.remove(datafile_name)  # remove the csv file if it exists

t_value = 0
ir_value = 0
red_value = 0
fieldnames = ["t_values", "ir_values", "red_values"]  # field names for csv_file

with open("data.csv", 'w', newline='') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()

while True:
    ser_data = ser.readline()
    ser_data = ser_data[:-2]
    ser_data = ser_data.decode()
    ser_data_list = ser_data.split(',')

    # eliminating bad data in csv file
    if (float(ser_data_list[1]) != 0) and (float(ser_data_list[2]) != 0):
        if abs((float(ser_data_list[1]) - ir_value) / float(ser_data_list[1])) > 1.01 or \
                abs((float(ser_data_list[2]) - red_value) / float(ser_data_list[2])) > 1.01:
            continue

        t_value = (float(ser_data_list[0]) / 1000000.0)
        ir_value = (float(ser_data_list[1]))
        red_value = (float(ser_data_list[2]))

        info = {
            "t_values": t_value,
            "ir_values": ir_value,
            "red_values": red_value
        }

        print(ser_data_list[0], ser_data_list[1], ser_data_list[2])
        with open("data.csv", 'a', newline='') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            csv_writer.writerow(info)  # write the values in the csv data file

# time.sleep(0.1)
