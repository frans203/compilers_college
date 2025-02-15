  #
  # modelo de saida para o compilador
  #

  .section .text
  .globl _start

_start:
  ## saida do compilador deve ser inserida aqui

  #  (72 - 101) * 4 + (14 * 77)
  mov $72, %rax
  mov $101, %rbx
  sub %rbx, %rax
  imul $4, %rax

  mov $14, %rcx
  imul $77, %rcx

  add %rcx, %rax

  call imprime_num
  call sair

  .include "runtime.s"
  
