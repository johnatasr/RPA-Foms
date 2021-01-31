import rpa


class RPAModule(object):
    def __init__(self):
        self.rp = rpa
        self.registers = None

    def set_list(self, registers):
        self.registers = registers

    def exec_command(self):
        self.rp.init()
        self.rp.url(self.registers[0])

        for command in self.registers:
            self.rp.type(command[1], command[2])
