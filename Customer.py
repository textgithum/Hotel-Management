from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import random

class Cust_win:
    def __init__(self, root):
        self.root = root
        self.root.title("Customer Details")
        self.root.geometry("1295x580+230+220")

#*************************** Variable*****************************
        self.var_ref = StringVar()
        x = random.randint(1000, 9999)
        self.var_ref.set(str(x))
        
        self.var_cust_name = StringVar()
        self.var_mother = StringVar()
        self.var_gender = StringVar()
        self.var_post = StringVar()
        self.var_mobile = StringVar()
        self.var_email = StringVar()
        self.var_nationality = StringVar()
        self.var_address = StringVar()
        self.var_id_proof = StringVar()
        self.var_id_number = StringVar()

#****************************** Title Label*********************************
        lbl_title = Label(root, text="ADD CUSTOMER DETAILS", font=("times new roman", 18, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=50)
#******************************logo********************************************
        img2 = Image.open("C:/Users/NIKKI/Desktop/image/logo.jpg")
        img2 = img2.resize((100, 40))  
        self.photo_image2 = ImageTk.PhotoImage(img2)

        lblimg2 = Label(root, image=self.photo_image2, bd=4, relief=RIDGE)
        lblimg2.place(x=5, y=2, width=100, height=40)

#****************************** Label Frame***********************************
        self.LabelFrameleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Customer Details", font=("times new roman", 12, "bold"), padx=2)
        self.LabelFrameleft.place(x=5, y=50, width=425, height=530)

#***************************** Label and Entry*********************************
        lbl_cust_ref = Label(self.LabelFrameleft, text="Customer Ref :", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_cust_ref.grid(row=0, column=0, sticky=W)

        enty_ref = ttk.Entry(self.LabelFrameleft, textvariable=self.var_ref, width=30, font=("times new roman", 13, "bold"), state="readonly")
        enty_ref.grid(row=0, column=1)

#****************************** Customer name********************************
        lbl_cname = Label(self.LabelFrameleft, text="Customer Name :", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_cname.grid(row=1, column=0, sticky=W)

        text_cname = ttk.Entry(self.LabelFrameleft, textvariable=self.var_cust_name, width=30, font=("times new roman", 13, "bold"))
        text_cname.grid(row=1, column=1)

#***************************** Mother name*********************************
        lbl_mname = Label(self.LabelFrameleft, text="Mother Name :", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_mname.grid(row=2, column=0, sticky=W)

        text_mname = ttk.Entry(self.LabelFrameleft, textvariable=self.var_mother, width=30, font=("times new roman", 13, "bold"))
        text_mname.grid(row=2, column=1)

#******************************* Gender***********************************
        lbl_gender = Label(self.LabelFrameleft, text="Gender :", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_gender.grid(row=3, column=0, sticky=W)

        combo_gender = ttk.Combobox(self.LabelFrameleft, textvariable=self.var_gender, font=("times new roman", 13, "bold"), width=27)
        combo_gender["value"] = ("Male", "Female", "Other")
        combo_gender.grid(row=3, column=1)

#****************************** Postcode**********************************
        lbl_postcode = Label(self.LabelFrameleft, text="PostCode :", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_postcode.grid(row=4, column=0, sticky=W)

        text_postcode = ttk.Entry(self.LabelFrameleft, textvariable=self.var_post, width=30, font=("times new roman", 13, "bold"))
        text_postcode.grid(row=4, column=1)

#****************************** mobilenumber******************************
        lbl_mobile = Label(self.LabelFrameleft, text="Mobile No :", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_mobile.grid(row=5, column=0, sticky=W)

        text_mobile = ttk.Entry(self.LabelFrameleft, textvariable=self.var_mobile, width=30, font=("times new roman", 13, "bold"))
        text_mobile.grid(row=5, column=1)

#******************************* email***********************************
        lbl_email = Label(self.LabelFrameleft, text="Email :", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_email.grid(row=6, column=0, sticky=W)

        text_email = ttk.Entry(self.LabelFrameleft, textvariable=self.var_email, width=30, font=("times new roman", 13, "bold"))
        text_email.grid(row=6, column=1)

#******************************* nationality*****************************
        lbl_naionality = Label(self.LabelFrameleft, text="Nationality :", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_naionality.grid(row=7, column=0, sticky=W)

        combo_naionality = ttk.Combobox(self.LabelFrameleft, textvariable=self.var_nationality, font=("times new roman", 13, "bold"), width=27)
        combo_naionality["value"] = ("Afghan", "Albanian", "Algerian", "American", "Andorran", "Angolan", "Anguillan", "Bolivian", "Belizeen", "Canadian", "chinese", "Danish", "Eritean", "French", "Greek", "Indian", "Japanese", "Lao", "Malian", "North Korean", "Pakistani", "Russian", "Spanish", "South Korean")
        combo_naionality.grid(row=7, column=1)

#*****************************idproof type combobox****************************
        lbl_id = Label(self.LabelFrameleft, text="Id Proof Type :", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_id.grid(row=8, column=0, sticky=W)

        combo_id = ttk.Combobox(self.LabelFrameleft, textvariable=self.var_id_proof, font=("times new roman", 13, "bold"), width=27)
        combo_id["value"] = ("Aadhaar Card", "Voter Id", "PAN Card", "Passport", "Driving License")
        combo_id.grid(row=8, column=1)

#*********************************** id number*******************************
        lbl_idnumber = Label(self.LabelFrameleft, text="Id Number :", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_idnumber.grid(row=9, column=0, sticky=W, padx=2)

        text_idnumber = ttk.Entry(self.LabelFrameleft, textvariable=self.var_id_number, width=30, font=("times new roman", 13, "bold"))
        text_idnumber.grid(row=9, column=1)

#**********************************address*************************************
        lbl_address = Label(self.LabelFrameleft, text="Address :", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_address.grid(row=10, column=0, sticky=W)

        text_address = ttk.Entry(self.LabelFrameleft, textvariable=self.var_address, width=30, font=("times new roman", 13, "bold"))
        text_address.grid(row=10, column=1)

#*********************************** btns**************************************
        btn_frame = Frame(self.LabelFrameleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=400, width=412, height=40)

        btnAdd = Button(btn_frame, text="Add", command=self.add_details, font=("times new roman", 13, "bold"), bg="black", fg="gold", width=9)
        btnAdd.grid(row=0, column=0, padx=1)

        btnUpdate = Button(btn_frame, text="Update",command=self.update, font=("times new roman", 13, "bold"), bg="black", fg="gold", width=9)
        btnUpdate.grid(row=0, column=1, padx=1)

        btnDelete = Button(btn_frame, text="Delete", command=self.delete,font=("times new roman", 13, "bold"), bg="black", fg="gold", width=9)
        btnDelete.grid(row=0, column=2, padx=1)

        btnReset = Button(btn_frame, text="Reset", command=self.reset,font=("times new roman", 13, "bold"), bg="black", fg="gold", width=9)
        btnReset.grid(row=0, column=3, padx=1)

#************************************* tabel frame************************************
        self.tabel_frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details And Search System", font=("times new roman", 12, "bold"), padx=2)
        self.tabel_frame.place(x=435, y=50, width=860, height=530)

        lbl_SearchBy = Label(self.tabel_frame, text="Search By", font=("times new roman", 12, "bold"), bg="red", fg="white")
        lbl_SearchBy.grid(row=0, column=0, sticky=W, padx=2)

        self.search_var=StringVar()

        combo_search = ttk.Combobox(self.tabel_frame, textvariable=self.search_var, font=("times new roman", 13, "bold"), width=24)
        combo_search["value"] = ("Mobile", "Ref")
        combo_search.grid(row=0, column=1, padx=2)

        self.text_search=StringVar()
        text_search = ttk.Entry(self.tabel_frame, textvariable=self.text_search, width=24, font=("times new roman", 13, "bold"))
        text_search.grid(row=0, column=2, padx=2)

        btn_search = Button(self.tabel_frame, text="Search", command=self.search, font=("times new roman", 13, "bold"), bg="black", fg="gold", width=9)
        btn_search.grid(row=0, column=3, padx=1)

        btn_show_all = Button(self.tabel_frame, command=self.fetch_details, text="Show All", font=("times new roman", 13, "bold"), bg="black", fg="gold", width=9)
        btn_show_all.grid(row=0, column=4, padx=1)

#**************************** show data tabel*******************************
        table_frame = Frame(self.tabel_frame, bd=2, relief=RIDGE)
        table_frame.place(x=0, y=50, width=860, height=350)

        scolll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scolll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.cust_details_table = ttk.Treeview(table_frame, columns=("ref", "name", "mother", "gender", "post", "mobile", "email", "nationality", "idproof", "idnumber", "address"), xscrollcommand=scolll_x.set, yscrollcommand=scolll_y.set)
        scolll_x.pack(side=BOTTOM, fill=X)
        scolll_y.pack(side=RIGHT, fill=Y)

        scolll_x.config(command=self.cust_details_table.xview)
        scolll_y.config(command=self.cust_details_table.yview)

        self.cust_details_table.heading("ref", text="Refer No")
        self.cust_details_table.heading("name", text="Name")
        self.cust_details_table.heading("mother", text="Mother")
        self.cust_details_table.heading("gender", text="Gender")
        self.cust_details_table.heading("post", text="Post")
        self.cust_details_table.heading("mobile", text="Mobile")
        self.cust_details_table.heading("email", text="Email")
        self.cust_details_table.heading("nationality", text="Nationality")
        self.cust_details_table.heading("idproof", text="Id Proof")
        self.cust_details_table.heading("idnumber", text="Id Number")
        self.cust_details_table.heading("address", text="Address")

        self.cust_details_table["show"] = "headings"

        self.cust_details_table.column("ref", width=100)
        self.cust_details_table.column("name", width=100)
        self.cust_details_table.column("mother", width=100)
        self.cust_details_table.column("gender", width=100)
        self.cust_details_table.column("post", width=100)
        self.cust_details_table.column("mobile", width=100)
        self.cust_details_table.column("email", width=100)
        self.cust_details_table.column("nationality", width=100)
        self.cust_details_table.column("idproof", width=100)
        self.cust_details_table.column("idnumber", width=100)
        self.cust_details_table.column("address", width=100)
        
        self.cust_details_table.pack(fill=BOTH, expand=1)
        self.cust_details_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_details()
#*********************************function call**************************************
    def add_details(self):
        if self.var_mobile.get() == "" or self.var_mother.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="1234", database="hotel_management")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into customer_details values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_ref.get(),
                    self.var_cust_name.get(),
                    self.var_mother.get(),
                    self.var_gender.get(),
                    self.var_post.get(),
                    self.var_mobile.get(),
                    self.var_email.get(),
                    self.var_nationality.get(),
                    self.var_id_proof.get(),
                    self.var_id_number.get(),
                    self.var_address.get(),
                ))

                conn.commit()
                self.fetch_details()
                conn.close()
                messagebox.showinfo("Success", "customer has been added", parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning", f"Some thing went wrong: {str(es)}", parent=self.root)

    def fetch_details(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="1234", database="hotel_management")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from customer_details")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.cust_details_table.delete(*self.cust_details_table.get_children())
            for row in rows:
                self.cust_details_table.insert("", END, values=row)
            conn.commit()
        conn.close()

    def get_cursor(self, events=""):
        cursor_row = self.cust_details_table.focus()
        content = self.cust_details_table.item(cursor_row)
        row = content["values"]

        self.var_ref.set(row[0])
        self.var_cust_name.set(row[1])
        self.var_mother.set(row[2])
        self.var_gender.set(row[3])
        self.var_post.set(row[4])
        self.var_mobile.set(row[5])
        self.var_email.set(row[6])
        self.var_nationality.set(row[7])
        self.var_id_proof.set(row[8])
        self.var_id_number.set(row[9])
        self.var_address.set(row[10])

    def update(self):
        if self.var_mobile.get() == "":
            messagebox.showerror("Error", "Please enter mobile number", parent=self.root)
        else:   
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="1234", database="hotel_management")
                my_cursor = conn.cursor()
                query = "UPDATE customer_details SET Name=%s, Mother=%s, Gender=%s, PostCode=%s, Mobile=%s, Email=%s, Nationality=%s, Idproof=%s, Idnumber=%s, Address=%s WHERE Ref=%s"
                data = (self.var_cust_name.get(), self.var_mother.get(), self.var_gender.get(), self.var_post.get(), self.var_mobile.get(), self.var_email.get(), self.var_nationality.get(), self.var_id_proof.get(), self.var_id_number.get(), self.var_address.get(), self.var_ref.get())
                my_cursor.execute(query, data)
                conn.commit()
                self.fetch_details()
                conn.close()
                messagebox.showinfo("Update", "Customer details have been updated successfully")
            except Exception as e:
                messagebox.showerror("Error", f"Error updating customer details: {str(e)}", parent=self.root)

    def delete(self):
        delete = messagebox.askyesno("Hotel Management System", "Do you want to delete this customer?", parent=self.root)
        if delete > 0:
            conn = mysql.connector.connect(host="localhost", username="root", password="1234", database="hotel_management")
            my_cursor = conn.cursor()
            query = "DELETE FROM customer_details WHERE Ref=%s"
            values = (self.var_ref.get(),)
            my_cursor.execute(query, values)
            conn.commit()
            self.fetch_details()
            conn.close()
        else:
            if not delete:
                return
            
    def reset(self):
        self.var_ref.set("")
        self.var_cust_name.set("")
        self.var_mother.set("")
        self.var_gender.set("")
        self.var_post.set("")
        self.var_mobile.set("")
        self.var_email.set("")
        self.var_nationality.set("")
        self.var_id_proof.set("")
        self.var_id_number.set("")
        self.var_address.set("")

    def search(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="1234", database="hotel_management")
        my_cursor = conn.cursor()

        my_cursor.execute("SELECT * FROM customer_details WHERE " + str(self.search_var.get()) + " LIKE '%" + str(self.text_search.get()) + "%'")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.cust_details_table.delete(*self.cust_details_table.get_children())
            for row in rows:
                self.cust_details_table.insert("", END, values=row)
            conn.commit()
        conn.close()

if __name__ == "__main__":
    root = Tk()
    obj = Cust_win(root)
    root.mainloop() 
