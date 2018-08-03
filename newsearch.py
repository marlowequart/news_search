'''
News Search

Given:


Return:


'''

from tkinter import *
#from numpy import *
import re
import urllib.request


class Application(Frame):


	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.grid()
		self.master = master



def open_gui(gui_quote_list):
#open a gui with the results displayed
	root = Tk()

	#Set the size of the window
	#root.geometry("400x300")
	root.title('News Brief')

	#create titles at the top of gui
	title1 = Label(root, text='This gui will ')
	title1.grid(row=0, columnspan=8)
	title2 = Label(root, text='Current Price')
	title2.grid(row=1,column=1)
	
	for num in range(len(gui_quote_list)):
		#create variable for symbol
#		dt=StringVar()
		initial_row=1

		#create label for nsamp entry
		label1 = Label(root, text='%s:' % gui_quote_list[num])
		label1.grid(row=initial_row+num, column=0)

		#create entry box for nsamp
		entry1 = Entry(root, bd=2)
		entry1.insert(END,0)
#		nsamp.set(100000)
		entry1.grid(row=initial_row+num,column=1)

		
	app = Application(root)
	root.mainloop()

#def get_quote(quote_list):
#get updated quotes



def search_news():
#search for news articles with given topics

	topics=['spinoff','merger']
	
def gain_loss():
#check for large % moves in previous 48 hours

	#p_change is the threshold for percent change to verify
	p_change='7'







def main():

	symbols=['BAC','AAPL','SYF','HRB','MHK']
#	get_quote(symbols)
	open_gui(symbols)





main()