from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox

class DetailsRoom:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x580+230+220")

        # Title Label
        lbl_title = Label(root, text="ROOM BOOKING", font=("times new roman", 18, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=50)

        # Logo
        img2 = Image.open("C:/Users/NIKKI/Desktop/image/logo.jpg")
        img2 = img2.resize((100, 40), Image.LANCZOS)
        self.photo_image2 = ImageTk.PhotoImage(img2)
        lblimg2 = Label(root, image=self.photo_image2, bd=4, relief=RIDGE)
        lblimg2.place(x=5, y=2, width=100, height=40)

        # Left Label Frame
        LabelFrameLeft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Room Details", font=("times new roman", 12, "bold"), padx=2)
        LabelFrameLeft.place(x=5, y=50, width=540, height=350)

        # Floor
        lbl_floor = Label(LabelFrameLeft, text="Floor", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_floor.grid(row=0, column=0, sticky=W, padx=20)
        self.var_floor = StringVar()
        entry_floor = ttk.Entry(LabelFrameLeft, textvariable=self.var_floor, width=22, font=("times new roman", 13, "bold"))
        entry_floor.grid(row=0, column=1, sticky=W)

        # Room No
        lbl_RoomNo = Label(LabelFrameLeft, text="Room No", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_RoomNo.grid(row=1, column=0, sticky=W, padx=20)
        self.var_roomNo = StringVar()
        entry_RoomNo = ttk.Entry(LabelFrameLeft, textvariable=self.var_roomNo, width=22, font=("times new roman", 13, "bold"))
        entry_RoomNo.grid(row=1, column=1, sticky=W)

        # Room Type
        lbl_RoomType = Label(LabelFrameLeft, text="Room Type", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_RoomType.grid(row=2, column=0, sticky=W, padx=20)
        self.var_roomType = StringVar()
        entry_RoomType = ttk.Entry(LabelFrameLeft, textvariable=self.var_roomType, width=22, font=("times new roman", 13, "bold"))
        entry_RoomType.grid(row=2, column=1, sticky=W)

        # Buttons Frame
        btn_frame = Frame(LabelFrameLeft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=250, width=500, height=40)

        btnAdd = Button(btn_frame, text="Add", command=self.add_details, font=("times new roman", 13, "bold"), bg="black", fg="gold", width=11)
        btnAdd.grid(row=0, column=0, padx=1)

        btnUpdate = Button(btn_frame, text="Update", command=self.update, font=("times new roman", 13, "bold"), bg="black", fg="gold", width=11)
        btnUpdate.grid(row=0, column=1, padx=1)

        btnDelete = Button(btn_frame, text="Delete", command=self.delete, font=("times new roman", 13, "bold"), bg="black", fg="gold", width=11)
        btnDelete.grid(row=0, column=2, padx=1)

        btnReset = Button(btn_frame, text="Reset", command=self.reset, font=("times new roman", 13, "bold"), bg="black", fg="gold", width=12)
        btnReset.grid(row=0, column=3, padx=1)

        # Right Side Frame
        LabelFrameRight = LabelFrame(self.root, bd=2, relief=RIDGE, text="Show Room Details", font=("times new roman", 12, "bold"), padx=2)
        LabelFrameRight.place(x=600, y=55, width=600, height=350)

        scroll_x = ttk.Scrollbar(LabelFrameRight, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(LabelFrameRight, orient=VERTICAL)

        self.room_table = ttk.Treeview(LabelFrameRight, columns=("floor", "roomno", "roomType"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("floor", text="Floor")
        self.room_table.heading("roomno", text="Room No")
        self.room_table.heading("roomType", text="Room Type")

        self.room_table['show'] = 'headings'

        self.room_table.column("floor", width=100)
        self.room_table.column("roomno", width=100)
        self.room_table.column("roomType", width=150)

        self.room_table.pack(fill=BOTH, expand=1)
        self.fetch_details()
        self.room_table.bind("<ButtonRelease-1>", self.get_cursor)

    def add_details(self):
        if self.var_floor.get() == "" or self.var_roomType.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="1234", database="hotel_management")
                my_cursor = conn.cursor()
                my_cursor.execute("INSERT INTO details (floor, roomNo, roomType) VALUES (%s, %s, %s)",
                                  (self.var_floor.get(), self.var_roomNo.get(), self.var_roomType.get()))
                conn.commit()
                self.fetch_details()
                conn.close()
                messagebox.showinfo("Success", "Room details added successfully", parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong:{str(es)}", parent=self.root)

    def update(self):
        if self.var_floor.get() == "":
            messagebox.showerror("Error", "Please enter a floor number to update", parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="1234", database="hotel_management")
            my_cursor = conn.cursor()
            my_cursor.execute("UPDATE details SET floor=%s, roomType=%s WHERE roomNo=%s",
                              (self.var_floor.get(), self.var_roomType.get(), self.var_roomNo.get()))
            conn.commit()
            self.fetch_details()
            conn.close()
            messagebox.showinfo("Success", "Room details updated successfully", parent=self.root)

    def delete(self):
        delete = messagebox.askyesno("Hotel Management System", "Do you want to delete this room?", parent=self.root)
        if delete > 0:
            conn = mysql.connector.connect(host="localhost", username="root", password="1234", database="hotel_management")
            my_cursor = conn.cursor()
            sql = "DELETE FROM details WHERE roomNo=%s"
            value = (self.var_roomNo.get(),)
            my_cursor.execute(sql, value)
            conn.commit()
            self.fetch_details()
            conn.close()
            messagebox.showinfo("Delete", "Successfully deleted room details", parent=self.root)
        else:
            return

    def reset(self):
        self.var_floor.set("")
        self.var_roomNo.set("")
        self.var_roomType.set("")

    def fetch_details(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="1234", database="hotel_management")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM details")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    def get_cursor(self, event=""):
        cursor_row = self.room_table.focus()
        content = self.room_table.item(cursor_row)
        row = content['values']

        self.var_floor.set(row[0])
        self.var_roomNo.set(row[1])
        self.var_roomType.set(row[2])


if __name__ == "__main__":
    root = Tk()
    obj = DetailsRoom(root)
    root.mainloop()


