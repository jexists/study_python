#!usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import shutil
from PIL import Image
import hashlib

import sys
sys.path.append('./')

for (dirpath, dirnames, filenmaes) in os.walk(r"./uniform_image"):
  for file in filenmaes:
    # 대문자-팀_시즌-시즌_홈어웨이숫자_번호.확장자
    # 예) Manchester-United_2020-2021_1.jpg
    original_image = dirpath + '/' + file
    bg_removed_image = os.path.splitext(original_image)[0] + '_remove.png'

    # 이미지 사이즈 받기
    image = os.path.abspath(os.path.join(dirpath, file))
    with Image.open(image) as image:
      width, height = image.size

    # 원본 이미지 사이즈 확인 후 리사이즈 900
    if width >= 1200 or height >= 900:
      print("용량확인")
      print("width",width)
      print("height",height)
      # image = Image.open(image)
      # image = image.resize((300, 300))




    # 저장할 경로 없으면 생성
    save_path = './final_image/'
    if not os.path.exists(save_path):
      os.mkdir(save_path)

    # 원본 이미지 복사
    shutil.copy(original_image, save_path)

  break
