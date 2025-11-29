---
layout: post
title: "Thuật toán và kiến thức"
categories: Pentest
tags: [redteam, devops, OS, PE, system, blueteam, immediately]
---

Thuật toán convert từ decimal sang binary

check số đã cho là chẵn hay lẻ, nếu là chẵn thì tạo tmp = 0; nếu là lẻ thì tạo tmp = 1
Chia số đó cho 2, chỉ lấy số chia, loại bỏ phần dư, nếu số chia = 0, exit
nếu thương khác không và là số chẵn, thêm 0 và đầu tmp, 
Nếu thương khác không và là số lẻ, thêm 1 vào đầu tmp và tiếp tục