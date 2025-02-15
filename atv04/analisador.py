import re               # Para uso de expressoes regulares
from enum import Enum   # Para uso do tipo enumerado
from typing import List

# REGEX da nossa linguagem "EC1"
REGEX_LINGUAGEM = r'\(|\d+|[\+\-\*/]|\)|\n'


# Classe Enumerada com a identificacao dos tokens
class TokenType(Enum):
    INVALIDO        = None

    # Tipos numericos
    NUMERO          = r'\d+'    # Somente numeros inteiros positivos por enquanto

    # Pontuacao
    PARENTESE_ESQ   = r'\('     # Parentese esquerdo
    PARENTESE_DIR   = r'\)'     # Parentese direito

    # Operadores
    SOMA            = r'\+'
    SUBTRACAO       = r'\-'
    MULTIPLICACAO   = r'\*'
    DIVISAO         = r'\/'

# Estrutura de um Token gerado pela analise lexica
class TokenStruct:
    tipo:   TokenType
    lexema: str
    posicao: int

    def __init__(self, tipo = TokenType.INVALIDO, lexema = '', posicao = -1, linha = -1, coluna = -1):
        self.tipo = tipo
        self.lexema = lexema
        self.posicao = posicao
        self.linha = linha
        self.coluna = coluna
    
    def print(self):
        print(f'tipo:   {self.tipo}')
        print(f'lexema: {self.lexema}')
        print(f'posicao: {self.posicao}')
        print(f'linha: {self.linha}')
        print(f'coluna: {self.coluna}')


####################################################################
####################################################################
def main():
    with open('./atv04/codigo_linhas_erro.ci', 'r') as arquivo:
        codigo = arquivo.read()
    tokens = analisador_lexico(codigo=codigo.strip())
    

    for token in tokens:
        token.print()
        print('-' * 20)


def analisador_lexico(codigo: str):
    tokens: List[TokenStruct] = []
    posicao_atual = 0
    position_new_line = 0
    linhas = codigo.splitlines()


    for match in re.finditer(REGEX_LINGUAGEM, codigo):
        lexema = match.group()
        posicao = match.start()

        linha, coluna = calcular_linha_coluna(linhas=linhas, posicao=posicao)

        if lexema == "\n":
            position_new_line += 1
            continue

        if(posicao > posicao_atual + position_new_line):
            trecho_invalido = codigo[posicao_atual:posicao]
            linha_errada, coluna_errada = calcular_linha_coluna(linhas=linhas, posicao=posicao_atual)

            if trecho_invalido.strip() != '':
             raise SyntaxError(f"Token {trecho_invalido} na linha {linha_errada} e coluna {coluna_errada} (posicao: {posicao}) INVALIDO")
            
            

        token = proximoToken(lexema=lexema, posicao=posicao, coluna=coluna, linha=linha)
        posicao_atual += len(lexema)

        tokens.append(token)
    return tokens

def proximoToken(lexema: str, posicao: int, linha:int, coluna) -> TokenStruct:
    for token_type in TokenType:
        if token_type.value and re.fullmatch(token_type.value, lexema):
            return TokenStruct(lexema=lexema, posicao=posicao, tipo=token_type, linha=linha, coluna=coluna)
    
    return TokenStruct(lexema=lexema, posicao=posicao, tipo=TokenType.INVALIDO)

def calcular_linha_coluna(linhas: List[str], posicao: int):
    contador = 0
    for i, linha in enumerate(linhas):
        if contador + len(linha) + 1 > posicao:
            coluna = posicao - contador + 1
            return i + 1, coluna
        contador += len(linha) + 1 #+1 por conta do \n
    return -1, -1

if __name__ == "__main__":
    main()
