---
layout: post
title: "Bypass co che bao mat cua windows defender"
categories: Pentest
tags: [redteam]
---

## Bai nay se giup moi nguoi hieu sau hon ve Windows Internal cung nhu bypass cac co che bao ve

- Một số cơ chế bảo vệ đơn giản mình gặp

+ Real-time Protection: Cơ chế này được tích hợp trong cả Microsoft Defender và các thành phần EDR khác. Chịu trách nhiệm giám sát realtime
+ Windows Defender Offline scan: Quét sâu ở ngoài môi trường hệ điều hành để diệt mã độc cứng đầu.
+ User Account Control (UAC): Cảnh báo và yêu cầu quyền quản trị khi ứng dụng muốn thay đổi hệ thống.
+ SmartScreen: Kiểm tra độ tin cậy của các trang web và tập tin tải về trên internet.
+ Windows Firewall: Lọc các gói tin mạng đến và đi, ngăn chặn kết nối độc hại từ bên ngoài.
+ Core Isolation & VBS: Dùng ảo hóa phần cứng để cô lập nhân hệ điều hành tránh bị tấn công tầng sâu.
+ AMSI,...

Đối với một số phương pháp mình sẽ hướng dẫn cách bypass khác nhau, sẽ update khi nào mình rảnh

1. Bypass UAC: 
Đây không phải kĩ thuật khó nhưng sài khá nhiều

Lạm dụng system configuration để launch một cmd ở s