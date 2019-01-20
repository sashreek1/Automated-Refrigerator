# datetime.datetime.today().strftime('%Y-%m-%d')

#import modules

from tkinter import *

from tkinter import messagebox

import datetime

import pyzbar1

import twilio_trial

import big_basket

import recipe_list

import image_recog

#class for the main inventory



class Inventory():

	def __init__(self,inv):
		self.inv=inv
		print(self.inv.values)
	def add_item_middle(self):

		self.add_item(main_app.text_box.get(),main_app.text_box1.get(),main_app.text_box2.get())
	def remove_item_middle(self):
		self.remove_item(main_app.text_box.get(),main_app.text_box1.get())
	def remove_item(self, name=None, quantity=0):
		abc=True
		for i in self.inv.values():
			if str(name)==i['name']:
				abc=False
		if abc:
			main_app.sms_and_messagebox(f'you do not have any item called {name}')
		ab=True
		for j,i in enumerate(self.inv.values()):
			print(j,i)	
			if name == i['name']:
				
				
				if int(quantity) > int(i["quantity"]):
					main_app.sms_and_messagebox(f"you dont have that many {name}s")
					break
				else:
					quan=i["quantity"]
					print(self.inv)
					self.inv[j]["quantity"]=int(quan)-int(quantity)
					print(self.inv)
	def add_item(self,name=None, quantity=0, expiry=None):

		self.inv[len(self.inv)]= {"name":name,'quantity':str(quantity) , "expiry":expiry}

	def retrieve_quantity(self,item):

		self.inv[item]["quantity"]

	def retrieve_expiry(self,item):

		self.inv[item]["expiry"]



# create an instance of inventory with some default items

the_inventory=Inventory({0:{'name':'tomato','quantity':'4', 'expiry':'20-01-2019'},

						 1:{'name':'carrot','quantity':'2', 'expiry':'23-01-2019'},

						 2:{'name':'carrot halwa','quantity':'500', "expiry":'25-01-2019' },

						 3:{'name': 'potato','quantity':'6', 'expiry':'25-01-2019'},

						 4:{'name': 'butter','quantity':'250', 'expiry':'25-01-2019'},

						 5:{'name': 'puri','quantity':'10', 'expiry':'25-01-2019'},

						 6:{'name': 'water','quantity':'270', 'expiry':'25-01-2019'},

						 7:{'name': 'onion','quantity':'5', 'expiry':'25-01-2019'},
						})





#class for main gui



class Application:

	def __init__(self,main):
		self.main=main

		# basic settings for window

		self.main.title("Smart Fridge")

		self.main.geometry("600x500")

		self.main.resizable(0,0)

		# menu stuff

		self.menubar=Menu(self.main)

		#display the menu

		root.config(menu=self.menubar)

		#all menus in the menubar

		# the tool sub-menu

		self.toolmenu=Menu(self.menubar)

		self.toolmenu.add_command(label="Add To Inventory", command=self.add_to_inventory_widget)  #add command here

		self.toolmenu.add_separator()

		self.toolmenu.add_command(label="Remove From Inventory", command=self.remove_from_inventory_widget)  #add command here

		self.toolmenu.add_separator()

		self.toolmenu.add_command(label="Recipes", command = self.show_recipes)           #add command here

		self.toolmenu.add_separator()

		self.toolmenu.add_command(label="Buy Items")           #add command here

		self.toolmenu.add_separator()

		self.toolmenu.add_command(label="Sticky Notes")           #add command here

		self.toolmenu.add_separator()

		self.toolmenu.add_command(label="Grocery List")           #add command here

		self.toolmenu.add_separator()

		self.menubar.add_cascade(label='Tools', menu=self.toolmenu)



		# the remainder sub-menu

		self.remindermenu=Menu(self.menubar)

		self.remindermenu.add_command(label="Expiry")    #add command here

		self.remindermenu.add_separator()

		self.remindermenu.add_command(label="Defrost")   #add command here

		self.remindermenu.add_separator()

		self.remindermenu.add_command(label="Festival Groceries")   #add command here

		self.remindermenu.add_separator()

		self.remindermenu.add_command(label="Soak Pulses")  #add command here

		self.remindermenu.add_separator()

		self.remindermenu.add_command(label="Medication")  #add command here

		self.remindermenu.add_separator()

		self.menubar.add_cascade(label="Reminders", menu=self.remindermenu)



		# the inventory sub-menu

		self.inventorymenu=Menu(self.menubar)

		self.inventorymenu.add_command(label="View Inventory", command=self.print_inventory)   #add command here

		self.menubar.add_cascade(label="Inventory", menu=self.inventorymenu)



		#end of the menu stuff

		self.new_frames()

		self.welcome=Label(self.info_frame, text="INVENTORY MANAGEMENT FOR THE MODERN HOUSEHOLD")

		self.welcome.config(font=('Courier',16))

		self.welcome.place(x=300,y=60,anchor='center',width=590,height=50)

		self.instructions=Label(self.tool_frame,text="Please choose an option").place(x=300,y=60,anchor='center',width=400,height=50)

	# different functions for all tools and features
		self.check_expiry()
	def new_frames(self):

		# the two main frames

		self.info_frame=Frame(self.main,height=150,width=600 ,bg='blue')

		self.tool_frame=Frame(self.main,height=350,width=600)

		# display the frames

		self.info_frame.pack(side="top")

		self.tool_frame.pack(side='bottom')

	def destroy_frames(self):

		self.info_frame.destroy()

		self.tool_frame.destroy()

	def add_to_inventory_widget(self):

		self.destroy_frames()
		self.new_frames()
		self.add_message=Label(self.tool_frame,text="Which item would you like to add ?").place(x=30,y=30)
		self.text_box=Entry(self.tool_frame)
		self.text_box.place(x=30,y=60)
		self.add_message1=Label(self.tool_frame,text="Enter quantity of Item").place(x=30,y=90)
		self.text_box1=Entry(self.tool_frame)
		self.text_box1.place(x=30,y=120)
		self.add_message2=Label(self.tool_frame,text="Enter expiry date of Item (DD-MM-YYYY)").place(x=30,y=150)
		self.text_box2=Entry(self.tool_frame)
		self.text_box2.place(x=30,y=180)
		self.enter= Button(self.tool_frame, text='Enter', command=the_inventory.add_item_middle)
		self.enter.place(x=60,y=200)

		self.bar_button = Button(self.tool_frame,text = 'Use Barcode', command= self.bar_code_scan)
		self.bar_button.place(x=240, y=55)

		self.ibm_button = Button(self.tool_frame,text = 'Recognise Object', command= self.ibm_scan)
		self.ibm_button.place(x=250, y=100)
	def remove_from_inventory_widget(self):
		self.destroy_frames()
		self.new_frames()
		self.add_message=Label(self.tool_frame,text="Which item would you like to remove ?").place(x=30,y=30)
		self.text_box=Entry(self.tool_frame)
		self.text_box.place(x=30,y=60)
		self.add_message1=Label(self.tool_frame,text="Enter quantity of Item").place(x=30,y=90)
		self.text_box1=Entry(self.tool_frame)
		self.text_box1.place(x=30,y=120)
		self.enter= Button(self.tool_frame, text='Enter', command=the_inventory.remove_item_middle)
		self.enter.place(x=60,y=200)
		self.bar_button = Button(self.tool_frame,text = 'Use Barcode', command= self.bar_code_scan)
		self.bar_button.place(x=240, y=55)

		self.ibm_button = Button(self.tool_frame,text = 'Recognise Object', command= self.ibm_scan)
		self.ibm_button.place(x=250, y=100)
	def bar_code_scan(self):
		self.text_box.delete(0,END)
		self.text_box.insert(0,str(pyzbar1.scan_code()))


	def ibm_scan(self):
		self.text_box.delete(0,END)
		self.text_box.insert(0,str(image_recog.scanner()))
	def print_inventory(self):
		self.destroy_frames()
		self.new_frames()
		self.tool_frame.config(background='white')
		print(the_inventory.inv)
		rows=len(the_inventory.inv)

		columns=3

		for i in range(-1,rows):

			for j in range(0,columns):

			    if j==0:

			        key='name'

			    elif j==1:

			        key='quantity'

			    elif j==2:

			        key='expiry'

			    if i<0:

			        item= Label(self.tool_frame, text=key, fg='white', bg='black') 

			    else:

			        item= Label(self.tool_frame, text=the_inventory.inv[i][key], fg='white', bg='black')                                          

			    item.place(x=100*((j*2)+1),y=int(350/len(the_inventory.inv)-(2*len(the_inventory.inv)))*(i+1))


	def show_recipes(self):
		self.destroy_frames()
		self.new_frames()

		heading1=Label(self.tool_frame, text="ALL RECIPES").place(x=20, y=5)
		heading2=Label(self.tool_frame, text="AVAILABLE RECIPES").place(x=300, y=5)
		# display list of all possible recipes
		self.all_rec_list = Listbox (self.tool_frame, width=25, height=150 )
		self.all_rec_list.place(x = 20, y=20)

		self.contents = recipe_list.all_recipes

		for i in range (0, len(self.contents)):

			self.all_rec_list.insert(END, self.contents[i]['name'])

		# display list of all available recipes
		self.all_avail_list = Listbox (self.tool_frame, width=25, height=150 )
		self.all_avail_list.place(x = 300, y=20)
		
		#get a list of names and quantities of items in inventory
		#self.available_items=[]
		#or i in range(0,len(the_inventory.inv)):




		self.available_items=[]
		for i in range(0,len(the_inventory.inv)):

			self.available_items.append([the_inventory.inv[i]['name'],the_inventory.inv[i]['quantity']])
		for recipe in self.contents:
			self.a=False
			print(recipe)
			print(self.available_items)
			for ingredient in recipe["ingredients"]:
				for i in self.available_items:
					if ingredient["name"] == i[0] and int(ingredient["quantity"]) <= int(i[1]):
						self.a=True
						break
					else:
						self.a=False
				if not self.a:
					break
			if self.a:
				self.all_avail_list.insert(END, recipe["name"])
			print(self.a)

	def sms_and_messagebox(self,text=None):
		self.message = messagebox.showinfo('alert', text)
		twilio_trial.SMS_sender(text)

	def if_expire(self, items=None):
		now = datetime.datetime.now()
		time=str(str(now.hour)+'/'+str(now.minute))
		if time == '3/37':
			print('a')
			date = str(now.day)+'-'+'0'+str(now.month)+'-'+str(now.year)
			for i in range(len(items)):
				if str(date) == items[i]['expiry']:
					self.sms_and_messagebox(f"{items[i]['name']} has expired.")
	def almost_expired(self,items=None):
		now = datetime.datetime.now()
		for i in range(len(items)):
			if int(now.year)==int(items[i]['expiry'][6:]):
				if int(now.month)==int(items[i]['expiry'][3:5]):
					if (int(now.day)+3)==int(items[i]['expiry'][:2]):
						self.sms_and_messagebox(f"{items[i]['name']} is going to expire in three days !")
	def check_expiry(self):
		
		self.almost_expired(the_inventory.inv)
		self.if_expire(the_inventory.inv)

if __name__ == "__main__":
	root=Tk()
	main_app=Application(root)
	root.mainloop()