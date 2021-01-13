import tkinter


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


def createCommandButton(root, text, command, padx=40, pady=20):
    my_button = tkinter.Button(
        master=root,
        text=text,
        command=lambda: command(root),
        padx=padx,
        pady=pady
    )
    return my_button


def button_0_func(root):
    return


def button_1_func(root):
    return


def button_2_func(root):
    return


def button_3_func(root):
    return


def button_4_func(root):
    return


def button_5_func(root):
    return


def button_6_func(root):
    return


def button_7_func(root):
    return


def button_8_func(root):
    return


def button_9_func(root):
    return


def button_add_func(root):
    return


def button_equal_func(root):
    return


def button_clear_func(root):
    return


def main():

    root_calc = tkinterSetup()
    root_calc.title('Simple Calculator')

    entry = createWideEntry(root_calc, width=35)
    entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

    button_0 = createCommandButton(
        root=root_calc,
        text='0',
        command=button_0_func
    )
    button_1 = createCommandButton(
        root=root_calc,
        text='1',
        command=button_1_func
    )
    button_2 = createCommandButton(
        root=root_calc,
        text='2',
        command=button_2_func
    )
    button_3 = createCommandButton(
        root=root_calc,
        text='3',
        command=button_3_func
    )
    button_4 = createCommandButton(
        root=root_calc,
        text='4',
        command=button_4_func
    )
    button_5 = createCommandButton(
        root=root_calc,
        text='5',
        command=button_5_func
    )
    button_6 = createCommandButton(
        root=root_calc,
        text='6',
        command=button_6_func
    )
    button_7 = createCommandButton(
        root=root_calc,
        text='7',
        command=button_7_func
    )
    button_8 = createCommandButton(
        root=root_calc,
        text='8',
        command=button_8_func
    )
    button_9 = createCommandButton(
        root=root_calc,
        text='9',
        command=button_9_func
    )
    button_add = createCommandButton(
        root=root_calc,
        text='+',
        command=button_add_func,
        padx=39
    )
    button_equal = createCommandButton(
        root=root_calc,
        text='=',
        command=button_equal_func,
        padx=91
    )
    button_clear = createCommandButton(
        root=root_calc,
        text='Clear',
        command=button_clear_func,
        padx=79
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

    root_calc.mainloop()


if __name__ == "__main__":
    main()
