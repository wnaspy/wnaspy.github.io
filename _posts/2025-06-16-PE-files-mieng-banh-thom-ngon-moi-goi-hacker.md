---
layout: post
title: "PE files - miếng bánh mật thơm ngon mà hacker nào cũng nên biết"
categories: Blueteam
tags: [beginner, pentest, redteam, PE]
---

# Lời nói đầu

Khi đã gia nhập vào thị trường lao động cạnh tranh khắc nghiệt nhất hành tinh - REDTEAM, bất kì một nắc cơ nào cũng phải biết đến file thực thi trên từng hệ điều hành. Linux thì có ELF, MAC thì MACH-O còn Windows thì có PE. Dễ hiểu thì phần lớn người dùng máy tính, hệ thống thông tin trên toàn thế giới đều dùng Windows nên việc nhắm target là người dùng Windows luôn được tin tặc khai thác mạnh mẽ

## 1. PE file là gì??

PE file là một định dạng riêng của Windows. Tất cả các file có thể thực thi được trên Windows(ngoại trừ VxDs và các loại file Dlls 16bit) đều sử dụng định dạng PE.

Vậy tại sao chúng ta lại cần phải tìm hiểu về PE file ? Có 2 lý do chính như sau: Nếu chúng ta muốn thêm các đoạn code vào trong những file thực thi hoặc nếu muốn unpacking bằng tay(manual unpacking) các file thực thi thì chúng ta cần hiểu rõ về PE file để can thiệp vào.

## 2. Cấu trúc 1 PE file cơ bản
![Parrot OS](/images/PE/2025-06-16_01-32.png)
Một file PE sẽ gồm 2 phần: Header và Sections
- Header:
    + DOS header
    + PE header
    + Section table
- Sections

## 3. Các kĩ thuật inject
Một trong những kĩ thuật mà mình biết là sẽ chèn shellcode độc hại vô chương trình hợp pháp, cách này giúp mã độc thực thi nhưng tránh bị phát hiện. Mã độc sẽ tạo 1 section mới, injection shellcode vào đây sau đó trỏ entrypoint vào vị trí này để chương trình thực thi, cuối cùng qua quay về entrypoint của chương trình gốc
{% include embed/youtube.html id="L5vWf5ge15U" %}

