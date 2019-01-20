# datetime.datetime.today().strftime('%Y-%m-%d')

#import modules

from tkinter import *

#import datetime

#import pyzbar1

#import twilio_trial

#import big_basket



#class for the main inventory



class Inventory():

    def __init__(self,inv):

        self.inv=inv

    def add_item_middle():

        self.add_item(main_app.text_box.get(),main_app.text_box1.get(),main_app.text_box2.get())

    def add_item(self,name=None, quantity=0, expiry=None):

        self.inv[len(self.inv)]= {"name":name,'quantity':str(quantity) , "expiry":expiry}

    def remove_item(self,name=None):

        self.inv.pop(name)

    def retrieve_quantity(self,item):

        self.inv[item]["quantity"]

    def retrieve_expiry(self,item):

        self.inv[item]["expiry"]



# create an instance of inventory with some default items

the_inventory=Inventory({0:{'name':'tomato','quantity':'1', 'expiry':'20-1-2019'},

						 1:{'name':'carrot','quantity':'2', 'expiry':'18-1-2019'},

						 2:{'name':'carrot halwa','quantity':'1/2 kg', "expiry":'25-1-2019' }

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

		self.toolmenu.add_command(label="Remove From Inventory")  #add command here

		self.toolmenu.add_separator()

		self.toolmenu.add_command(label="Recipes")           #add command here

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

		self.inventorymenu.add_command(label="View Inventory")   #add command here

		self.menubar.add_cascade(label="Inventory", menu=self.inventorymenu)



		#end of the menu stuff

		self.new_frames()

		self.welcome=Label(self.info_frame, text="INVENTORY MANAGEMENT FOR THE MODERN HOUSEHOLD")

		self.welcome.config(font=('Courier',16))

		self.welcome.place(x=300,y=60,anchor='center',width=590,height=50)

		self.instructions=Label(self.tool_frame,text="Please choose an option").place(x=300,y=60,anchor='center',width=400,height=50)

	# different functions for all tools and features

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

		#self.bar_button = Button(self.tool_frame,text = 'Use Barcode').place(x=30, y=65)



        def print_inventory(self):

                self.destroy_frames()

                self.new_frames()

                self.tool_frame.config(background='black')

                rows=3

                columns=len(the_inventory.inv)

                for i in range(-1,rows):

                    for j in range(0,columns):

                        if j==0:

                            key='name'

                        elif j==1:

                            key='quantity'

                        elif j==2:

                            key='expiry'

                        if i<0:

                            item= Label(self.tool_frame, text=key) 

                        else:

                            item= Label(self.tool_frame, text=the_inventory.inv[rows][key])                                          

                        item.place(x=100*((j**2)+1),y=int(500/len(the_inventory.inv))+50)

                

	



		



if __name__ == "__main__":

	root=Tk()

	main_app=Application(root)

	root.mainloop()