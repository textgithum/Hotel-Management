from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
from register import Register
from Customer import Cust_win
from room import Roombooking
from hotel import HotelManagementSystem


def main():
    win=Tk()
    app=Login_window(win)
    win.mainloop()


class Login_window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        img_path = "C:/Users/NIKKI/Desktop/image/build.jpg"
        img = Image.open(img_path)
        img = img.resize((1550, 800))
        self.photo_image = ImageTk.PhotoImage(img)

        self.var_email=StringVar()
        self.var_passward=StringVar() 

        lblimg = Label(root, image=self.photo_image, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=0, relwidth=1, relheight=1)

        frame = Frame(self.root, bg="white")
        frame.place(x=610, y=170, width=340, height=450)

        logo_path = r"C:\Users\NIKKI\Desktop\image\login.jpeg"
        img1 = Image.open(logo_path)
        img1 = img1.resize((100, 100))
        self.photo_image1 = ImageTk.PhotoImage(img1)

        lblimg1 = Label(frame, image=self.photo_image1, bg="white", borderwidth=0)
        lblimg1.place(x=120, y=0, width=100, height=100)

        get_str = Label(frame, text="Get Started", font=("times new roman", 20, "bold"), fg="black", bg="white")
        get_str.place(x=95, y=100)

        username = Label(frame, text="Username", font=("times new roman", 15, "bold"), fg="black", bg="white")
        username.place(x=70, y=155)

        self.txtuser = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txtuser.place(x=40, y=180, width=270)

        password = Label(frame, text="Password", font=("times new roman", 15, "bold"), fg="black", bg="white")
        password.place(x=70, y=225)

        self.txtpass = ttk.Entry(frame, font=("times new roman", 15, "bold"), show="*")
        self.txtpass.place(x=40, y=250, width=270)

        logo_2 = r"C:\Users\NIKKI\Desktop\image\login.jpeg"
        img2 = Image.open(logo_2)
        img2 = img2.resize((25, 25))
        self.photo_image2 = ImageTk.PhotoImage(img2)

        lblimg2 = Label(image=self.photo_image2, bg="white", borderwidth=0)
        lblimg2.place(x=650, y=323, width=25, height=25)

        logo_3 = r"C:\Users\NIKKI\Desktop\image\passward.png"
        img3 = Image.open(logo_3)
        img3 = img3.resize((25, 25))
        self.photo_image3 = ImageTk.PhotoImage(img3)

        lblimg3 = Label(image=self.photo_image3, bg="white", borderwidth=0)
        lblimg3.place(x=650, y=395, width=25, height=25)

        loginbtn = Button(frame, command=self.login,text="Login",  font=("times new roman", 15, "bold"), bd=3, relief=RIDGE, fg="White", bg="red", activeforeground="white", activebackground="red")
        loginbtn.place(x=110, y=300, width=120, height=35)

        registerbtn = Button(frame, command=self.rigister_window, text="New User Register", font=("times new roman", 12, "bold"), border=0, fg="black", bg="white", activeforeground="white", activebackground="white")
        registerbtn.place(x=10, y=350, width=160, height=35)

        forgetbtn = Button(frame,  text="Forget Password", font=("times new roman", 12, "bold"), border=0, fg="black", bg="white", activeforeground="white", activebackground="white")
        forgetbtn.place(x=7, y=390, width=160, height=35)
    
    def rigister_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window) 

    def login(self):
        username = self.txtuser.get()  # Consistent use of variables for getting username
        passward = self.txtpass.get()  # Fixed typo here from 'passward' to 'password'

        if not username or not passward:
            messagebox.showerror("Error", "All fields are required")
        elif username == "Nikki" and passward == "Priya":
            messagebox.showinfo("Success", "Welcome Nikki!")
        else:
            try:
                # Ensure these credentials are correct and appropriate for your MySQL setup
                conn = mysql.connector.connect(host="localhost", username="root", password="1234", database="hotel_management")
                my_cursor = conn.cursor()
                # Ensure your table and column names are correctly spelled here
                my_cursor.execute("SELECT * FROM register WHERE email = %s AND passward = %s", (username, passward))
                row = my_cursor.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Invalid username or password")
                else:
                    open_main = messagebox.askyesno("Yes & No", "Access only admin")
                    if open_main:
                        self.new_window = Toplevel(self.root)
                        self.app = HotelManagementSystem(self.new_window)
                    else:
                        return
            except mysql.connector.Error as e:
                messagebox.showerror("Database Error", str(e))
            finally:
                if conn is not None:
                    conn.close()



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

    class HotelManagementSystem:
        def __init__(self, root):
            self.root = root
            self.root.title("Hotel Management System")
            self.root.geometry("1600x800+0+0")

#******************************First Image****************************
            img1 = Image.open("C:/Users/NIKKI/Desktop/image/hotel.jpg")
            img1 = img1.resize((1600, 140))
            self.photo_image1 = ImageTk.PhotoImage(img1)

            lblimg1 = Label(root, image=self.photo_image1, bd=4, relief=RIDGE)
            lblimg1.place(x=0, y=0, width=1600, height=140)

    #*********************************logo********************************
            img2 = Image.open("C:/Users/NIKKI/Desktop/image/logo.jpg")
            img2 = img2.resize((230, 140))
            self.photo_image2 = ImageTk.PhotoImage(img2)

            lblimg2 = Label(root, image=self.photo_image2, bd=4, relief=RIDGE)
            lblimg2.place(x=0, y=0, width=230, height=140)

    #***************************Title Label********************************
            lbl_title = Label(root, text="HOTEL MANAGEMENT SYSTEM", font=("times new roman", 40, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
            lbl_title.place(x=0, y=140, width=1600, height=50)

    #***************************Main Frame**********************************
            main_frame = Frame(self.root, bd=4, relief=RIDGE)
            main_frame.place(x=0, y=190, width=1600, height=620)

    #****************************Menu Label*********************************
            lbl_menu=Label(main_frame,text="MENU",font=("times new roman",20,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
            lbl_menu.place(x=0,y=0,width=230)

    #*************************** Button Frame********************************
            btn_frame = Frame(main_frame, bd=4, relief=RIDGE)
            btn_frame.place(x=0, y=35, width=228, height=230)

    #***************************** Buttons*************************************
            cust_btn=Button(btn_frame,text="CUSTOMER",command=self.cust_details,width=20,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
            cust_btn.grid(row=0,column=0,pady=1)

            room_btn=Button(btn_frame,text="ROOM",command=self.room_booking,width=20,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
            room_btn.grid(row=1,column=0,pady=1)

            details_btn=Button(btn_frame,text="DETAILS",width=20,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
            details_btn.grid(row=2,column=0,pady=1)

            report_btn=Button(btn_frame,text="REPORT",width=20,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
            report_btn.grid(row=3,column=0,pady=1)

            logout_btn=Button(btn_frame,text="LOGOUT",width=20,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
            logout_btn.grid(row=4,column=0,pady=1)

    #**************************Right Side Image*****************************
            img3 = Image.open("C:/Users/NIKKI/Desktop/image/rest.jpg")
            img3 = img3.resize((1310, 600))
            self.photo_image3 = ImageTk.PhotoImage(img3)

            lblimg3 = Label(main_frame, image=self.photo_image3, bd=4, relief=RIDGE)
            lblimg3.place(x=225, y=0, width=1310, height=600)

    #******************** Down Image*************************************
            img4 = Image.open("C:/Users/NIKKI/Desktop/image/build.jpg")
            img4 = img4.resize((230, 210))
            self.photo_image4 = ImageTk.PhotoImage(img4)

            lblimg4 = Label(main_frame, image=self.photo_image4, bd=4, relief=RIDGE)
            lblimg4.place(x=0, y=260, width=230, height=190)

            img5 = Image.open("C:/Users/NIKKI/Desktop/image/food.jpg")
            img5 = img5.resize((230, 190))
            self.photo_image5 = ImageTk.PhotoImage(img5)

            lblimg5 = Label(main_frame, image=self.photo_image5, bd=4, relief=RIDGE)
            lblimg5.place(x=0, y=450, width=230, height=170)

        def cust_details(self):
            self.new_window=Toplevel(self.root)
            self.app=Cust_win(self.new_window)

        def room_booking(self):
            self.new_window=Toplevel(self.root)
            self.app=Roombooking(self.new_window)


    
    
    

if __name__ == "__main__":
    main()