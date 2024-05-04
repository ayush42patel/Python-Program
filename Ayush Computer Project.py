import csv, os, datetime, time
from termcolor import colored
from prettytable import from_csv, PrettyTable

#fontcolors using termcolor
class fontcolor():
	def green(string):
		return colored(string, "green", attrs=['bold'])
	def white(string):
		return colored(string, "white", attrs=['bold'])
	def yellow(string):
		return colored(string, "yellow", attrs=['bold'])
	def cyan(string):
		return colored(string, "cyan", attrs=['bold'])
	def red(string):
		return colored(string, "red", attrs=['bold'])
	def blue(string):
		return colored(string, "blue", attrs=['bold'])

#smb ==> symbols
class smb:
	WARN = fontcolor.red(" [-] ")
	DONE = fontcolor.green(" [+] ")
	INPUT = fontcolor.cyan(" [»] ")
	INFO = fontcolor.yellow(" [!] ")
	ARROW = fontcolor.cyan(" > ")

banr = '''
|-------------------------------------------------------------------------------|
|                                                                               |
|  STUDENTS OF CLASS 12 A PRIYANSH KHARE,AYUSH PATEL AND PREM SINGH PRESENTS    |
|            ╔══╗  ╦═══╦   ╔═╗     BANK                                         |
|            ║══║  ║ ║ ║   ╚═╗     MANAGEMENT                                   |
|            ╚══╩  ╚   ╚   ╚═╝     SYSTEM                                       |
|                                                                               |
|-------------------------------------------------------------------------------|
          '''

def banner():
	print(fontcolor.cyan(banr))

class num:
  one = fontcolor.yellow("[1]")
  two = fontcolor.yellow("[2]")
  three = fontcolor.yellow("[3]")
  four = fontcolor.yellow("[4]")
  five = fontcolor.yellow("[5]")
  six = fontcolor.yellow("[6]")
  seven = fontcolor.yellow("[7]")
  eight = fontcolor.yellow("[8]")
  nine = fontcolor.yellow("[9]")

def border_msg(msg):
    row = len(msg)
    m = ''.join(['        +'] + ['-' *row] + ['+'])
    h = fontcolor.cyan(m)
    result= h + '\n' + fontcolor.cyan("        |") + fontcolor.white(msg) + fontcolor.cyan("|") + '\n' + h
    print((result))

choice_one = fontcolor.white("Create a NEW Account")
choice_two = fontcolor.white("View all Accounts in Database")
choice_three = fontcolor.white("Search for an Account in Database")
choice_four = fontcolor.white("Modify an Account in Database")
choice_five = fontcolor.white("Remove an Account from Database")
choice_six = fontcolor.white("Project Development Team")
choice_seven = fontcolor.white("Loan Procedure")
choice_eight = fontcolor.white("Quit")
choice_nine = fontcolor.white("Delete Database")

#choice menu 
def display_menu():
	 banner()
	 border_msg(" Welcome To Bank Management System ! ")
	 print("\n" + smb.ARROW + fontcolor.cyan("CHOOSE AN OPTION :") + "\n")
	 print(smb.ARROW + num.one + choice_one)
	 print(smb.ARROW + num.two + choice_two)
	 print(smb.ARROW + num.three + choice_three)
	 print(smb.ARROW + num.four + choice_four)
	 print(smb.ARROW + num.five + choice_five)
	 print(smb.ARROW + num.six + choice_six)
	 print(smb.ARROW + num.seven + choice_seven)
	 print(smb.ARROW+ num.eight + choice_eight)
	 print(smb.ARROW+ num.nine + choice_nine)

raw_database = 'raw_data.csv'
bank_database = 'bank.csv'

#function for clearing screen
def clr_scr():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')

#press enter to continue message
def continue_msg():
	input("\n" + smb.ARROW + fontcolor.cyan("Press Enter To Continue : "))
	clr_scr()

##### validation functions #####
def validate_name(name):
	if name.replace(" ", "").isalpha():
		pass
	else:
		print("\n" + smb.WARN + fontcolor.red("Name Is Invalid ! It Should Not Have Digits !"))
		quit()

def validate_class(value):
	valid_classes = ('C','S')
	if value in valid_classes:
		pass
	else:
		print("\n" + smb.WARN + fontcolor.red("Invalid Class !"))
		quit()

def validate_accnum(accnum):
	try:
		acc = int(accnum)
	except ValueError:
		print("\n" + smb.WARN + fontcolor.red("Acount Number Must Be A Number !"))
		quit()

def validate_dob(dob):
	try:
		date_of_birth = datetime.datetime.strptime(dob, "%d/%m/%Y")
	except:
		print("\n" + smb.WARN + fontcolor.red("Incorrect date ! Valid Format Is (DD/MM/YYYY)"))
		quit()

def validate_sex(sex):
	valid_sexes = set('mftMFT')
	if sex in valid_sexes:
		pass
	else:
		print("\n" + smb.WARN + fontcolor.red("Invalid Gender !"))
		quit()

def validate_phonenum(phonenum):
	if len(phonenum) == 10:
		try:
			phone = int(phonenum)
		except ValueError:
			print("\n" + smb.WARN + fontcolor.red("Phone Number Must Not Contains Letters !"))
			quit()
	else:
		print("\n" + smb.WARN + fontcolor.red("It Must Contain 10 Digits !"))
		quit()
def validate_loan(loan_num):
  if loan_num.isalpha():
    print("\n" + smb.WARN + fontcolor.red ("Only Numeric Values allowed!"))
    quit()

# main-function-1
#function to add accounts in database
def add_user():
	print("\n")
	border_msg(" Add A New User's Account Information To Database ")
	print("\n")
	stu_name = input(smb.DONE + fontcolor.green("Account Holder's Name : "))
	validate_name(stu_name)
	stu_father = input(smb.DONE + fontcolor.green("Father's Name : "))
	validate_name(stu_father)
	stu_class = input(smb.DONE + fontcolor.green("Account Type (C or S) : "))
	validate_class(stu_class)
	acc_num = input(smb.DONE + fontcolor.green("Account No : "))
	validate_accnum(acc_num)
	stu_dob = input(smb.DONE + fontcolor.green("DOB (DD/MM/YYYY) : "))
	validate_dob(stu_dob)
	stu_sex = input(smb.DONE + fontcolor.green("Sex (M/F/T) : "))
	validate_sex(stu_sex)
	phone_num = input(smb.DONE + fontcolor.green("Phone No of User (+91) : "))
	validate_phonenum(phone_num)
	
	user_data = []
	user_data.append(stu_name)
	user_data.append(stu_father)
	user_data.append(stu_class)
	user_data.append(acc_num)
	user_data.append(stu_dob)
	user_data.append(stu_sex)
	user_data.append(phone_num)

	header = ['Account Holder','Father','Account Type','Account No','DOB','Sex(M/F/T)','Phone']
	with open(raw_database, 'a') as f:
		writer = csv.writer(f)
		writer.writerow(i for i in header)
		writer.writerows([user_data])
		f.close()
	
    #removing duplicate headers and writing new file 'user.csv'
	inFile = open(raw_database, 'r')
	outFile = open(bank_database, 'w')
	listLines = []
	for line in inFile:
		if line in listLines:
			continue
		else:
			outFile.write(line)
			listLines.append(line)
	outFile.close()
	inFile.close()
	
	try:
		x = PrettyTable()
		x.field_names = header
		x.add_row([user_data[0],user_data[1],user_data[2],user_data[3],user_data[4],user_data[5],user_data[6]])
		print("\n" + smb.DONE + fontcolor.green("Quick Overview :"))
		print(fontcolor.white(x))
		print("\n" + smb.DONE + fontcolor.green("Data Saved Successfully !"))
	except Exception:
		print("\n" + smb.WARN + fontcolor.red("Something Went Wrong ! Check Your Code !"))
	finally:
		continue_msg()

# main-function-2
#function to view the list of users in database
def view_users():
	print("\n")
	border_msg(" Total Account Holder's Record In Our Bank Management System ")
	try:
		fp = open(bank_database, "r")
		file = from_csv(fp)
		fp.close()
		print(file)
	except (csv.Error, FileNotFoundError):
		print("\n" + smb.WARN + fontcolor.red("Something Went Wrong ! Check 'users.csv' File !"))
	finally:
		continue_msg()

# main-function-3
#function to search user with account num
def search_user():
	print("\n")
	border_msg(" Search for an Account Inside the Database ")
	roll = input("\n" + smb.DONE + fontcolor.green("Enter Account No. To Search : "))
	try:
		fd = open(bank_database, "r", encoding="utf-8")
		reader = csv.reader(fd)
		for row in reader:
			if len(row) > 0:
				if roll == row[3]:
					print("\n")
					print(fontcolor.green("\t----- Account FOUND -----") + "\n")
					print(smb.DONE + fontcolor.green("Account Holder's Name : ") + row[0])
					print(smb.DONE + fontcolor.green("Father's Name : ") + row[1])
					print(smb.DONE + fontcolor.green("Class : ") + row[2])
					print(smb.DONE + fontcolor.green("Roll No : ") + row[3])
					print(smb.DONE + fontcolor.green("DOB (DD/MM/YYYY) : ") + row[4])
					print(smb.DONE + fontcolor.green("Sex (M/F/T) : ") + row[5])
					print(smb.DONE + fontcolor.green("Phone No : ") + row[6])
					break
		else:
			print("\n" + smb.WARN + fontcolor.red("user Not Found In Our Database !!!"))
		
	except FileNotFoundError:
		print("\n" + smb.WARN + fontcolor.red("No Records To Search !"))
	finally:
		continue_msg()

#main-function-4
#function to update user data
def update_user():
    print("\n")
    border_msg(" Update user's Record In Database ")
    roll_num = input("\n" + smb.DONE + fontcolor.green("Enter Account No. To Update : "))
    try:
    	index_user = None
    	updated_data = []
    	fe = open(user_database, "r", encoding="utf-8")
    	reader = csv.reader(fe)
    	counter = 0
    	
    	for row in reader:
    		if len(row) > 0:
    			if roll_num == row[3]:
    				index_user = counter
    				print("\n" + fontcolor.green('\t----- RECORD FOUND -----') + "\n")
    				print(smb.DONE + fontcolor.cyan("User Found At Index =>"), index_user)
    				print(smb.DONE + fontcolor.cyan("Account Holder's Name =>"), row[0])
    				user_data = []
    				print("\n")
    				
    				new_stu_name = input(smb.DONE + fontcolor.green("Enter user's New Name : "))
    				validate_name(new_stu_name)
    				new_stu_father = input(smb.DONE + fontcolor.green("Enter Father's New Name : "))
    				validate_name(new_stu_father)
    				new_stu_class = input(smb.DONE + fontcolor.green("Enter New Account Type : "))
    				validate_class(new_stu_class)
    				new_roll_num = input(smb.DONE + fontcolor.green("Enter New Account No : "))
    				validate_rollnum(new_roll_num)
    				new_stu_dob = input(smb.DONE + fontcolor.green("Enter New DOB (DD/MM/YYYY) : "))
    				validate_dob(new_stu_dob)
    				new_stu_sex = input(smb.DONE + fontcolor.green("Enter New Sex (M/F/T) : "))
    				validate_sex(new_stu_sex)
    				new_phone_num = input(smb.DONE + fontcolor.green("Enter New Phone No (+91) : "))
    				validate_phonenum(new_phone_num)
    				
    				user_data.append(new_stu_name)
    				user_data.append(new_stu_father)
    				user_data.append(new_stu_class)
    				user_data.append(new_roll_num)
    				user_data.append(new_stu_dob)
    				user_data.append(new_stu_sex)
    				user_data.append(new_phone_num)

    				updated_data.append(user_data)
    			
    			else:
    				updated_data.append(row)
    			counter += 1
    
    except FileNotFoundError:
    	print("\n" + smb.WARN + fontcolor.red("No Records To Update !"))

#writing update to csv file
    if index_user is not None:
        with open(user_database, "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(updated_data)
            print("\n" + smb.DONE + fontcolor.green("Data Updated Successfully ! "))
            continue_msg()
    else:
        print("\n" + smb.WARN + fontcolor.red("user Not Found In Our Database !!!"))
        continue_msg()
        
# main-function-5
#function to delete user record
def delete_user():
    border_msg(" Delete user's Record From Database ")
    roll = input("\n" + smb.WARN + fontcolor.red("Enter Roll No. To Delete : "))
    
    try:
    	user_found = False
    	updated_data = []
    	ff = open(user_database, "r", encoding="utf-8")
    	reader = csv.reader(ff)
    	counter = 0
    	for row in reader:
    		if len(row) > 0:
    			if roll != row[3]:
    				updated_data.append(row)
    				counter += 1
    			else:
    				user_found = True
    
    except FileNotFoundError:
    	print("\n" + smb.WARN + fontcolor.red("No Records To Delete !"))

    if user_found is True:
        with open(user_database, "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(updated_data)
        print("\n" + smb.DONE + fontcolor.green("Roll No. Deleted Successfully"))
        continue_msg()
    else:
    	print("\n" + smb.WARN + fontcolor.red("Roll No. Not Found In Our Database !!!"))
    	continue_msg()

#main-function-6
#about us
def about_us():
	print("\n")
	border_msg(" Project Development Team ")
	#print("\n")
	z = PrettyTable()
	field_1 = fontcolor.green("Team Member")
	field_2 = fontcolor.green("Designation")
	field_3 = fontcolor.green("Standard")
	z.field_names = [field_1,field_2,field_3]
	
	z.add_row(['Priyansh Khare', 'Developer','XII A'])
	z.add_row(['Ayush Patel', 'Developer','XII A'])
	z.add_row(['Prem Singh', 'Developer','XII A'])

	print(z)
	continue_msg()

#main-function-7
#Loan Procedure
def Loan():
    print('\n')
    border_msg('Loan Procedure')
    z=PrettyTable()
    field_1=fontcolor.green("Name")
    field_2=fontcolor.green("Phone num")
    field_3=fontcolor.green("Account no:")
    field_4=fontcolor.green("Address")
    field_5=fontcolor.green('Loan ammount')
    field_6=fontcolor.green("Simple inerest")
    field_7=fontcolor.green("Compound interest")
    z.field_names=[field_1,field_2,field_3,field_4,field_5,field_6,field_7]
    rate=int(input("Enter Rate : "))
    Time=int(input("Enter time : "))
    stu_name = input(smb.DONE + fontcolor.green(" Holder's Name : "))
    validate_name(stu_name)
    acc_num = input(smb.DONE + fontcolor.green("Account No : "))
    validate_accnum(acc_num)
    phone_num = input(smb.DONE + fontcolor.green("Phone No of User (+91) : "))
    validate_phonenum(phone_num)
    add=input(smb.DONE + fontcolor.green("Address :"))
    loan_num=int(input(smb.DONE + fontcolor.green("Loan Amount :")))
    n=loan_num*rate*Time/100
    si=n
    for i in (0,Time):
      m=loan_num*rate*Time/100
      m=m+m
    ci=m
    user_data = []
    user_data.append(stu_name)
    user_data.append(phone_num)
    user_data.append(acc_num)
    user_data.append(add)
    user_data.append(loan_num)
    user_data.append(si)
    user_data.append(ci)
    header=['Name','Account no','Phone no','Loan Amount','Simple interest','Compound interest']
    with open('Loan database','w') as f:
      writer=csv.writer(f)
      writer.writerow(i for i in header)
      writer.writerows([user_data])
      f.close()

      print(f"Loan Required :- {loan_num} Debt Duration :- {Time} Interest % :- {m} {stu_name} you will have to pay {loan_num + n} until {Time}")

#main-function-8
#delete-database
def delete():
  file = 'bank.csv'
  if(os.path.exists(file) and os.path.isfile(file)):
    os.remove(file)
    print("Database Permanently Deleted")
  else:
    print("Database not Found")
  file1 = 'raw_data.csv'
  if(os.path.exists(file1) and os.path.isfile(file1)):
    os.remove(file1)


#looping the whole program
while True:
  print("+-------------------------------------+")
  choice=input("You want to start using BMS ? (Y/N) : ")
  print("+-------------------------------------+")
  if choice == "Y" or choice=="Yes" or choice=="y":
    display_menu()
    
    choice = input("\n" + smb.ARROW + fontcolor.cyan("Enter Your Choice : "))
    if choice == '1':
        add_user()
    elif choice == '2':
        view_users()
    elif choice == '3':
        search_user()
    elif choice == '4':
        update_user()
    elif choice == '5':
        delete_user()
    elif choice == '6':
    	about_us()
    elif choice == '7':
      Loan()
    elif choice == '8':
    	print("\n" + smb.DONE + fontcolor.green('''
      |----------------------------------------------------|
      |                                                    |
      |     Thanks For Using Our Bank Management System    |
      |                                                    |
      |----------------------------------------------------|
      '''))
    	print(smb.WARN + fontcolor.red('''
      |-------------------------------------------|
      |                  Quitting....             |
      |-------------------------------------------|
      '''))
    	time.sleep(2)
    	quit()
    elif choice == '9':
      delete()
  elif choice=="N" or choice=="No" or choice=="n":
    	print("\n" + smb.DONE + fontcolor.green('''
      |----------------------------------------------------|
      |                                                    |
      |    Thanks For Using Our Bank Management System     |
      |                                                    |
      |----------------------------------------------------|'''))
    	print(smb.WARN + fontcolor.red(''''
      |-------------------------------------------|
      |                 Quitting....              |
      |-------------------------------------------|
      '''))
    	time.sleep(2)
    	quit()
  else:
    print('''
    |------------------------------------------|
    |                                          |
    |     Please enter a valid option (Y/N)    |
    |                                          |
    |------------------------------------------|
    ''')
