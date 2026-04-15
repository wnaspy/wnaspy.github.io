---
layout: post
title: "Vì sao nói viết malware là nghệ thuật lập trình socket"
categories: RedTeam
tags: [Readteam]
---

# Mở bài
## Như mình đã nói, làm thế nào để ransomware mã hóa dữ liệu một cách nhanh chóng

- Như chúng ta đã biết, Ransomware là một loại mã độc tống tiền, nó mã hóa các file của người dùng và yêu cầu tiền chuộc

Tuy nhiên các nhóm Ransomware đều sẽ có một quy trình tấn công cơ bản như sau:

+ Chọn các file mục tiêu quan trọng: Ransomware không mã hóa tất cả các file, chúng sẽ chỉ chọn những file nhạy cảm, lưu nhiều dữ liệu như .exe, .bak, .docx, .pdf,...Việc lựa chọn mục tiêu và loại bỏ các chướng ngại làm tăng tốc đáng kể khả năng tấn công
+ Kĩ thuật mã hóa: Bên cạnh đó, ransomware sẽ phát triển các thuật toán mã hóa khác nhau, phải đủ mạnh để không thể bẻ khóa và phải đủ nhanh để có thể chạy
+ Mã hóa 1 phần dữ liệu: Ransomware không mã hóa toàn bộ file, chúng có thể lựa chọn mã hóa phần đầu, phần giữa hoặc phần cuối.
+ Loại bỏ mục tiêu: Với các file đã bị mã hóa, thông thường sẽ có những dấu hiệu nhận diện để tránh mã hóa lại, có thể đặt magic header tùy nhóm
... Mình sẽ nói tiếp nếu có thời gian