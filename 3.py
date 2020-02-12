class IntException(Exception):
    def __init__(self):
        self.txt = 'Введено не число '


res_list = []
while True:
    inp_user = input('Введите число или Enter для выхода ')
    if inp_user == '':
        break
    else:
        try:
            if inp_user.isdigit():
                res_list.append(int(inp_user))
            elif inp_user.count('.') > 1:
                raise IntException
            else:
                for sym in inp_user:
                    if not sym.isdigit() and sym != '.':
                        raise IntException
                res_list.append(float(inp_user))
        except IntException as err:
            print(err.txt)

print(res_list)