.global _start
.section .data

.section .text
_start:
mov $1, %rax
push %rax
mov $2, %rax
push %rax
mov $32, %rax
pop %rbx
imul %rbx, %rax
push %rax
mov $3, %rax
push %rax
mov $10, %rax
pop %rbx
add %rbx, %rax
pop %rbx
add %rbx, %rax
pop %rbx
add %rbx, %rax
call imprime_num
call sair
.include "runtime.s"