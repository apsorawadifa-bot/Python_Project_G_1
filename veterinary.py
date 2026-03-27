from logging import root
import re
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

        global text_Pet_Name, text_Owner_Name, text_DOB, text_Breed, text_Appointment_Date, text_Phone
        global pet_type_var, sex_var, vaccinated_var


        label_Pet_Name=Label(Dataframe,text="Pet Name:",font=("Calibri (Body)",13,"bold"),padx=2,pady=6)
        label_Pet_Name.grid(row=0,column=0,sticky=W)
        self.text_Pet_Name=Entry(Dataframe,font=("arial",11,"bold"),width=20)
        self.text_Pet_Name.grid(row=0,column=1)

        label_Owner_Name=Label(Dataframe,text="Owner Name:",font=("Calibri (Body)",13,"bold"),padx=2,pady=6)
        label_Owner_Name.grid(row=1,column=0,sticky=W)
        self.text_Owner_Name=Entry(Dataframe,font=("arial",11,"bold"),width=20)
        self.text_Owner_Name.grid(row=1,column=1)

        label_DOB=Label(Dataframe,text="Date of birth",font=("Calibri(Body)",13,"bold"),padx=2,pady=6,)
        label_DOB.grid(row=2,column=0,sticky=W)
        self.text_DOB=Entry(Dataframe,font=("arial",11,"bold"),width=20)
        self.text_DOB.grid(row=2,column=1)

        label_Pet_Type=Label(Dataframe,text="Pet Type:",font=("Calibri (Body)",13,"bold"),padx=2,pady=6)
        label_Pet_Type.grid(row=3,column=0,sticky=W)
        self.pet_type_var=StringVar()
        combo_Pet_Type=ttk.Combobox(Dataframe,textvariable=pet_type_var,state="readonly",font=("arial",11,"bold"),width=18)
        combo_Pet_Type['values']=("Dog", "Cat", "Bird") 
        combo_Pet_Type.grid(row=3, column=1)


        label_Sex=Label(Dataframe,text="Sex:",font=("Calibri (Body)",13,"bold"),padx=2,pady=6)
        label_Sex.grid(row=4,column=0,sticky=W)
        self.sex_var = StringVar()

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

        label_Breed=Label(Dataframe,text="Breed:",font=("Calibri (Body)",13,"bold"),padx=2,pady=6)
        label_Breed.grid(row=6,column=0,sticky=W)
        self.text_Breed=Entry(Dataframe,font=("arial",11,"bold"),width=20)
        self.text_Breed.grid(row=6,column=1)

class Veterinary:
    def __init__(self,root):
        self.text_Breed.grid(row=6,column=1) 

        label_Appointment_Date=Label(Dataframe,text="Appointment Date:",font=("Calibri (Body)",13,"bold"),padx=2,pady=6)
        label_Appointment_Date.grid(row=7,column=0,sticky=W)
        self.text_Appointment_Date=Entry(Dataframe,font=("arial",11,"bold"),width=20)
        self.text_Appointment_Date.grid(row=7,column=1)

        label_Phone=Label(Dataframe,text="Phone:",font=("Calibri (Body)",13,"bold"),padx=2,pady=6)
        label_Phone.grid(row=8,column=0,sticky=W)
        self.text_Phone=Entry(Dataframe,font=("arial",11,"bold"),width=20)
        self.text_Phone.grid(row=8,column=1)

        #=======================================button======================================

        button_Doctor_list=Button(Buttonframe,text="Find Doctor",bg="green",fg="white",font=("Calibri (Body)",13,"bold"),width=18)
        button_Doctor_list.grid(row=0,column=0)

        button_update=Button(Buttonframe,text="Update",bg="green",fg="white",font=("Calibri (Body)",13,"bold"),width=18,command=self.update_info)
        button_update.grid(row=0,column=1)

        button_clear=Button(Buttonframe,text="Clear",bg="green",fg="white",font=("Calibri (Body)",13,"bold"),width=18)
        button_clear.grid(row=0,column=2)

        button_exit=Button(Buttonframe,text="Exit",bg="green",fg="white",font=("Calibri (Body)",13,"bold"),width=18)
        button_exit.grid(row=0,column=3)

    def clear_data(self):
         self.text_Pet_Name.delete(0, END)
         self.text_Owner_Name.delete(0, END)
         self.text_DOB.delete(0, END)
         self.text_Phone.delete(0, END)
         self.text_Breed.delete(0, END)
         self.text_Appointment_Date.delete(0, END)

         self.pet_type_var.set("")
         self.sex_var.set("")
         self.vaccinated_var.set("")
        

    def update_info(self):
         update_window = Toplevel()
         update_window.title("Update Information")
         update_window.geometry("650x500")

         pet_name = text_Pet_Name.get()
         if pet_name == "":
             messagebox.showerror("Error", "Pet Name is required!")
             return
         if not pet_name.isalpha():
             messagebox.showerror("Error", "Pet Name must contain only letters!")
             return
         
         owner_name = text_Owner_Name.get()
         if not owner_name.isalpha():
             messagebox.showerror("Error", "Owner Name must contain only letters!")
             return
         
         D_O_B = text_DOB.get()
         example= r"^\d{1,2}/\d{1,2}/\d{4}$"

         if not re.match(example, D_O_B):
             messagebox.showerror("Error", "Date must be like dd/mm/yyyy (e.g., 20/05/2025)!")
             return
         
         pet_type =  pet_type_var.get()
         if not pet_type:
             messagebox.showerror("Error", "Please select a Pet Type!")
             return
         
         sex = sex_var.get()
         if not sex:
             messagebox.showerror("Error", "Please select a Sex!")
             return

         vaccinated = vaccinated_var.get()
         if not vaccinated:
             messagebox.showerror("Error", "Please select if Vaccinated!")
             return
         
         Breed = text_Breed.get()
         if not Breed.isalpha():
             messagebox.showerror("Error", "Breed must contain only letters!")
             return
         
         Appointment_Date = text_Appointment_Date.get()
         #=====================validate date format using regex========================
         pattern = r"^\d{1,2}/\d{1,2}/\d{4}$"

         if not re.match(pattern, Appointment_Date):
             messagebox.showerror("Error", "Date must be like dd/mm/yyyy (e.g., 20/04/2026)!")
             return
         
         phone = text_Phone.get()
         if not phone.isdigit():
             messagebox.showerror("Error", "Phone must contain only numbers!")
             return

        

         Label(update_window, text="Pet Name: " + pet_name,font=("Calibri (Body)",11,"bold"),padx=2,pady=6).pack()
         Label(update_window, text="Owner Name: " + owner_name,font=("Calibri (Body)",11,"bold"),padx=2,pady=6).pack()
         Label(update_window, text="Date of Birth: " + D_O_B,font=("Calibri (Body)",11,"bold"),padx=2,pady=6).pack()
         Label(update_window, text="Pet Type: " + pet_type,font=("Calibri (Body)",11,"bold"),padx=2,pady=6).pack()
         Label(update_window, text="Sex: " + sex,font=("Calibri (Body)",11,"bold"),padx=2,pady=6).pack()
         Label(update_window, text="Vaccinated: " + vaccinated,font=("Calibri (Body)",11,"bold"),padx=2,pady=6).pack()
         Label(update_window, text="Breed: " + Breed,font=("Calibri (Body)",11,"bold"),padx=2,pady=6).pack()
         Label(update_window, text="Appointment Date: " + Appointment_Date,font=("Calibri (Body)",11,"bold"),padx=2,pady=6).pack()
         Label(update_window, text="Phone: " + phone,font=("Calibri (Body)",11,"bold"),padx=2,pady=6).pack()
             

#======================close Button========================

         Button(update_window, text="Close", font=("Arial", 12), bg="red", fg="white",command=update_window.destroy,width=18).pack(pady=20)

#=====================Confirm Button========================    
    
         Button(update_window,text="Confirm",font=("Arial", 12),bg="green",fg="white",command=lambda: [messagebox.showinfo("Success", "Submit Successfully ✅"), update_window.destroy()],width=18).pack(pady=40)
    

    def find_doctor_window(self):
         self.find_doctor=Toplevel()  
         self.find_doctor.title("Find the Doctor")
         self.find_doctor.geometry("800x400")


         self.doctor_var = StringVar()
         
         self.tree = ttk.Treeview(self.find_doctor, columns=("Name", "Specialty", "Phone", "Day", "Time"), show="headings")
         self.tree.heading("Name", text="Name")
         self.tree.heading("Specialty", text="Specialty")
         self.tree.heading("Phone", text="Phone")
         self.tree.heading("Day", text="Day")
         self.tree.heading("Time", text="Time")

         doctors = [
         {"Name": "Dr. Liza", "Specialty": "Cat", "Phone": "123456", "Day": "Monday to Wednesday", "Time": "12:00 PM - 4:00 PM"},
         {"Name": "Dr. Narisha", "Specialty": "Bird", "Phone": "654321", "Day": "Thursday to Saturday", "Time": "10:00 AM - 6:00 PM"},
         {"Name": "Dr. Apsora", "Specialty": "Dog", "Phone": "987654", "Day": "Monday to Friday", "Time": "10:00 PM - 6:00 AM"},
         {"Name": "Dr. Amira", "Specialty": "Cat", "Phone": "456789", "Day": "Tuesday to Saturday", "Time": "8:00 AM - 5:00 PM"},
         {"Name": "Dr. Yash", "Specialty": "Medicine", "Phone": "321654", "Day": "Sunday to Wednesday", "Time": "6:00 AM - 3:00 PM"},
         {"Name": "Dr. Rafi", "Specialty": "Surgery", "Phone": "789123", "Day": "Thursday to Saturday", "Time": "3:00 PM - 12:00 AM"},
         ]

         for doc in doctors:
            self.tree.insert("", END, values=(doc["Name"], doc["Specialty"], doc["Phone"] ,doc["Day"], doc["Time"]))

         self.tree.pack(pady=20, fill=BOTH, expand=True)    

         Button(self.find_doctor, text="Select Doctor",bg="green",fg="white",font=("Calibri (Body)",13,"bold"), command=self.select_doctor).pack(pady=20)


        
        
    def select_doctor(self):

         selected = self.tree.selection()
         if not selected:
             messagebox.showerror("Error", "Please select a doctor!")
             return
         
         selection_id= selected[0]
         doctor_info = self.tree.item(selected, "values")
         self.doctor_var.set(doctor_info[0])  
         messagebox.showinfo("Doctor Selected", f"You have selected {doctor_info[0]} as your doctor.")
         self.find_doctor.destroy()