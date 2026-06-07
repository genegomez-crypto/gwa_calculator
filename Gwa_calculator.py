import tkinter as tk
from tkinter import messagebox
from datetime import datetime

class GWACalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("GWA CALCULATOR")
        self.root.geometry("330x600")
        self.root.resizable(False, False)

        self.bg_color = "#FFEFF7"
        self.pink = "#FFC0DE"        
        self.dark_pink = "#FF69B4"
        self.gray = "#D3D3D3"
        self.light_pink = "#F8C8DC"
        self.text_color = "#000000"

        self.root.configure(bg=self.bg_color)
        self.subjects = []  

        header = tk.Label(root, text="GWA CALCULATOR", font=("Arial", 15, "bold"), fg=self.dark_pink, bg=self.bg_color)
        header.pack(pady=4)

        info_frame = tk.Frame(root, bg=self.gray, bd=1, relief=tk.SOLID)
        info_frame.pack(fill=tk.X, padx=8, pady=2)

        tk.Label(info_frame, text="Information", font=("Arial", 9), bg=self.gray, anchor="w").pack(fill=tk.X, padx=4, pady=1)

        row1 = tk.Frame(info_frame, bg=self.gray)
        row1.pack(fill=tk.X, padx=4, pady=2)

        tk.Label(row1, text="Student No.:", font=("Arial", 9, "bold"), bg=self.gray).pack(side=tk.LEFT, padx=1)
        
        self.student_no = tk.Entry(row1, width=12, font=("Arial", 9))
        self.student_no.pack(side=tk.LEFT, padx=2)

        tk.Label(row1, text="Year:", font=("Arial", 9, "bold"), bg=self.gray).pack(side=tk.LEFT, padx=3)
        
        self.year = tk.Entry(row1, width=5, font=("Arial", 9))
        self.year.insert(0, datetime.now().year)
        self.year.pack(side=tk.LEFT, padx=1)

        add_frame = tk.Frame(root, bg=self.gray, bd=1, relief=tk.SOLID)
        add_frame.pack(fill=tk.X, padx=8, pady=2)

        tk.Label(add_frame, text="Add Subject", font=("Arial", 9), bg=self.gray, anchor="w").pack(fill=tk.X, padx=4, pady=1)

        row2 = tk.Frame(add_frame, bg=self.gray)
        row2.pack(fill=tk.X, padx=4, pady=2)

        tk.Label(row2, text="Subj:", font=("Arial", 9, "bold"), bg=self.gray).pack(side=tk.LEFT, padx=1)
        self.subj = tk.Entry(row2, width=11, font=("Arial", 9))
        self.subj.pack(side=tk.LEFT, padx=2)

        tk.Label(row2, text="Grade:", font=("Arial", 9, "bold"), bg=self.gray).pack(side=tk.LEFT, padx=1)
        self.grade = tk.Entry(row2, width=11, font=("Arial", 9), bg="#FFFFFF", justify="center")
        self.grade.pack(side=tk.LEFT, padx=2)
        self.grade.bind("<Key>", lambda e: "break")  
      
        add_btn = tk.Button(row2, text="Add", font=("Arial", 8), bg=self.gray, command=self.add_subj)
        add_btn.pack(side=tk.LEFT, padx=1)
        check_btn = tk.Button(row2, text="✔️", font=("Arial", 8, "bold"), bg="#90EE90", width=2, command=self.add_subj)
        check_btn.pack(side=tk.LEFT, padx=1)

        list_frame = tk.Frame(root, bg=self.gray, bd=1, relief=tk.SOLID)
        list_frame.pack(fill=tk.BOTH, expand=True, padx=8, pady=2)

        tk.Label(list_frame, text="Subjects List", font=("Arial", 9, "bold"), bg=self.gray, anchor="w").pack(fill=tk.X, padx=4, pady=1)

        head = tk.Frame(list_frame, bg=self.light_pink)
        head.pack(fill=tk.X, padx=2, pady=1)
        tk.Label(head, text="SUBJECT", font=("Arial", 8, "bold"), bg=self.light_pink, width=18).pack(side=tk.LEFT)
        tk.Label(head, text="GRADE", font=("Arial", 8, "bold"), bg=self.light_pink, width=8).pack(side=tk.LEFT)

        self.listbox = tk.Frame(list_frame, bg="#FFFFFF")
        self.listbox.pack(fill=tk.BOTH, expand=True, padx=2, pady=1)

        pad_frame = tk.Frame(root, bg=self.bg_color)
        pad_frame.pack(pady=2)

        btns = [
            '1','2','3',
            '4','5','6',
            '7','8','9',
            '.','0','UNDO'
        ]

        positions = [
            (0,0), (0,1), (0,2),
            (1,0), (1,1), (1,2),
            (2,0), (2,1), (2,2),
            (3,0), (3,1), (3,2)
        ]

        for i, val in enumerate(btns):
            r, c = positions[i]
            if val == "UNDO":
                btn = tk.Button(pad_frame, text=val, font=("Arial", 8, "bold"),
                                bg="#F1D4E6", fg="#333333", width=4, height=1,
                                command=self.undo_last)
            else:
                btn = tk.Button(pad_frame, text=val, font=("Arial", 10, "bold"),
                                bg=self.pink, fg="#FFFFFF", width=4, height=1,
                                command=lambda v=val: self.press_num(v))
            btn.grid(row=r, column=c, padx=1, pady=1)

 
        clear_btn = tk.Button(pad_frame, text="CLEAR", font=("Arial", 8, "bold"),
                             bg="#FFB6C1", fg="#333333", width=4, height=1,
                             command=self.clear_all)
        clear_btn.grid(row=4, column=0, padx=1, pady=1)

        next_btn = tk.Button(pad_frame, text="NEXT", font=("Arial", 8, "bold"),
                             bg="#F1D4E6", fg="#333333", width=10, height=1,
                             command=self.add_subj)
        next_btn.grid(row=4, column=1, columnspan=2, padx=1, pady=1)

        calc_btn = tk.Button(root, text="CALCULATE GWA", font=("Arial", 9, "bold"),
                             bg=self.gray, width=16, command=self.calc_gwa)
        calc_btn.pack(pady=3)

        self.gwa_text = tk.Label(root, text="GWA: ---", font=("Arial", 10, "bold"), fg=self.dark_pink, bg=self.bg_color)
        self.gwa_text.pack()

        self.status_text = tk.Label(root, text="Status: ---", font=("Arial", 8), bg=self.bg_color)
        self.status_text.pack()

        footer = tk.Label(root, text="Made by: Sophia, Revegene & John Albert",
                          font=("Arial", 6), fg="#997788", bg=self.bg_color)
        footer.pack(pady=2)

    def press_num(self, val):
        self.grade.insert(tk.END, val)

    def undo_last(self):
        current = self.grade.get()
        if current:
            self.grade.delete(len(current)-1, tk.END)

    def clear_all(self):
        # 1. Clear input fields
        self.subj.delete(0, tk.END)
        self.grade.delete(0, tk.END)
        # 2. Clear data list
        self.subjects.clear()
        # 3. Clear all items displayed in subject list
        for widget in self.listbox.winfo_children():
            widget.destroy()
        # 4. Reset GWA display
        self.gwa_text.config(text="GWA: ---")
        self.status_text.config(text="Status: ---")
        # 5. Focus back
        self.subj.focus()

 
    def add_subj(self):
        n = self.subj.get().strip()
        g = self.grade.get().strip()

        if not n or not g:
            messagebox.showwarning("Warning", "Fill Subject & Grade first!")
            return

        try:
            g = float(g)
        except:
            messagebox.showerror("Error", "Grade must be number only")
            return

        self.subjects.append([n, g])

        row = tk.Frame(self.listbox, bg="#FFFFFF")
        row.pack(fill=tk.X)
        tk.Label(row, text=n, width=18, bg="#FFFFFF", font=("Arial", 7, "bold"), anchor="w").pack(side=tk.LEFT)
        tk.Label(row, text=f"{g:.2f}", width=8, bg="#FFFFFF", font=("Arial", 7)).pack(side=tk.LEFT)

        self.subj.delete(0, tk.END)
        self.grade.delete(0, tk.END)
        self.subj.focus()

    def calc_gwa(self):
        if not self.subjects:
            messagebox.showinfo("Info", "Add subjects first")
            return

        stud_no_val = self.student_no.get().strip()
        year_val = self.year.get().strip()

        if not stud_no_val or not year_val:
            messagebox.showwarning("Warning", "Enter Student No. & Year")
            return

        total = 0
        count = len(self.subjects)
        for s in self.subjects:
            total += s[1]

        gwa = total / count
        self.gwa_text.config(text=f"GWA: {gwa:.2f}")

        if 1.00 <= gwa <= 1.25:
            status = "PRESIDENT'S LIST"
            color = "#E91E63"
        elif 1.26 <= gwa <= 1.75:
            status = "DEAN'S LIST"
            color = "#EC407A"
        else:
            status = "GOOD JOB"
            color = "#995577"

        self.status_text.config(text=f"Status: {status}", fg=color)

        messagebox.showinfo("Result",
            f"Student No.: {stud_no_val}\n"
            f"Year: {year_val}\n"
            f"GWA: {gwa:.2f}\n\n{status}")

if __name__ == "__main__":
    root = tk.Tk()
    app = GWACalculator(root)
    root.mainloop()