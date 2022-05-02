#!/bin/env python
#-*- coding: utf-8 -*-

import platform
import multiprocessing

print("운영체제",platform.system())
print("운영체제의 상세정보",platform.platform())
print("운영체제 버전",platform.version())
print("프로세서",platform.processor())
print("cpu수", multiprocessing.cpu_count())
