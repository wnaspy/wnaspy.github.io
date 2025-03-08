---
layout: post
title: "Hướng dẫn tạo blog với Jekyll và Chirpy trên GitHub Pages"
date: 2025-03-08 18:30:00 +0700
categories: blog
tags: [jekyll, chirpy, github, tutorial]
author: "konchan"
---

## 📌 Bước 1: Chuẩn bị môi trường  

Trước khi bắt đầu, hãy đảm bảo bạn đã cài đặt các công cụ cần thiết trên máy tính. Lưu ý mình sẽ làm việc với terminal khá nhiều nên nếu có bạn chưa biết thì cứ mở CMD trên Windows nhé

### 🔹Github  
Đăng kí một tài khoản [tại đây](https://github.com/)
### 🔹Git  
- **Tải Git** từ [git-scm.com](https://git-scm.com/downloads) và cài đặt theo hướng dẫn.  
- Kiểm tra xem Git đã được cài đặt chưa
  ```
  git --version
  ```
  nếu đã cài đặt nó sẽ hiện lên version bản git đã cài, thế là OK

### 🔹Cài đặt Ruby và Bundler

Tải Ruby+Devkit từ [rubyinstaller.org](https://rubyinstaller.org), nên dùng bản mới nhất nhé

Kiểm tra phiên bản Ruby:
```
ruby -v
```

Cài đặt Bundler và Jekyll:

```
gem install bundler jekyll
```

Kiểm tra:
```
bundler -v
jekyll -v
```
🔹 Cài đặt Visual Studio Code (Tùy chọn)

Tải VS Code từ [code.visualstudio.com](https://code.visualstudio.com).
Cài đặt và thêm các extension: Github Pull request.

## 📌 Bước 2: Tạo blog với Chirpy
### 🔹 Tạo kho lưu trữ trên GitHub
Truy cập [cotes2020/chirpy-starter](https://github.com/cotes2020/chirpy-starter).

Nhấn Use this template → Create a new repository.
Đặt tên repo là `<username>.github.io`
Chọn Public, sau đó nhấn Create repository.
### 🔹 Tải mã nguồn về máy

``` 
git clone https://github.com/<username>/<repository-name>.git
```
sau khi đã clone, thì cd vô thư mục của bạn 
```
cd <repository-name>
```
⚠️ Thay <username> và <repository-name> bằng thông tin GitHub của bạn.

🔹 Cài đặt các thư viện cần thiết
```
bundle install
```
## 📌 Bước 3: Cấu hình blog
Mở file _config.yml và chỉnh sửa theo nhu cầu của bạn.
```
title: "Blog của Tôi"
tagline: "Một blog cá nhân với Jekyll và Chirpy"
url: "https://<username>.github.io"
baseurl: "/<repository-name>"  # Để trống ("") nếu dùng <username>.github.io
timezone: Asia/Ho_Chi_Minh
theme: chirpy
lang: vi_VN
author:
  name: "<Tên của bạn>"
  email: "<email@example.com>"
⚠️ Thay <username>, <repository-name>, <Tên của bạn> và <email@example.com> bằng thông tin thực tế.
```
## 📌 Bước 4: Chạy blog trên localhost
Để xem blog trên máy trước khi đưa lên GitHub:

```
bundle exec jekyll serve
```

Mở trình duyệt và truy cập: `http://localhost:4000`

## 📌 Bước 5: Đưa blog lên GitHub Pages
🔹 Cấu hình Git

```
git config --global user.name "Tên của bạn"
git config --global user.email "email@example.com"
```

🔹 Đẩy mã nguồn lên GitHub

```
git add .
git commit -m "Khởi tạo blog với Chirpy"
git push origin main
```
🔹 Kích hoạt GitHub Actions
Truy cập GitHub repository của bạn.
Vào tab Actions, chọn Enable workflows.
Chờ quá trình build hoàn tất, blog sẽ tự động được triển khai! 🎉
## 📌 Bước 6: Truy cập blog
Nếu dùng `<username>.github.io`, blog của bạn sẽ xuất hiện tại:

`https://<username>.github.io`
# 🎯 Kết luận
Bạn đã hoàn tất việc tạo blog với Jekyll và Chirpy! 🚀
Từ bây giờ, bạn có thể viết bài mới bằng cách tạo file .md trong thư mục _posts và đẩy lên GitHub.

Nếu có câu hỏi hay thắc mắc chỗ nào có thể ib mình để được giải đáp