import os

current_working_dir = os.getcwd()

files = os.listdir(current_working_dir)

for f in files:
	print(f)