clients = 'Pablo, Ricardo'

#functions-------------------------------------------
def _start():
    print('-#'*50)
    print('WELCOME TO YODO SUITE, PLEASE CHOOSE AN OPTION TO PROCEED:')
    print('-#'*50)
    print('↓  '*33)
    print('1- [C]REATE A CLIENT')
    print('2- [D]ELETE A CLIENT')
    print('3- [U]PDATE A CLIENT')
    print('[E]XIT')

def create_client(client: str):
    global clients #global is for indicate the use of a global variable into func
    if client not in clients:
        _add_comma_space()
        clients += client
        print('CLIENT SUCCESFULLY ADDED!')
    else:
        print('THIS CLIENT ALREADY EXIST!')

def update_client(client: str, new_client: str):
    global clients
    if client in clients:
        clients = clients.replace(client_name, new_client)
    else:
        print('THE CLIENT IS NOT IN DATA')

def show_clients():
    global clients
    print(clients)

# private functions

def _add_comma_space():#private function (_)
    global clients
    clients += ', '

def _get_client_name():
    return input('WHAT IS THE CLIENT NAME: ')

#------------------------------------------------------
if __name__ == '__main__':
    while True:
        _start()

        command = input()
        command = command.upper()

        if command == 'C':
            client_name = _get_client_name()
            create_client(client_name)
            show_clients()
        elif command == 'D':
            pass
        elif command == 'U':
            client_name = _get_client_name()
            new_client = input('WHAT IS THE NEW CLIENT NAME: ')
            update_client(client_name, new_client)
            show_clients()
        elif command == 'E':
            print('THANKS FOR USING YODO SUITE')
            break
        else:
            print('INVALID COMMAND!')
        