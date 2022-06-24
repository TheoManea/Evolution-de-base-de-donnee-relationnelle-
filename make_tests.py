from glob import glob
import os 

# première étape on créer les bd
def create_bd():

	for i in range(0,10):
		try:
			os.mkdir(f"tests/bd{i}/")
			os.system(f"python create_bd.py tests/bd{i}/village")
			os.system(f"python insertRandomValue.py tests/bd{i}/village")
		except:
			pass

def run_test():
	dir_list = glob("tests/*/", recursive = True)
	copy = []

	for i in range(0,len(dir_list)):
		try:
			copy.append(dir_list[i].replace("\\","/"))
		except:
			pass

	for i in range(0,len(copy)):
		print(f"test n°{i} : ")
		os.system(f"python bruteforce.py {copy[i]}village")


if __name__ == '__main__':
	create_bd()
	run_test()