import csv
import os
from datetime import datetime

class csv_files:
    def __init__(self,attendances_objects,finger_obj):
        size_attend=len(attendances_objects)
        count=0
        self.file_name = self.generate_file_name ()
        self.location_file='attendances_csv_files/'+self.file_name
        csv_file_name=self.location_file+'.csv'
        print("file_name" ,csv_file_name)
        with open (csv_file_name, mode='w',newline='') as csv_file:
            self.fieldnames = ['user_name', 'user_id', 'timestamp', 'status']
            writer = csv.DictWriter (csv_file,delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL ,fieldnames=self.fieldnames)
            writer.writeheader ()
            for attend_obj in attendances_objects:
                user_name=finger_obj.get_username_machine(attend_obj.user_id)
                writer.writerow ({'user_name':user_name , 'user_id':attend_obj.user_id,'timestamp':attend_obj.timestamp,'status':'push'})
                count+=1
        if count==size_attend:
            print("Successful pushed to csv file......")
            print("Data in BioMetric will ne Cleared")
            if finger_obj.clearFingerPrint():
                print ("Clear Attendances in Biometric machine successful...... ")
        print("Attendances write in CSV Files.....................")

    def get_file_name(self):
        return self.file_name

    def get_location(self):
        return self.location_file

    def generate_file_name(self):
        timetopush = datetime.today ()
        timetopush_st = timetopush.strftime ('%Y-%m-%d %H%M%S')
        file_name = timetopush_st + '_attendanceread'
        return file_name

