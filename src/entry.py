import click
from monitor import pymonitor
from slaver import slaver_client
@click.group()
def cli():
	print 
"""

.______          ___       ______ .______    __   _______   _______ .______      
|   _  \        /   \     /      ||   _  \  |  | |       \ |   ____||   _  \     
|  |_)  |      /  ^  \   |  ,----'|  |_)  | |  | |  .--.  ||  |__   |  |_)  |    
|      /      /  /_\  \  |  |     |   ___/  |  | |  |  |  ||   __|  |      /     
|  |\  \----./  _____  \ |  `----.|  |      |  | |  '--'  ||  |____ |  |\  \----.
| _| `._____/__/     \__\ \______|| _|      |__| |_______/ |_______|| _| `._____|
                              														

"""

@click.command()
def server():
	print 
"""

.______          ___       ______ .______    __   _______   _______ .______      
|   _  \        /   \     /      ||   _  \  |  | |       \ |   ____||   _  \     
|  |_)  |      /  ^  \   |  ,----'|  |_)  | |  | |  .--.  ||  |__   |  |_)  |    
|      /      /  /_\  \  |  |     |   ___/  |  | |  |  |  ||   __|  |      /     
|  |\  \----./  _____  \ |  `----.|  |      |  | |  '--'  ||  |____ |  |\  \----.
| _| `._____/__/     \__\ \______|| _|      |__| |_______/ |_______|| _| `._____|
                              														

"""
	pymonitor()

@click.command()
def client():
	slaver_client()


@click.command()
def init():
	print "init a racpider project"	

cli.add_command(server)
cli.add_command(client)	
