import re

TOKEN_INT = 'INT'
TOKEN_PLUS = 'PLUS'
TOKEN_MINUS = 'MINUS'
TOKEN_MUL = 'MUL'
TOKEN_DIV = 'DIV'
TOKEN_LPAREN = 'LPAREN'
TOKEN_RPAREN = 'RPAREN'

#tokeniza a expressao vindo da string matematica em uma lista de tokens identificaveis
def tokenize(expression):
    token_specifications = [
        (TOKEN_INT, r'\d+'),
        (TOKEN_PLUS, r'\+'),
        (TOKEN_MINUS, r'-'),
        (TOKEN_MUL, r'\*'),
        (TOKEN_DIV, r'/'),
        (TOKEN_LPAREN, r'\('),
        (TOKEN_RPAREN, r'\)'),
    ]

    tokens = []
    regex = '|'.join(f'(?P<{pair[0]}>{pair[1]})' for pair in token_specifications)
    for match in re.finditer(regex, expression):
        kind = match.lastgroup
        value = match.group(kind)
        tokens.append((kind, value))
    
    return tokens

# classe para representar nós da arvore 
class ASTNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class Parser: 
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
    
    def peek(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else (None, None)
    
    def consume(self):
        token = self.tokens[self.pos]
        self.pos = self.pos + 1
        return token
    
    def parse_primary(self):
        token_type, token_value = self.consume();
        if token_type == TOKEN_INT:
            return ASTNode(int(token_value))
        
        elif token_type == TOKEN_LPAREN:
            node = self.parse_expression()
            self.consume()

            return node
    
    def parse_term(self):
        node = self.parse_primary()
        while self.peek()[0] in (TOKEN_MUL, TOKEN_DIV):
            op_type, _ = self.consume()
            right = self.parse_primary()
            node = ASTNode(op_type, node, right)
        return node

    def parse_expression(self):
        node = self.parse_term()
        while self.peek()[0] in (TOKEN_PLUS, TOKEN_MINUS):
            op_type, _ = self.consume()
            right = self.parse_term()
            node = ASTNode(op_type, node, right);
        return node
    

class CodeGenerator:
    def __init__(self):
        self.code = [".global _start", ".section .data", "", ".section .text", "_start:"]

    def generate(self, node):
        if isinstance(node.value, int):
            self.code.append(f"mov ${node.value}, %rax") # Se for numero move pra RAX
        else:
            # gera o codigo para o operando direito
            self.generate(node.right)
            self.code.append(f"push %rax")
            self.generate(node.left)
            self.code.append(f"pop %rbx")

            if node.value == 'PLUS':
                self.code.append(f"add %rbx, %rax")
            elif node.value == 'MINUS':
                self.code.append(f'sub %rbx, %rax')
            elif node.value == 'MUL':
                self.code.append(f'imul %rbx, %rax')
            elif node.value == 'DIV':
                self.code.append('cqto') #Estende %rax para %rdx:%rax
                self.code.append(f"idiv %rbx") #divide %rdx:rax por %rbx
    def get_code(self):
        return "\n".join(self.code) + '\ncall imprime_num\ncall sair\n.include "runtime.s"'
    

#Passos
#1. Tokeniza a entrada
#2. Constrói a AST
#3. Gera código assembly
def compile_expression(expression):
    tokens = tokenize(expression)
    parser = Parser(tokens) 
    ast = parser.parse_expression() # constroi a AST
    generator = CodeGenerator()
    generator.generate(ast)
    return generator.get_code()

def read_ci_file(filename):
    with open(filename, 'r') as file:
        return file.read().strip()

def generate_asm_file(assembly_code):
    with open("06.asm", 'w') as file:
        file.write(assembly_code)
        print("File successfully generated")

expression_from_file = read_ci_file("./06-01.ci")
assembly_code = compile_expression(expression=expression_from_file)
print(assembly_code);
generate_asm_file(assembly_code=assembly_code)