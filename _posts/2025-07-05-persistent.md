---
layout: post
title: "Dll injection"
categories: [Pentest]
tags: [beginner, pentest, redteam, PE]
---

# DLL injection là gì?
- Như một hacker chuyên nghiệp thì DLL Injection là một trong những kĩ thuật cơ bản để persist.
1. Tại sao lại DLL injection??
Thông thường nếu inject một file exe thì sẽ dễ bị detect nếu rà soát, tuy nhiên nếu inject dll vào các tiến trình hợp pháp như svchost.exe hay các tiến trình hệ thống, nếu rà soát không kĩ có thể dễ dàng bỏ lỡ bởi nó sẽ ít bị để ý hơn .exe
2. Real case
Tôi gặp 1 case trong quá trình làm lab với bạn, attacker inject vô ctf loader -> khó bị phát hiện
3. Các hàm thực hiện
----------
OpenProcess: Mo 1 process
VirtualAllocEx: Cap phat bo nho
WriteProcessMemory: Viet vao
GetProcAddress
CreateRemoteProcess: 
CloseHandler:

---------
create Threadshellcode

virtuAlloc
memcpy
convert thanh ham con tro

-------------

lay duong dan dll