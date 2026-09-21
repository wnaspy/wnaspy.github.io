# Bộ 10 bài luyện tập CTF - RSA
 
> Nguyên tắc luyện tập: đọc đề → tự đoán "lỗ hổng nằm ở đâu" → viết script Python (dùng `sympy`, `pycryptodome`, hoặc thư viện `gmpy2`) → chỉ mở phần Đáp án khi đã thử ít nhất 10-15 phút.
 
Cài sẵn trước khi bắt đầu:
```bash
pip install sympy pycryptodome gmpy2
```
 
---
 
## Bài 1 — Factor n cơ bản (khởi động)
 
```
n = 3233
e = 17
c = 2790
```
**Gợi ý**: n rất nhỏ. Factor trực tiếp bằng `sympy.factorint()` hoặc thử chia tay.
 
---
 
## Bài 2 — n hơi lớn hơn, cần công cụ
 
```
n = 92565752233748521
e = 65537
c = 15427086843431102
```
**Gợi ý**: n vẫn factor được bằng máy tính cá nhân, nhưng `sympy.factorint` thuần có thể chậm. Thử dùng [factordb.com](http://factordb.com) (dán n vào ô tìm kiếm) hoặc `sympy.ntheory.factor_.factorint` với timeout dài hơn.
 
---
 
## Bài 3 — Common Modulus Attack
 
Cùng một n, cùng bản rõ M, nhưng mã hóa 2 lần với 2 số mũ e khác nhau:
 
```
n  = 143
e1 = 7
c1 = 64
e2 = 11
c2 = 25
```
**Gợi ý**: Nếu `gcd(e1, e2) = 1`, dùng thuật toán Euclid mở rộng tìm `a, b` sao cho `a*e1 + b*e2 = 1`, rồi tính:
$$M = c1^a \times c2^b \mod n$$
(Một trong hai số a, b sẽ âm — cần tính nghịch đảo modulo cho số hạng đó.)
 
---
 
## Bài 4 — Low Public Exponent Attack (e=3, không padding)
 
```
e = 3
n = 2988348162058574136915891421498819466320163312926952423791023078876139
c = 2716161331923531973844857787479985881975885030509
```
**Gợi ý**: Nếu bản rõ M nhỏ đến mức `M^3 < n` (không bị "cuộn" qua modulo), thì phép mã hóa thực chất KHÔNG dùng đến modulo. Chỉ cần khai căn bậc 3 thông thường (không phải modular) của c.
 
```python
from gmpy2 import iroot
m, exact = iroot(c, 3)
```
 
---
 
## Bài 5 — Fermat's Factorization (p và q quá gần nhau)
 
```
n = 17993
e = 5
c = 4441
```
**Gợi ý**: Kiểm tra xem `sqrt(n)` có gần với một số nguyên không. Nếu p, q gần nhau, dùng thuật toán Fermat:
```python
import math
a = math.isqrt(n) + 1
while True:
    b2 = a*a - n
    b = math.isqrt(b2)
    if b*b == b2:
        p, q = a-b, a+b
        break
    a += 1
```
 
---
 
## Bài 6 — Wiener's Attack (d quá nhỏ)
 
```
n = 90581
e = 17993
c = 12321
```
**Gợi ý**: Khi `d < n^0.25 / 3` (d quá nhỏ so với n), khai triển liên phân số (continued fraction) của `e/n` sẽ "lộ" ra d. Dùng thư viện có sẵn `owiener` (`pip install owiener`) để không phải tự code từ đầu:
```python
import owiener
d = owiener.attack(e, n)
```
 
---
 
## Bài 7 — Chung ước số nguyên tố giữa 2 khóa (Shared Prime / GCD Attack)
 
Hai bài toán RSA khác nhau, nhưng vô tình dùng chung 1 số nguyên tố p:
 
```
n1 = 1699366721
e1 = 65537
c1 = 543216789
 
n2 = 2210911213
e2 = 65537
c2 = 987654321
```
**Gợi ý**: Tính `gcd(n1, n2)`. Nếu kết quả > 1, đó chính là số nguyên tố chung p → suy ra q1 = n1/p, q2 = n2/p → tính được cả 2 private key.
 
---
 
## Bài 8 — n là số chính phương (p = q)
 
```
n = 26602531 
e = 3
c = 15550407
```
**Gợi ý**: Trường hợp hiếm nhưng CTF hay "cài bẫy": nếu p = q, thì `n = p^2` → chỉ cần lấy căn bậc 2 của n để tìm p trực tiếp, không cần factor phức tạp.
```python
import math
p = math.isqrt(n)
assert p * p == n
```
 
---
 
## Bài 9 — Cho biết φ(n) thay vì n bị factor sẵn
 
Đề bài đưa thẳng cho em `n` và `φ(n)` (tình huống giả lập: lộ thông tin phụ):
 
```
n   = 3233
phi = 3120
e   = 17
c   = 2790
```
**Gợi ý**: Từ `n` và `φ(n)`, ta có hệ phương trình:
- p + q = n − φ(n) + 1
- p × q = n
→ Giải phương trình bậc 2: `x² − (p+q)x + n = 0` để tìm p, q.
 
---
 
## Bài 10 — Partial Key Exposure (biết một phần bit của p)
 
```
n = 1000000000000000000000039
e = 65537
c = 123456789012345678901234
# Biết: p bắt đầu bằng các chữ số "1000000000..." (nửa trên của p bị lộ)
```
**Gợi ý**: Đây là dạng nâng cao dùng thuật toán **Coppersmith's Attack** (dựa trên lattice reduction). Không cần tự code từ đầu — dùng thư viện `sympy` kết hợp `sage` (nếu có) hoặc script `coppersmith.sage` có sẵn trên GitHub tìm theo từ khóa "coppersmith small roots factorization". Đây là bài để em làm quen khái niệm, không bắt buộc giải hoàn chỉnh nếu mới bắt đầu.
 
---
 
## ĐÁP ÁN & SCRIPT GIẢI
 
<details>
<summary>👉 Bấm để xem đáp án Bài 1</summary>
```python
from sympy import factorint
n, e, c = 3233, 17, 2790
p, q = list(factorint(n).keys())
phi = (p-1)*(q-1)
d = pow(e, -1, phi)
m = pow(c, d, n)
print(m)  # 65 -> 'A'
```
</details>
<details>
<summary>👉 Bấm để xem đáp án Bài 2</summary>
```python
from sympy import factorint
n = 92565752233748521
e = 65537
c = 15427086843431102
factors = factorint(n)
p, q = list(factors.keys())
phi = (p-1)*(q-1)
d = pow(e, -1, phi)
m = pow(c, d, n)
print(m)
```
Nếu máy chạy lâu, thử copy `n` vào factordb.com để lấy p, q trực tiếp.
</details>
<details>
<summary>👉 Bấm để xem đáp án Bài 3 (Common Modulus)</summary>
```python
from sympy import gcdex
 
n = 143
e1, c1 = 7, 64
e2, c2 = 11, 25
 
a, b, g = gcdex(e1, e2)  # a*e1 + b*e2 = g (g nên = 1)
a, b = int(a), int(b)
 
if a < 0:
    c1 = pow(c1, -1, n)
    a = -a
if b < 0:
    c2 = pow(c2, -1, n)
    b = -b
 
m = (pow(c1, a, n) * pow(c2, b, n)) % n
print(m)
```
</details>
<details>
<summary>👉 Bấm để xem đáp án Bài 4 (Low exponent)</summary>
```python
from gmpy2 import iroot
c = 2716161331923531973844857787479985881975885030509
m, exact = iroot(c, 3)
print(m, exact)  # exact=True nghĩa là m^3 = c chính xác, không qua modulo
```
</details>
<details>
<summary>👉 Bấm để xem đáp án Bài 5 (Fermat)</summary>
```python
import math
n, e, c = 17993, 5, 4441
 
a = math.isqrt(n) + 1
while True:
    b2 = a*a - n
    b = math.isqrt(b2)
    if b*b == b2:
        p, q = a-b, a+b
        break
    a += 1
 
phi = (p-1)*(q-1)
d = pow(e, -1, phi)
m = pow(c, d, n)
print(p, q, m)
```
</details>
<details>
<summary>👉 Bấm để xem đáp án Bài 6 (Wiener)</summary>
```python
# pip install owiener
import owiener
n, e, c = 90581, 17993, 12321
d = owiener.attack(e, n)
m = pow(c, d, n)
print(d, m)
```
</details>
<details>
<summary>👉 Bấm để xem đáp án Bài 7 (Shared Prime)</summary>
```python
from math import gcd
 
n1, e1, c1 = 1699366721, 65537, 543216789
n2, e2, c2 = 2210911213, 65537, 987654321
 
p = gcd(n1, n2)
if p > 1:
    q1 = n1 // p
    q2 = n2 // p
    phi1 = (p-1)*(q1-1)
    d1 = pow(e1, -1, phi1)
    m1 = pow(c1, d1, n1)
    print("p =", p, "| m1 =", m1)
else:
    print("Không tìm thấy ước chung — thử cặp n khác")
```
*(Lưu ý: với bộ số ví dụ trên, em cần thay bằng cặp n thực sự có chung thừa số để thấy kết quả — đây là bài minh họa kỹ thuật, hãy tự tạo cặp n test bằng cách chọn p chung, q1 ≠ q2 khác nhau.)*
</details>
<details>
<summary>👉 Bấm để xem đáp án Bài 8 (n chính phương)</summary>
```python
import math
n, e, c = 26602531, 3, 15550407
p = math.isqrt(n)
assert p*p == n
q = p
phi = p*(p-1)  # công thức φ(p^2) = p(p-1) khi n = p^2
d = pow(e, -1, phi)
m = pow(c, d, n)
print(p, m)
```
</details>
<details>
<summary>👉 Bấm để xem đáp án Bài 9 (biết n và φ(n))</summary>
```python
import math
 
n, phi, e, c = 3233, 3120, 17, 2790
 
# p + q = n - phi + 1 ; p*q = n
s = n - phi + 1  # p + q
# Giải x^2 - s*x + n = 0
disc = s*s - 4*n
sqrt_disc = math.isqrt(disc)
p = (s + sqrt_disc) // 2
q = (s - sqrt_disc) // 2
 
d = pow(e, -1, phi)
m = pow(c, d, n)
print(p, q, m)
```
</details>
<details>
<summary>👉 Bài 10 (Coppersmith) — gợi ý mở rộng thay vì đáp án đầy đủ</summary>
Bài này nâng cao, cần SageMath thực thụ. Nếu em muốn đi sâu, tìm đọc:
- Keyword: "Coppersmith factorization with known high bits of p"
- Thư viện tham khảo: `RsaCtfTool` (GitHub) — công cụ tổng hợp gần như MỌI kiểu tấn công RSA phổ biến, rất đáng cài để dùng trong thi CTF thực tế.
```bash
git clone https://github.com/Ganapati/RsaCtfTool
cd RsaCtfTool
python3 RsaCtfTool.py --publickey key.pub --uncipherfile cipher.txt
```
</details>
---
 
## Bảng tổng hợp: nhìn đề đoán lỗ hổng
 
| Dấu hiệu trong đề | Khả năng cao là dạng tấn công |
|---|---|
| n < ~2^70, không có gì đặc biệt | Factor trực tiếp (factordb/sympy) |
| 2 bản mã, cùng n, khác e | Common Modulus Attack |
| e = 3 hoặc rất nhỏ, message ngắn | Low Exponent (căn bậc e) |
| p, q gần bằng sqrt(n) | Fermat's Factorization |
| d nhỏ bất thường, e lớn gần n | Wiener's Attack |
| Nhiều cặp (n, c) trong 1 đề | Kiểm tra GCD giữa các n (shared prime) |
| n là số chính phương hoàn hảo | p = q, n = p² |
| Đề cho thêm φ(n) hoặc gợi ý nửa bit của p/q | Giải phương trình bậc 2 / Coppersmith |
| Công cụ tổng hợp khi bí | `RsaCtfTool` — thử tự động hết các kiểu tấn công |
 
Chúc em luyện tập vui vẻ và "đập tan" hết các bài CTF RSA! 💪
