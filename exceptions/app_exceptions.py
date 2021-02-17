class AppExcetion(Exception):
    def __init__(self, method, msg_error: str, args):
        super().__init__()
        self.method = method
        self.message = msg_error
        self.args = args

    def get_method(self):
        methods: dict = {
            'insert': 'inserir',
            'update': 'atualizar',
            'delete': 'deletar',
            'execute': 'executar',
            'reset': 'resetar',
            'load': 'carregar',
            'start': 'carregar',
        }

        method_selected = [value for key, value in methods.items() if key == self.method]

        return method_selected[0]

    def __str__(self):
        if self.message:
            if self.args is not None:
                return f'Não foi possível {self.get_method()} {self.args}  --> Error: {self.message}'
            else:
                return f'Não foi possível {self.get_method()} --> Error: {self.message}'
        else:
            return 'AppExcetion has been raised'
