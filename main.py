clients = 'Pablo, Ricardo'

#functions-------------------------------------------
def _start():
    print('-#'*50)
    print('WELCOME TO YODO SUITE, PLEASE CHOOSE AN OPTION TO PROCEED:')
    print('-#'*50)
    print('↓  '*33)
    print('1- [C]REATE A CLIENT')
    print('2- [D]ELETE A CLIENT')

def create_client(client: str):
    global clients #global is for indicate the use of a global variable into func
    if client not in clients:
        _add_comma_space()
        clients += client
        print('CLIENT SUCCESFULLY ADDED!')
    else:
        print('THIS CLIENT ALREADY EXIST!')

def show_clients():
    global clients
    print(clients)

def _add_comma_space():#private function (_)
    global clients
    clients += ', '

#------------------------------------------------------
if __name__ == '__main__':
    _start()

    command = input()

    if command == 'C':
        client_name = input('WHAT IS THE CLIENT NAME: ')
        create_client(client_name)
        show_clients()
    elif command == 'D':
        pass
    else:
        print('INVALID COMMAND!')