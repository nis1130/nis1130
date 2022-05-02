#!/usr/bin/env python3

from subprocess import *
from pyrsistent import b
from xlsxwriter import *

cmd = "vmstat 1 5 | awk '{now=strftime(\"%Y-%m-%d %T \"); print now $0}'"
p = Popen(cmd, shell=True, stdout=PIPE)
(ret, err) = p.communicate()

workbook1 = Workbook('vmstat.xlsx')
worksheet = workbook1.add_worksheet()
rows = (ret.split(b"\n"))

for row_idx, row in enumerate(rows):
    colums = row.split()
    for col_idx , col in enumerate(colums):
        worksheet.write(row_idx, col_idx, col)
workbook1.close()
