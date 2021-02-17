import tkinter as tk
import tkinter.font as tkFont
from repositories.form_repository import FormRepository
from automation.rpa_automation import RPAModule
from exceptions.app_exceptions import AppExcetion
from time import sleep


class App:
    def __init__(self, root):
        self.url: str = tk.StringVar()
        self.key: str = tk.StringVar()
        self.value: str = tk.StringVar()
        self.msg: str = tk.StringVar()
        self.selected_row = None
        self.msg.set("")

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

        GLabel_469 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=14)
        GLabel_469["font"] = ft
        GLabel_469["fg"] = "#333333"
        GLabel_469["justify"] = "center"
        GLabel_469["text"] = "Digite a URL"
        GLabel_469.place(x=30, y=45, width=534, height=30)

        GLineEdit_980=tk.Entry(root, textvariable=self.url)
        GLineEdit_980["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_980["font"] = ft
        GLineEdit_980["fg"] = "#333333"
        GLineEdit_980["justify"] = "center"
        GLineEdit_980["text"] = self.url
        GLineEdit_980.place(x=30,y=70,width=531,height=30)

        GLineEdit_792=tk.Entry(root, textvariable=self.key)
        GLineEdit_792["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_792["font"] = ft
        GLineEdit_792["fg"] = "#333333"
        GLineEdit_792["justify"] = "center"
        GLineEdit_792["text"] = self.key
        GLineEdit_792.place(x=30,y=140,width=183,height=30)

        GLineEdit_546=tk.Entry(root, textvariable=self.value)
        GLineEdit_546["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_546["font"] = ft
        GLineEdit_546["fg"] = "#333333"
        GLineEdit_546["justify"] = "center"
        GLineEdit_546["text"] = self.value
        GLineEdit_546.place(x=240,y=140,width=185,height=30)

        GButton_898=tk.Button(root)
        GButton_898["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_898["font"] = ft
        GButton_898["fg"] = "#000000"
        GButton_898["justify"] = "center"
        GButton_898["text"] = "Novo"
        GButton_898.place(x=480,y=140,width=84,height=30)
        GButton_898["command"] = self.insert_command

        GButton_728=tk.Button(root)
        GButton_728["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_728["font"] = ft
        GButton_728["fg"] = "#000000"
        GButton_728["justify"] = "center"
        GButton_728["text"] = "Atualizar"
        GButton_728.place(x=480,y=170,width=84,height=30)
        GButton_728["command"] = self.update_command

        GButton_812=tk.Button(root)
        GButton_812["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_812["font"] = ft
        GButton_812["fg"] = "#000000"
        GButton_812["justify"] = "center"
        GButton_812["text"] = "Deletar"
        GButton_812.place(x=480,y=200,width=84,height=30)
        GButton_812["command"] = self.delete_command

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
        GButton_618.place(x=480,y=270,width=88,height=54)
        GButton_618["command"] = self.execute_command

        GButton_324=tk.Button(root)
        GButton_324["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_324["font"] = ft
        GButton_324["fg"] = "#000000"
        GButton_324["justify"] = "center"
        GButton_324["text"] = "Resetar"
        GButton_324.place(x=480,y=380,width=70,height=25)
        GButton_324["command"] = self.reset_command

        GLabel_473 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_473["font"] = ft
        GLabel_473["fg"] = "#333333"
        GLabel_473["justify"] = "center"
        GLabel_473["text"] = self.msg
        GLabel_473.place(x=30, y=470, width=300, height=20)

        self.repo = FormRepository()
        self.rpa = RPAModule()
        self.scroll = tk.Scrollbar(root)
        #self.scroll.grid(row=2, column=2, rowspan=6)
        self.listBox.bind('<<ListboxSelect>>', self.get_selected_row)
        self.listBox.configure(yscrollcommand=self.scroll)
        self.scroll.configure(command=self.listBox.yview)

    def insert_command(self):
        try:
            if self.fields_validation():
                self.msg.set('Inserindo Input ...')
                self.repo.create(*self.get_input_values())
                self.load_command()
                self.reset_inputs()
        except Exception as error:
            self.execute_exception(
                method=self.insert_command.__name__.split('_')[0],
                error=error,
            )

    def update_command(self):
        try:
            if self.fields_validation():
                self.repo.update(*self.get_input_values(id=True))
                self.load_command()
                self.reset_inputs()
        except Exception as error:
            self.execute_exception(
                method=self.update_command.__name__.split('_')[0],
                error=error,
            )

    def delete_command(self):
        try:
            if self.selected_row is not None:
                self.msg.set('Deletando Input ...')
                self.repo.delete(self.selected_row[0])
                self.load_command()
                self.reset_inputs()
        except Exception as error:
            self.execute_exception(
                method=self.delete_command.__name__.split('_')[0],
                error=error,
            )

    def execute_command(self):
        try:
            self.rpa.exit()
            self.msg.set('Executando ...')
            self.rpa.set_registers(self.listBox.get(0, tk.END))
            self.rpa.exec_command()
        except Exception as error:
            self.execute_exception(
                method=self.execute_command.__name__.split('_')[0],
                error=error,
            )

    def reset_command(self):
        try:
            self.repo.truncate()
            self.load_command()
            self.reset_inputs()
        except Exception as error:
            self.execute_exception(
                method=self.reset_command.__name__.split('_')[0],
                error=error,
                args='todos registros'
            )

    def load_command(self):
        try:
            self.listBox.delete(0, tk.END)
            self.msg.set('Carrengando ...')
            for row in self.repo.get_all():
                self.listBox.insert(tk.END, row)
        except Exception as error:
            self.execute_exception(
                method=self.load_command.__name__.split('_')[0],
                error=error,
                args='todos registros'
            )

    def get_selected_row(self, event):
        try:
            index = self.listBox.curselection()[0]
            self.selected_row = self.listBox.get(index)
            self.url.set(self.selected_row[1])
            self.key.set(self.selected_row[2])
            self.value.set(self.selected_row[3])
        except IndexError:
            print("No selected row")

    def get_input_values(self, id=False):
        args = [self.url.get(), self.key.get(), self.value.get()]

        if id:
            args.insert(0, self.selected_row[0])

        return args

    def start_database(self, *, initialize_app=False):
        try:
            if initialize_app is False:
                self.msg.set('Carregando SQlite ...')
            self.repo.create_database()
            self.reset_inputs()
        except Exception as error:
            self.execute_exception(
                method=self.start_database.__name__.split('_')[0],
                error=error,
                args='SQLite' if initialize_app is False else None
            )

    def reset_inputs(self):
        self.url.set("")
        self.key.set("")
        self.value.set("")
        self.msg.set("")

    def fields_validation(self):
        if any(field == "" for field in [self.url.get(), self.key.get(), self.value.get()]):
            return False
        else: return True

    def execute_exception(self, method, error, args=None):
        self.msg.set(AppExcetion(method, error, args).__str__())
        sleep(3)
        self.reset_inputs()
        self.load_command()



















