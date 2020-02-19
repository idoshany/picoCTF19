#!/usr/bin/python3
'''(0xaeed09cb,0xb7acde91,0xb7facecd)
asm3:
	<+0>:	push   ebp
	<+1>:	mov    ebp,esp
	<+3>:	xor    eax,eax
	<+5>:	mov    ah,BYTE PTR [ebp+0xb]
	<+8>:	shl    ax,0x10
	<+12>:	sub    al,BYTE PTR [ebp+0xe]
	<+15>:	add    ah,BYTE PTR [ebp+0xd]
	<+18>:	xor    ax,WORD PTR [ebp+0x12]
	<+22>:	nop
	<+23>:	pop    ebp
	<+24>:	ret    
'''
from struct import pack,unpack

def little(arg):
	return pack('<I', arg)

def word(data):
	return unpack('<H', data)[0]

#4 bytes each[ebp   ][RET][ARG1][ARG2][ARG3]
def asm3(arg1, arg2, arg3):
	ebp = 0
	stack = bytearray((little(0) + little(0) + little(arg1) + little(arg2) + little(arg3)))
	ax = stack[ebp + 0xb] << 8 #mov ah,BYTE PTR [ebp+0xb]
	ax = ((ax & 0xffff) << 16) & 0xffff #shl ax,0x10
	print("ax", "0x%04x" % ax) 
	al = ((ax & 0x00ff) - stack[ebp + 0xe])& 0xff #mov al,BYTE PTR [ebp+0xe]
	print("al", "0x%2x" % al) 
	ax = ((ax & 0xff00) | al) & 0xffff 
	print("ax", "0x%04x" % ax)
	ah = ((ax & 0xff00) + stack[ebp + 0xd]) & 0xffff #add ah,BYTE PTR [ebp+0xd]
	print("ah", "0x%2x" % ah)
	ax = ((ax & 0xff) | ah << 8) & 0xffff
	print("ax", "0x%04x" % ax)
	ax ^= word(stack[ebp+0x12 : ebp+0x12+0x2]) & (0xffff) #xor ax,WORD PTR [ebp+0x12]
	print("ax", "0x%04x" % ax)

asm3(0xaeed09cb,0xb7acde91,0xb7facecd)