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
@click.pass_context
def update(ctx, client_uid):
    """Updates a client"""
    pass

@clients.command()
@click.pass_context
def delete(ctx, client_uid):
    """Deletes a client"""
    pass

all = clients
