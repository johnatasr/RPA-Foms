import tkinter as tk
import tkinter.font as tkFont
from repositories import input_repository as InputRepository


class App:
    def __init__(self, root):

        self.url: str = tk.StringVar()
        self.input: str = tk.StringVar()
        self.value: str = tk.StringVar()

        #setting title
        root.title("RPA Forms v1.0")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_185=tk.Label(root)
        ft = tkFont.Font(family='Times',size=13)
        GLabel_185["font"] = ft
        GLabel_185["fg"] = "#333333"
        GLabel_185["justify"] = "center"
        GLabel_185["text"] = "Input"
        GLabel_185.place(x=30,y=110,width=183,height=30)

        GLabel_3=tk.Label(root)
        ft = tkFont.Font(family='Times',size=13)
        GLabel_3["font"] = ft
        GLabel_3["fg"] = "#333333"
        GLabel_3["justify"] = "center"
        GLabel_3["text"] = "Valor "
        GLabel_3.place(x=240,y=110,width=186,height=30)

        GLabel_465=tk.Label(root)
        ft = tkFont.Font(family='Times',size=18)
        GLabel_465["font"] = ft
        GLabel_465["fg"] = "#333333"
        GLabel_465["justify"] = "center"
        GLabel_465["text"] = "RPA Forms"
        GLabel_465.place(x=30,y=20,width=534,height=30)

        GLineEdit_980=tk.Entry(root)
        GLineEdit_980["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_980["font"] = ft
        GLineEdit_980["fg"] = "#333333"
        GLineEdit_980["justify"] = "center"
        GLineEdit_980["text"] = "url"
        GLineEdit_980.place(x=30,y=70,width=531,height=30)

        GLineEdit_792=tk.Entry(root)
        GLineEdit_792["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_792["font"] = ft
        GLineEdit_792["fg"] = "#333333"
        GLineEdit_792["justify"] = "center"
        GLineEdit_792["text"] = "url"
        GLineEdit_792.place(x=30,y=140,width=183,height=30)

        GLineEdit_546=tk.Entry(root)
        GLineEdit_546["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_546["font"] = ft
        GLineEdit_546["fg"] = "#333333"
        GLineEdit_546["justify"] = "center"
        GLineEdit_546["text"] = "value"
        GLineEdit_546.place(x=240,y=140,width=185,height=30)

        GButton_898=tk.Button(root)
        GButton_898["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_898["font"] = ft
        GButton_898["fg"] = "#000000"
        GButton_898["justify"] = "center"
        GButton_898["text"] = "Novo"
        GButton_898.place(x=480,y=140,width=84,height=30)
        GButton_898["command"] = self.GButton_898_command

        GButton_728=tk.Button(root)
        GButton_728["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_728["font"] = ft
        GButton_728["fg"] = "#000000"
        GButton_728["justify"] = "center"
        GButton_728["text"] = "Atualizar"
        GButton_728.place(x=480,y=170,width=84,height=30)
        GButton_728["command"] = self.GButton_728_command

        GButton_812=tk.Button(root)
        GButton_812["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_812["font"] = ft
        GButton_812["fg"] = "#000000"
        GButton_812["justify"] = "center"
        GButton_812["text"] = "Deletar"
        GButton_812.place(x=480,y=200,width=84,height=30)
        GButton_812["command"] = self.GButton_812_command

        GListBox_212=tk.Listbox(root)
        GListBox_212["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GListBox_212["font"] = ft
        GListBox_212["fg"] = "#333333"
        GListBox_212["justify"] = "center"
        GListBox_212.place(x=30,y=200,width=396,height=260)
        self.listBox = GListBox_212

        GButton_618=tk.Button(root)
        GButton_618["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_618["font"] = ft
        GButton_618["fg"] = "#000000"
        GButton_618["justify"] = "center"
        GButton_618["text"] = "Executar"
        GButton_618.place(x=480,y=320,width=88,height=54)
        GButton_618["command"] = self.GButton_618_command

        GButton_324=tk.Button(root)
        GButton_324["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_324["font"] = ft
        GButton_324["fg"] = "#000000"
        GButton_324["justify"] = "center"
        GButton_324["text"] = "Resetar"
        GButton_324.place(x=480,y=420,width=70,height=25)
        GButton_324["command"] = self.GButton_324_command

    def insert_command(self):
        print("command")

    def update_command(self):
        print("command")

    def delete_command(self):
        print("command")

    def execute_command(self):
        print("command")

    def reset_command(self):
        print("command")

    def load_command(self):
        self.listBox.delete(0, tk.END)
        for row in InputRepository.get_all():
            self.listBox.insert(tk.END, row)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()





















