---
layout: post
title: "Pytorch cài đặt cho người mới bắt đầu"
categories: Blueteam
tags: [blueteam, beginner, system, devops]
---

# Lời nói đầu
Bài này sẽ hướng dẫn mọi người cài đặt pytorch cho đỡ rác máy trên anaconda. Tao ghét ML, tao ghét big data, tao ghét mọi thứ liên quan đến biến đổi đơn vị
# 
Mình sẽ coi như mọi người đã cài đặt anaconda thành công và add vào biến môi trường rồi
1. 
conda create -n torch_env python=3.11
2. 
conda activate torch_env
3. 
conda install pytorch::pytorch
conda install ipykernel
4. 
python -m ipykernel install --user --name=torch_env --display-name "Python (PyTorch)"
5. 
conda env remove --name <env>
6. 
conda env list