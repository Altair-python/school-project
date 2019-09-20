from tkinter import *
from tkinter import ttk
from time import sleep,localtime,time
import sqlite3
from colorama import Fore,Style,init
from tkinter import messagebox
from multiprocessing import Process
from collections import Counter
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import ssl
import pickle
import logging
from sys import platform
import os

current_plat=platform

if current_plat=='linux' or current_plat=='darwin':
	logfile_p='logfile.log'
	setting_p='setting.data'
	db_p='Library.db'

else:
	save=os.getlogin()
	try:
		os.mkdir(f'C:\\Users\\{save}\\AppData\\Local\\lIBRARY')

	except FileExistsError:
		pass

	logfile_p=f'C:\\Users\\{save}\\AppData\\Local\\lIBRARY\\logfile.log'
	setting_p=f'C:\\Users\\{save}\\AppData\\Local\\lIBRARY\\setting.data'
	db_p=f'C:\\Users\\{save}\\AppData\\Local\\lIBRARY\\Library.db'

#print(logfile_p,setting_p,db_p)



logging.basicConfig(filename=logfile_p,filemode='w' ,level=logging.DEBUG)


context = ssl.create_default_context()
try:
	with open(setting_p,'rb') as f:
		settings=pickle.load(f)
		#print(settings)
		is_it_fresh=False

except IOError:
	is_it_fresh=True
	settings={}


init()
global dd
dd=0
MONTH=[1,2,3,4,5,6,7,8,9,10,11,12]
DAY_NONLEAP=[31,28,31,30,31,30,31,31,30,31,30,31]
DAY_LEAP=[31,29,31,30,31,30,31,31,30,31,30,31]

global FONTS
FONTS=('System', 'Terminal', 'Fixedsys', 'Modern', 'Roman', 'Script', 'Courier', 'MS Serif', 'MS Sans Serif', 'Small Fonts', 'Marlett', 'Arial', 'Arabic Transparent', 'Arial Baltic',
	   'Arial CE', 'Arial CYR', 'Arial Greek', 'Arial TUR', 'Batang', '@Batang', 'BatangChe', '@BatangChe', 'Gungsuh', '@Gungsuh', 'GungsuhChe', '@GungsuhChe', 'Courier New',
	   'Courier New Baltic', 'Courier New CE', 'Courier New CYR', 'Courier New Greek', 'Courier New TUR', 'DaunPenh', 'DokChampa', 'Estrangelo Edessa', 'Euphemia', 'Gautami', 'Vani',
	   'Gulim', '@Gulim', 'GulimChe', '@GulimChe', 'Dotum', '@Dotum', 'DotumChe', '@DotumChe', 'Impact', 'Iskoola Pota', 'Kalinga', 'Kartika', 'Khmer UI', 'Lao UI', 'Latha',
	   'Lucida Console', 'Malgun Gothic', '@Malgun Gothic', 'Mangal', 'Meiryo', '@Meiryo', 'Meiryo UI', '@Meiryo UI', 'Microsoft Himalaya', 'Microsoft JhengHei', '@Microsoft JhengHei',
	   'Microsoft YaHei', '@Microsoft YaHei', 'MingLiU', '@MingLiU', 'PMingLiU', '@PMingLiU', 'MingLiU_HKSCS', '@MingLiU_HKSCS', 'MingLiU-ExtB', '@MingLiU-ExtB', 'PMingLiU-ExtB',
	   '@PMingLiU-ExtB', 'MingLiU_HKSCS-ExtB', '@MingLiU_HKSCS-ExtB', 'Mongolian Baiti', 'MS Gothic', '@MS Gothic', 'MS PGothic', '@MS PGothic', 'MS UI Gothic', '@MS UI Gothic',
	   'MS Mincho', '@MS Mincho', 'MS PMincho', '@MS PMincho', 'MV Boli', 'Microsoft New Tai Lue', 'Nyala', 'Microsoft PhagsPa', 'Plantagenet Cherokee', 'Raavi', 'Segoe Script', 'Segoe UI',
	   'Segoe UI Semibold', 'Segoe UI Light', 'Segoe UI Symbol', 'Shruti', 'SimSun', '@SimSun', 'NSimSun', '@NSimSun', 'SimSun-ExtB', '@SimSun-ExtB', 'Sylfaen', 'Microsoft Tai Le',
	   'Times New Roman', 'Times New Roman Baltic', 'Times New Roman CE', 'Times New Roman CYR', 'Times New Roman Greek', 'Times New Roman TUR', 'Tunga', 'Vrinda', 'Shonar Bangla',
	   'Microsoft Yi Baiti', 'Tahoma', 'Microsoft Sans Serif', 'Angsana New', 'Aparajita', 'Cordia New', 'Ebrima', 'Gisha', 'Kokila', 'Leelawadee', 'Microsoft Uighur', 'MoolBoran',
	   'Symbol', 'Utsaah', 'Vijaya', 'Wingdings', 'Andalus', 'Arabic Typesetting', 'Simplified Arabic', 'Simplified Arabic Fixed', 'Sakkal Majalla', 'Traditional Arabic', 'Aharoni',
	   'David', 'FrankRuehl', 'Levenim MT', 'Miriam', 'Miriam Fixed', 'Narkisim', 'Rod', 'FangSong', '@FangSong', 'SimHei', '@SimHei', 'KaiTi', '@KaiTi', 'AngsanaUPC', 'Browallia New',
	   'BrowalliaUPC', 'CordiaUPC', 'DilleniaUPC', 'EucrosiaUPC', 'FreesiaUPC', 'IrisUPC', 'JasmineUPC', 'KodchiangUPC', 'LilyUPC', 'DFKai-SB', '@DFKai-SB', 'Lucida Sans Unicode',
	   'Arial Black', 'Calibri', 'Cambria', 'Cambria Math', 'Candara', 'Comic Sans MS', 'Consolas', 'Constantia', 'Corbel', 'Franklin Gothic Medium', 'Gabriola', 'Georgia',
	   'Palatino Linotype', 'Segoe Print', 'Trebuchet MS', 'Verdana', 'Webdings')

global SIZE
SIZE=tuple(range(1,101))

global DEFAULTFONT
DEFAULTFONT={'family': 'Segoe UI', 'size': 9}
NEWFONT=DEFAULTFONT

global td
td=localtime()

global year
year=td.tm_year

global TESTING_WORDS
TESTING_WORDS=''
TEST_WORDS=[chr(i) for i in range(65,123)]
for i in TEST_WORDS:
	if TEST_WORDS.index(i)%20==0:
		TESTING_WORDS+='\n'
	TESTING_WORDS+=i

TESTING_SETTING={'family': 'Segoe UI', 'size': 9}


conn=sqlite3.connect(db_p)
c=conn.cursor()


def logger(clfn_name,v1=None,v2=None,v3=None,v4=None):
	logging.debug(f'time:{time()}::{clfn_name}:{v1}:{v2}:{v3}:{v4}')


def sizer(param : str):
	app.geometry(param)

def run_in_parallel(*fns):
	for fn in fns:
		p=Process(target=fn)
		p.start()



def helper_func(match):
	emails_id=int(match[1])
	c.execute(f'SELECT EMAIL FROM PERSONSTAT WHERE SRL={emails_id};')
	email=list(c.fetchall()[0])[0]
	#print(email)
	return email


def hlp_func_a_day_before(match):
	try:
		with smtplib.SMTP('smtp.gmail.com',587,timeout=120) as s:
			s.ehlo()
			s.starttls()
			user=settings['email']
			passw=settings['password']
			s.login(f'{user}',f'{passw}')
			s.ehlo()
			match=helper_func(match)
			message = MIMEMultipart()
			message["From"] = f'{user}'
			message["To"] = match    #''
			message["Subject"] = 'The Library'
			Body='THIS IS AN EMAIL FROM KVAG LIBRARY AND THIS IS AN REGARDING THE RETURN DATE OF THE BOOK. \n THE DATE OF RETURNIN IS TOMMOROW TO AVOID THE FINE PLEASE RETURN THE BOOK TOMMOROW'
			message.attach(MIMEText(Body, "plain"))
			status=s.sendmail(user, match, message.as_string())
			return status
	except Exception as e:
		logger('a day before',e)
		print(e)
		pass

def hlp_func_delay(match):
	try:
		with smtplib.SMTP('smtp.gmail.com',587,timeout=120) as s:
			s.ehlo()
			s.starttls()
			user=settings['email']
			passw=settings['password']
			s.login(f'{user}',f'{passw}')
			s.ehlo()
			book_code=match[0]
			c.execute(f'SELECT BOOK FROM BOOKSTAT WHERE SRL={book_code}')
			book_name=c.fetchall()[0][0]
			match=helper_func(match)
			message = MIMEMultipart()
			message["From"] = f'{user}'
			message["To"] = match
			message["Subject"] = 'The Library'
			Body=f'THIS IS AN EMAIL FROM KVAG LIBRARY AND THIS IS AN REGARDING LATE RETURNING OF THE BOOK. \n YOU HAVEN\'T RETURNED THE BOOK {book_name} TO AVOID LARGE AMOUNT FINE PLEASE RETURN THE BOOK AS SOON AS POSSIBLE \n THANK YOU'
			message.attach(MIMEText(Body, "plain"))
			status=s.sendmail(user, match, message.as_string())
			return status
	except Exception as e:
		logger('delay',e)
		print(e)
		pass

def send_email():
	c.execute('SELECT * FROM BRWDTIME')
	s=''
	matching=c.fetchall()
	for match in matching:
		match=list(match)
		sleep(0.00000001)
		month,date=match[2],match[3]
		td_month=td.tm_mon
		td_date=td.tm_mday
		if month-td_month==0:
			#print(abs(td_date-date))
			if abs(td_date-date)==13:
				#print('187')
				s=hlp_func_a_day_before(match)
				print(s)
			elif abs(td_date-date)>14:
				s=hlp_func_delay(match)
				#print('192')
				print(s)
		else:
			diff=abs(month-td_month)
			for i in range(diff):
				if i==0:
					if year%4==0 and year%100!=0 or year%400==0:
						d=DAY_LEAP[MONTH.index(month)]-date
						d+=td_date
					else:
						d=DAY_NONLEAP[MONTH.index(month)]-date
						d+=td_date
				else:
					if year%4==0 and year%100!=0 or year%400==0:
						d+=DAY_LEAP[month-i+1]
					else:
						d+=DAY_NONLEAP[month-i+1]


			if d==13:
				s=hlp_func_a_day_before(match)
				#print(s,match)

			elif d>14:
				#hlp_func_a_day_before(match,'nairarjuns521@gmail.com')
				s=hlp_func_delay(match)
				#print(s,match)


		#print('done sending')
		logger('send_email',s)



logger('paths',logfile_p,setting_p,db_p)


logger('Running the code')

class lib:

	def __init__(self):
		self.rb_name=''
		self.rb_code=0
		self.book_code=0
		self.book_name=''
		self.act=0
		self.tables()


	def tables(self):
		try:
			c.execute('CREATE TABLE IF NOT EXISTS BOOKSTAT ("SRL" INT,"BOOK" TEXT,"FROM" TEXT,"STAT" TEXT);')
			c.execute('CREATE TABLE IF NOT EXISTS PERSONSTAT ("SRL" INT,"name" TEXT,"Address" TEXT,"EMAIL" TEXT,"STAT" TEXT);')
			c.execute('CREATE TABLE IF NOT EXISTS BRWDTIME ("BOOK CODE" INT,"PERSON CODE" INT,"RET MONTH" INT,"RET DAY" INT);')
			c.execute('CREATE TABLE IF NOT EXISTS QUEUE ("BOOK CODE" INT, "BRW1 CODE" INT,"BRW2 CODE" INT,"BRW3 CODE" INT,"BRW4 CODE" INT);')

		except Exception as e:
			print(e)


	#def intro(self):
		#print(Fore.WHITE + "#Lib 2.0 "+ Style.RESET_ALL)
		#print(Fore.LIGHTRED_EX + "#Following can be done: " + Style.RESET_ALL)
		#print(Fore.CYAN+"#1}Borrow","\n","#2}Return"+Style.RESET_ALL)
		#print(Fore.CYAN + "#3}Available Books","\n","#4}Add new books to Lib"+ Style.RESET_ALL)
		#print('\n\n')


	def bookstat(self,bcode,rbcode=None,brw=False,db=c):
		logger('booktstat',bcode,rbcode,brw)
		if not brw:
			db.execute(f'SELECT STAT FROM BOOKSTAT WHERE SRL={int(bcode)};')
			book_stat=db.fetchall()
			if book_stat!=[]:
				stats=book_stat[0][0]
				return stats
			else:
				return IndexError
		else:
			try:
				curr_mon=td.tm_mon
				curr_date=td.tm_mday
				#curr_date+=13

				db.execute('UPDATE BOOKSTAT SET STAT="BRWD" WHERE SRL={};'.format(bcode))
				db.execute('UPDATE PERSONSTAT SET STAT="BRWD" WHERE SRL={};'.format(rbcode))
				db.execute('INSERT INTO BRWDTIME VALUES(?,?,?,?)',(bcode,rbcode,curr_mon,curr_date))
				db.execute("commit")
				conn.commit()
				return True,None

			except Exception as e:
				print(e)
				return False ,e


	def personstat(self,rb_code,db=c):
		logger('personstat',rb_code,None,None)
		try:
			db.execute('SELECT name FROM PERSONSTAT WHERE SRL={};'.format(rb_code))
			stats=db.fetchall()
			if stats!=[]:
				return True
			else:
				return False
		except Exception:
			return False


	def register(self,pername : str,add :str,email : str, db=c):
		logger('register',pername,add,email)
		a=True
		c=0
		last=0
		try:
			while a:
				if c<3:
					db.execute('SELECT * FROM PERSONSTAT')
					books=db.fetchall()
					if books==[]:
						last=0
					else:
						last=books[len(books)-1][0]
					c+=1

				else:
					a=False
			curr=last+1
			db.execute('INSERT INTO PERSONSTAT VALUES(?,?,?,?,?);',(int(curr),str(pername),str(add),str(email),str("NT")))
			#print('Your id no. is {}'.format(curr))
			db.execute("commit")
			conn.commit()
			return 'Your Id is {}'.format(curr)

		except Exception as e:
			print(e)
			return e

			#print('Encountered an error try again after sometime')


	def borrow_book(self, book_code, rb_code, book_name=''):
		logger('borrow',book_code,rb_code)
		book_stat=self.bookstat(book_code)

		if book_stat=='BRWD':
			#print(Fore.GREEN+'The book is borrowed by another person  ☹'+Style.BRIGHT+Style.RESET_ALL)
			#print(Fore.MAGENTA+'Thank You'+Style.BRIGHT+Style.RESET_ALL)
			return 'Book Has Been Borrowed by Another Person'

		else:
			if self.personstat(rb_code):
				book,er=self.bookstat(book_code,rb_code,brw=True)
				if book:
					#print(Fore.YELLOW+'The book {} has been issued'.format(book_name)+Style.BRIGHT+Style.RESET_ALL)
					#print(Fore.BLUE+'Thank You ☺'+Style.RESET_ALL)
					return 'The Book is Issued Successfully'

				else:
					#print('Some error has been occured')
					return er

			else:
				#print('The person doesn\'t exists')
				#print('pls trying registering')
				return 'The Person Haven\'t Registered yet \n Pls try after Registering'


	def add_book(self,book_name : str,written_by : str,db=c):
		logger('add_book',book_name,written_by)
		try:
			a=True
			c=0
			last=0
			while a:
				if c<3:
					db.execute('SELECT * FROM BOOKSTAT')
					books=db.fetchall()

					if books==[]:
						last=0

					else:
						last=books[len(books)-1][0]

					c+=1
				else:
					a=False

			curr=last+1
			db.execute('INSERT INTO BOOKSTAT VALUES(?,?,?,?);',(int(curr),book_name,written_by,"NT"))
			#print('BOOK HAS BEEN ADDED')
			db.execute("commit")
			conn.commit()
			return 'The Book has been added'+'\n'+f'The book code is {curr}'


		except Exception as e:
			print('Encountered an error try again after sometime')
			return e


	def recieve_book(self,book_code,rb_code,db=c):
		logger('return',book_code,rb_code)
		db.execute(f'SELECT STAT FROM BOOKSTAT WHERE SRL={book_code};')
		book=db.fetchall()
		book=book[0][0]
		db.execute(f'SELECT STAT FROM PERSONSTAT WHERE SRL={rb_code};')
		per=db.fetchall()
		per=per[0][0]
		if book=='BRWD' and per=='BRWD':
			try:
				db.execute(f'UPDATE BOOKSTAT SET STAT="NT" WHERE SRL={book_code};')
				db.execute(f'UPDATE PERSONSTAT SET STAT="NT" WHERE SRL={rb_code};')
				db.execute(f'SELECT "RET MONTH","RET DAY" FROM BRWDTIME WHERE "BOOK CODE"={book_code}')
				a=db.fetchall()
				db.execute(f'DELETE FROM BRWDTIME WHERE "BOOK CODE"={book_code}')
				c.execute("commit")
				conn.commit()
				#print('Thank You')
				return 'The Book Has Been Returned Successfully',a[0]

			except Exception as e:
				#print('Encountered an error try again after sometime')
				print(e)
				return e




	def available_book(self,db=c):
		logger('available_book')
		try:
			db.execute('SELECT * FROM BOOKSTAT')
			books=db.fetchall()
			end=''
			for book in books:
				c=0
				for b in book:
					end+=str(b)
					end+='     '
				end+='\n'


			return end

		except Exception as e:
			print(e)
			print('Error')

	def all_book(self):
		logger('available')
		c.execute(f'SELECT * FROM BOOKSTAT;')
		global matching
		matching=c.fetchall()
		#print('hey\'s')
		return matching


x=lib()
def popupmsg(msg,erpop=True):
	popup = Tk()

	def leavemini():
		popup.destroy()

	popup.wm_title("MSG")

	label = ttk.Label(popup, text=msg)
	label.pack(side="top", fill="x", pady=10)
	if erpop:
		B1 = ttk.Button(popup, text = "Okay", command = leavemini)
		B1.pack()
	else:
		popup.geometry('300x300')

	popup.mainloop()

class lIBRARY(Tk):

	def __init__(self, *args, **kwargs):

		Tk.__init__(self, *args, **kwargs)
		Tk.iconbitmap(self,default='130304.ico')

		Tk.wm_title(self, "Library")

		container = Frame(self)
		container.pack(side="top", fill="both", expand = True)
		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)

		self.frames = {}

		for F in (StartPage, Borrow, Recieve, Register, Adder, Available, ByName, ByAuth, Setting, FreshStart):

			frame = F(container, self)
			self.frames[F] = frame
			frame.grid(row=0, column=0, sticky="nsew")

		if not is_it_fresh:
			self.show_frame(StartPage)

		else:
			self.show_frame(FreshStart)


	def show_frame(self, cont):

		if cont==Setting:
			messagebox.showinfo('Info','It is not ready yet')
			#sizer('600x400')
			return

		frame = self.frames[cont]
		frame.tkraise()


class StartPage(Frame):

	def __init__(self, parent, controller):
		Frame.__init__(self,parent)
		self.init_window(controller)



	def init_window(self,controller):

		#self.master.title("LIBRARY")
		#self.pack(fill=BOTH, expand=1)

		#l1=Label(self,text='#Lib 1.0')
		#l1.place(x=120,y=0)


		b1 = ttk.Button(self, text="BORROW BOOK",command=lambda: controller.show_frame(Borrow))  #,command=self.do1 ,height=5,width=16
		b1.place(x=10, y=60)

		b2 = ttk.Button(self, text="RECIEVE BOOK",command=lambda: controller.show_frame(Recieve))  #,command=self.do1 recieve ,height=5,width=16
		b2.place(x=190, y=60)

		b3 = ttk.Button(self, text="REGISTER",command=lambda: controller.show_frame(Register))  #,command=self.do1 recieve ,height=5,width=16
		b3.place(x=10, y=120)

		b4 = ttk.Button(self, text="AVAILABLE BOOK",command=lambda: controller.show_frame(Available))  #,command=self.do1 recieve ,height=5,width=16
		b4.place(x=190, y=120)

		b5 = ttk.Button(self, text="Add A Book",command=lambda: controller.show_frame(Adder))
		b5.place(x=10,y=180)

		b6 = ttk.Button(self, text="Settings",command=lambda: controller.show_frame(Setting))  #,command=self.do1 recieve ,height=5,width=16
		b6.place(x=190, y=180)



class Borrow(Frame):

	def __init__(self, parent, controller):
		Frame.__init__(self,parent)
		self.main_window(controller)


	def main_window(self,controller):

		l1=ttk.Label(self,text='Issue The Book',font=(DEFAULTFONT['family'],DEFAULTFONT['size']))
		l1.place(x=137)

		global enter1
		enter1 = ttk.Entry(self)
		enter1.place(x=180,y=120)

		label1 = ttk.Label(self, text="Enter the Book Code",font=(DEFAULTFONT['family'],DEFAULTFONT['size']))
		label1.place(x=20,y=120)

		global enter2
		enter2 = ttk.Entry(self)
		enter2.place(x=180,y=160)
		label2 = ttk.Label(self, text="Enter the Registeration Code",font=(DEFAULTFONT['family'],DEFAULTFONT['size']))
		label2.place(x=20,y=160)

		#button = ttk.Button(self, text="Visit Page 1")
		#button.pack()

		button2 = ttk.Button(self, text="Issue",command=lambda: self.printer(controller))
		button2.place(x=200,y=200)

		button3=ttk.Button(self, text="Back to Main Menu",command=lambda: self.pageshifter(controller))
		button3.place(x=200,y=240)


	def printer(self,controller):
		try:
			b_code=int(enter1.get())
			u_code=int(enter2.get())
			sleep(0.00000001)
			err=x.borrow_book(b_code,u_code)

			c.execute(f'SELECT * FROM QUEUE WHERE "BOOK CODE"={b_code};')
			is_it_occupied=c.fetchall()
			print(is_it_occupied)
			#print(er=='Book Has Been Borrowed by Another Person' and empty and x.personstat(u_code))
			if is_it_occupied==[]:
				pass
			else:
				is_it_occupied=list(is_it_occupied[0])

			h=0 in is_it_occupied
			g=is_it_occupied==[]
			is_it_free= h or g
			print(is_it_free)
			#print(is_it_free,is_it_occupied[0])
			if err=='Book Has Been Borrowed by Another Person' and x.personstat(u_code):
				if is_it_free or is_it_occupied==[]:
					yes_no=messagebox.askyesno('Info','The book is borrowed by another person do you want to wait until the book comes??')
					# print(yes_no)
					if yes_no:
						self.queue(b_code,u_code,is_it_occupied)

			elif not x.personstat(u_code):
				messagebox.showinfo('Info','You haven\'t registered yet')

			elif not 0 in is_it_occupied and not g:
				messagebox.showinfo('Info',err+' and the queue is full')

			else:
				messagebox.showinfo('Info',err)



		except ValueError:
			messagebox.showerror('Error','You have written something which is not a no.')

		except IndexError:
			u_code=int(enter2.get())
			if not x.personstat(u_code):
				messagebox.showerror('Error','You entered something which is not available'+'You haven\'t registered yet')

			else:
				messagebox.showerror('Error','You entered something which is not available')

		except Exception as e:
			messagebox.showerror('Error',e)


	def pageshifter(self,controller):
		controller.show_frame(StartPage)

	def queue(self,b_code,u_code,list_):
		if list_ == list():
			c.execute('INSERT INTO QUEUE VALUES (?,?,?,?,?);',(b_code,u_code,0,0,0))
		elif list_.index(0)==2:
			c.execute(f'UPDATE QUEUE SET "BRW2 CODE"={u_code} WHERE "BOOK CODE"={b_code};')
		elif list_.index(0)==3:
			c.execute(f'UPDATE QUEUE SET "BRW3 CODE"={u_code} WHERE "BOOK CODE"={b_code};')
		elif list_.index(0)==4:
			c.execute(f'UPDATE QUEUE SET "BRW4 CODE"={u_code} WHERE "BOOK CODE"={b_code};')
		c.execute("commit")
		conn.commit()



class Recieve(Frame):

	def __init__(self, parent, controller):
		Frame.__init__(self,parent)
		self.main_window(controller)
		try:
			self.fixed=settings['fine']

		except Exception:
			self.fixed=2

	def fine_calc(self,diff):
		if diff<=7:
			return self.fixed

		else:
			ab_max=diff-7
			current=self.fixed+ab_max*self.fixed
			#print(ab_max,current,diff)
			return current

	def queue(self,b_code):
		try:
			c.execute(f'SELECT * FROM QUEUE WHERE "BOOK CODE"={b_code};')
			is_it_occupied=c.fetchall()
			is_it_occupied=list(is_it_occupied[0])
			counted=Counter(is_it_occupied)[0]
			if counted==3:
				u_code=is_it_occupied[1]
				er=x.borrow_book(b_code,u_code)
				c.execute(f'DELETE FROM QUEUE WHERE "BOOK CODE"={b_code};')

			elif counted==2: #tedious task starts here
				u_code=is_it_occupied[1]
				er=x.borrow_book(b_code,u_code)
				c.execute(f'UPDATE QUEUE SET "BRW1 CODE"={is_it_occupied[2]} WHERE "BOOK CODE"={b_code};')
				c.execute(f'UPDATE QUEUE SET "BRW2 CODE"={0} WHERE "BOOK CODE"={b_code};')

			elif counted==1:
				u_code=is_it_occupied[1]
				er=x.borrow_book(b_code,u_code)
				c.execute(f'UPDATE QUEUE SET "BRW1 CODE"={is_it_occupied[2]} WHERE "BOOK CODE"={b_code};')
				c.execute(f'UPDATE QUEUE SET "BRW2 CODE"={is_it_occupied[3]} WHERE "BOOK CODE"={b_code};')
				c.execute(f'UPDATE QUEUE SET "BRW3 CODE"={0} WHERE "BOOK CODE"={b_code};')
			elif counted==0:
				u_code=is_it_occupied[1]
				er=x.borrow_book(b_code,u_code)
				c.execute(f'UPDATE QUEUE SET "BRW1 CODE"={is_it_occupied[2]} WHERE "BOOK CODE"={b_code};')
				c.execute(f'UPDATE QUEUE SET "BRW2 CODE"={is_it_occupied[3]} WHERE "BOOK CODE"={b_code};')
				c.execute(f'UPDATE QUEUE SET "BRW3 CODE"={is_it_occupied[4]} WHERE "BOOK CODE"={b_code};')
				c.execute(f'UPDATE QUEUE SET "BRW4 CODE"={0} WHERE "BOOK CODE"={b_code};')

			c.execute("commit")
			conn.commit()

		except Exception as e:
			logger('QUEUE FOR THE PEOPLE',e)
			pass



	def main_window(self,controller):
		l1=ttk.Label(self,text='Return The Book',font=(DEFAULTFONT['family'],DEFAULTFONT['size']))
		l1.place(x=137)

		global enter3
		enter3 = ttk.Entry(self)
		enter3.place(x=180,y=120)

		label1 = ttk.Label(self, text="Enter the Book Code",font=(DEFAULTFONT['family'],DEFAULTFONT['size']))
		label1.place(x=20,y=120)

		global enter4
		enter4 = ttk.Entry(self)
		enter4.place(x=180,y=160)
		label2 = ttk.Label(self, text="Enter the Registeration Code",font=(DEFAULTFONT['family'],DEFAULTFONT['size']))
		label2.place(x=20,y=160)

		#button = ttk.Button(self, text="Visit Page 1")
		#button.pack()

		button2 = ttk.Button(self, text="Return",command=lambda: self.printer(controller))
		button2.place(x=200,y=200)

		button3=ttk.Button(self, text="Back to Main Menu",command=lambda: self.pageshifter(controller))
		button3.place(x=200,y=240)


	def printer(self,controller):
		try:

			b_code=int(enter3.get())
			u_code=int(enter4.get())
			#sleep(0.00000001)
			er,times=x.recieve_book(b_code,u_code)
			self.queue(b_code)
			#print(times)
			month,date=times
			td_month=td.tm_mon
			td_date=td.tm_mday
			if month-td_month==0:
				if abs(td_date-date)<=13:
					messagebox.showinfo('Info',er)
				else:
					messagebox.showinfo('Fine',f'You have a fine of rupees {self.fine_calc(abs(td_date-date))}')

			else:
				diff=abs(month-td_month)
				for i in range(diff):
					if i==0:
						if year%4==0 and year%100!=0 or year%400==0:
							d=DAY_LEAP[MONTH.index(month)]-date
							d+=td_date
						else:
							d=DAY_NONLEAP[MONTH.index(month)]-date
							d+=td_date
					else:
						if year%4==0 and year%100!=0 or year%400==0:
							d+=DAY_LEAP[month-i+1]
						else:
							d+=DAY_NONLEAP[month-i+1]

					#print(d)


				if d<=13:
					messagebox.showinfo('Info',er)
				else:
					messagebox.showinfo('Fine',f'You have a fine of rupees {self.fine_calc(abs(d))}')



		except ValueError:
			messagebox.showerror('Error','You have written something which is not a no.')

		except Exception as e:
			messagebox.showerror('Error',e)


	def pageshifter(self,controller):
		controller.show_frame(StartPage)

class Register(Frame):

	def __init__(self, parent, controller):
		Frame.__init__(self,parent)
		self.main_window(controller)


	def main_window(self,controller):
		l1=ttk.Label(self,text='Return The Book',font=(DEFAULTFONT['family'],DEFAULTFONT['size']))
		l1.place(x=137)

		global enter5
		enter5 = ttk.Entry(self)
		enter5.place(x=180,y=120)

		label1 = ttk.Label(self, text="Name of the Person",font=(DEFAULTFONT['family'],DEFAULTFONT['size']))
		label1.place(x=20,y=120)

		global enter6
		enter6 = ttk.Entry(self)
		enter6.place(x=180,y=160)

		label2 = ttk.Label(self, text="Address of the Person",font=(DEFAULTFONT['family'],DEFAULTFONT['size']))
		label2.place(x=20,y=160)

		global enter19
		enter19 = ttk.Entry(self)
		enter19.place(x=180,y=200)

		label30 = ttk.Label(self, text="Email of the person",font=(DEFAULTFONT['family'],DEFAULTFONT['size']))
		label30.place(x=20,y=200)

		#button = ttk.Button(self, text="Visit Page 1")
		#button.pack()

		button2 = ttk.Button(self, text="Register",command=lambda: self.printer(controller))
		button2.place(x=200,y=240)

		button3=ttk.Button(self, text="Back to Main Menu",command=lambda: self.pageshifter(controller))
		button3.place(x=200,y=280)


	def printer(self,controller):

		per=str(enter5.get())
		add=str(enter6.get())
		email=str(enter19.get())
		sleep(0.00000001)
		if per!='' and add!='' and email!='':
			er=x.register(per,add,email)
			messagebox.showinfo('Info',er)
		else:
			messagebox.showinfo('Error','The Field Was left Empty')


	def pageshifter(self,controller):
		controller.show_frame(StartPage)


class Adder(Frame):

	def __init__(self, parent, controller):
		Frame.__init__(self,parent)
		self.add(controller)

	def add(self,controller):

		lab=ttk.Label(self,text='ADD A BOOK',font=(DEFAULTFONT['family'],DEFAULTFONT['size']))
		lab.place(x=137)

		global enter7
		enter7 = ttk.Entry(self)
		enter7.place(x=200,y=80)

		label1 = ttk.Label(self, text="Name of the Book",font=(DEFAULTFONT['family'],DEFAULTFONT['size']))
		label1.place(x=20,y=80)

		global enter8
		enter8 = ttk.Entry(self)
		enter8.place(x=200,y=120)

		label2 = ttk.Label(self, text="Name of the Author of the Book",font=(DEFAULTFONT['family'],DEFAULTFONT['size']))
		label2.place(x=20,y=120)

		button4 = ttk.Button(self, text="Add",command=lambda: self.printer(controller))
		button4.place(x=200,y=200)

		button5=ttk.Button(self, text="Back to Main Menu",command=lambda: self.pageshifter(controller))
		button5.place(x=200,y=240)

	def printer(self,controller):

		name=str(enter7.get())
		auth=str(enter8.get())
		sleep(0.00000001)
		if name!='' and auth!='':
			er=x.add_book(name,auth)
			messagebox.showinfo('Info',er)
			matching=x.all_book()
		else:
			messagebox.showerror('Error','The Field Was left Empty')


	def pageshifter(self,controller):
		controller.show_frame(StartPage)

class Available(Frame):

	def __init__(self, parent, controller):
		Frame.__init__(self,parent)
		self.av(controller)

	def av(self,controller):

		button4 = ttk.Button(self, text="Search By Name",command=lambda: self.pageshifter(controller,ByName))
		button4.place(x=120,y=100)

		button5 = ttk.Button(self, text="Search By Author",command=lambda: self.pageshifter(controller,ByAuth))
		button5.place(x=120,y=150)

		button6 = ttk.Button(self, text="Show All",command=lambda: self.byshow())
		button6.place(x=120,y=200)

		button7=ttk.Button(self, text="Back to Main Menu",command=lambda: self.pageshifter(controller))
		button7.place(x=120,y=250)


	def byshow(self):
		root=Tk()
		s = ttk.Style()
		s.configure('my.TButton', font=('Helvetica', 8))

		global scrollbar2
		scrollbar2 = ttk.Scrollbar(root)
		scrollbar2.config(orient=VERTICAL)
		scrollbar2.grid(row=0,column=5,rowspan=15)
		#b1.config(font=('Helvetica', '20'))        .pack(side=RIGHT,fill=Y)
		#Refresh  Error
		matching=x.all_book()
		#print('hello')
		try:
			tree2.delete(*tree2.get_children())
			#print('done deleting')
		except Exception:
			logger('tree2 doesn\'t exists yet')
			#print('it error')

		tree2=ttk.Treeview(root,yscrollcommand=scrollbar.set,height=13)
		tree2['columns']=('Bcode','Name','By','Stat')
		tree2.column("#0", width=40)
		tree2.column('Bcode',width=100)
		tree2.column('Name',width=120)
		tree2.column('By',width=100)
		tree2.column('Stat',width=80)
		tree2.heading('#0',text='Sno')
		tree2.heading('Bcode',text='Book Code')
		tree2.heading('Name',text='Name of the Book')
		tree2.heading('By',text='Author')
		tree2.heading('Stat',text='Stat')
		for no,i in enumerate(matching,start=1):
			tree2.insert('',text=no,index="end",values=i)

		tree2.grid(row=0,column=0,columnspan=10, rowspan=10)
		scrollbar2.config(command = tree2.yview)

		root.geometry('445x290')
		root.mainloop()

	def pageshifter(self,controller,page=None):
		if page is None:
			controller.show_frame(StartPage)
		else:
			if page in [ByName,ByAuth]:
				sizer('600x400')

				global matching
				matching=x.all_book()
			controller.show_frame(page)



class ByName(Frame):

	def __init__(self, parent, controller):
		Frame.__init__(self,parent)
		self.byname(controller)

	def byname(self,controller):
		try:
			s = ttk.Style()
			s.configure('my.TButton', font=('Helvetica', 8))

			global scrollbar
			scrollbar = ttk.Scrollbar(self)
			scrollbar.config(orient=VERTICAL)
			scrollbar.pack(side=RIGHT,fill=Y)

			global enter9
			enter9=ttk.Entry(self,font=('Verdana',10))
			enter9.insert(index=0,string='Search')
			enter9.place(x=200,y=50)

			b1=ttk.Button(self, text="←",command=lambda: self.pageshifter(controller))
			#b1.config(font=('Helvetica', '20'))
			b1.place(x=0)

			b2=ttk.Button(self, text="Go",command=self.search)
			b2.place(x=363,y=50)

		except Exception as e:
			logger('BYNAME',e)
			pass


	def pageshifter(self,controller,page=None):
		if page is None:
			controller.show_frame(StartPage)
			sizer('350x350')
		else:
			controller.show_frame(page)

	def search(self):
		quat=str(enter9.get())
		c.execute(f'SELECT * FROM BOOKSTAT WHERE BOOK LIKE "{quat}%";')
		global matching
		matching=c.fetchall()
		try:
			tree.delete(*tree.get_children())
		except Exception as e:
			logger('TREE 1 DOESN\'T EXISTS YET',e)
			pass
		if not matching==[]:
			tree=ttk.Treeview(self,yscrollcommand=scrollbar.set,height=13)
			tree['columns']=('Bcode','Name','By','Stat')
			tree.column("#0", width=40)
			tree.column('Bcode',width=100)
			tree.column('Name',width=120)
			tree.column('By',width=100)
			tree.column('Stat',width=80)
			tree.heading('#0',text='Sno')
			tree.heading('Bcode',text='Book Code')
			tree.heading('Name',text='Name of the Book')
			tree.heading('By',text='Author')
			tree.heading('Stat',text='Stat')
			for no,i in enumerate(matching,start=1):
				tree.insert('',text=no,index="end",values=i)

			tree.place(y=100,x=100)
			scrollbar.config(command = tree.yview)

		else:
			messagebox.showinfo('Info','No book Found!')
			try:
				tree.delete(*tree.get_children())
			except Exception as e:
				logger('Tree 1',e)
				pass

class ByAuth(Frame):

	def __init__(self, parent, controller):
		Frame.__init__(self,parent)
		self.byauth(controller)

	def byauth(self,controller):

		s = ttk.Style()
		s.configure('my.TButton', font=('Helvetica', 8))

		global scrollbar1
		scrollbar1 = ttk.Scrollbar(self)
		scrollbar1.config(orient=VERTICAL)
		scrollbar1.pack(side=RIGHT,fill=Y)

		global enter10
		enter10=ttk.Entry(self,font=('Verdana',10))
		enter10.insert(index=0,string='Search')
		enter10.place(x=200,y=50)

		b4=ttk.Button(self, text="←",command=lambda: self.pageshifter(controller))
		#b1.config(font=('Helvetica', '20'))
		b4.place(x=0)

		b5=ttk.Button(self, text="Go",command=self.search)
		b5.place(x=363,y=50)


	def pageshifter(self,controller,page=None):
		if page is None:
			controller.show_frame(StartPage)
			sizer('350x350')
		else:
			controller.show_frame(page)

	def search(self):
		quat=str(enter10.get())
		c.execute(f'SELECT * FROM BOOKSTAT WHERE "FROM" LIKE "{quat}%";')
		matching=c.fetchall()
		try:
			tree1.delete(*tree1.get_children())
		except Exception as e:
			logger('BYNAUTH',e)
			pass
		if not matching==[]:
			tree1=ttk.Treeview(self,yscrollcommand=scrollbar.set,height=13)
			tree1['columns']=('Bcode','Name','By','Stat')
			tree1.column("#0", width=40)
			tree1.column('Bcode',width=100)
			tree1.column('Name',width=120)
			tree1.column('By',width=100)
			tree1.column('Stat',width=80)
			tree1.heading('#0',text='Sno')
			tree1.heading('Bcode',text='Book Code')
			tree1.heading('Name',text='Name of the Book')
			tree1.heading('By',text='Author')
			tree1.heading('Stat',text='Stat')
			for no,i in enumerate(matching,start=1):
				tree1.insert('',text=no,index="end",values=i)

			tree1.place(y=100,x=100)
			scrollbar1.config(command = tree1.yview)

		else:
			messagebox.showinfo('Info','No book Found!')
			try:
				tree1.delete(*tree1.get_children())
			except Exception as e:
				logger('tree 1',e)
				pass



class Setting(Frame):

	def __init__(self, parent, controller):
		Frame.__init__(self,parent)
		self.setting(controller)

	def setting(self,controller):

		global scrollbar3
		scrollbar3 = ttk.Scrollbar(self)
		scrollbar3.config(orient=HORIZONTAL)
		scrollbar3.grid(row=0)

		global llb3

		llb3=ttk.Notebook(self)
		f1 = Frame(llb3)
		llb3.add(f1,text=TESTING_WORDS)														#,font=(TESTING_SETTING['family'],TESTING_SETTING['size']) ,xscrollcommand=scrollbar.set
		llb3.grid(row=10,column=20)

		bb1=ttk.Button(self,text='Back',command = lambda: self.pageshifter(controller))
		bb1.grid(row=0,column=0)

		l=Label(self)
		l.grid(row=5,column=2)

		global cb1

		cb1=ttk.Combobox(self,values=FONTS)
		cb1.grid(row=10,column=2)
		cb1.set(DEFAULTFONT['family'])

		llb1=ttk.Label(self,text='Font',font=(DEFAULTFONT['family'],DEFAULTFONT['size']))
		llb1.grid(row=10,column=0)

		l=Label(self)
		l.grid(row=11,column=2)

		global cb2

		cb2=ttk.Combobox(self,values=SIZE)
		cb2.grid(row=13,column=2)
		cb2.set(DEFAULTFONT['size'])
		cb2.bind('<<ComboboxSelected>>',self.modified)

		llb2=ttk.Label(self,text='Size',font=(DEFAULTFONT['family'],DEFAULTFONT['size']))
		llb2.grid(row=13,column=0)
		#scrollbar2.config(command = llb3.xview)



	def pageshifter(self,controller,page=None):
		if page is None:
			controller.show_frame(StartPage)
			sizer('350x350')
		else:
			controller.show_frame(page)

	def modified(self,_):
		size=cb2.get()
		print(size)
		TESTING_SETTING['size']=size
		llb3.configure(font=(TESTING_SETTING['family'],TESTING_SETTING['size']))

class FreshStart(Frame):

	def __init__(self, parent, controller):
		Frame.__init__(self,parent)
		self.fs(controller)

	def fs(self,controller):
		l1=ttk.Label(self,text='Configuration',font=(DEFAULTFONT['family'],DEFAULTFONT['size']))
		l1.place(x=137)

		# bl=Label()
		# bl.grid(row=1)

		global enter11
		enter11 = ttk.Entry(self)
		enter11.place(x=222,y=120)

		label1 = ttk.Label(self, text="Enter the Library E-mail Add.",font=(DEFAULTFONT['family'],DEFAULTFONT['size']))
		label1.place(x=0,y=120)

		global enter12
		enter12 = ttk.Entry(self)
		enter12.place(x=222,y=160)
		label2 = ttk.Label(self, text="Enter the Password",font=(DEFAULTFONT['family'],DEFAULTFONT['size']))
		label2.place(x=0,y=160)

		global enter13
		enter13 = ttk.Entry(self)
		enter13.place(x=222,y=200)
		label2 = ttk.Label(self, text="Enter the amount of fine you want charge",font=(DEFAULTFONT['family'],DEFAULTFONT['size']))
		label2.place(x=0,y=200)

		#button = ttk.Button(self, text="Visit Page 1")
		#button.pack()

		button2 = ttk.Button(self, text="Ok",command=lambda: self.theonetimeonly(controller))
		button2.place(x=200,y=240)

	def pageshifter(self,controller,page=None):
		if page is None:
			controller.show_frame(StartPage)
			sizer('350x350')
		else:
			controller.show_frame(page)

	def theonetimeonly(self,controller):
		user_name=str(enter11.get())
		password=str(enter12.get())
		fine=float(enter13.get())
		settings['email']=user_name
		settings['password']=password
		settings['fine']=fine
		with open(setting_p,'wb') as f:
			pickle.dump(settings,f)
		self.pageshifter(controller)



def runner_gui():
	global app
	app = lIBRARY()
	app.geometry('380x380')
	app.mainloop()
	sys.exit()

def table_refresher():
	while True:
		c.execute(f'SELECT * FROM BOOKSTAT;')
		matching=c.fetchall()


if __name__ == '__main__':
	run_in_parallel(runner_gui,send_email)

# runner_gui()
