import sys
import pandas as pd
from datetime import datetime
from pandas import ExcelWriter
from pandas import ExcelFile
class panadobject():
    def __init__(self,file_path):
        file_path+='.csv'
        print("file_path ",file_path)
        self.dataFram=pd.read_csv(file_path)
        self.size_datafram=self.dataFram.shape

    def get_number_row(self):
        return self.size_datafram[0]

    def convert_date(self,datstr):
        dat = datetime.strptime (
            datstr, '%Y-%m-%d %H:%M:%S')
        return dat

    def get_number_column(self):
        return self.size_datafram[1]

    def get_DataFramObject(self):
        return self.dataFram

    def save_asexcel(self,file_name):
        file_name_excel='attendances_excel/'+file_name+'.xlsx'
        print("file_name_excel ",file_name_excel)
        self.dataFram.to_excel(file_name_excel,index=False)


    def update_satuts(self,status,number_row):
        self.dataFram.loc[number_row,'status']=status

    def renamedataframe(self):
        pass

    def save_file(self,file_name):
        #print("File pushed Name ",file_name)
        file_name_loaction='attendances_csv_files/'+file_name+'_pushed.csv'
        print("file name csv location ",file_name_loaction)
        self.dataFram.to_csv(file_name_loaction,index=0,header=True)




# def main():
#     filepath="attendacne2.csv"
#     panObject=panadobject(filepath)
#     print(panObject.get_number_row())
#     panObject.prepare_datafram()
#     panObject.datatype()
#     #panObject.update_satuts("Done",3)
#     #panObject.save_file()
#     #panadobject.renamedataframe()
#
# if __name__ == '__main__':
#    main()