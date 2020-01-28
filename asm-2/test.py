def asm2(arg1, arg2):
# [bits 32]
# input - (0x7,0x18)
# asm2:
# 	<+0>:	push   ebp
# 	<+1>:	mov    ebp,esp
# 	<+3>:	sub    esp,0x10 ; allocating 16 bytes for the local args
# 	<+6>:	mov    eax,DWORD PTR (ebp-0x8)[c   ](ebp-0x4][d   ][e   ][RET ](ebp+0x8)[ARG1](ebp+0xc)[ARG2]
	eax = arg2
# 	<+9>:	mov    DWORD PTR [ebp-0x4],eax
	d = arg2
# 	<+12>:	mov    eax,DWORD PTR [ebp+0x8]
	eax = arg1
# 	<+15>:	mov    DWORD PTR [ebp-0x8],eax
	c = arg1
# 	<+18>:	jmp    0x50c <asm2+31>
# 	<+20>:	add    DWORD PTR [ebp-0x4],0x1
# 	<+24>:	add    DWORD PTR [ebp-0x8],0xcc
# 	<+31>:	cmp    DWORD PTR [ebp-0x8],0x3937
# 	<+38>:	jle    0x501 <asm2+20>
	while c <= int(0x3937):
		d +=1
		c += int(0xcc)
# 	<+40>:	mov    eax,DWORD PTR [ebp-0x4]
# 	<+43>:	leave  
# 	<+44>:	ret    
	return d
print(hex(asm2(int(0x7),int(0x18))))