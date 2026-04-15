---
layout: post
title: "DLL side loading trong mã độc"
categories: RedTeam
tags: [Readteam]
---

# Mở bài

## Trước khi nói về DLL side loading - một trong những kĩ thuật được malware sử dụng phổ biến thì chúng ta hãy cùng tìm hiểu về DLL. Vậy DLL là gì???

DLL (viết tắt của Dynamic Link Library – Thư viện liên kết động) là một tệp tin chứa mã lệnh và dữ liệu có thể được nhiều chương trình khác nhau trên Windows cùng sử dụng. Hãy tưởng tượng bạn có một tủ dụng cụ chung (tệp DLL) đựng búa, kéo, tua vít. Thay vì mỗi người thợ (mỗi chương trình) phải tự rèn lấy búa, kéo riêng, họ chỉ cần ra tủ chung lấy dùng khi cần. Điều này giúp tiết kiệm không gian và tránh trùng lặp. Lý do mà mã độc sử dụng dll là vì nó rất dễ dùng, nó có thể dùng hijacking, sideload, tránh phồng file,...


## DLL Side Loading là gì??
DLL side loading là kĩ thuật mã độc sẽ sử dụng những file exe hợp pháp để load DLL độc hại của nó. Đúng vậy bạn không nghe nhầm đâu, malware sẽ dùng các file.exe hợp pháp để load các các thư viện dll độc hại 

Hãy hình dung như sau: Một file konchan.exe gọi abc.dll và tải hàm hehe() 

Tuy nhiên thay vì gọi đến hàm hehe trong abc.dll của hệ thống, kẻ tấn công sẽ tạo 1 file abc.dll khác có cùng hàm hehe() được export, nhưng logic của hàm này do attacker kiểm soát. Để hiểu vấn đề này chúng ta cần phải hiểu thứ tự ưu tiên mà hệ điều hành load

Mình không nói trong trường hợp set cứng đường dẫn mà là trong trường hợp đường dẫn ko set cứng, thứ tự ưu tiên sẽ diện ra như sau:

Thông thường, thứ tự tìm kiếm DLL trên Windows (từ cao xuống thấp):

1. Thư mục chứa file EXE của ứng dụng.

2. Thư mục hệ thống (System32).

3. Thư mục hệ thống (SysWOW64 nếu ứng dụng 32-bit trên 64-bit).

4. Thư mục Windows.

5. Thư mục hiện tại (current working directory) - nhưng có thể thay đổi tùy chế độ.

6. Các thư mục trong biến môi trường PATH.


Hiểu về vấn đề mày rồi chứ. Do bình thường trong thư mục hiện tại chứa file konchan.exe không có abc.dll nên sẽ tìm trong System32. Tuy nhiên attacker có rất nhiều cách. Một trong số đó là copy file hợp pháp ra một thư mục riêng và thêm file .dll cùng tên mà file thực thi được copy ra gọi đến, lúc này thường sẽ kết hợp cơ chế persistent cơ mà mình sẽ không nói đến nó. Khi chương trình tại thư mục đôc hại đó chạy, file dll độc hại được load đến -> hàm được gọi -> trigger code bẩn

Một cách khác đó là dùng các file hợp pháp, như đính kèm phần mềm AI của bên hợp pháp và cài sẵn .dll độc hại vào trong đó. Nhớ về thứ tự ưu tiên rồi chứ :))) Dll cũng được kích hoạt khi chạy chương trình

Dieu nay cung thuong thay trong trojan horse, nguy trang duoi phan hop phap, khi scan normal user se chu y den cac file .exe ma khong de y file .dll. Khi scan tren virus total, cac file .exe do thong thuong se la file sach nen antivirus khong detect duoc :v 

Thx for reading