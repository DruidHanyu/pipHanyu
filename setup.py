#!/usr/bin/python
#-*- coding:utf-8 -*-

#############################################
# File Name: setup.py
# Author: Hanyu
# Mail: hanyuzhang94@bupt.edu.cn
# Created Time:  2019-7-23 19:17:34
#############################################
from setuptools import setup, find_packages


setup(
    name = "littlebear",
    version = "1.0.0",
    keywords = ("pip", "littlebear", "hanyu"),
    description = " Tool edited by hanyu",
    long_description = "Description in Github: https://github.com/DruidHanyu/littlebear",
    license = "Hanyu",

    url = "https://github.com/DruidHanyu/pipHanyu",
    author = "Hanyu",
    author_email = "zhanghanyu94@bupt.edu.cn",

    packages = find_packages(),
    include_package_data = True,
    platforms = "any",
    install_requires = []
)

