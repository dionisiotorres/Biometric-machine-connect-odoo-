import csv
from datetime import datetime
import sys
import os
sys.path.insert(1,os.path.abspath("./pyzk"))
from zk import ZK, const
class finger_machine:

    def __init__(self,ip,port,timeout=5, password=0, force_udp=False, ommit_ping=False):
        self.ip=ip
        self.port=port
        try:
            print ('Connecting to device .............')
            self.zk = ZK (self.ip, self.port, timeout, password, force_udp, ommit_ping)
            self.conn= self.zk.connect ()
            if self.conn.is_connect:
                print("Sucsseful Connect")
                #print(" Conn ",self.conn)
                newtime = datetime.today ()
                print("Today Time ",newtime)
                self.conn.set_time (newtime)
                zktime = self.conn.get_time ()
                print ("Time in Finger Print ",zktime)
                # print("Device Name ",self.conn.get_device_name())
                # print(" Face Version ",self.conn.get_face_version())
                # print (" Get Network", self.conn.get_network_params ())
                print("get mac ",self.conn.get_mac())
        except:
            print ("Finger Printer Not Connected to initilization Machine....")
            return False

    def get_finger_attendence(self):
        try:
            self.conn=self.zk.connect()
            if self.conn.is_connect:
                # Get attendances (will return list of Attendance object)
                attendances = self.conn.get_attendance ()
                # print(" Satus ",attendances[1].status," User ID ",attendances[1].user_id," punh ",attendances[1].punch, " Time ",attendances[1].timestamp)
                if attendances:
                    print("Get Attendence Successful ")
                    print("There are ",len(attendances)," attendances in Biometric machine ")
                    # for att in attendances:
                    #     print(att,"\n.. ")
                    return attendances
                else:
                    print("No Employee Entered to device in get_attendence")
                    return attendances
            else:
                print("Finger Printer Not Connected in get_attendence() ")
                return False
        except:
            print ("Finger Printer Not Connected in get_attendence() ")
            return False

    def get_users(self):
        try:
            self.conn=self.zk.connect()
            users=[]
            if self.conn.is_connect:
                # Get attendances (will return list of Attendance object)
                users = self.conn.get_users()
                #users=self.conn.get_user_template(1,155)
                if users:
                    print("Get Users Successful.....")
                    for user in users:
                        print(f"User Name {user.name} User ID {user.user_id}")
                    return users
                else:
                    print ("No Employee Entered to device in get_users")
                    return users
            else:
                print ("Finger Printer Not Connected in get_users ")
                return -1
        except:
            print ("Finger Printer Not Connected in get_users ")
            return -1


    def clearFingerPrint(self):
        try:
            self.conn = self.zk.connect ()
            if self.conn.is_connect:
                conclear = self.conn.clear_attendance ()
                #print ("con clear ", conclear)
                return True
            else:
                print(" Finger Print Not Connect So we can not clear attendence in clearFingerPrint()")
                return False
        except:
            print (" Finger Print Not Connect So we can not clear attendence in clearFingerPrint()")
            return False

    def get_username_machine(self,user_id):
        users=self.conn.get_users()
        for user in users:
            if user.user_id==user_id:
                return user.name





