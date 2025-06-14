---
layout: post
categories: [Pentest]
tags: [blueteam, beginner, pentest, redteam, behavier]
---

# Góc nhìn của 1 Redteamer

- Dưới góc độ là một nhà nghiên cứu bảo mật, đặc biệt trong vai trò redteam thì code injection là một trong những thứ mà mình thấy khá thú vị. Việc tạo ra một con malware để đánh cắp thông tin hoặc đơn giản chỉ là quậy phá nhằm thỏa mãn nhu cầu của bản thân là điều mình từng mơ ước. Tuy nhiên, để có cái nhìn bao quát hơn ta phải hiểu blueteam phát hiện mã độc như nào để từ đó update tư duy thay đổi các đoạn mã nhằm persistent một cách yên lặng nhất.

# Góc nhìn của Blueteamer

- Dưới góc độ của blueteam có rất nhiều tool hỗ trợ trong việc rà soát mã độc, hôm nay ta sẽ đi tìm hiểu Windows Sysinternals. Sysinternals tools được tạo ra bởi Mark Russinovich và Bryce Cogswell, có hơn 70 công cụ khác nhau trong bộ suite này nhưng a sẽ target vào 3 cái chính là Process Monitor, Process Explorer và AutoRuns

## 1. Process Explorer cheatsheet
+ View -> Select columns -> show command: Hiện thị command mà mỗi process đang dùng
+ Bất cứ chương trình hợp pháp nào thông thường sẽ có description và company -> không có 1 trong 2 thì nên check nhé
+ Ctrl D: mở DLLs mà process đó load vào 
+ Handle:  process sẽ có các handle như thao tác với Registry, WinAPI
+ Kiểm tra Signature và Virus Total
+ Phân tích string trong 1 file thực thi cũng là một trong những kĩ thuật static dynamic, chúng ta có thêm xem được cả trên đĩa lẫn trong memory (string trong memory chỉ show những chuỗi ánh xạ vào bộ nhớ)

## 2. AutoRuns cheatsheet

Như tên gọi, AutoRuns chính là công cụ sẽ giúp phát hiện nhưng nơi bắt đầu của một hệ thống giúp malware perisist.
+ Options -> Scan options -> Verify

## 3. Process Monitor

{% include embed/youtube.html id="L5vWf5ge15U" %}

