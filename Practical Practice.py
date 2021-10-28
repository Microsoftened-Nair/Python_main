from tkinter import *

def fib():
    n = int(nEntry.get())
    lst = [0,1]
    for i in range(1, n+1):
         if i==1:
             a = lst[0]+lst[1]
             lst.append(a)
         if i > 1:
             a = lst[-1] + lst[-2]
             lst.append(a)

    m = len(lst)
    l2.configure(text='Your Fibonacci series is {}'.format(lst[0:m - 2]))

root = Tk()
root.title('Fibonacci Series')

head = LabelFrame(root, text='Fibonacci Series', font=('Segoe UI', 20, 'bold'), relief=RIDGE, bd=10)
head.pack()

l1 = Label(head, text='Enter the number of elements in fibonacci series: ', font=('Segoe UI', 15))
l1.pack()

nEntry = Entry(head, font=('Segoe UI', 20, 'bold'))
nEntry.pack()

l2 = Label(head, font=('Segoe UI', 18, 'bold'))
l2.pack()

submit = Button(head, text='Submit', font=('Segoe UI', 15), command=fib)
submit.pack()

root.mainloop()

# lst = [0,1]
# n = int(input(''))
#
# for i in range(1, n+1):
#      if i==1:
#          a = lst[0]+lst[1]
#          lst.append(a)
#      if i > 1:
#          a = lst[-1] + lst[-2]
#          lst.append(a)
#
# m = len(lst)
# print(lst[0:m-2])
