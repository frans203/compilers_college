import sys

def gerar_assembly(valor_constante, nome_arquivo_saida):
    with open(nome_arquivo_saida, "w") as arquivo:
        arquivo.write('.section .text\n')
        arquivo.write('.globl _start\n')
        arquivo.write('_start: \n')
        arquivo.write(f"    mov ${valor_constante}, %rax\n")
        arquivo.write("    call imprime_num\n")
        arquivo.write("    call sair\n")
        arquivo.write('.include "runtime.s"\n')

def main():
    if len(sys.argv) != 2:
        print(f"Uso: {sys.argv[0]} <arquivo de entrada>")
        sys.exit(1)

    try:
        with open(sys.argv[1], 'r') as arquivo_entrada:
            valor_constante = int(arquivo_entrada.read().strip()) 
            print(valor_constante)
    except Exception as e:
        print(f"Erro ao ler o arquivo de entrada: {e}")   
        sys.exit(1)

    nome_arquivo_saida = 'programa.s'
    gerar_assembly(valor_constante=valor_constante, nome_arquivo_saida=nome_arquivo_saida)
    print(f'Arquivo assembly: {nome_arquivo_saida}')


if __name__ == "__main__":
    main()