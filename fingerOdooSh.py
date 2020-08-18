import pytz
from datetime import datetime
import xmlrpc.client
from configparser import ConfigParser
class odoosh_finger:
    def get_database(self):
        config_object = ConfigParser ()
        config_object.read ("config.ini")
        # Get the password
        databaseinfo = config_object["DATABASE"]
        url=databaseinfo["url"]
        #print("Url is ",url , "type ",type(url))
        db=databaseinfo["db"]
        #print("db is ",db , "type ",type(db))
        databaselist = [url,db]
        return databaselist

    def get_username_pass(self):
        config_object = ConfigParser ()
        config_object.read ("config.ini")
        # Get the password
        username_pass_info = config_object["USERDATA"]
        user_name=username_pass_info["user_name"]
        password=username_pass_info["password"]
        print("user name ",user_name)
        print("pass word ",password)
        username_pass_infolist=[user_name,password]
        return username_pass_infolist

    def __init__(self):
        databaselist=self.get_database()
        self.url = databaselist[0]  # port of odoo
        self.db = databaselist[1]  # name of database
        username_pass_info=self.get_username_pass()
        self.username = username_pass_info[0]
        self.password = username_pass_info[1]
        self.models = None
        self.common = None
        try:
            self.models = xmlrpc.client.ServerProxy ('{}/xmlrpc/2/object'.format (self.url))
            self.common = xmlrpc.client.ServerProxy ('{}/xmlrpc/2/common'.format (self.url))
            self.uid = self.common.authenticate(self.db, self.username, self.password, {})
            print (' Connect to odoo sh \n User ID for odoo = ', self.uid)
            partners = self.models.execute_kw (self.db, self.uid, self.password,
                                           'hr.attendance', 'check_access_rights',
                                           ['read'], {})
            print ("Can Access hr Attendance ", partners)
        except:
            msg = QMessageBox ()
            msg.setIcon (QMessageBox.Information)
            msg.setText ("Incorrect DataBase Data")
            msg.setInformativeText ("May be incorrect on URL DataBase or DataBase name")
            msg.setWindowTitle ("Invalid login DataBase")
            x = msg.exec_ ()
            print("Not Connect withOdoo sh in intiConnOdooSh() ")

    def pushattendens(self, panadObj,pandataframe):
            print ('User ID for odoo = ', self.uid)
            time_tz=self.models.execute_kw(self.db, self.uid, self.password,'res.users', 'read',[self.uid], {'fields': ['tz']})
            print("Time Zone is ",time_tz)
            #pandataframe = panadobject ("attendacne.csv")
            for ind in panadObj.index:
                machine_userID = str(panadObj['user_id'][ind])
                machine_attendance_time = pandataframe.convert_date (panadObj['timestamp'][ind])
                employee_id= self.get_employee_id (machine_userID)
                print("emp_id ",employee_id)
                if(employee_id):
                    print("This Attendacne User has Employee id ",employee_id)
                    odoo_attendance_row=self.is_there_check_in(employee_id,machine_attendance_time)
                    #print("odoo attendance row ",odoo_attendance_row)
                    try:
                        if odoo_attendance_row:
                            #print("The Attendacne row ",odoo_attendance_row)
                            if self.is_there_check_out(odoo_attendance_row):
                                print ("Created Check in .........")
                                if self.create_new_check_in (employee_id, machine_attendance_time,time_tz):
                                    print ("successful Created Check in for Employee id ",employee_id)
                                    pandataframe.update_satuts ("successful", ind)
                                else:
                                    print("Not successful Created Check in for employee id ",employee_id)
                                    pandataframe.update_satuts ("Failed", ind)
                            else:
                                print ("Updated Check Out........")
                                if self.update_employee_check_out(odoo_attendance_row, machine_attendance_time,time_tz):
                                    print("successful Updated Check Out")
                                    pandataframe.update_satuts ("successful", ind)
                                else:
                                    print ("Not successful Updated Check Out")
                                    pandataframe.update_satuts ("Failed", ind)
                        else:
                            print("The id employee ",employee_id," not have machine Attendance")
                            if self.create_new_check_in(employee_id, machine_attendance_time,time_tz):
                                print("successful Created Check in")
                                pandataframe.update_satuts ("successful", ind)
                            else:
                                print("Not successful Created Check in")
                                pandataframe.update_satuts ("Failed", ind)
                    except:
                        print("There is confilect in data ..... ")
                        pandataframe.update_satuts ("Failed", ind)
                else:
                    print("This User ID not Linked with Odoo employee",machine_userID)


    #Start Func Create
    def create_new_check_in(self,emp_id,attendance_time,time_tz):
        #print("User Time Attendance Before TimeZone ",attendance_time," for employee id ",emp_id)
        attendance_time=self.get_local_timezone(attendance_time,time_tz)
        #print("User Time Attendance After TimeZone ",attendance_time," for employee id ",emp_id)
        # emp_id is a list so
        attendance_id_row=self.models.execute_kw (self.db, self.uid, self.password, 'hr.attendance', 'create', [{
                                    'employee_id':emp_id,
                                    'check_in': attendance_time
                                }])
        if attendance_id_row:
            print("Successful Created Check In for employee id ",emp_id," and Attendance Time ",attendance_time)
            return True
        else:
            print("Failed in Creating Check In for employee id ",emp_id," and Attendance Time ",attendance_time)
            return False
        return False
    #end Func Create

    #Start Func Update
    def update_employee_check_out(self,employee_attendance_id, machine_attendance_time,time_tz):
        #print ("User Time Attendance Before TimeZone ", machine_attendance_time)
        machine_attendance_time = self.get_local_timezone (machine_attendance_time, time_tz)
        #print ("User Time Attendance After TimeZone ", machine_attendance_time)
        id_update = self.models.execute_kw (self.db, self.uid, self.password, 'hr.attendance', 'write',
                                            [employee_attendance_id, {'check_out': machine_attendance_time}])
        if id_update:
            print("Successful Update Check Out.....")
            return True
        else:
            print("Not Successful uodate Check Out.....")
            return False
        return False
   #End Func Update


    def get_employee_id(self, machine_userID):
        emp_id=self.models.execute_kw (self.db, self.uid, self.password, 'hr.employee', 'search',
                                       [[['device_id', '=', machine_userID]]])
        if emp_id:
            emp_id=emp_id[0]
            return emp_id
        return emp_id


    def is_there_check_in(self,emp_id,attendance_time):
        odoo_atten_row_id=self.get_attendance_id(emp_id)
        if odoo_atten_row_id:
            #print(" Last Attendance ID For User ",odoo_atten_row_id)
            check_in_time = self.models.execute_kw (self.db, self.uid, self.password,
                                               'hr.attendance', 'read',
                                               [odoo_atten_row_id], {'fields': ['check_in']})
            if check_in_time:
                _check_in_time = check_in_time[0]['check_in']
                #print ("type check in time ", type (_check_in_time))
                _check_in_time = datetime.strptime (_check_in_time, '%Y-%m-%d %H:%M:%S')
               # print("Convert Type Check in time to Date.. ")
                if attendance_time.date()==_check_in_time.date():
                    return odoo_atten_row_id
                else:
                    return False
            else:
                return False
        else:
            return False

    def get_attendance_id(self, emp_id):
        odoo_attendance_row = self.models.execute_kw (self.db, self.uid, self.password,
                                       'hr.attendance', 'search', [[['employee_id', '=', emp_id]]], {'limit': 1})
        if odoo_attendance_row:
            odoo_attendance_row=odoo_attendance_row[0]
            return odoo_attendance_row
        return odoo_attendance_row


    def is_there_check_out(self,odoo_attendance_row):
        check_out_time = self.models.execute_kw (self.db, self.uid, self.password, 'hr.attendance', 'read',
                                                 [odoo_attendance_row], {'fields': ['check_out']})
        _check_out_time = check_out_time[0]['check_out']
        if _check_out_time:
            #print("This Attendance row is",odoo_attendance_row, "has Ckeck Out ",_check_out_time)
            return True
        else:
            #print("This User not has Attendance Check Out...")
            return False
        return False


    def get_local_timezone(self,atten_time, time_tz):
        atten_time = datetime.strptime (
            atten_time.strftime ('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S')
        local_tz = pytz.timezone (
            time_tz[0]['tz'] or 'Africa/Cairo')
        local_dt = local_tz.localize (atten_time, is_dst=None)
        utc_dt = local_dt.astimezone (pytz.utc)
        utc_dt = utc_dt.strftime ("%Y-%m-%d %H:%M:%S")
        atten_time = datetime.strptime (
            utc_dt, "%Y-%m-%d %H:%M:%S")
        atten_time = atten_time.strftime ("%Y-%m-%d %H:%M:%S")
        return atten_time

def main():
    odoosh_obj=odoosh_finger()
    #odoosh_finger.get_database(odoosh_obj)

if __name__ == '__main__':
    main()

