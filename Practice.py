from tkinter import  *
import tkinter.ttk as ttk
root = Tk()
style = ttk.Style()
style.theme_create('style_class',

                   # getting the settings
                   settings={

                       # getting through the Labelframe
                       # widget
                       'TLabelframe': {

                           # configure the changes
                           'configure': {
                               'background': '#2c3038'
                           }
                       },

                       # getting through the Labelframe's
                       # label widget
                       'TLabelframe.Label': {
                           'configure': {
                               'background': '#2c3038',
                               'foreground': '#00fff7'
                           }
                       }
                   }
                   )
style.theme_use('style_class')

# created a label frame with title "Group"
labelframe = ttk.LabelFrame(root, text="Group")

# provide padding
labelframe.pack(padx=30, pady=30)

# created the text label inside the the labelframe
left = Label(labelframe, text="Geeks for Geeks")

left.pack()

root.mainloop()
