---
layout: post
categories: Pentest
tags: [pentest, immediately, redteam]
---
# Bài 1: Cách virus lây file
Đối với các dòng Ransomware hoặc cơ bản là những mẫu mã độc lây file thường thấy trên mạng, module duyệt file/folderphải diễn ra nhanh chóng để có thể mã hóa hoặc lây lan ra toàn bộ hệ thống người dùng. Tuy nhiên tốc độ duyệt như nào lại phụ thuộc vào thuật toán cũng như ngôn ngữ mà attacker sử dụng. Lấy ví dụ về 1 con mã độc lây file đơn giản mà mình từng phân tích, cách bước sẽ như sau
+) Sửa đổi registry -> không cho view toàn bộ các file ẩn cũng như không hiện đuôi file
+) Ẩn file người dùng hiện tại và thay thế bằng các file exe (application) cùng tên với file gốc. Các file exe này sẽ có cùng icon như file người dùng nhằm lừa người dùng tiếp tục thực thi
-> khi người dùng click, mã độc tiếp tục lây lan UwU
Có thể thấy, việc duyệt cây thư mục hệ thống rất quan trọng trong việc phát triển mã độc, cố lên nhé 