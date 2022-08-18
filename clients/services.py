import csv
import os
from clients.models import Client
import click

class ClientService():
    def __init__(self, table_name: str):
        self.table_name = table_name

    def create_client(self, client: Client):
        with open(self.table_name, mode='a') as f:
            writer = csv.DictWriter(f, fieldnames=Client.schema())
            writer.writerow(client.to_dict())
        
    def list_clients(self):
        with open(self.table_name, mode='r') as f:
            reader = csv.DictReader(f, fieldnames=Client.schema())
            return list(reader)

    def update(self, update_client: Client):
        list_of_clients = self.list_clients()
        updated_client = []
        for client in list_of_clients:
            if client['uid'] == update_client.uid:
                updated_client.append(update_client.to_dict())
            else:
                updated_client.append(client)
            
            self._save_to_disc(updated_client)

    def _save_to_disc(self, clients):
        tmp_table = self.table_name + '.tmp'
        with open(tmp_table, mode='w') as f:
            writer = csv.DictWriter(f,fieldnames=Client.schema())
            writer.writerows(clients)
        
            os.remove(self.table_name)
            os.rename(tmp_table, self.table_name)
    
    @staticmethod
    def _update_client(client: Client):
        print('Leave empty if you do not want to modify the value')

        client.name = click.prompt('New name', type=str, default=client.name)
        client.company = click.prompt('New company', type=str, default=client.company)
        client.email = click.prompt('New email', type=str, default=client.email)
        client.position = click.prompt('New position', type=str, default=client.position)

        return client