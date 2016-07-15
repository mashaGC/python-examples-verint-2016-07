_author_ = 'mariag'

def int_str(int_arg, str_arg):
    if type(int_arg) != int:
        raise Exception ("int_arg expects integer")
    if type(str_arg) != str:
        raise Exception ("str_arg expects string")

int_str('3',4)