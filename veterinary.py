from tkinter import*
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox






class Veterinary:
    def __init__(self,root):
        self.root=root
        self.root.title("Veterinary Appiontment Appication")
        self.root.geometry("800x600+0+0")


        labeltitle=Label(self.root,bd=20,relief=RIDGE,text="+ Pet Care Bd",fg="red",bg="white",font=("Times New Roman",30,"bold"))    
        labeltitle.pack(side=TOP,fill=X)

        Dataframe=Frame(self.root,bd=20,relief=RIDGE)
        Dataframe.place(x=0,y=100,width=800,height=400)  

        Buttonframe=Frame(self.root,bd=20,relief=RIDGE)
        Buttonframe.place(x=0,y=515,width=800,height=70)

        global text_Pet_Name, text_Owner_Name, text_Phone
        global pet_type_var, sex_var, vaccinated_var


        label_Pet_Name=Label(Dataframe,text="Pet Name:",font=("Calibri (Body)",13,"bold"),padx=2,pady=6)
        label_Pet_Name.grid(row=0,column=0,sticky=W)
        text_Pet_Name=Entry(Dataframe,font=("arial",11,"bold"),width=20)
        text_Pet_Name.grid(row=0,column=1)

        label_Owner_Name=Label(Dataframe,text="Owner Name:",font=("Calibri (Body)",13,"bold"),padx=2,pady=6)
        label_Owner_Name.grid(row=1,column=0,sticky=W)
        text_Owner_Name=Entry(Dataframe,font=("arial",11,"bold"),width=20)
        text_Owner_Name.grid(row=1,column=1)

        label_Phone=Label(Dataframe,text="Phone Number:",font=("Calibri(Body)",13,"bold"),padx=2,pady=6,)
        label_Phone.grid(row=2,column=0,sticky=W)
        text_Phone=Entry(Dataframe,font=("arial",11,"bold"),width=20)
        text_Phone.grid(row=2,column=1)

        label_Pet_Type=Label(Dataframe,text="Pet Type:",font=("Calibri (Body)",13,"bold"),padx=2,pady=6)
        label_Pet_Type.grid(row=3,column=0,sticky=W)
        pet_type_var=StringVar()
        combo_Pet_Type=ttk.Combobox(Dataframe,textvariable=pet_type_var,state="readonly",font=("arial",11,"bold"),width=18)
        combo_Pet_Type['values']=("Dog", "Cat", "Bird") 
        combo_Pet_Type.grid(row=3, column=1)


        label_Sex=Label(Dataframe,text="Sex:",font=("Calibri (Body)",13,"bold"),padx=2,pady=6)
        label_Sex.grid(row=4,column=0,sticky=W)
        sex_var = StringVar()

        male_radio = Radiobutton(Dataframe, text="Male", variable=sex_var, value="Male")
        male_radio.grid(row=4, column=1, sticky=W)
        female_radio = Radiobutton(Dataframe, text="Female", variable=sex_var, value="Female") 
        female_radio.grid(row=4, column=2, sticky=W)

        label_Vaccinated=Label(Dataframe,text="Vaccinated:",font=("Calibri (Body)",13,"bold"),padx=2,pady=6,)
        label_Vaccinated.grid(row=5,column=0,sticky=W)
        vaccinated_var=StringVar()
        radio_yes=Radiobutton(Dataframe,text="Yes",variable=vaccinated_var,value="Yes")
        radio_yes.grid(row=5,column=1,sticky=W)
        radio_no=Radiobutton(Dataframe,text="No",variable=vaccinated_var,value="No")
        radio_no.grid(row=5,column=2,sticky=W)

    
        #=======================================button======================================

        button_Doctor_list=Button(Buttonframe,text="Find Doctor",bg="green",fg="white",font=("Calibri (Body)",13,"bold"),width=18)
        button_Doctor_list.grid(row=0,column=0)

        button_update=Button(Buttonframe,text="Update",bg="green",fg="white",font=("Calibri (Body)",13,"bold"),width=18)
        button_update.grid(row=0,column=1)

        button_clear=Button(Buttonframe,text="Clear",bg="green",fg="white",font=("Calibri (Body)",13,"bold"),width=18)
        button_clear.grid(row=0,column=2)

        button_exit=Button(Buttonframe,text="Exit",bg="green",fg="white",font=("Calibri (Body)",13,"bold"),width=18)
        button_exit.grid(row=0,column=3)

    def update_info(self):
         update_window = Toplevel()
         update_window.title("Update Information")
         update_window.geometry("600x400")

         pet_name = text_Pet_Name.get()
         owner_name = text_Owner_Name.get()
         phone = text_Phone.get()
         pet_type = pet_type_var.get()
         sex = sex_var.get()
         vaccinated = vaccinated_var.get()

        

         Label(update_window, text="Pet Name: " + pet_name,font=("Calibri (Body)",13,"bold"),padx=2,pady=6).pack()
         Label(update_window, text="Owner Name: " + owner_name,font=("Calibri (Body)",13,"bold"),padx=2,pady=6).pack()
         Label(update_window, text="Phone: " + phone,font=("Calibri (Body)",13,"bold"),padx=2,pady=6).pack()
         Label(update_window, text="Pet Type: " + pet_type,font=("Calibri (Body)",13,"bold"),padx=2,pady=6).pack()
         Label(update_window, text="Sex: " + sex,font=("Calibri (Body)",13,"bold"),padx=2,pady=6).pack()
         Label(update_window, text="Vaccinated: " + vaccinated,font=("Calibri (Body)",13,"bold"),padx=2,pady=6).pack()
             

#======================close Button========================

         Button(update_window, text="Close", font=("Arial", 12), bg="red", fg="white",command=update_window.destroy,width=18).pack(pady=20)

#=====================Confirm Button========================    
    
         Button(update_window,text="Confirm",font=("Arial", 12),bg="green",fg="white",command=lambda: [messagebox.showinfo("Success", "Submit Successfully ✅"), update_window.destroy()],width=18).pack(pady=40)


root=Tk() 
ob=Veterinary(root)
root.mainloop()