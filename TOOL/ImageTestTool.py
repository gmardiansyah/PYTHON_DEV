from tkinter import *
import serial.tools.list_ports
import serial

# create root window 
root = Tk() 

# root window title and dimension 
root.title("Tool") 
root.geometry('600x350') 

# adding menu bar in root window 
# new item in menu bar labelled as 'New' 
# adding more items in the menu bar 
menu = Menu(root) 
item = Menu(menu) 
item.add_command(label='New') 
menu.add_cascade(label='File', menu=item) 
root.config(menu=menu) 

def btnScanclicked(): 
	ports = serial.tools.list_ports.comports()
	ports = [port.device for port in ports]
	ports = ("\n".join(map(str, ports)))
	txt.insert(END, ports) 

def btnOpenclicked():
	port = EntryPort.get() 
	baudrate = EntryBaudrate.get()
	activePort = serial.Serial(port, baudrate, timeout=1)

def btnClearclicked():
	txt.delete('1.0', END)

#ButtonScanSerial
btnScan = Button(root, text = "Scan Serial Port" , 
			fg = "black", command=btnScanclicked) 
btnScan.grid(column=0, row=0) 

#ButtonOpenSerial
btnOpen = Button(root, text = "Open Serial Port" , 
			fg = "black", command=btnOpenclicked) 
btnOpen.place(x=190, y=55)

#ButtonClearPortList
btnClearPort = Button(root, text = "Clear Port List   " , 
			fg = "black", command=btnClearclicked) 
btnClearPort.place(x=0, y=30)

# GetImagesFromAddress CAM>>ICU 0x01
# AckReceivingCommand CAM<<>>ICU 0x02
# StatingfetchingImageComplete CAM<<ICU 0x03
# RequestAccessMemoryFor(X)Minutes CAM<<ICU 0x04
# SendClassResult CAM<<ICU 0x05

#LabelGetImagesFromAddress
lblGetImagesFromAddress = Label(root, text = "GetImagesFromAddress")  
lblGetImagesFromAddress.place (x=0, y=90)

#LabelTotalImage
lblTotalImage = Label(root, text = "Total Image")  
lblTotalImage.place (x=0, y=110)

#EntryTotalImage
EntryTotalImage = Entry(root, width=10) 
EntryTotalImage.place(x=70, y=110)

#LabelAddress
lblAddress = Label(root, text = "Address")  
lblAddress.place (x=140, y=110)

#EntryAddress
EntryAddress = Entry(root, width=10) 
EntryAddress.place(x=190, y=110)

#ButtonExecuteTask1
btnExecuteTask1 = Button(root, text = "Execute" , 
			fg = "black", command=btnClearclicked) 
btnExecuteTask1.place(x=260, y=110)

#LabelAckReceivingCommand
lblAckReceivingCommand = Label(root, text = "AckReceivingCommand")  
lblAckReceivingCommand.place (x=0, y=140)

#ButtonExecuteTask2
btnExecuteTask2 = Button(root, text = "Execute" , 
			fg = "black", command=btnClearclicked) 
btnExecuteTask2.place(x=0, y=160)

#StatingfetchingImageComplete
lblStatingfetchingImageComplete = Label(root, text = "StatingfetchingImageComplete")  
lblStatingfetchingImageComplete.place (x=0, y=190)

#ButtonExecuteTask3
btnExecuteTask3 = Button(root, text = "Execute" , 
			fg = "black", command=btnClearclicked) 
btnExecuteTask3.place(x=0, y=210)


#RequestAccessMemoryFor
lblRequestAccessMemoryFor = Label(root, text = "RequestAccessMemoryFor")  
lblRequestAccessMemoryFor.place (x=0, y=240)

#LabelTime
lblTime = Label(root, text = "Time")  
lblTime.place (x=0, y=260)

#EntryTime
EntryTime = Entry(root, width=10) 
EntryTime.place(x=35, y=260)

#ButtonExecuteTask4
btnExecuteTask4 = Button(root, text = "Execute" , 
			fg = "black", command=btnClearclicked) 
btnExecuteTask4.place(x=105, y=260)

#SendClassResult
lblSendClassResult = Label(root, text = "SendClassResult")  
lblSendClassResult.place (x=0, y=290)

#ButtonExecuteTask5
btnExecuteTask5 = Button(root, text = "Execute" , 
			fg = "black", command=btnClearclicked) 
btnExecuteTask5.place(x=0, y=310)


#LabelEntryPort
lblPort = Label(root, text = "Port")  
lblPort.place (x=190, y=0)

#EntryPortSerialtoOpen
EntryPort = Entry(root, width=10) 
EntryPort.place(x=250, y=0)

#LabelEntryBaudrate
lblBaudrate = Label(root, text = "Baudrate")  
lblBaudrate.place (x=190, y=30)

#EntryBaudrateSerialtoOpen
EntryBaudrate = Entry(root, width=10) 
EntryBaudrate.place(x=250, y=30)


# adding Entry Field 
txt = Text(root, width=10, height=5) 
txt.place(x=100, y=0)

root.mainloop()
