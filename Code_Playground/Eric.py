
while True:
			name = input("What's your name? \n")
			if name.isdigit():
				print("Number Error")
				break
			elif name == "Bruno" or name == "bruno":
				print("Hello " + name)
				break
			else:
				print("Huh? ")		
	
#elif name == "Bruno" or name == "bruno":
#	print("God is that you?")		
#else:
#	print("Liar")
