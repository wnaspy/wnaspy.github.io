---
layout: post
title: "COM Hijacking"
categories: Pentest
tags: [readteam]
---

# Mở bài

- Bài này sẽ tóm tắt nhanh kĩ thuật COM Hijacking thông Windows Thumbnail Cache - lợi dụng việc load DLL bằng explorer.exe để thực thi mã độc

# Thân bài 

## COM là gì
## Thứ tự tìm kiếm hive trong Registry

1.	HKEY_CURRENT_USER 
2.  HKEY_LOCAL_MACHINE
3.  HKEY_CLASSES_ROOT 

## Cách thực hiện 

1. Đăng kí một reg trong 

- HKEY_CURRENT_USER (HKCU) – ưu tiên cho user hiện tại Computer\HKEY_CURRENT_USER\Software\Classes\CLSID 

2. Xóa thumbcache 

- Remove-Item -Path "$env:LOCALAPPDATA\Microsoft\Windows\Explorer\thumbcache_*.db" -Force -ErrorAction SilentlyContinue

3. Dung explorer va khoi dong lai

- Stop-Process -Name explorer -Force

- Start-Process explorer.exe

# Uư điểm

- Tránh bị monitor