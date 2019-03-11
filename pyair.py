from src.airctrl import AirClient
import sys
import time
import os
from tkinter import *

# ip = sys.argv[1]
ip = '192.168.13.106'

airctrl = AirClient(ip)
airctrl.load_key()


# airctrl.get_status()
# resp = airctrl.get_raw()
# while True:
#     os.system('cls')
#     print('PM2,5: {}'.format(airctrl.get_raw()['pm25']))
#     time.sleep(2)

def refresh():
    philipsData = airctrl.get_raw()
    txtPm25.delete(0, END)
    txtAler.delete(0, END)
    txtBright.delete(0, END)

    txtPm25.insert(0, philipsData['pm25'])
    txtAler.insert(0, philipsData['iaql'])
    txtBright.insert(0, philipsData['aqil'])

window = Tk()
window.title('pyair')

lblPm25 = Label(window, text='Poziom cząstek PM 2,5: ')
lblPm25.grid(column=0, row=0)

txtPm25 = Entry(window, width=3)
txtPm25.grid(column=1, row=0)

lblAler = Label(window, text='Poziom alergenów: ')
lblAler.grid(column=0, row=1)

txtAler = Entry(window, width=3)
txtAler.grid(column=1, row=1)

lblBright = Label(window, text='Jasność wyświetlacza: ')
lblBright.grid(column=0, row=2)

txtBright = Entry(window, width=3)
txtBright.grid(column=1, row=2)

btnRefresh = Button(window, text='Odśwież', anchor="w", command=refresh)
btnRefresh.grid(column=0, row=3, sticky='w')

refresh()
window.mainloop()
#test gita