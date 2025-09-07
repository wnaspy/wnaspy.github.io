---
layout: post
title: "Crackmes, cuộc tình ngang trái giữa reverse và pwn"
categories: Pentest
tags: [pentest, redteam, system, reverse]
---

# Lời nói đầu
- Bài này sẽ tổng hợp quá trình mình thực hành và làm trên crackmes
# Challenges
- pass giải né: crackmes.one
- 1. Very easy disassembly execise
+ Định dạng pe32, loại console, code C, compiler MingG, mode 32bit
debug bằng x32dbg
pass: 124816
- 2. good girl	
+ Định dạng ELF64, kiến trúc AMD64, mode 64bit
- 3. korshunK's Very easy
+ Định dạng PE64, kiến trúc AMD64, mode64 bit
debug bằng x64dbg, ida pro
pass: your mum is very sexy
- 3. danek228's easy crackme 2.0
+ Định dạng PE64, kiến trúc I368, mode32 bit
debug bằng x632bg
pass: your mum is very sexy