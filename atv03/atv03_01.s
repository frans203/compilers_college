  #
  # modelo de saida para o compilador
  #

  .section .text
  .globl _start

_start:
  # (8 * 11 - 12 * 9) + (112 - 19)
    mov $8, %rax
    imul $11, %rax
    mov $12, %rbx
    imul $9, %rbx
    # rax - rbx 
    sub %rbx, %rax 

    mov $112, %rcx
    sub $19, %rcx
    
    add %rcx, %rax

    call    imprime_num
    call    sair

  .include "runtime.s"
  
