  #
  # modelo de saida para o compilador
  #

  .section .text
  .globl _start

_start:
  ## saida do compilador deve ser inserida aqui
  #  (7374 * 657) + (13121517 * 256) + 4294979641
    mov $7374, %rax
    imul $657, %rax

    mov $13121517, %rbx
    imul $256, %rbx

    add %rax, %rbx

    mov $4294979641, %rax # necessario fazer dessa forma pois 4294979641 é de 64 bits
    add %rbx, %rax
   
  call imprime_num
  call sair

  .include "runtime.s"
  
