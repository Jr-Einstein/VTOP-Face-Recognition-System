from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
from PIL import  ImageFilter
import webbrowser




class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("VTOP Face Attendance System")

        try:
            # Blue bar pic in header
            img = Image.open(r"C:\Users\amans\OneDrive\Desktop\face_recognition system\college_images\collegepic.jpg")
            img = img.resize((1370, 190))
            self.photoimg = ImageTk.PhotoImage(img)

            f_lbl = Label(self.root, image=self.photoimg)
            f_lbl.place(x=0, y=0, width=1370, height=90)

            # Logo image
            img1 = Image.open(r"C:\Users\amans\OneDrive\Desktop\face_recognition system\college_images\logo.jpg")
            img1 = img1.resize((155, 90))
            self.photoimg1 = ImageTk.PhotoImage(img1)

            f_lbl1 = Label(self.root, image=self.photoimg1)
            f_lbl1.place(x=0, y=0, width=155, height=90)

            # Background image
            img2 = Image.open(r"C:\Users\amans\OneDrive\Desktop\face_recognition system\college_images\bg.jpg")
            img2 = img2.resize((1530, 710))
            self.photoimg2 = ImageTk.PhotoImage(img2)

            f_lbl2 = Label(self.root, image=self.photoimg2)
            f_lbl2.place(x=0, y=90, width=1530, height=610)

            # Title
            title_lbl = Label(self.root, text="DEVELOPERS' INFO!                                         ", font=("times new roman", 20, "bold"), bg="white", fg="dark blue")
            title_lbl.place(x=0, y=130, width=1530, height=45)

            # Team member details
            members = [
            {"name": "Aman kumar singh", "reg_id": "22BCY10258", "linkedin": "linkedin.com/in/aman-kumar-singh04", "image": r"C:\Users\Lenovo\OneDrive\Desktop\face_recognition_system\face_recognition system\college_images\aman.jpg"},
            {"name": "Mahi jain", "reg_id": "22BCY10144", "linkedin": "linkedin.com/in/mahi-jain-69bb3b251", "image": r"C:\Users\Lenovo\OneDrive\Desktop\face_recognition_system\face_recognition system\college_images\mahi5.jpg"},
            {"name": "Shivansh Kuntal", "reg_id": "22BCY10290", "linkedin": "linkedin.com/in/shivansh-kuntal-498b52251", "image": r"C:\Users\Lenovo\OneDrive\Desktop\face_recognition_system\face_recognition system\college_images\shivansh.jpg"},
            {"name": "Nupur Shivani", "reg_id": "22BCY10066", "linkedin": "linkedin.com/in/nupurshivani", "image": r"C:\Users\Lenovo\OneDrive\Desktop\face_recognition_system\face_recognition system\college_images\nupur.jpg"},
            {"name": "Apoorva", "reg_id": "22BCY10070", "linkedin": "linkedin.com/in/apoorva-goyal-498729250", "image": r"C:\Users\Lenovo\OneDrive\Desktop\face_recognition_system\face_recognition system\college_images\apoorva.jpg"}
            ]
            # Function to display members
            self.display_members(members)
            back_btn = Button(self.root, text="←", command=self.close_window)
            back_btn.place(x=10, y=100) 

        

        except Exception as e:
            print(f"Error: {e}")

       

    def close_window(self):
        self.root.destroy()

    def display_members(self, members):
        x = 50
        y = 200

        for member in members:
            try:
                # Load member image
                img_member = Image.open(member["image"])
                img_member = img_member.resize((150, 150))
                photoimg_member = ImageTk.PhotoImage(img_member)

                # Display member image
                lbl_member = Label(self.root, image=photoimg_member)
                lbl_member.image = photoimg_member  # Keep a reference
                lbl_member.place(x=x, y=y)

                # Display member details
                full_details = f"{member['name']} ({member['reg_id']})"
                lbl_name = Label(self.root, text=full_details, font=("times new roman", 12, "bold"), bg="white")
                lbl_name.place(x=x, y=y + 160)

                lbl_linkedin = Label(self.root, text=member["linkedin"], font=("times new roman", 10), bg="white", fg="blue", cursor="hand2")
                lbl_linkedin.place(x=x, y=y + 190)
                lbl_linkedin.bind("<Button-1>", lambda e, link=member["linkedin"]: self.open_link(link))
                x += 250
                if x > 1350:
                    x = 50
                    y += 300
            except Exception as e:
                print(f"Error loading {member['name']}'s image: {e}")

    def open_link(self, link):
        webbrowser.open(link)


if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()
