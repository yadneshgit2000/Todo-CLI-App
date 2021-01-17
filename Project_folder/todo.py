import os
import sys
from datetime import date
today = date.today()

file1 = "todo.txt"
file2 = "done.txt"

def create_files():
	if(not (os.path.isfile(file1) and os.path.isfile(file2))):		#checks whether initially files are present or not 											 
		with open(file1,"w+") as f:					#if not then files will be created
			pass
		with open(file2,"w+") as f:
			pass
	return

def check():
	with open(file1,"r") as f:
		count = 0
		content = f.readlines()
		for line in content:
			count += 1			
	return count

def help():
	print(f'Usage :-')
	print(f'$ ./todo add "todo item"  # Add a new todo')
	print(f'$ ./todo ls               # Show remaining todos')
	print(f'$ ./todo del NUMBER       # Delete a todo')
	print(f'$ ./todo done NUMBER      # Complete a todo')
	print(f'$ ./todo help             # Show usage')
	print(f'$ ./todo report           # Statistics')
	return

def ls():
	global total
	if (total==0):
		print("There are no pending todos!")
		return
	remaining = total 
	with open(file1,"r") as f:
		for line in f:
			print(f'[{remaining}]',line, end="")
			remaining -= 1
	return

def report():
	global total
	with open(file2,"r") as f:
		count = 0
		content = f.readlines()
		for line in content:
			count += 1
	print(today.strftime("%Y-%m-%d"), end=" ")
	print("Pending :",total,"Completed :",count)
	return
	
def add(item):
	with open(file1,"r+") as f:
		lines = f.read()
		f.seek(0,0)
		f.write(item.rstrip('\r\n')+'\n'+lines)
	print(f'Added todo: "{item}"')
	return

def del_fun(number):
	global total
	if(number>total or number<1):
		print(f'Error: todo #{number} does not exist. Nothing deleted.')
		return
	else:
		with open(file1,"r") as f:
			lines = f.readlines()
		del lines[(total-number)]
		with open(file1,"w+") as f:
			for line in lines:
				f.write(line)
		print(f'Deleted todo #{number}')
		total -=1
	return
			
def done_fun(number):
	global total
	if(number>total or number<1):
		print(f'Error: todo #{number} does not exist.')
		return
	else:
		with open(file1,"r") as f:
			lines = f.readlines()
		temp = str(lines[(total-number)])
		temp = f'x {today.strftime("%Y-%m-%d")} {temp}'
		del lines[(total-number)]
		with open(file1,"w+") as f:
			for line in lines:
				f.write(line)
		with open(file2,"r+") as f:
			lines = f.read()
			f.seek(0,0)
			f.write(temp.rstrip('\r\n')+'\n'+lines)
		
		print(f'Marked todo #{number} as done.')
		total -=1
	return
	
if __name__=="__main__":	
	try:
		create_files()		
		total = check()
		command = sys.argv[1]
		if(command =='help'):
			help()

		elif(command =='ls'):
			ls()
			
		elif(command =='report'):
			report()
		try:
			arg = sys.argv[2]
			if (command == 'add'):
				add(arg)
				total += 1
			elif(command == 'del'):
				del_fun(int(arg))
			elif(command == 'done'):
				done_fun(int(arg))
				 
		except IndexError:
			if(command=='add'):
				print("Error: Missing todo string. Nothing added!")
			elif(command=='del'):
				print("Error: Missing NUMBER for deleting todo.")
			elif(command=='done'):
				print("Error: Missing NUMBER for marking todo as done.")
			pass
						
	except IndexError:
		help()
