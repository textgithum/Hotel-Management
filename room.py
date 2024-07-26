from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import random
from time import strftime
from datetime import datetime

class Roombooking:
    def __init__(self, root):
        self.root = root
        self.root.title("Room Details")
        self.root.geometry("1295x580+230+220")

        # ********************** variable**************************
        self.var_contact = StringVar()
        self.var_checkin = StringVar()
        self.var_checkout = StringVar()
        self.var_roomtype = StringVar()
        self.var_roomavailable = StringVar()
        self.var_noofdays = StringVar()
        self.var_paidtax = StringVar()
        self.var_actualtotal = StringVar()
        self.var_total = StringVar()
        self.var_meal = StringVar()

        # ************************* Title Label*********************************
        lbl_title = Label(root, text="ROOMBOOKING", font=("times new roman", 18, "bold"), bg="black", fg="gold", bd=4,
                          relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=50)

        # *************************** Logo***************************************
        img2 = Image.open("C:/Users/NIKKI/Desktop/image/logo.jpg")
        img2 = img2.resize((100, 40))
        self.photo_image2 = ImageTk.PhotoImage(img2)
        lblimg2 = Label(root, image=self.photo_image2, bd=4, relief=RIDGE)
        lblimg2.place(x=5, y=2, width=100, height=40)

        # ******************************* Label Frame**********************************
        self.LabelFrameleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Roombooking Details",
                                         font=("times new roman", 12, "bold"), padx=2)
        self.LabelFrameleft.place(x=5, y=50, width=425, height=530)

        # ***************************** Label and Entry******************************
        # *********************** Customer contact*****************************
        lbl_contact = Label(self.LabelFrameleft, text="Customer Contact :", font=("times new roman", 12, "bold"),
                            padx=2, pady=6)
        lbl_contact.grid(row=0, column=0, sticky=W)

        Text_contact = ttk.Entry(self.LabelFrameleft, textvariable=self.var_contact, width=22,
                                 font=("times new roman", 13, "bold"), )
        Text_contact.grid(row=0, column=1, sticky=W)

        # ********************** Fetch data button****************************
        btnFetchData = Button(self.LabelFrameleft, command=self.Fetch_data, text="Fetch Data",
                              font=("times new roman", 8, "bold"), bg="black", fg="gold", width=8)
        btnFetchData.place(x=350, y=6)

        # ********************** Check_in*************************************
        lbl_in = Label(self.LabelFrameleft, text="Check_In Date :", font=("times new roman", 12, "bold"), padx=2,
                       pady=6)
        lbl_in.grid(row=1, column=0, sticky=W)

        Text_in = ttk.Entry(self.LabelFrameleft, textvariable=self.var_checkin, width=30,
                            font=("times new roman", 13, "bold"))
        Text_in.grid(row=1, column=1)

        # ********************** Check_out**********************************
        lbl_out = Label(self.LabelFrameleft, text="Check_Out Date :", font=("times new roman", 12, "bold"), padx=2,
                        pady=6)
        lbl_out.grid(row=2, column=0, sticky=W)

        Text_out = ttk.Entry(self.LabelFrameleft, textvariable=self.var_checkout, width=30,
                             font=("times new roman", 13, "bold"))
        Text_out.grid(row=2, column=1)

        # *************************** Room Type*****************************
        lbl_type = Label(self.LabelFrameleft, text="Room Type :", font=("times new roman", 12, "bold"), padx=2,
                         pady=6)
        lbl_type.grid(row=3, column=0, sticky=W)

        conn = mysql.connector.connect(host="localhost", username="root", password="1234", database="hotel_management")
        my_cursor = conn.cursor()
        my_cursor.execute("select roomType from details")
        ide = my_cursor.fetchall()

        combo_type = ttk.Combobox(self.LabelFrameleft, textvariable=self.var_roomtype,
                                  font=("times new roman", 13, "bold"), width=27)
        combo_type["value"] = ide
        combo_type.grid(row=3, column=1)

        # *****************************Available Room************************
        lbl_room = Label(self.LabelFrameleft, text="Available Room :", font=("times new roman", 12, "bold"), padx=2,
                         pady=6)
        lbl_room.grid(row=4, column=0, sticky=W)

        #Text_room = ttk.Entry(self.LabelFrameleft, textvariable=self.var_roomavailable, width=30,
         #                     font=("times new roman", 13, "bold"))
        #Text_room.grid(row=4, column=1)
        conn = mysql.connector.connect(host="localhost", username="root", password="1234", database="hotel_management")
        my_cursor = conn.cursor()
        my_cursor.execute("select roomNo from details")
        rows = my_cursor.fetchall()

        combo_roomNo = ttk.Combobox(self.LabelFrameleft, textvariable=self.var_roomavailable,
                                  font=("times new roman", 13, "bold"), width=27)
        combo_roomNo["value"] = rows
        combo_roomNo.grid(row=4, column=1)


        # ******************************* Meal********************************
        lbl_meal = Label(self.LabelFrameleft, text="Meal :", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_meal.grid(row=5, column=0, sticky=W)

        Text_meal = ttk.Entry(self.LabelFrameleft, textvariable=self.var_meal, width=30,
                              font=("times new roman", 13, "bold"))
        Text_meal.grid(row=5, column=1)

        # **************************** No of Days****************************
        lbl_NoOfDays = Label(self.LabelFrameleft, text="No Of Days :", font=("times new roman", 12, "bold"), padx=2,
                             pady=6)
        lbl_NoOfDays.grid(row=6, column=0, sticky=W)

        Text_NoOfDays = ttk.Entry(self.LabelFrameleft, textvariable=self.var_noofdays, width=30,
                                   font=("times new roman", 13, "bold"))
        Text_NoOfDays.grid(row=6, column=1)

        # **************************** Paid tax******************************
        lbl_paid = Label(self.LabelFrameleft, text="Paid Tax :", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_paid.grid(row=7, column=0, sticky=W)

        Text_paid = ttk.Entry(self.LabelFrameleft, textvariable=self.var_paidtax, width=30,
                              font=("times new roman", 13, "bold"))
        Text_paid.grid(row=7, column=1)

        # *****************************Sub total*****************************
        lbl_sub = Label(self.LabelFrameleft, text="Sub Total :", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_sub.grid(row=8, column=0, sticky=W)

        Text_sub = ttk.Entry(self.LabelFrameleft, textvariable=self.var_actualtotal, width=30,
                             font=("times new roman", 13, "bold"))
        Text_sub.grid(row=8, column=1)

        # *****************************Total Cost***************************
        lbl_Idnumber = Label(self.LabelFrameleft, text="Total Cost :", font=("times new roman", 12, "bold"), padx=2,
                             pady=6)
        lbl_Idnumber.grid(row=9, column=0, sticky=W)

        Text_Idnumber = ttk.Entry(self.LabelFrameleft, textvariable=self.var_total, width=30,
                                   font=("times new roman", 13, "bold"))
        Text_Idnumber.grid(row=9, column=1)

        # ******************************Bill button***************************
        btnBill = Button(self.LabelFrameleft, command=self.total,text="Bill", font=("times new roman", 13, "bold"), bg="black",
                         fg="gold", width=9)
        btnBill.grid(row=10, column=0, padx=1, sticky=W)

        # ******************************Buttons******************************
        btn_frame = Frame(self.LabelFrameleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=400, width=412, height=40)

        btnAdd = Button(btn_frame, text="Add", command=self.add_details, font=("times new roman", 13, "bold"),
                        bg="black", fg="gold", width=9)
        btnAdd.grid(row=0, column=0, padx=1)

        btnUpdate = Button(btn_frame, command=self.update,text="Update", font=("times new roman", 13, "bold"), bg="black", fg="gold",
                           width=9)
        btnUpdate.grid(row=0, column=1, padx=1)

        btnDelete = Button(btn_frame, command=self.delete,text="Delete", font=("times new roman", 13, "bold"), bg="black", fg="gold",
                           width=9)
        btnDelete.grid(row=0, column=2, padx=1)

        btnReset = Button(btn_frame,command=self.reset, text="Reset", font=("times new roman", 13, "bold"), bg="black", fg="gold",
                          width=9)
        btnReset.grid(row=0, column=3, padx=1)

        # ****************************Rightside image*******************************
        img3 = Image.open("C:/Users/NIKKI/Desktop/image/room.jpg")
        img3 = img3.resize((546, 300))
        self.photo_image3 = ImageTk.PhotoImage(img3)
        lblimg3 = Label(root, image=self.photo_image3, bd=4, relief=RIDGE)
        lblimg3.place(x=750, y=55, width=546, height=300)

        # **************************Table frame search system*************************
        self.tabel_frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details And Search System",
                                      font=("times new roman", 12, "bold"), padx=2)
        self.tabel_frame.place(x=435, y=340, width=860, height=240)

        lbl_SearchBy = Label(self.tabel_frame, text="Search By", font=("times new roman", 12, "bold"), bg="red",
                             fg="white")
        lbl_SearchBy.grid(row=0, column=0, sticky=W, padx=2)

        self.search_var = StringVar()

        combo_search = ttk.Combobox(self.tabel_frame, textvariable=self.search_var,
                                    font=("times new roman", 13, "bold"), width=24)
        combo_search["value"] = ("Contact", "Room")
        combo_search.grid(row=0, column=1, padx=2)

        self.text_search = StringVar()
        text_search = ttk.Entry(self.tabel_frame, textvariable=self.text_search, width=24,
                                font=("times new roman", 13, "bold"))
        text_search.grid(row=0, column=2, padx=2)

        btn_search = Button(self.tabel_frame, command=self.search,text="Search", font=("times new roman", 13, "bold"), bg="black",
                            fg="gold", width=9)
        btn_search.grid(row=0, column=3, padx=1)

        btn_show_all = Button(self.tabel_frame, command=self.fetch_details,text="Show All", font=("times new roman", 13, "bold"), bg="black",
                              fg="gold", width=9)
        btn_show_all.grid(row=0, column=4, padx=1)

        # ***************************Show data table*********************************
        table_frame = Frame(self.tabel_frame, bd=2, relief=RIDGE)
        table_frame.place(x=0, y=50, width=860, height=180)

        scolll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scolll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.room_table = ttk.Treeview(table_frame,
                                       columns=("Contact", "Checkin", "Checkout", "RoomType", "RoomAvailable",
                                                "Meal", "NoOfDays"), xscrollcommand=scolll_x.set, yscrollcommand=scolll_y.set)
        scolll_x.pack(side=BOTTOM, fill=X)
        scolll_y.pack(side=RIGHT, fill=Y)

        scolll_x.config(command=self.room_table.xview)
        scolll_y.config(command=self.room_table.yview)

        self.room_table.heading("Contact", text="Contact")
        self.room_table.heading("Checkin", text="Check In")
        self.room_table.heading("Checkout", text="Check Out")
        self.room_table.heading("RoomType", text="Room Type")
        self.room_table.heading("RoomAvailable", text="Room Available")
        self.room_table.heading("Meal", text="Meal")
        self.room_table.heading("NoOfDays", text="No Of Days")

        self.room_table["show"] = "headings"

        self.room_table.column("Contact", width=100)
        self.room_table.column("Checkin", width=100)
        self.room_table.column("Checkout", width=100)
        self.room_table.column("RoomType", width=100)
        self.room_table.column("RoomAvailable", width=100)
        self.room_table.column("Meal", width=100)
        self.room_table.column("NoOfDays", width=100)
        self.room_table.bind("<ButtonRelease>",self.get_cursor)


        self.room_table.pack(fill=BOTH, expand=1)
        self.fetch_details()
    def add_details(self):
        if self.var_contact.get() == "" or self.var_checkin.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="1234", database="hotel_management")
                my_cursor = conn.cursor()
                my_cursor.execute("INSERT INTO room VALUES (%s, %s, %s, %s, %s, %s, %s)", (
                    self.var_contact.get(),
                    self.var_checkin.get(),
                    self.var_checkout.get(),
                    self.var_roomtype.get(),
                    self.var_roomavailable.get(),
                    self.var_meal.get(),
                    self.var_noofdays.get(),
                ))
                conn.commit()
                self.fetch_details
                messagebox.showinfo("Success", "Customer has been added", parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)
            finally:
                if conn.is_connected():
                    conn.close()


       
    def get_cursor(self, events=""):
        cursor_row = self.room_table.focus()
        content = self.room_table.item(cursor_row)
        row = content["values"]

        self.var_contact.set(row[0])
        self.var_checkin.set(row[1])
        self.var_checkout.set(row[2])
        self.var_roomtype.set(row[3])
        self.var_roomavailable.set(row[4])
        self.var_meal.set(row[5])
        self.var_noofdays.set(row[6])

     #update function   
    def update(self):
            if self.var_contact.get() == "":
                messagebox.showerror("Error", "Please enter mobile number", parent=self.root)
            else:   
                try:
                    conn = mysql.connector.connect(host="localhost", username="root", password="1234", database="hotel_management")
                    my_cursor = conn.cursor()
                    query = "UPDATE room SET  checkin=%s, checkout=%s, roomtype=%s, roomavailable=%s, meal=%s, noofdays=%s, WHERE self.var_contact.get(), "
                    data = (self.var_checkin.get(), self.var_checkout.get(), self.var_roomtype.get(), self.var_roomavailable.get(), self.var_meal.get(), self.var_noofdays.get(), self.var_contact.get(), )
                    my_cursor.execute(query, data)
                    conn.commit()
                    self.fetch_details()
                    conn.close()
                    messagebox.showinfo("Update", "Room details have been updated successfully")
                except Exception as e:
                    messagebox.showerror("Error", f"Error updating customer details: {str(e)}", parent=self.root)
    def delete(self):
        delete = messagebox.askyesno("Hotel Management System", "Do you want to delete this customer?", parent=self.root)
        if delete > 0:
            conn = mysql.connector.connect(host="localhost", username="root", password="1234", database="hotel_management")
            my_cursor = conn.cursor()
            query = "DELETE FROM room WHERE contact=%s"
            values = (self.var_contact.get(),)
            my_cursor.execute(query, values)
            conn.commit()
            self.fetch_details()
            conn.close()
        else:
            if not delete:
                return
            

    def reset(self):
        self.var_contact.set("")
        self.var_checkin.set("")
        self.var_checkout.set("")
        self.var_roomtype.set("")
        self.var_roomavailable.set("")
        self.var_meal.set("")
        self.var_noofdays.set("")



    def fetch_details(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="1234", database="hotel_management")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from room")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.room_table.delete(*self.room_table.get_children())
            for row in rows:
                self.room_table.insert("", END, values=row)
            conn.commit()
        conn.close()
    
    
    def Fetch_data(self):
        if self.var_contact.get() == "":
            messagebox.showerror("Error", "Please Enter Contact Number", parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="1234",
                                           database="hotel_management")
            my_cursor = conn.cursor()
            query = ("select Name, Gender, Email, Nationality, Address from customer_details where Mobile=%s")
            value = (self.var_contact.get(),)
            my_cursor.execute(query, value)
            rows = my_cursor.fetchone()

            if rows is None:
                messagebox.showerror("Error", "This Number Not Found", parent=self.root)
            else:
                conn.close()

                showDataframe = Frame(self.root, bd=4, relief=RIDGE, padx=2)
                showDataframe.place(x=450, y=55, width=300, height=180)

                labels = ["Name", "Gender", "Email", "Nationality", "Address"]

                for i, label_text in enumerate(labels):
                    label = Label(showDataframe, text=f"{label_text}:", font=("time new roman", 12, "bold"))
                    label.place(x=0, y=i * 30)

                    value_label = Label(showDataframe, text=rows[i], font=("time new roman", 12, "bold"))
                    value_label.place(x=90, y=i * 30)

    #search system
    def search(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="1234", database="hotel_management")
        my_cursor = conn.cursor()

        my_cursor.execute("SELECT * FROM room WHERE " + str(self.search_var.get()) + " LIKE '%" + str(self.text_search.get()) + "%'")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.room_table.delete(*self.room_table.get_children())
            for row in rows:
                self.room_table.insert("", END, values=row)
            conn.commit()
        conn.close()

    def total(self):
        inDate=self.var_checkin.get()
        outDate=self.var_checkout.get()
        inDate=datetime.strptime(inDate,"%d/%m/%Y")
        outDate=datetime.strptime(outDate,"%d/%m/%Y")
        self.var_noofdays.set(abs(outDate-inDate).days)

        if (self.var_meal.get() == "Breakfast" and self.var_roomtype.get() == "Single"):
            q1 = float(300)  # Cost for the meal
            q2 = float(700)  # Cost for the room
            q3 = float(self.var_noofdays.get())  # Number of days

            q4 = q1 + q2  # Total cost for meal and room per day
            q5 = q3 * q4  # Total cost for all days

            tax_rate = 0.09  # 9% tax
            tax_amount = q5 * tax_rate  # Tax calculated on the total amount
            total_with_tax = q5 + tax_amount  # Total amount including tax

            # Format output as currency
            Tax = "Rs. " + "%.2f" % tax_amount
            ST = "Rs. " + "%.2f" % q5
            TT = "Rs. " + "%.2f" % total_with_tax

            # Set the outputs to the respective variables
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)
        elif (self.var_meal.get() == "Lunch" and self.var_roomtype.get() == "Single"):
            q1 = float(400)  # Cost for the meal
            q2 = float(700)  # Cost for the room
            q3 = float(self.var_noofdays.get())  # Number of days

            q4 = q1 + q2  # Total cost for meal and room per day
            q5 = q3 * q4  # Total cost for all days

            tax_rate = 0.09  # 9% tax
            tax_amount = q5 * tax_rate  # Tax calculated on the total amount
            total_with_tax = q5 + tax_amount  # Total amount including tax

            # Format output as currency
            Tax = "Rs. " + "%.2f" % tax_amount
            ST = "Rs. " + "%.2f" % q5
            TT = "Rs. " + "%.2f" % total_with_tax

            # Set the outputs to the respective variables
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)
        
        elif (self.var_meal.get() == "Dinner" and self.var_roomtype.get() == "Single"):
            q1 = float(450)  # Cost for the meal
            q2 = float(700)  # Cost for the room
            q3 = float(self.var_noofdays.get())  # Number of days

            q4 = q1 + q2  # Total cost for meal and room per day
            q5 = q3 * q4  # Total cost for all days

            tax_rate = 0.09  # 9% tax
            tax_amount = q5 * tax_rate  # Tax calculated on the total amount
            total_with_tax = q5 + tax_amount  # Total amount including tax

            # Format output as currency
            Tax = "Rs. " + "%.2f" % tax_amount
            ST = "Rs. " + "%.2f" % q5
            TT = "Rs. " + "%.2f" % total_with_tax

            # Set the outputs to the respective variables
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get() == "Breakfast" and self.var_roomtype.get() == "Double"):
            q1 = float(300)  # Cost for the meal
            q2 = float(1000)  # Cost for the room
            q3 = float(self.var_noofdays.get())  # Number of days

            q4 = q1 + q2  # Total cost for meal and room per day
            q5 = q3 * q4  # Total cost for all days

            tax_rate = 0.09  # 9% tax
            tax_amount = q5 * tax_rate  # Tax calculated on the total amount
            total_with_tax = q5 + tax_amount  # Total amount including tax

            # Format output as currency
            Tax = "Rs. " + "%.2f" % tax_amount
            ST = "Rs. " + "%.2f" % q5
            TT = "Rs. " + "%.2f" % total_with_tax

            # Set the outputs to the respective variables
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get() == "Lunch" and self.var_roomtype.get() == "Double"):
            q1 = float(400)  # Cost for the meal
            q2 = float(1000)  # Cost for the room
            q3 = float(self.var_noofdays.get())  # Number of days

            q4 = q1 + q2  # Total cost for meal and room per day
            q5 = q3 * q4  # Total cost for all days

            tax_rate = 0.09  # 9% tax
            tax_amount = q5 * tax_rate  # Tax calculated on the total amount
            total_with_tax = q5 + tax_amount  # Total amount including tax

            # Format output as currency
            Tax = "Rs. " + "%.2f" % tax_amount
            ST = "Rs. " + "%.2f" % q5
            TT = "Rs. " + "%.2f" % total_with_tax

            # Set the outputs to the respective variables
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get() == "Dinner" and self.var_roomtype.get() == "Double"):
            q1 = float(450)  # Cost for the meal
            q2 = float(1000)  # Cost for the room
            q3 = float(self.var_noofdays.get())  # Number of days

            q4 = q1 + q2  # Total cost for meal and room per day
            q5 = q3 * q4  # Total cost for all days

            tax_rate = 0.09  # 9% tax
            tax_amount = q5 * tax_rate  # Tax calculated on the total amount
            total_with_tax = q5 + tax_amount  # Total amount including tax

            # Format output as currency
            Tax = "Rs. " + "%.2f" % tax_amount
            ST = "Rs. " + "%.2f" % q5
            TT = "Rs. " + "%.2f" % total_with_tax

            # Set the outputs to the respective variables
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get() == "Breakfast" and self.var_roomtype.get() == "Luxury"):
            q1 = float(300)  # Cost for the meal
            q2 = float(1200)  # Cost for the room
            q3 = float(self.var_noofdays.get())  # Number of days

            q4 = q1 + q2  # Total cost for meal and room per day
            q5 = q3 * q4  # Total cost for all days

            tax_rate = 0.09  # 9% tax
            tax_amount = q5 * tax_rate  # Tax calculated on the total amount
            total_with_tax = q5 + tax_amount  # Total amount including tax

            # Format output as currency
            Tax = "Rs. " + "%.2f" % tax_amount
            ST = "Rs. " + "%.2f" % q5
            TT = "Rs. " + "%.2f" % total_with_tax

            # Set the outputs to the respective variables
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get() == "Lunch" and self.var_roomtype.get() == "Luxury"):
            q1 = float(400)  # Cost for the meal
            q2 = float(1200)  # Cost for the room
            q3 = float(self.var_noofdays.get())  # Number of days

            q4 = q1 + q2  # Total cost for meal and room per day
            q5 = q3 * q4  # Total cost for all days

            tax_rate = 0.09  # 9% tax
            tax_amount = q5 * tax_rate  # Tax calculated on the total amount
            total_with_tax = q5 + tax_amount  # Total amount including tax

            # Format output as currency
            Tax = "Rs. " + "%.2f" % tax_amount
            ST = "Rs. " + "%.2f" % q5
            TT = "Rs. " + "%.2f" % total_with_tax

            # Set the outputs to the respective variables
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get() == "Dinner" and self.var_roomtype.get() == "Luxury"):
            q1 = float(450)  # Cost for the meal
            q2 = float(1200)  # Cost for the room
            q3 = float(self.var_noofdays.get())  # Number of days

            q4 = q1 + q2  # Total cost for meal and room per day
            q5 = q3 * q4  # Total cost for all days

            tax_rate = 0.09  # 9% tax
            tax_amount = q5 * tax_rate  # Tax calculated on the total amount
            total_with_tax = q5 + tax_amount  # Total amount including tax

            # Format output as currency
            Tax = "Rs. " + "%.2f" % tax_amount
            ST = "Rs. " + "%.2f" % q5
            TT = "Rs. " + "%.2f" % total_with_tax

            # Set the outputs to the respective variables
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)














        








if __name__ == "__main__":
    root = Tk()
    obj = Roombooking(root)
    root.mainloop()
