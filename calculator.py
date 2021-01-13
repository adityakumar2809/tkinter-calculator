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


def main():

    root_calc = tkinterSetup()
    root_calc.title('Simple Calculator')

    entry = createWideEntry(root_calc, width=35)


if __name__ == "__main__":
    main()
