---
layout: post
title: "Tập tành làm quen Assembly phần 1"
categories: Blueteam
tags: [pentest, beginner, coding, beginner, blueteam]
---

# Assembly là gì?
# Lập trình Assembly
## Kiểu dữ liệu cơ bản
- BYTE: 8 bit, char
- WORD: 16 bit, char
- DWORD: 32 bit, integer
- QUADWORD: 64 bit, integer
- DOUBLE QUADWORD: 128 bit
## Thanh ghi cờ thông dụng
- CF: carry flag
- SF: sign flag
- ZF: zero flag
- OF: overflow flag
- PF: parity flag
## Operand
- immediate: làm với số.
ví dụ `add rax, 14`
- registry: làm với thanh ghi
ví dụ `mov rax, rbx`
- memory: làm việc với vùng nhớ 
ví dụ `or rax, [rbx + rsi*8]`
## Các thanh ghi thông dụng
![Parrot OS](/images/asm/register-po.jpg)
Ngoài ra RIP: pointer register
### Bài tập chuyển từ mã asm sang C
```
mov rax,42        | rax = 42
imul r12,-47      | r12 *=-47
shl r15,8         | r15 = r15 << 8
xor ecx,80000000h | ecx ^= 80000000h
sub r9b,14        | r9b -= 14
mov rax,rbx       | rax = rbx
add rbx,r10       | rbx += r10
mul rbx           | rbx:rax = rax*rbx
and r8w,0ff00h    | r8w &= 0ff00h
mov rax,[r13]     | rax += *r13
sub qword ptr [r8],17 | *(long long*)r8 -= 17
shl word ptr [r12],2  | *(short*)r12<<=2
or rcx,[rbx+rsi*8]  | rcx |= *(rbx+rsi*8)
```
## Memory addressing
Khi một lệnh x86-64 muốn truy cập vào địa chỉ ô nhớ thay vì truy cập qua thanh ghi, nó sẽ truy cập qua 4 thành phần. 


EffectiveAddress = BaseReg + IndexReg * ScaleFactor + Disp


Trong đó base register có thể là bất cứ thanh ghi nào, index register là bất kì thanh ghi nào trừ RSP, scale Factor gồm 2,4,6 và Disp là hằng 8bit, 16bit hoặc 32bit. 

### Bài tập làm quen

```
mov rax,[Val]               | RIP + DISP
mov rax,[rbx]               | baseReg
mov rax,[rbx+16]            | baseReg + Disp
mov rax,[r15*8+48]          | indexReg * scaleFactor + Disp
mov rax,[rbx+r15]           | baseReg + indexReg
mov rax,[rbx+r15+32]        | baseReg + indexReg + Disp
mov rax,[rbx+r15*8]         | baseReg + indexReg * scaleFactor 
mov rax,[rbx+r15*8+64]      | baseReg + indexReg * scaleFactor + Disp
```

## Các tập lệnh 


```
adc	Add with carry – Cộng hai số + cờ Carry (CF). Dùng khi thực hiện phép cộng nhiều phần (như cộng 64-bit bằng 2 lần 32-bit).
add	Cộng hai số nguyên. Cập nhật các cờ như CF (carry), ZF (zero), OF (overflow).
dec	Giảm giá trị xuống 1.
inc	Tăng giá trị lên 1.
mul	Nhân số nguyên không dấu. Nhân ngầm với thanh ghi AL, AX, EAX hoặc RAX.
imul	Nhân số nguyên có dấu. Có thể dùng 2 hoặc 3 toán hạng.
div	Chia không dấu. Thường chia AX, DX:AX, EDX:EAX, hoặc RDX:RAX.
idiv	Chia có dấu. Cách dùng như div.
neg	Đảo dấu (âm thành dương, dương thành âm): neg eax = 0 - eax.
and	Phép AND từng bit giữa 2 toán hạng. Thường dùng để làm sạch bit (mask).
or	Phép OR từng bit. Dùng để bật bit cụ thể.
not	Phủ định bit: đảo từng bit (1 → 0, 0 → 1).
bsf	Bit Scan Forward – tìm bit 1 đầu tiên từ LSB (ít ý nghĩa nhất).
bsr	Bit Scan Reverse – tìm bit 1 đầu tiên từ MSB (nhiều ý nghĩa nhất).
bt	Bit Test – kiểm tra bit tại vị trí cụ thể, lưu kết quả vào cờ CF.
btr	Bit Test and Reset – như bt nhưng đặt bit đó về 0.
bts	Bit Test and Set – như bt nhưng đặt bit đó thành 1.
lahf	Tải các cờ trạng thái (SF, ZF, AF, PF, CF) từ RFLAGS vào thanh ghi AH.
cld	Xóa cờ Direction Flag (DF) → đảm bảo các lệnh chuỗi (string ops) tăng địa chỉ thay vì giảm.
mov	Di chuyển dữ liệu từ nguồn đến đích.
movsx / movsxd	Di chuyển số nguyên có kéo dấu (sign extension).
movzx	Di chuyển số nguyên có thêm 0 vào phần trên (zero extension).
lea	Load Effective Address – Tính địa chỉ hiệu dụng, nhưng không truy cập bộ nhớ. Rất hữu dụng để tính toán nhanh.
cmp	So sánh 2 toán hạng (như phép trừ, không lưu kết quả mà chỉ cập nhật cờ).
cmovcc	Conditional Move – Di chuyển nếu thỏa điều kiện, ví dụ cmove (equal), cmovg (greater)...
jcc	Jump nếu có điều kiện, như je, jne, jl, jg, ja, jb...
jmp	Jump không điều kiện – nhảy thẳng đến nhãn hoặc địa chỉ.
call	Gọi thủ tục: đẩy địa chỉ tiếp theo vào stack rồi nhảy đến hàm.
ret	(không có trong danh sách nhưng liên quan) – trở về từ call.
cmpsb, cmpsw, cmpsd, cmpsq	So sánh 2 chuỗi byte/word/dword/qword – tự động tăng/giảm địa chỉ dựa trên DF.
lodsb, lodsw, lodsd, lodsq	Nạp một phần tử chuỗi từ [rsi] vào al/ax/eax/rax.
cpuid	Truy vấn thông tin CPU: vendor, features, số core...
cwd, cdq, cqo	Mở rộng dấu trước khi chia (dành cho idiv), ví dụ: cdq chuyển EAX → EDX:EAX có dấu.
```

## Bài tập cộng trừ số với assembly và c


```
// main.cpp
#include "stdio.h"

#define ASSEMBLY


#ifdef ASSEMBLY

extern "C" int Sum_(int a, int b, int c);
extern "C" int Sub_(int a, int b);
#else

int Sum_(int a, int b, int c)
{
	return a + b + c;
}
int Sub_(int a, int b)
{
	return a - b;
}

#endif
void printOutput(int result)
{
	printf("%d\n",result);
}
int main()
{
	int a, b, c, sum, sub;
	a = 2;
	b =	20;
	c = 20;
	sum = Sum_(a, b, c);
	sub = Sub_(a, b);
	printOutput(sum);
	printOutput(sub);
	return 0;
}
```

```
// kon.asm
.CODE


Sum_ PROC
	MOV RAX, RCX
	ADD RAX, RDX
	ADD RAX, R8
	ret
Sum_ ENDP

Sub_ Proc
	MOV RAX, RCX
	SUB RAX, RDX
	RET
Sub_ ENDP
END
```

## Toán tử LOGIC

Với toán tử logic ta sẽ làm quen với các phép toán XOR, AND, OR và một chút shift

```
// main.cpp
#include "stdio.h"

#define ASSEMBLY


#ifdef ASSEMBLY

extern "C" int Sum_(int a, int b, int c);
extern "C" int Sub_(int a, int b);
extern "C" int Xor_(int a, int b);
extern "C" int And_(int a, int b);
#else


#endif
void printOutput(int result)
{
	printf("the dick make the eye binds %d\n",result);
}
int main()
{
	int a, b, c, sum, sub, xor_, and_;
	a = 2;
	b =	20;
	c = 20;
	sum = Sum_(a, b, c);
	sub = Sub_(a, b);
	xor_ = Xor_(a, b);
	and_ = And_(a, b);
	printOutput(sum);
	printOutput(sub);
	printOutput(xor_);
	printOutput(and_);
	return 0;
}
```

```
kon.asm
.CODE


Sum_ PROC
	MOV RAX, RCX
	ADD RAX, RDX
	ADD RAX, R8
	ret
Sum_ ENDP

Sub_ Proc
	MOV RAX, RCX
	SUB RAX, RDX
	RET
Sub_ ENDP

Xor_ Proc
	MOV RAX, RCX
	XOR RAX, RDX
	RET
Xor_ ENDP

And_ Proc
	MOV RAX, RCX
	AND RAX, RDX
	RET
And_ ENDP
END
```