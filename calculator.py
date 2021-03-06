import tkinter


global first_operand, last_operation
last_operation = '+'
first_operand = 0


def tkinterSetup():
    root = tkinter.Tk()
    return root


def createLabel(root, text):
    my_label = tkinter.Label(
        master=root,
        text=text
    )
    return my_label


def createWideEntry(root, width=60):
    entry = tkinter.Entry(root, width=width, borderwidth=5)
    return entry


def createCommandButton(
        root,
        text,
        command,
        command_arg,
        entry,
        padx=40,
        pady=20
        ):
    my_button = tkinter.Button(
        master=root,
        text=text,
        command=lambda: command(root, command_arg, entry),
        padx=padx,
        pady=pady
    )
    return my_button


def button_numeric_func(root, number, entry):
    # entry.delete(0, tkinter.END)
    entry.insert(tkinter.END, number)


def button_special_func(root, choice, entry):
    global first_operand, last_operation
    if choice == 'clear':
        entry.delete(0, tkinter.END)
        first_operand = 0
    elif choice == 'add':
        first_operand += float(entry.get())
        last_operation = '+'
        entry.delete(0, tkinter.END)
    elif choice == 'sub':
        first_operand -= float(entry.get())
        last_operation = '-'
        entry.delete(0, tkinter.END)
    elif choice == 'mul':
        first_operand = 1 if first_operand == 0 else first_operand
        first_operand *= float(entry.get())
        last_operation = '*'
        entry.delete(0, tkinter.END)
    elif choice == 'div':
        if first_operand != 0:
            first_operand /= float(entry.get())
        else:
            first_operand = float(entry.get())
        last_operation = '/'
        entry.delete(0, tkinter.END)
    elif choice == 'equal':
        if last_operation == '+':
            first_operand += float(entry.get()) if entry.get() != '' else 0
        elif last_operation == '-':
            first_operand -= float(entry.get()) if entry.get() != '' else 0
        elif last_operation == '*':
            first_operand *= float(entry.get()) if entry.get() != '' else 1
        elif last_operation == '/':
            first_operand /= float(entry.get()) if entry.get() != '' else 1
        entry.delete(0, tkinter.END)
        entry.insert(0, first_operand)
        first_operand = 0


def main():

    root_calc = tkinterSetup()
    root_calc.title('Simple Calculator')

    entry = createWideEntry(root_calc, width=35)
    entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

    button_0 = createCommandButton(
        root=root_calc,
        text='0',
        command=button_numeric_func,
        command_arg=0,
        entry=entry
    )
    button_1 = createCommandButton(
        root=root_calc,
        text='1',
        command=button_numeric_func,
        command_arg=1,
        entry=entry
    )
    button_2 = createCommandButton(
        root=root_calc,
        text='2',
        command=button_numeric_func,
        command_arg=2,
        entry=entry
    )
    button_3 = createCommandButton(
        root=root_calc,
        text='3',
        command=button_numeric_func,
        command_arg=3,
        entry=entry
    )
    button_4 = createCommandButton(
        root=root_calc,
        text='4',
        command=button_numeric_func,
        command_arg=4,
        entry=entry
    )
    button_5 = createCommandButton(
        root=root_calc,
        text='5',
        command=button_numeric_func,
        command_arg=5,
        entry=entry
    )
    button_6 = createCommandButton(
        root=root_calc,
        text='6',
        command=button_numeric_func,
        command_arg=6,
        entry=entry
    )
    button_7 = createCommandButton(
        root=root_calc,
        text='7',
        command=button_numeric_func,
        command_arg=7,
        entry=entry
    )
    button_8 = createCommandButton(
        root=root_calc,
        text='8',
        command=button_numeric_func,
        command_arg=8,
        entry=entry
    )
    button_9 = createCommandButton(
        root=root_calc,
        text='9',
        command=button_numeric_func,
        command_arg=9,
        entry=entry
    )
    button_add = createCommandButton(
        root=root_calc,
        text='+',
        command=button_special_func,
        command_arg='add',
        entry=entry,
        padx=39
    )
    button_sub = createCommandButton(
        root=root_calc,
        text='-',
        command=button_special_func,
        command_arg='sub',
        entry=entry,
        padx=41
    )
    button_mul = createCommandButton(
        root=root_calc,
        text='*',
        command=button_special_func,
        command_arg='mul',
        entry=entry,
        padx=40
    )
    button_div = createCommandButton(
        root=root_calc,
        text='/',
        command=button_special_func,
        command_arg='div',
        entry=entry,
        padx=41
    )
    button_equal = createCommandButton(
        root=root_calc,
        text='=',
        command=button_special_func,
        command_arg='equal',
        entry=entry,
        padx=87
    )
    button_clear = createCommandButton(
        root=root_calc,
        text='Clear',
        command=button_special_func,
        command_arg='clear',
        entry=entry,
        padx=77
    )

    # Place button on screen
    button_1.grid(row=3, column=0)
    button_2.grid(row=3, column=1)
    button_3.grid(row=3, column=2)

    button_4.grid(row=2, column=0)
    button_5.grid(row=2, column=1)
    button_6.grid(row=2, column=2)

    button_7.grid(row=1, column=0)
    button_8.grid(row=1, column=1)
    button_9.grid(row=1, column=2)

    button_0.grid(row=4, column=0)
    button_clear.grid(row=4, column=1, columnspan=2)
    button_add.grid(row=5, column=0)
    button_equal.grid(row=5, column=1, columnspan=2)

    button_sub.grid(row=6, column=0)
    button_mul.grid(row=6, column=1)
    button_div.grid(row=6, column=2)

    root_calc.mainloop()


if __name__ == "__main__":
    main()
