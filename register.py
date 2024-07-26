from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector


class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")

        #***************varibles
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_security_q=StringVar()
        self.var_securityA=StringVar()
        self.var_passward=StringVar()
        self.var_confpass=StringVar()
        self.var_checkbtn=IntVar()


        # bg image
        img_path = r"C:\Users\NIKKI\Desktop\image\reg1.jpg"
        img = Image.open(img_path)
        img = img.resize((1600, 900))
        self.photo_image = ImageTk.PhotoImage(img)

        lblimg = Label(root, image=self.photo_image, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=0, relwidth=1, relheight=1)

        # left image
        img_path1 = r"C:\Users\NIKKI\Desktop\image\reg1.jpg"
        img1 = Image.open(img_path1)
        img1 = img1.resize((470, 550))
        self.photo_image1 = ImageTk.PhotoImage(img1)

        lblimg1 = Label(root, image=self.photo_image1, bd=4, relief=RIDGE)
        lblimg1.place(x=100, y=100, width=470, height=550)

        # main frame
        frame = Frame(self.root, bg="white")
        frame.place(x=570, y=100, width=800, height=550)

        register_lbl = Label(frame, text="REGISTER HERE", font=("times new roman", 20, "bold"), fg="darkgreen",
                             bg="white")
        register_lbl.place(x=20, y=20)

        # label and entry
        # *****************row1
        fname = Label(frame, text="First Name", font=("times new roman", 15, "bold"), bg="white")
        fname.place(x=50, y=100)

        fname_entry = ttk.Entry(frame, textvariable=self.var_fname,font=("time new roman", 15, "bold"))
        fname_entry.place(x=50, y=130, width=250)

        l_name = Label(frame, text="Last Name", font=("times new roman", 15, "bold"), bg="white")
        l_name.place(x=370, y=100)

        l_name_entry = ttk.Entry(frame,textvariable=self.var_lname, font=("time new roman", 15, "bold"))
        l_name_entry.place(x=370, y=130, width=250)

        # ***********row2
        contact = Label(frame, text="Contact No", font=("times new roman", 15, "bold"), bg="white")
        contact.place(x=50, y=170)

        self.txt_contact = ttk.Entry(frame,textvariable=self.var_contact, font=("time new roman", 15, "bold"))
        self.txt_contact.place(x=50, y=200, width=250)

        email = Label(frame, text="Email", font=("times new roman", 15, "bold"), bg="white")
        email.place(x=370, y=170)

        self.txt_email = ttk.Entry(frame,textvariable=self.var_email,font=("time new roman", 15, "bold"))
        self.txt_email.place(x=370, y=200, width=250)

        # **************row3
        security_q = Label(frame, text="Select Security Question", font=("times new roman", 15, "bold"), bg="white")
        security_q.place(x=50, y=240)

        self.combo_security_q = ttk.Combobox(frame, textvariable=self.var_security_q,font=("time new roman", 15, "bold"), state="readonly")
        self.combo_security_q["values"] = ("Select","Your Birth Place", "Your Pet Name", "Your best Place")
        self.combo_security_q.place(x=50, y=270, width=250)

        security = Label(frame, text="Security Answer", font=("times new roman", 15, "bold"), bg="white")
        security.place(x=370, y=240)

        self.txt_security = ttk.Entry(frame,textvariable=self.var_securityA, font=("time new roman", 15, "bold"))
        self.txt_security.place(x=370, y=270, width=250)

        # ************row4
        pswd = Label(frame, text="Password", font=("times new roman", 15, "bold"), bg="white")
        pswd.place(x=50, y=310)

        self.txt_pswd = ttk.Entry(frame,textvariable=self.var_passward, font=("time new roman", 15, "bold"), show="*")
        self.txt_pswd.place(x=50, y=340, width=250)

        confirm_pswd = Label(frame, text="Confirm Password", font=("times new roman", 15, "bold"), bg="white")
        confirm_pswd.place(x=370, y=310)

        self.txt_confirm_pswd = ttk.Entry(frame, textvariable=self.var_confpass,font=("time new roman", 15, "bold"), show="*")
        self.txt_confirm_pswd.place(x=370, y=340, width=250)

        # ******************check button
        Checkbtn = Checkbutton(frame, variable=self.var_checkbtn,text="I Agree The Terms & Condition", font=("time new roman", 12, "bold"),
                                onvalue=1, offvalue=0)
        Checkbtn.place(x=50, y=380)

        # btns
        img2 = Image.open(r"C:\Users\NIKKI\Desktop\image\rg1.jpeg")
        img2 = img2.resize((200, 50))
        self.photoimage2 = ImageTk.PhotoImage(img2)
        b1 = Button(frame,command=self.register_details, image=self.photoimage2, borderwidth=0, cursor="hand2", font=("time new roman", 15, "bold"))
        b1.place(x=50, y=420, width=200)

        img3 = Image.open(r"c:\Users\NIKKI\Desktop\image\Login-Now-Button.png")
        img3 = img3.resize((200, 50))
        self.photoimage3 = ImageTk.PhotoImage(img3)
        b2 = Button(frame, image=self.photoimage3, borderwidth=0, cursor="hand2", font=("time new roman", 15, "bold"))
        b2.place(x=370, y=420, width=200)

    




    #****************function
    def register_details(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_security_q.get()=="Select":
            messagebox.showerror("Error","All field are required")
        elif self.var_passward.get()!=self.var_confpass.get():
            messagebox.showerror("Error","Pleasen agree our terms and condition")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="1234", database="hotel_management")
            my_cursor = conn.cursor()
            query=("select*from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exist,please try another email")
            else:
                my_cursor.execute("INSERT INTO register (fname, lname, contact, email, security_q, securityA, passward) VALUES (%s, %s, %s, %s, %s, %s, %s)", (
                        self.var_fname.get(),
                        self.var_lname.get(),
                        self.var_contact.get(),
                        self.var_email.get(),
                        self.var_security_q.get(),
                        self.var_securityA.get(),
                        self.var_passward.get(),
                       
                    ))


                conn.commit()
                conn.close()
                messagebox.showinfo("Success","Register Successfully")


            
    

if __name__ == "__main__":
    root = Tk()
    app = Register(root)
    root.mainloop()

