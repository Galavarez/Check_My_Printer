import win32com.client                  # Импорт модуля поиска притеров Онлайн
import os, sys, win32print              # Импорт модулей для RawPrint
from PyQt5.QtWidgets import *           # Импорт модулей PyQt5
from form import Ui_Form                # Импортируем форму
import RawPrint                         # Импортируем модуль для печати Raw
import res_rc                           # Импортируем ресурсы

class MainWindow(Ui_Form, QMainWindow):
    def __init__(self):        
        super().__init__()     # инициализируется форму        
        self.setupUi(self)     # инициализируется файл с дизайном
        # Запуск моих функций
        self.myListPrinters()

        # Обработка событий на нажатия кнопки
        self.button_nozzle_check.clicked.connect(self.click_nozzle_check)
        self.button_head_cleaning_normal.clicked.connect(self.click_head_cleaning_normal)
        self.button_head_cleaning_deep.clicked.connect(self.click_head_cleaning_deep)
        self.listWidget_2.clicked.connect(self.searchName)


    def click_nozzle_check(self): 
        str = self.listWidget_2.currentItem().text()
        if 'canon' in str.lower():
            # print('canon')
            RawPrint.SpoolPrint(self.listWidget_2.currentItem().text(), RawPrint.canon_nozzle_check)
        if 'epson' in str.lower():
            # print('epson')
            RawPrint.SpoolPrint(self.listWidget_2.currentItem().text(), RawPrint.epson_nozzle_check)        
        

    def click_head_cleaning_normal(self):
        str = self.listWidget_2.currentItem().text()
        if 'canon' in str.lower():
            RawPrint.SpoolPrint(self.listWidget_2.currentItem().text(), RawPrint.canon_head_cleaning_normal)
        if 'epson' in str.lower():
            RawPrint.SpoolPrint(self.listWidget_2.currentItem().text(), RawPrint.epson_head_cleaning_normal)

    def click_head_cleaning_deep(self):
        str = self.listWidget_2.currentItem().text()
        if 'canon' in str.lower():
            RawPrint.SpoolPrint(self.listWidget_2.currentItem().text(), RawPrint.canon_head_cleaning_deep)
        if 'epson' in str.lower():
            RawPrint.SpoolPrint(self.listWidget_2.currentItem().text(), RawPrint.epson_head_cleaning_deep)

    def myListPrinters(self):
        wmi = win32com.client.GetObject("winmgmts:")
        for usb in wmi.InstancesOf("Win32_Printer"):
            if usb.WorkOffline:
                # print(usb.DeviceID + ' Off')
                # self.listWidget_2.addItem(usb.DeviceID)
                pass
            else:
                # print(usb.DeviceID + ' On')
                self.listWidget_2.addItem(usb.DeviceID)
                # print (usb.DeviceID)
                # print (usb.WorkOffline)  

    def searchName(self):
        str = self.listWidget_2.currentItem().text()
        if 'canon' in str.lower():
            print('canon')
        if 'epson' in str.lower():
            print('epson')



# Запуск формы
if __name__ == '__main__':
    app = QApplication(sys.argv)    
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


