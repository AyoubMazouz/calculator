from tkinter import *
from sympy import sympify
from tkinter.font import *
# Imports 
# tkinter for the GUI
# tkinter.font to custimize the font
# sympy to calculate diffrente operation.

def main():
	# root initiate the screen.
	# And setting the window title.
	root = Tk(className='Calculator')
	# Some colors for buttons, label, entry and root.
	dark = '#393e46'
	medium = '#00adb5'
	light = '#eeeeee'
	# Changing window color
	root.config(bg=dark)
	

	# It checks for invalid attemts and try ignore it or make fix it.
	# First if statement prevent passing double operation symbols.
	# Second statement prevent unnecessary '0' and so does the third one.
	def num_btn_click(num):
		if num in '.+/*-':
			if entry.get()[-1] in '.+/*-':
				delete()
				entry.insert(END, num)
			else:
				entry.insert(END, num)

		elif entry.get() == '0':
			if num != '0':
				clear('entry')
				entry.insert(END, num)
		elif entry.get() == 'nan':
			clear('entry')
			entry.insert(END, num)
		else:
			try:
				if entry.get()[-2] in '+/*-' and entry.get()[-1] == '0':
					if num != '0':
						delete('0')
						entry.insert(END, num)
				else:
					entry.insert(END, num)
			except: 
				entry.insert(END, num)

	# This function try to make the operation if it does it display information in label and entry.
	# If there id an exception the error method is called.
	# operation = round(sympify(entry.get()), 3)
	# Using sympy library > sympy.sympify 
	# It alow us to pass in a string (should be a valid number and operators) and return the result.
	# for more information see > https://docs.sympy.org/latest/index.html
	def equal():
		try:
			operation = round(sympify(entry.get().replace('×', '*')), 6)
			label['text'] = f'{entry.get()} ='
			clear('entry')
			entry.insert(END, operation)
		except:
			error('show')

	def square():
		try:
			operation = sympify(entry.get().replace('×', '*')) ** 2
			label['text'] = f'({entry.get()})^2 ='
			clear('entry')
			entry.insert(END, operation)
		except:
			error('show')

	def cube():
		try:
			operation = sympify(entry.get().replace('×', '*')) ** 3
			label['text'] = f'({entry.get()})^3 ='
			clear('entry')
			entry.insert(END, operation)
		except:
			error('show')

	def square_root():
		try:
			operation = '%g'%(sympify(entry.get().replace('×', '*')) ** 0.5)
			label['text'] = f'√({entry.get()}) ='
			clear('entry')
			entry.insert(END, operation)
		except:
			error('show')
	
	# It allow to delete one char at a time.
	# Make sure if entry has no value insert '0' in it.
	def delete(arg=''):
		if arg == '0':
			entry.delete(len(entry.get()) - 1, END)
		else:
			if entry.get() != '0':
				entry.delete(len(entry.get()) - 1, END)

			if entry.get() == '':
				defult_entry()

		

	# it clears entry and label according to the given argument 'arg'.
	def clear(arg=''):
		if 'entry' == arg:
			entry.delete(0, END)

		else:
			label['text'] = '0'
			entry.delete(0, END)
			defult_entry()

		# when an error is rised the entry and label has message text from the error function.
		# This if statment check if error text in entry, if so, then label also has error message,
		#  so it calls error without arguments.
		if 'Inalid Operation' == entry.get():
			error()

	# Insert '0' to entry to be the defult text, Entry widget has no 'text' option.
	# This function is call ones when programm starts, and several time in other fuctions.
	def defult_entry():
		entry.insert(0, '0')

	# 'error' handle any exception thrown by equal function
	# call clear() > show meassage in entry and label
	def error(arg=''):
		if 'show' == arg:
			clear()
			clear('entry')
			entry.insert(END, 'Inalid Operation')
			label['text'] = 'Press clear'
		else:
			clear()

	def test():
		pass

	# 'font' is a Font object, used to custimize the font, it is passed to the dictionary 'b' and 'l'. 
	font = Font(family='Roboto', size=22)
	# Dictionary 'b' holds options for all Buttonm widgets.
	b = {
		'w': 5,
		'h': 2,
		'fg': light,
		'bg': dark,
		'font': font,
		'bd': 0,
		'abg': medium,
		'afg': light
	}
	# Dictionary 'l' holds options for label and entry
	l = {
		'w': 20,
		'fg': light,
		'bg': dark,
		'font': font,
		'pady': 6,
		'bd': 0,
		'justify': 'right'
	}
	# 'label' is a Label widget, where the operation is shown.
	# 'entry' is an Entry widget, where the user type the operation.
	label = Label(root, text = "0", width=l['w'], font=l['font'], bg=l['bg'], fg=l['fg'], 
		pady=l['pady'], anchor=NW)
	entry = Entry(root, width=l['w'], font=l['font'], bg=l['bg'], fg=l['fg'], bd=l['bd'], 
		justify=l['justify'])

	# This function is called at the starts of the programm.
	defult_entry()
	# Creating object button*10 [button0 - button9].
	# 'b' is a dictionay holding button opitons.
	# If you want to make a change to the color or other values, you can change 
	# 		just the value in the dictionary.
	button9 = Button(root, text = "9", width=b['w'], height=b['h'], font=b['font'], fg=b['fg'], 
		bg=b['bg'], bd=b['bd'], activebackground=b['abg'], activeforeground=b['afg'], 
		command = lambda:num_btn_click("9"))
	button8 = Button(root, text = "8", width=b['w'], height=b['h'], font=b['font'], fg=b['fg'], 
		bg=b['bg'], bd=b['bd'], activebackground=b['abg'], activeforeground=b['afg'], 
		command = lambda:num_btn_click("8"))
	button7 = Button(root, text = "7", width=b['w'], height=b['h'], font=b['font'], fg=b['fg'], 
		bg=b['bg'], bd=b['bd'], activebackground=b['abg'], activeforeground=b['afg'], 
		command = lambda:num_btn_click("7"))
	button6 = Button(root, text = "6", width=b['w'], height=b['h'], font=b['font'], fg=b['fg'], 
		bg=b['bg'], bd=b['bd'], activebackground=b['abg'], activeforeground=b['afg'], 
		command = lambda:num_btn_click("6"))
	button5 = Button(root, text = "5", width=b['w'], height=b['h'], font=b['font'], fg=b['fg'], 
		bg=b['bg'], bd=b['bd'], activebackground=b['abg'], activeforeground=b['afg'], 
		command = lambda:num_btn_click("5"))
	button4 = Button(root, text = "4", width=b['w'], height=b['h'], font=b['font'], fg=b['fg'], 
		bg=b['bg'], bd=b['bd'], activebackground=b['abg'], activeforeground=b['afg'], 
		command = lambda:num_btn_click("4"))
	button3 = Button(root, text = "3", width=b['w'], height=b['h'], font=b['font'], fg=b['fg'], 
		bg=b['bg'], bd=b['bd'], activebackground=b['abg'], activeforeground=b['afg'], 
		command = lambda:num_btn_click("3"))
	button2 = Button(root, text = "2", width=b['w'], height=b['h'], font=b['font'], fg=b['fg'], 
		bg=b['bg'], bd=b['bd'], activebackground=b['abg'], activeforeground=b['afg'], 
		command = lambda:num_btn_click("2"))
	button1 = Button(root, text = "1", width=b['w'], height=b['h'], font=b['font'], fg=b['fg'], 
		bg=b['bg'], bd=b['bd'], activebackground=b['abg'], activeforeground=b['afg'], 
		command = lambda:num_btn_click("1"))
	button0 = Button(root, text = "0", width=b['w'], height=b['h'], font=b['font'], fg=b['fg'], 
		bg=b['bg'], bd=b['bd'], activebackground=b['abg'], activeforeground=b['afg'], 
		command = lambda:num_btn_click("0"))
	btn_dot = Button(root, text = ".", width=b['w'], height=b['h'], font=b['font'], fg=b['fg'], 
		bg=b['bg'], bd=b['bd'], activebackground=b['abg'], activeforeground=b['afg'], 
		command = lambda:num_btn_click("."))
	btn_delete = Button(root, text = "D", width=b['w'], height=b['h'], font=b['font'], fg=b['fg'], 
		bg=b['bg'], bd=b['bd'], activebackground=b['abg'], activeforeground=b['afg'], 
		command = delete)
	btn_clear = Button(root, text = "C", width=b['w'], height=b['h'], font=b['font'], fg=b['fg'], 
		bg=b['bg'], bd=b['bd'], activebackground=b['abg'], activeforeground=b['afg'], 
		command = lambda:clear())
	btn_equal = Button(root, text = "=", width=b['w']*2, height=b['h'], font=b['font'], fg=b['fg'], 
		bg=b['bg'], bd=b['bd'], activebackground=b['abg'], activeforeground=b['afg'], 
		command = equal)
	btn_plus = Button(root, text = "+", width=b['w'], height=b['h'], font=b['font'], fg=b['fg'], 
		bg=b['bg'], bd=b['bd'], command = lambda:num_btn_click("+"))
	btn_minus = Button(root, text = "-", width=b['w'], height=b['h'], font=b['font'], fg=b['fg'], 
		bg=b['bg'], bd=b['bd'], activebackground=b['abg'], activeforeground=b['afg'], 
		command = lambda:num_btn_click("-"))
	btn_multiply = Button(root, text = "×", width=b['w'], height=b['h'], font=b['font'], fg=b['fg'], 
		bg=b['bg'], bd=b['bd'], activebackground=b['abg'], activeforeground=b['afg'], 
		command = lambda:num_btn_click("×"))
	btn_divide = Button(root, text = "/", width=b['w'], height=b['h'], font=b['font'], fg=b['fg'], 
		bg=b['bg'], bd=b['bd'], activebackground=b['abg'], activeforeground=b['afg'], 
		command = lambda:num_btn_click("/"))
	btn_open_parenthsis = Button(root, text = "(", width=b['w'], height=b['h'], font=b['font'], 
		fg=b['fg'], bd=b['bd'], bg=b['bg'], activebackground=b['abg'], activeforeground=b['afg'], 
		command = lambda:num_btn_click("("))
	btn_close_parenthsis = Button(root, text = ")", width=b['w'], height=b['h'], font=b['font'], 
		fg=b['fg'], bd=b['bd'], bg=b['bg'], activebackground=b['abg'], activeforeground=b['afg'], 
		command = lambda:num_btn_click(")"))
	btn_square = Button(root, text = "x^2", width=b['w'], height=b['h'], font=b['font'], 
		fg=b['fg'], bd=b['bd'], bg=b['bg'], activebackground=b['abg'], activeforeground=b['afg'], 
		command = square)
	btn_cube = Button(root, text = "x^3", width=b['w'], height=b['h'], font=b['font'], 
		fg=b['fg'], bd=b['bd'], bg=b['bg'], activebackground=b['abg'], activeforeground=b['afg'], 
		command = cube)
	btn_square_root = Button(root, text = "√", width=b['w'], height=b['h'], font=b['font'], 
		fg=b['fg'], bd=b['bd'], bg=b['bg'], activebackground=b['abg'], activeforeground=b['afg'], 
		command = square_root)

	# using the grid system to place each buttom in place.
	label.grid(row = 0, column = 0, columnspan = 4)
	entry.grid(row = 1, column = 0, columnspan = 4)
	btn_open_parenthsis.grid(row = 2, column = 0)
	btn_close_parenthsis.grid(row = 2, column = 1)
	btn_clear.grid(row = 2, column = 2)
	btn_delete.grid(row = 2, column = 3)
	btn_square.grid(row = 3, column = 0)
	btn_cube.grid(row = 3, column = 1)
	btn_square_root.grid(row = 3, column = 2)
	btn_divide.grid(row = 3, column = 3)
	button1.grid(row = 4, column = 0)
	button2.grid(row = 4, column = 1)
	button3.grid(row = 4, column = 2)
	btn_multiply.grid(row = 4, column = 3)
	button4.grid(row = 5, column = 0)
	button5.grid(row = 5, column = 1)
	button6.grid(row = 5, column = 2)
	btn_minus.grid(row = 5, column = 3)
	button7.grid(row = 6, column = 0)
	button8.grid(row = 6, column = 1)
	button9.grid(row = 6, column = 2)
	btn_plus.grid(row = 6, column = 3)
	btn_dot.grid(row = 7, column = 0)
	button0.grid(row = 7, column = 1)
	btn_equal.grid(row = 7, column = 2, columnspan=2)
	
	
	

	# 'mainloop' is needed to run the programm
	root.mainloop()

# Only run when '__name__' this file == to '__main__' the main file.
if __name__ == '__main__': 
	main()

# This project is made for learning.
# This code is a mess, I did the best I could.
# sorry if I didn't explain my functions well.
# Thanks for your time.