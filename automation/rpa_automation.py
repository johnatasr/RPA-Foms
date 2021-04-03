import rpa


class RPAModule(object):
    def __init__(self):
        self.rpa = rpa
        self.registers = None
        self.has_init = False

    def set_registers(self, registers):
        self.registers = registers

    def exec_command(self):
        self.rpa.init()
        self.has_init = True
        self.rpa.url(self.registers[0][1])

        for command in self.registers:
            self.rpa.type(command[2], command[3])

    def exit(self):
        if self.has_init:
            self.rpa.close()