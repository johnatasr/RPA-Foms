from app.root_app import App
import tkinter as tk

root = tk.Tk()
app = App(root)
app.start_database(initialize_app=True)
app.load_command()
root.mainloop()

