import tkinter as tk
from gwa_calculator import GWACalculator

if __name__ == "__main__":
    root = tk.Tk()
    app = GWACalculator(root)
    root.mainloop()