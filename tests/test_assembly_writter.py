from assembly_writter import AssemblyWriter

asm_code = ['LOAD 8', 'LOAD 8', 'LOAD 5', 'ADD 8, 8', 'DIV 5, 2']
assembly_writer = AssemblyWriter()
assembly_writer.write(asm_code)
