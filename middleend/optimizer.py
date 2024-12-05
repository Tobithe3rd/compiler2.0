class Optimizer:
    def __init__(self, ir):
        self.ir = ir

    def optimize(self):
        """Optimize the intermediate representation."""
        optimized_ir = []
        for instruction in self.ir:
            optimized_instruction = self.optimize_instruction(instruction)
            if optimized_instruction:
                optimized_ir.append(optimized_instruction)
        return optimized_ir

    def optimize_instruction(self, instruction):
        """Perform optimization on a single instruction."""
        # Example optimization: Constant folding (e.g., 5 + 3 -> 8)
        if "ADD" in instruction:
            parts = instruction.split()
            if parts[1].isdigit() and parts[2].isdigit():
                result = int(parts[1]) + int(parts[2])
                return f"CONST {result}"
        elif "SUB" in instruction:
            parts = instruction.split()
            if parts[1].isdigit() and parts[2].isdigit():
                result = int(parts[1]) - int(parts[2])
                return f"CONST {result}"
        elif "MUL" in instruction:
            parts = instruction.split()
            if parts[1].isdigit() and parts[2].isdigit():
                result = int(parts[1]) * int(parts[2])
                return f"CONST {result}"
        elif "DIV" in instruction:
            parts = instruction.split()
            if parts[1].isdigit() and parts[2].isdigit():
                result = int(parts[1]) // int(parts[2])
                return f"CONST {result}"
        # Return the instruction if no optimization is applied
        return instruction
