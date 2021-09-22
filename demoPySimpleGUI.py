import PySimpleGUI as sg

#sg.theme('DarkGrey12')

layout = [
	[sg.Text('Hello World!')]

]

window = sg.Window('My First Window', layout, size=(1400,600))

event, values = window.read()

window.close()