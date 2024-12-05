class SymbolTable:
    def __init__(self):
        self.symbols = {}

    def define(self, name, value=None):
        if name in self.symbols:
            raise ValueError(f"Variable '{name}' is already defined.")
        self.symbols[name] = value

    def assign(self, name, value):
        if name not in self.symbols:
            raise ValueError(f"Variable '{name}' is not defined.")
        self.symbols[name] = value

    def lookup(self, name):
        if name not in self.symbols:
            raise ValueError(f"Variable '{name}' is not defined.")
        return self.symbols[name]
