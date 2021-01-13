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


def main():

    root_calc = tkinterSetup()
    root_calc.title('Simple Calculator')


if __name__ == "__main__":
    main()
