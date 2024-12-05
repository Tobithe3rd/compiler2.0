import subprocess

class AssemblyGenerator:
    def __init__(self, llvm_ir: str, output_file: str = "output.s"):
        self.llvm_ir = llvm_ir
        self.output_file = output_file

    def save_ir_to_file(self, file_name="output.ll"):
        with open(file_name, "w") as f:
            f.write(self.llvm_ir)

    def generate_assembly(self):
        # Save LLVM IR to a file
        ir_file = "output.ll"
        self.save_ir_to_file(ir_file)

        # Use llc to generate assembly
        try:
            subprocess.run(
                ["llc", "-filetype=asm", ir_file, "-o", self.output_file],
                check=True
            )
            print(f"Assembly code generated in {self.output_file}")
        except subprocess.CalledProcessError as e:
            print("Error during assembly generation:", e)

        

LLVM_BIN = r"C:\Program Files\LLVM\bin\clang.exe"  # Update this path as needed

def generate_assembly(llvm_ir_file, output_asm_file):
    try:
        subprocess.run(
            [LLVM_BIN, llvm_ir_file, "-S", "-o", output_asm_file],
            check=True
        )
        print(f"Assembly generated in {output_asm_file}")
    except subprocess.CalledProcessError as e:
        print("Error during assembly generation:", e)
