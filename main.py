import time
import sys
import csv
import os

CLIENT_TABLE = '.clients.csv'
CLIENT_SCHEMA = ['name', 'company', 'email', 'position']
clients = []

def _initialize_clients_data():
    with open(CLIENT_TABLE, mode='r') as f:
        reader = csv.DictReader(f, fieldnames=CLIENT_SCHEMA)
        for row in reader:
            clients.append(row)


def _save_clients():
    tmp_table_name = '{0}.tmp'.format(CLIENT_TABLE)
    with open(tmp_table_name, mode='w') as f:
        writer = csv.DictWriter(f, fieldnames=CLIENT_SCHEMA)
        writer.writerows(clients)
        
        os.remove(CLIENT_TABLE)
        os.rename(tmp_table_name, CLIENT_TABLE)

#functions-------------------------------------------
def create_client(client):
    global clients #global is for indicate the use of a global variable into func
    if client not in clients:
        clients.append(client)
        print('CLIENT SUCCESFULLY ADDED!')
    else:
        print('THIS CLIENT ALREADY EXIST!')


def update_client(client_id: str, new_client: dict):
    global clients
    if len(clients) - 1 >= int(client_id):
        clients[int(client_id)] = new_client
        print('CLIENT UPDATED')
    else:
        print('CLIENT ID IS NOT IN DATA')


def delete_client(client_id: str):
    global clients
    if int(client_id) >= len(clients):
        print('ID IS NOT IN DATA')
    for i, client in enumerate(clients):
        if i == int(client_id):
            print('THE CLIENT WAS DELETED')
            del clients[i]
            break


def show_clients():
    global clients
    print('↓ '* 10)
    for i, client in enumerate(clients):
        print('{0} | {1} | {2} | {3} | {4}'.format(i, client['name'], client['company'], client['email'], client['position']))
    print('↑ '* 10)
    time.sleep(1.5)


def find_client(client_name: str):
    global clients
    count = 0
    for client in clients:
        if client['name'] != client_name:
            count += 1
            if count == len(clients):
                print('THE CLIENT WAS NOT FOUND')
            else:
                continue
        else:
            print('THE CLIENT WAS FOUND')


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
    _initialize_clients_data()
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
            print('--CLIENT TO BE REPLACED--')
            client_id = _get_client_field('ID')
            print('--NEW CLIENT--')
            new_client = {
                'name': _get_client_field('NAME'),
                'company': _get_client_field('COMPANY'),
                'email' : _get_client_field('EMAIL'),
                'position' : _get_client_field('POSITION')
            }
            update_client(client_id, new_client)
            show_clients()
        elif command == 'D':
            client_id = _get_client_field('ID')
            delete_client(client_id)
            show_clients()
        elif command == 'S':
            client_name = _get_client_name()
            find_client(client_name)
        elif command == 'E':
            _save_clients()
            _exit()
            break
        else:
            print('INVALID COMMAND!')
        