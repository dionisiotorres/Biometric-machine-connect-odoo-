from fingerOdooSh import odoosh_finger
from finger_machine import finger_machine
from csv_class import csv_files
from pandaclass import panadobject
from configparser import ConfigParser
from PyQt5.QtWidgets import QMessageBox

def get_ip_port():
    config_object = ConfigParser ()
    config_object.read ("config.ini")
    # Get the password
    device_data = config_object["DEVICEDATA"]
    ip = device_data["ip"]
    print("ip is ",ip , "type ",type(ip))
    port = int(device_data["port"])
    print("port is ",port , "type ",type(port))
    device_data_list = [ip, port]
    return device_data_list

def main():
    device_data=get_ip_port()
    try:
        finger_obj = finger_machine(device_data[0], device_data[1])
        attends_objects = finger_obj.get_finger_attendence ()
        if attends_objects:
            csv_obj = csv_files (attends_objects, finger_obj)
            file_name=csv_obj.get_file_name()
            try:
                dataframe = panadobject (file_name)
                panadObj=dataframe.dataFram
                if panadObj.isnull:
                    objodoosh = odoosh_finger ()
                    objodoosh.pushattendens (panadObj,dataframe)
                    print("File Name ",file_name)
                    dataframe.save_file(file_name)
                    dataframe.save_asexcel (file_name)
            except:
                print ("No CSV File.......................... ")
        else:
            print("No Attedances in Biometric Machine ............")
            print("Please enter Attendances Data......")
    except:
        msg = QMessageBox ()
        msg.setIcon (QMessageBox.Information)
        msg.setText ("Incorrect ip or port Number")
        msg.setInformativeText ("May be incorrect ip or port check setting network")
        msg.setWindowTitle ("Ckecking Network")
        x = msg.exec_ ()
        print("Check Ip and port in Config.ini ")

if __name__ == '__main__':
   main()