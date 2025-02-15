  #
  # modelo de saida para o compilador
  #

  .section .text
  .globl _start

_start:
  ## saida do compilador deve ser inserida aqui
  # (7 * 6 * 5) / (4 * 3 * 2 * 1)
    mov $7, %rax
    imul $6, %rax
    imul $5, %rax

    mov $4, %rbx
    imul $3, %rbx
    imul $2, %rbx

    cqto
    idiv %rbx # RDX:RAX / RBX

  call imprime_num
  call sair

  .include "runtime.s"
  
