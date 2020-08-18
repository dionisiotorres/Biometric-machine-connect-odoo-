# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login-2.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from configparser import ConfigParser
from PyQt5 import QtCore,QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from pandaclass import panadobject
from pushattendances import Ui_MainWindow
class Ui_Form(object):
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

    def check_login(self):
        password_text=self.text_password.text()
        user_name_text=self.text_username.text()
        # link between login view and push attendances
        username_pass_info=self.get_username_pass()
        if user_name_text==username_pass_info[0] and password_text==username_pass_info[1]:
            print("successful login in.........")
            msg = QMessageBox ()
            msg.setIcon (QMessageBox.Information)
            msg.setText ("successful login in")
            msg.setInformativeText ("Correct Username and password")
            msg.setWindowTitle ("Login Correct")
            x = msg.exec_ ()
            self.window=QtWidgets.QMainWindow()
            self.ui=Ui_MainWindow()
            self.ui.setupUi(self.window)
            self.window.show()
        else:
            print("Not successful login in ")
            msg = QMessageBox ()
            msg.setIcon (QMessageBox.Information)
            msg.setText ("Not successful login in")
            msg.setInformativeText ("May be incorrect password or username")
            msg.setWindowTitle ("Login Invalid")
            x=msg.exec_()

    def setupUi(self, Form):
        Form.setObjectName("Attendances")
        Form.resize(410, 367)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(110, 240, 121, 23))
        self.pushButton.setObjectName("pushButton")
        self.text_password = QtWidgets.QLineEdit(Form)
        self.text_password.setGeometry(QtCore.QRect(80, 170, 191, 20))
        self.text_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.text_password.setObjectName("lineEdit_2")
        self.text_username = QtWidgets.QLineEdit(Form)
        self.text_username.setGeometry(QtCore.QRect(80, 110, 191, 20))
        self.text_username.setObjectName("lineEdit")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(50, 20, 291, 51))
        self.textBrowser.setFrameShape(QtWidgets.QFrame.HLine)
        self.textBrowser.setUndoRedoEnabled(False)
        self.textBrowser.setReadOnly(True)
        self.textBrowser.setObjectName("textBrowser")
        ## click event
        self.pushButton.clicked.connect(self.check_login)
        ##

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setToolTip(_translate("Form", "login with odoo user "))
        self.pushButton.setText(_translate("Form", "login"))
        self.text_password.setPlaceholderText(_translate("Form", "Enter Password "))
        self.text_username.setPlaceholderText(_translate("Form", "Enter User Name"))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">   Hello in Push Attendances Program </span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())