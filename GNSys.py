import os
import subprocess
import tkinter as tk
from tkinter import *
import random
import pandas as pd
from datetime import datetime
#login system must have:
# pasword protected login---------solved
# log failed attempts with day time and text--------solved
# trainieee name/institution/ID and hours trained.---------solved
# restart---------solved
# hidden log temps and login attempts---------solved
# loggin ---------solved
# time since running

def process_exists(process_name):
    call = 'TASKLIST', '/FI', 'imagename eq %s' % process_name
    # use buildin check_output right away
    output = subprocess.check_output(call).decode()
    # check in last line for process name
    last_line = output.strip().split('\r\n')[-1]
    # because Fail message could be translated
    return last_line.lower().startswith(process_name.lower())
def USBconfig():
    #-------------------run usb config----------------
    os.system(r"C:\AFS\UH60\2.2.1.27\bin\CAPTUsbConfig.exe")
    print(" Usb config running");# to do....execute ios.exe after usb config is done and closed
    trackUSB=1
  
def start():
    process1Track=process_exists("CAPTUsbConfig.exe")
    while process1Track==True:
        print("USB config happening")
        #bgUSB="red"  button status change

    #-------------------run capte ios-----------------
    print("USB config done")
    print("Starting simulation enviroment")
    os.system(r"C:\AFS\UH60\2.2.1.27\bin\IOS.exe")
    print("System runing")
def pause():
    print("System paused")
def sync():
    print("Sync ok?")
def SystemStart():
    window = tk.Tk()
    w, h = window.winfo_screenwidth(), window.winfo_screenheight()
    window.geometry("%dx%d+0+0" % (w, h-100))
    window.title("UH60M Simuldor Activado")
    myfont = "Times 20 bold"
    btfont="Times 10 bold"
    bgUSB="green"

    lbl1 =Label(window, text="Para iniciar el simulador se requieren 3 pasos",font=myfont)
    lblSync = Label(window, text="1) Proceso de arranque de ciclico, colectivo y pedales",font=myfont)
    #lblusb = Label(window, text=" 2) Reconocimiento de dispositivos USB",font=myfont)
    lblIOS = Label(window, text="2) Inicio de interfaz de simulador",font=myfont)
    #btnUSB = Button(window, text="Reconocimiento de dispositivos USB",font=btfont, bg=bgUSB, fg="white",command=USBconfig)
    trackUSB=0
    #btnSync = Button(window, text="Reconocimiento de dispositivos USB",font=btfont, bg="green", fg="white",command=sync)
        
    btnIOS = Button(window, text="Inicio de interfaz de simulador",font=btfont, bg="green", fg="white",command=start)
    btnPause = Button(window, text="Pausar Simulador" ,font=btfont, bg="green", fg="white",command=pause)
    lbl1.pack(side=TOP)
    lblSync.pack(side=TOP)
    #btnSync.pack(side=TOP)
    #lblusb.pack(side=TOP)
    #btnUSB.pack(side=TOP)
    lblIOS.pack(side=TOP)
    btnIOS.pack(side=TOP)
    btnPause.pack(side=TOP)  
    
    # Code to add widgets will go here...
    window.mainloop()
def retrieve_user():
    myLabel = Label(login,text=userEntry.get())
    myLabel.pack(side=TOP)
    myLabel2 = Label(login,text=pswEntry.get())
    myLabel.pack(side=TOP)
    return 
def SystemLogin():

     login=tk.Tk()
     w, h = login.winfo_screenwidth(), login.winfo_screenheight()
     login.geometry("%dx%d+0+0" % (w, h-100))
     login.title("UH60M Simuldor Activado")
     myfont = "Times 20 bold"
     btfont="Times 10 bold"
     bgUSB="green"
     #---------------username------------------------------------
     
     labelUsr=Label(login ,text="Introduce Usuario",font=myfont )
     labelUsr.pack(side=TOP)
     userName=tk.StringVar()
     userEntry=Entry(login, width=15, font=myfont, textvariable=userName)
     userEntry.pack(side=TOP)  
     #------------------pasword----------------------------------
     labelPSW=Label(login,text="Introduce contraseña",font=myfont)
     userPassword =StringVar()
     labelPSW.pack(side=TOP)
     pswEntry=tk.Entry(login, width=15, font=myfont, textvariable=userPassword,show='*')
     pswEntry.pack(side=TOP)
     #------------------Crew----------------------------------
     labelCaptain=Label(login,text="Introduce Nombre del primer oficial estudiante",font=myfont)
     captain =StringVar()
     labelCaptain.pack(side=TOP)
     captainEntry=tk.Entry(login, width=15, font=myfont, textvariable=captain)
     captainEntry.pack(side=TOP)
     labelCOP=Label(login,text="Introduce Nombre del segundo oficial estudiante",font=myfont)
     copilot =StringVar()
     labelCOP.pack(side=TOP)
     copilotEntry=tk.Entry(login, width=15, font=myfont, textvariable=copilot)
     copilotEntry.pack(side=TOP)
     labelINSTIT=Label(login,text="Institución",font=myfont)
     instit =StringVar()
     labelINSTIT.pack(side=TOP)
     institEntry=tk.Entry(login, width=15, font=myfont, textvariable=instit)
     institEntry.pack(side=TOP)    
     #-----------------access logic-----------------------------
     def retrieve_user():
        usrLabel = Label(login,text=userEntry.get())
        usrLabel.pack(side=TOP)
        pswLabel = Label(login,text=pswEntry.get())
        pswLabel.pack(side=TOP)
        ###-----Variables obtention for appending to df----#
        user=userEntry.get()
        psw=pswEntry.get()
        cap=captainEntry.get()
        cop=copilotEntry.get()
        instuto=institEntry.get()
        now = datetime.now()
        horaInic= now.strftime("%H:%M:%S")
        horaFin= now.strftime("%H:%M:%S")
        #------------access Credentials-----------------------
        accesList = ['JavierVite','Jorge Pineda','Cap Pineda']
        accesPsw= ['Zuricata92','vuelo91']
        userIndex=0
        attempt=0
        if institEntry.index("end") and captainEntry.index("end")!= 0:
            if user in accesList:
                userIndex=accesList.index(user)
                pswIndex=accesPsw.index(psw)
                if userIndex==pswIndex:
                    accesLabel= Label(login,text="Access granted!")
                    accesLabel.pack(side=TOP)
                    #-----dataframe appending to and from  csv-----#
                    data=[[horaInic,horaFin,instuto,user,cap,cop,0]]
                    df_work=pd.DataFrame(data,columns=['Hora de inicio', 'Hora de fin','Institucion','Instructor', 'Piloto','Copiloto','Horas voladas'])
                    df_public1=pd.read_csv(r'C:\AFS\UH60\2.2.1.27\bin\task1\key1.csv',header=0)
                    df_private=pd.read_csv(r'C:\AFS\UH60\2.2.1.27\bin\task1\key_P.csv',header=0)
                    df_public=pd.concat([df_public1,df_work],verify_integrity=True,ignore_index = True)
                    df_public.to_csv(r'C:\AFS\UH60\2.2.1.27\bin\task1\key1.csv')
                    print(df_private)
                

                    login.destroy()
                    #this is the main entry point#                
                    SystemStart()               
        else:  
            print("Credenciales incorrectas o registrar usuarios e institución correctamente. intente denuevo")                            
            print(user)
            print(len(user))
            print(psw)
            print(len(psw))
            print("Credenciales incorrectas o registrar usuarios e institución correctamente. intente denuevo")
            attempt+1
            accesLabel= Label(login,text="Credenciales incorrectas. intente denuevo.", bg="red")
            accesLabel.pack(side=TOP)
            return 
     buttonCal = tk.Button(login, text="Validar", command=retrieve_user).pack(side=TOP)     

     # SystemStart()<<<<<<sistem start if loggin succesfull

     login.mainloop()




if __name__ == "__main__":
    SystemLogin()
