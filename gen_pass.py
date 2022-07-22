import random,csv,encrypt


upper_case=["W","E","R"",T","Y","I","O","P","L","K","J","G","F","D","S","A","Z","C","V","B","N","M"]
lower_case=["q","w","e","r","y","u","o","p","l","k","j","h","g","f","d","s","a","x","c","b","n","m"]
digits=[5,2,9,6,4,1,3,7,8,0]
punctuation=["~","@","#","$","%","^","&","*","(","+"]


def generator(len_pass):
	options=digits+upper_case+punctuation+lower_case+digits+punctuation+lower_case+upper_case+digits
	pass_word=[]
	for i in range(0,len_pass+1):
		word=random.choice(options)
		pass_word.append(word) 
	print("\nYOUR PASSWORD:",end="")
	for i in pass_word:
		print(i,end="")
	print("\n")


def csv_writer(username,e_mail_id,password,web_name):
	row=[username,e_mail_id,password,web_name]

	with open("First_Pass.csv", 'a') as file:
		csv_write= csv.writer(file)
		csv_write.writerow(row)
		file.close()


def csv_reader():

	print("Username\tEmail\t\tPassword\t\t Website")
	a=0
	with open("First_Pass.csv", 'r') as csvfile:
		csvreader = csv.reader(csvfile)
		for row in csvreader:
			pass_w=encrypt.decode(row[2])
			print(f"{row[0]}\t\t{row[1]}\t\t\t{pass_w}\t\t\t{row[3]}")
	csvfile.close()
























	

	


