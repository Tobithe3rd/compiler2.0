from middleend.optimizer import Optimizer

ir = ["ADD 5 3", "MUL 2 4", "DIV 10 2"]
optimizer = Optimizer(ir)
optimized_ir = optimizer.optimize()
print(optimized_ir)  # Expected output: ['CONST 8', 'CONST 8', 'CONST 5']
