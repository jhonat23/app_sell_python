import click
from clients.services import ClientService
from clients.models import Client
from tabulate import tabulate

@click.group()
def clients():
    """Manages the clients lifecycle"""
    pass

@clients.command()
@click.option('-n', '--name', type=str, prompt=True, help='The client name')
@click.option('-c', '--company', type=str, prompt=True, help='The client company')
@click.option('-e', '--email', type=str, prompt=True, help='The client email')
@click.option('-p', '--position', type=str, prompt=True, help='The client position')
@click.pass_context
def create(ctx, name, company, email, position):
    """Create a new client"""
    client = Client(name, company, email, position)
    client_service = ClientService(ctx.obj['clients_table'])
    client_service.create_client(client)

@clients.command()
@click.pass_context
def list_clients(ctx):
    """List all clients"""
    client_service = ClientService(ctx.obj['clients_table'])
    headers = [i.capitalize() for i in Client.schema()]
    list_of_clients = client_service.list_clients()
    table = []
    for client in list_of_clients:
        table.append([client['name'], client['company'], client['email'], client['position'], client['uid']])
    tab = tabulate(table, headers)
    print(tab)

@clients.command()
@click.argument('client_uid', type=str)
@click.pass_context
def update(ctx, client_uid):
    """Updates a client"""
    client_service = ClientService(ctx.obj['clients_table'])
    clients = client_service.list_clients()
    client = [client for client in clients if client['uid'] == client_uid]

    if client:
        client = ClientService._update_client(Client(**client[0]))
        client_service.update(client)
        print('Client updated')
    else:
        print('Client not found')

@clients.command()
@click.argument('client_uid', type=str)
@click.pass_context
def delete(ctx, client_uid: str):
    """Deletes a client"""
    client_service = ClientService(ctx.obj['clients_table'])
    if click.confirm('Are you sure you want to delete the client with uid: {}'.format(client_uid)):
        client_service.delete(client_uid)

all = clients
