"""
The MIT License (MIT)

Copyright (c) 2020 Viktor "Los Skillos" Pabjan

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
""" 

#Tin programming language
#Jesus why am I wasting time by creating this
osn = "win"
import os
import sys
import time
at = False
parts = {}
if sys.argv[1] != '':
	filepath = sys.argv[1]
else:
	filepath = 'test.tin'
attype = ""
vrb = {}

with open(filepath) as f:
    content = f.readlines()
content = [x.strip() for x in content] 
cnt = 0
vrb["result"] = 0
num = 0
ispart = False
scancont = content
while num != len(scancont):
	readline = scancont[num]
	if ispart:
		parts[readline] = num
		ispart = False
	else:
		if readline == "part":
			ispart = True
	num = num + 1

while cnt != len(content):
	readline = content[cnt]
	if at:
		if attype == "cmd":
			os.system(readline)
			at = False
			attype = ""
		if attype == "clear_setup":
			osn = readline
			at = False
			attype = ""
		if attype == "clear":
			if osn == "win":
				os.system("cls")
			if osn == "linux":
				os.system("clear")
			at = False
			attype = ""
		if attype == "type":
			print(readline)
			at = False
			attype = ""
		if attype == "type_var":
			print(vrb[readline])
			attype = ""
			at = False			
		if attype == "input":
			vrb["input"] = input()
			at = False
			attype = ""
		if attype == "var_data":
			var_data = readline
			vrb[var_name] = var_data
			attype = ""
			at = False
		if attype == "var_name":
			var_name = readline
			attype = "var_data"
		if attype == "var_count_2":
			var2 = int(vrb[readline])
			if op == "a":
				vrb[str(var1)] = var1 + var2
			if op == "m":
				vrb[str(var1)] = var1 * var2
			if op == "s":
				vrb[str(var1)] = var1 - var2
			if op == "d":
				vrb[str(var1)] = var1 / var2
			at = False
			attype = ""
		if attype == "var_count_op":
			op = readline
			attype = "var_count_2"
		if attype == "var_count":
			var1 = int(vrb[readline])
			attype = "var_count_op"
		if attype == "wait":
			wait = int(readline)
			time.sleep(wait)
			at = False
			attype = ""
		if attype == "var_input":
			inpvar = readline
			vrb[inpvar] = input()
			at = False
			attype = ""
		if attype == "goto":
			cnt = int(parts[readline])
			at = False
			attype = ""
	else:
		if readline == "goto":
			at = True
			attype = "goto"
		if readline == "cmd":
			at = True
			attype = "cmd"
		if readline == "var_input":
			at = True
			attype = "var_input" 
		if readline == "clear_setup":
			at = True
			attype = "clear_setup"
		if readline == "clear":
			at = True
			attype = "clear"
		if readline == "input":
			at = True
			attype = "input"
		if readline == "wait":
			at = True
			attype = "wait"
		if readline == "type":
			at = True
			attype = "type"
		if readline == "var":
			at = True
			attype = "var_name"
		if readline == "type_var":
			at = True
			attype = "type_var"
		if readline == "var_count":
			at = True
			attype = "var_count"
	cnt = cnt + 1
