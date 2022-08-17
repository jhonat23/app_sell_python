import time
import sys

clients = [
    {
        'name': 'Pablo',
        'company': 'Google',
        'email': 'pablo@google.com',
        'position': 'Software Engineer',
    },
    {
        'name': 'Ricardo',
        'company': 'Facebook',
        'email': 'ricardo@facebook.com',
        'position': 'Data Engineer',
    }
    ]

#functions-------------------------------------------
def create_client(client):
    global clients #global is for indicate the use of a global variable into func
    if client not in clients:
        clients.append(client)
        print('CLIENT SUCCESFULLY ADDED!')
    else:
        print('THIS CLIENT ALREADY EXIST!')


def update_client(client: str, new_client: str):
    global clients
    if client in clients:
        index = clients.index(client)
        clients[index] = new_client
        print(F'THE CLIENT {client} UPDATED')
    else:
        print('THE CLIENT IS NOT IN DATA')


def delete_client(client: str):
    global clients
    if client in clients:
        clients.remove(client)
        print(F'THE CLIENT {client} DELETED')
    else:
        print('THE CLIENT IS NOT IN DATA')


def show_clients():
    global clients
    print('↓ '* 10)
    for i, client in enumerate(clients):
        print('{0} | {1} | {2} | {3} |'.format(client['name'], client['company'], client['email'], client['position']))
    print('↑ '* 10)
    time.sleep(1.5)


def find_client(client: str):
    global clients
    count = 0
    for c in clients:
        if c != client:
            count += 1
            if count == len(clients):
                print(f'THE CLIENT {client} IS NOT FOUND!')
                return False
            else:
                continue
        elif c == client:
            print(f'THE CLIENT {client} HAS BEEN FOUND!')
            return True


# private functions

def _start():
    print('-#'*50)
    print('WELCOME TO YODO SUITE, PLEASE CHOOSE AN OPTION TO PROCEED:')
    print('-#'*50)
    print('↓  '*33)
    print('1- [C]REATE A CLIENT')
    print('2- [R]READ CLIENT LIST')
    print('3- [U]PDATE A CLIENT')
    print('4- [D]ELETE A CLIENT')   
    print('5- [S]EARCH CLIENT')
    print('[E]XIT')


def _exit():
    print('-#'*50)
    print('↓  '*33)
    print('THANKS FOR USING YODO SUITE')


def _get_client_name():
    client_name = None
    while not client_name:
        client_name = input('WHAT IS THE CLIENT NAME: ')
        if client_name == 'exit':
            client_name == None
            break
    if not client_name:
        sys.exit()
    return client_name


def _get_client_field(field_name):
    field = None
    while not field:
        field = input(F'WHAT IS THE CLIENT {field_name}: ')
    return field
    

#------------------------------------------------------
if __name__ == '__main__':
    while True:
        _start()

        command = input()
        command = command.upper()

        if command == 'C':
            client = {
                'name': _get_client_field('NAME'),
                'company': _get_client_field('COMPANY'),
                'email' : _get_client_field('EMAIL'),
                'position' : _get_client_field('POSITION')
            }
            create_client(client)
            show_clients()
        elif command == 'R':
            show_clients()
        elif command == 'U':
            client_name = _get_client_name()
            new_client = input('WHAT IS THE NEW CLIENT NAME: ')
            update_client(client_name, new_client)
            show_clients()
        elif command == 'D':
            client_name = _get_client_name()
            delete_client(client_name)
            show_clients()
        elif command == 'S':
            client_name = _get_client_name()
            find_client(client_name)
        elif command == 'E':
            _exit()
            break
        else:
            print('INVALID COMMAND!')
        