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


def createCommandButton(root, text, command):
    my_button = tkinter.Button(
        master=root,
        text=text,
        command=lambda: command(root)
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

    root_calc.mainloop()


if __name__ == "__main__":
    main()
