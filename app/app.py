import tkinter as tk
import tkinter.font as tkFont


class App:
    def __init__(self, root):
        #setting title
        root.title("RPA Forms")
        #setting window size
        width=610
        height=558
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLineEdit_625=tk.Entry(root)
        GLineEdit_625["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_625["font"] = ft
        GLineEdit_625["fg"] = "#393d49"
        GLineEdit_625["justify"] = "center"
        GLineEdit_625["text"] = "Entry"
        GLineEdit_625.place(x=30,y=140,width=200,height=30)

        GButton_808=tk.Button(root)
        GButton_808["bg"] = "#1e90ff"
        GButton_808["cursor"] = "sizing"
        ft = tkFont.Font(family='Times',size=10)
        GButton_808["font"] = ft
        GButton_808["fg"] = "#f9f9f9"
        GButton_808["justify"] = "center"
        GButton_808["text"] = "Adicionar"
        GButton_808.place(x=460,y=140,width=122,height=30)
        GButton_808["command"] = self.GButton_808_command

        GLineEdit_888=tk.Entry(root)
        GLineEdit_888["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_888["font"] = ft
        GLineEdit_888["fg"] = "#393d49"
        GLineEdit_888["justify"] = "center"
        GLineEdit_888["text"] = "Entry"
        GLineEdit_888.place(x=250,y=140,width=197,height=30)

        GLabel_170=tk.Label(root)
        GLabel_170["cursor"] = "target"
        ft = tkFont.Font(family='Times',size=18)
        GLabel_170["font"] = ft
        GLabel_170["fg"] = "#393d49"
        GLabel_170["justify"] = "center"
        GLabel_170["text"] = "Input Name"
        GLabel_170["relief"] = "sunken"
        GLabel_170.place(x=70,y=90,width=122,height=30)

        GListBox_520=tk.Listbox(root)
        GListBox_520["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GListBox_520["font"] = ft
        GListBox_520["fg"] = "#393d49"
        GListBox_520["justify"] = "center"
        GListBox_520.place(x=30,y=210,width=374,height=301)

        GLabel_286=tk.Label(root)
        ft = tkFont.Font(family='Times',size=18)
        GLabel_286["font"] = ft
        GLabel_286["fg"] = "#393d49"
        GLabel_286["justify"] = "center"
        GLabel_286["text"] = "Valor"
        GLabel_286.place(x=310,y=90,width=70,height=25)

        GButton_214=tk.Button(root)
        GButton_214["bg"] = "#1e90ff"
        ft = tkFont.Font(family='Times',size=10)
        GButton_214["font"] = ft
        GButton_214["fg"] = "#f2f3f7"
        GButton_214["justify"] = "center"
        GButton_214["text"] = "Atualizar"
        GButton_214.place(x=460,y=180,width=123,height=30)
        GButton_214["command"] = self.GButton_214_command

        GButton_555=tk.Button(root)
        GButton_555["bg"] = "#f74914"
        ft = tkFont.Font(family='Times',size=10)
        GButton_555["font"] = ft
        GButton_555["fg"] = "#f1ecec"
        GButton_555["justify"] = "center"
        GButton_555["text"] = "Deletar "
        GButton_555.place(x=460,y=220,width=125,height=30)
        GButton_555["command"] = self.GButton_555_command

        GButton_952=tk.Button(root)
        GButton_952["bg"] = "#5fb878"
        ft = tkFont.Font(family='Times',size=10)
        GButton_952["font"] = ft
        GButton_952["fg"] = "#f5f1f1"
        GButton_952["justify"] = "center"
        GButton_952["text"] = "Executar"
        GButton_952.place(x=450,y=400,width=127,height=63)
        GButton_952["command"] = self.GButton_952_command

        GLabel_163=tk.Label(root)
        ft = tkFont.Font(family='Times',size=18)
        GLabel_163["font"] = ft
        GLabel_163["fg"] = "#393d49"
        GLabel_163["justify"] = "center"
        GLabel_163["text"] = "Adicione o nome do input do formulario e valor"
        GLabel_163.place(x=50,y=20,width=503,height=37)

    def GButton_808_command(self):
        print("command")


    def GButton_214_command(self):
        print("command")


    def GButton_555_command(self):
        print("command")


    def GButton_952_command(self):
        print("command")


if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    root.mainloop()