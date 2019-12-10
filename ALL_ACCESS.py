import numpy
import os


from tkinter import *
from tkinter import ttk

from pynput.keyboard import Key,Controller
import time
import pickle




username_dic={}
password_dic={}

def key(item):
    
    keyboard=Controller()
    for a in item:
        keyboard.press(a)
        
        
def start(item):
    
    #print(item)
    

    keyboard=Controller()

    os.startfile(item)
    
   
    time.sleep(8)
    
    #name='yosef'
    #password='baneta'
    na_saved=open('na','rb')
    name_li=pickle.load(na_saved)

    us_saved=open('us','rb')
    username_dic=pickle.load(us_saved)

    pa_saved=open('pa','rb')
    password_dic=pickle.load(pa_saved)


    
    key(username_dic[item])
    keyboard.press(Key.tab)
    key(password_dic[item])
    keyboard.press(Key.enter)
    keyboard.press(Key.enter)
    keyboard.press(Key.enter)
    keyboard.press(Key.enter) 
    





        

def save():
    
    save_window=Tk()
    save_window.title('SAVE NEW ACCOUNT')
    save_window.geometry('325x200+300+100')

    savename=StringVar()
    saveusername=StringVar()
    savepassword=StringVar()
    savebox=StringVar()

    Label(save_window,text='LOCATION & NAME').grid(row=2,column=2)
    Label(save_window,text='USER NAME').grid(row=3,column=2)
    Label(save_window,text='PASSWORD').grid(row=4,column=2)
    Label(save_window,text='BOX NUMBER').grid(row=5,column=2)
    

    save_name=Entry(save_window,textvariable=savename)
    save_username=Entry(save_window,textvariable=saveusername)
    save_password=Entry(save_window,show='*',textvariable=savepassword)
    save_box=Entry(save_window,textvariable=savebox)
    
    save_name.config(width=30)
    save_name.grid(row=2,column=3)

    save_username.config(width=30)
    save_username.grid(row=3,column=3)
    
    save_password.config(width=30)
    save_password.grid(row=4,column=3)

    save_box.config(width=30)
    save_box.grid(row=5,column=3)
    
    def complete_save():
        
        savename=save_name.get()
        saveusername=save_username.get()
        savepassword=save_password.get()
        savebox=save_box.get()

        #####

        na_saved=open('na','rb')
        name_li=pickle.load(na_saved)

        us_saved=open('us','rb')
        username_dic=pickle.load(us_saved)

        pa_saved=open('pa','rb')
        password_dic=pickle.load(pa_saved)

        name_li[int(savebox)-1]=savename
        username_dic[savename]=saveusername
        password_dic[savename]=savepassword

        na_saved=open('na','wb')
        pickle.dump(name_li,na_saved)
        na_saved.close
        
        us_saved=open('us','wb')
        pickle.dump(username_dic,us_saved)
        us_saved.close

        pa_saved=open('pa','wb')
        pickle.dump(password_dic,pa_saved)
        pa_saved.close

        

        Label(save_window,text='...........SUCESSFULLY SAVED............').grid(row=10,column=3)
        
       

        


    save_button=Button(save_window,text='SAVE',bg='green',command=complete_save)
    save_button.grid(row=6,column=3)
    save_button.config(height=1,width=10)





   
def load():
    


    window=Tk()
    window.title('LAUNCH ACCOUNT')
    window.geometry('325x390+300+100')
    

    
    n=0
    
   


    na_saved=open('na','rb')
    name_li=pickle.load(na_saved)

    
    button1=Button(window,text=name_li[0][22:-4],fg='blue',command=lambda: start(name_li[0]))
    
    button1.config(height=8,width=14)
    button1.grid(row=1,column=1)
    

    button2=Button(window,text=name_li[1][22:-4],fg='blue',command=lambda: start(name_li[1]))
    button2.config(height=8,width=14)
    button2.grid(row=1,column=2)

    button3=Button(window,text=name_li[2][22:-4],fg='blue',command=lambda: start(name_li[2]))
    button3.config(height=8,width=14)
    button3.grid(row=1,column=3)

    button4=Button(window,text=name_li[3][22:-4],fg='blue',command=lambda: start(name_li[3]))
    button4.config(height=8,width=14)
    button4.grid(row=2,column=1)

    button5=Button(window,text=name_li[4][22:-4],fg='blue',command=lambda: start(name_li[4]))
    button5.config(height=8,width=14)
    button5.grid(row=2,column=2)

    button6=Button(window,text=name_li[5][22:-4],fg='blue',command=lambda: start(name_li[5]))
    button6.config(height=8,width=14)
    button6.grid(row=2,column=3)

    button7=Button(window,text=name_li[6][22:-4],fg='blue',command=lambda: start(name_li[6]))
    button7.config(height=8,width=14)
    button7.grid(row=3,column=1)

    button8=Button(window,text=name_li[7][22:-4],fg='blue',command=lambda: start(name_li[7]))
    button8.config(height=8,width=14)
    button8.grid(row=3,column=2)

    button9=Button(window,text=name_li[8][22:-4],fg='blue',command=lambda: start(name_li[8]))
    button9.config(height=8,width=14)
    button9.grid(row=3,column=3)

   
        
      

def settings():
    settings_window=Tk()
    settings_window.title('MANAGE PASSWORD')
    settings_window.geometry('350x200+300+100')
    
    oldusername=StringVar()
    newusername=StringVar()

    oldpassword=StringVar()
    newpassword=StringVar()
    checkpassword=StringVar()


    Label(settings_window,text='CURRENT USERNAME').grid(row=2,column=2)
    Label(settings_window,text='CURRENT PASSWORD').grid(row=3,column=2)

    Label(settings_window,text='NEW USERNAME').grid(row=4,column=2)
    Label(settings_window,text='NEW PASSWORD').grid(row=5,column=2)
    Label(settings_window,text='RE-ENTER PASSWORD').grid(row=6,column=2)

    setting_oldusername=Entry(settings_window,textvariable=oldusername)
    

    setting_oldpassword=Entry(settings_window,show='*',textvariable=oldpassword)
    setting_newusername=Entry(settings_window,textvariable=newusername)
    setting_password=Entry(settings_window,show='*',textvariable=newpassword)
    setting_checkpassword=Entry(settings_window,show='*',textvariable=checkpassword)

    setting_oldusername.config(width=30)
    setting_oldusername.grid(row=2,column=3)

    setting_oldpassword.config(width=30)
    setting_oldpassword.grid(row=3,column=3)
    
    setting_newusername.config(width=30)
    setting_newusername.grid(row=4,column=3)
    

    setting_password.config(width=30)
    setting_password.grid(row=5,column=3)

    setting_checkpassword.config(width=30)
    setting_checkpassword.grid(row=6,column=3)


    def settings_complete():
        mainpas_saved=open('main_pas','rb')
        main_password_dic=pickle.load(mainpas_saved)
        

        oldusername=setting_oldusername.get()
        oldpassword=setting_oldpassword.get()
        newusername=setting_newusername.get()
        newpassword=setting_password.get()
        checkpassword=setting_checkpassword.get()



        try:
            main_password_dic[str(oldusername)]

        except KeyError as Er:

            Label(settings_window,text='..oops! somethingwent wrong.',fg='red').grid(row=8,column=3)
        else:
            pass

        if oldpassword == main_password_dic[str(oldusername)] and newpassword == checkpassword:

            del main_password_dic[oldusername]
            main_password_dic[newusername]=newpassword

            mainpas_saved=open('main_pas','wb')
            pickle.dump(main_password_dic,mainpas_saved)
            mainpas_saved.close

            Label(settings_window,text='...........SUCESSFULLY CHANGED............').grid(row=10,column=3)
            
        



    settings_button=Button(settings_window,text='ENTER ',bg='green',command=settings_complete)
    settings_button.grid(row=7,column=3)
    settings_button.config(height=1,width=10)
    
            
        
        
    


    

    

    



   


    







def main():
    

    window=Tk()
    window.title('ALL-IN-ONE by YOSEF BANETA (346-719-5433)')
    window.geometry('650x550+300+100')
    button1=Button(text='RUN PROGRAMS',bg='light yellow',command=load)
    button1.config(height=15,width=30)
    button1.grid(row=1,column=1)

    button2=Button(text='ADD NEW',bg='light blue',command=save)
    button2.config(height=15,width=30)
    button2.grid(row=1,column=2)

    button3=Button(text='CHANGE PASSWORD',bg='light pink',command=settings)
    button3.config(height=15,width=30)
    button3.grid(row=1,column=3)
            
            


    



main()








