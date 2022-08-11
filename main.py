
clients = 'Pablo, Ricardo'

def create_client(client: str):
    global clients #global is for indicate the use of a global variable into func
    _add_comma_space()
    clients += client

def show_clients():
    global clients
    print(clients)

def _add_comma_space():#private function
    global clients
    clients += ', '

if __name__ == '__main__':
    show_clients()
    create_client('David')
    show_clients()