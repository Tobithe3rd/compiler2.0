# ir.py

from dataclasses import dataclass
from typing import Union

@dataclass
class IRInstruction:
    def __init__(self, op, arg1=None, arg2=None, dest=None):
        self.op = op        # Operation (e.g., LOAD, STORE, ADD, etc.)
        self.arg1 = arg1    # First argument (optional)
        self.arg2 = arg2    # Second argument (optional)
        self.dest = dest    # Destination for result (optional)

    def __repr__(self):
        return f"IRInstruction(op='{self.op}', arg1={self.arg1}, arg2={self.arg2}, dest={self.dest})"


@dataclass
class IRAssign(IRInstruction):
    target: str
    value: Union[str, int]

    def __repr__(self):
        return f"{self.target} = {self.value}"

@dataclass
class IRBinaryOp(IRInstruction):
    target: str
    left: Union[str, int]
    op: str
    right: Union[str, int]

    def __repr__(self):
        return f"{self.target} = {self.left} {self.op} {self.right}"

@dataclass
class IRLabel(IRInstruction):
    label: str

    def __repr__(self):
        return f"{self.label}:"

# Extend with more instructions as needed
