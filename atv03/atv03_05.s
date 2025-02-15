  #
  # modelo de saida para o compilador
  #

  .section .text
  .globl _start

_start:
  ## saida do compilador deve ser inserida aqui
    mov $512, %rax
    imul $65, %rax

    mov $5657, %rbx 
    imul $23, %rbx 

    sub %rbx, %rax # pode dar erro se nós nao armazenassemos
    # o valor resultante em um registrador de 64 bits

    test %rax, %rax # se o nmr em rax é positivo ele dispara a função positivo
    # jns siginfica jump if not signed in
    # se tiver sinal ele continua o resto do programa sem executa a rotina 'positivo'
    jns positivo 

  # call imprime_num # A func espera um numero não negativo, o q não é o caso do resultado anterior
  call sair
positivo:
    call imprime_num
    call sair
  .include "runtime.s"
  
