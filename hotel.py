from tkinter import *
from PIL import Image, ImageTk
from Customer import Cust_win
from room import Roombooking
from details import DetailsRoom

class HotelManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management Sys tem")
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

        details_btn=Button(btn_frame,command=self.room_details,text="DETAILS",width=20,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
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

    def room_details(self):
        self.new_window=Toplevel(self.root)
        self.app=DetailsRoom(self.new_window)


if __name__ == "__main__":
    root = Tk()
    obj = HotelManagementSystem(root)
    root.mainloop()
