# -*- coding: utf-8 -*-

import click
import yaml
from ckan_loaddata.ckan import CKAN

@click.group()
def cli():
    pass

@click.command()
@click.argument('task', type=click.File('rb'))
def loaddata(task):
    """Upload data to a CKAN instance."""
    click.echo('Upload data to CKAN')
    conf = yaml.load(task)
    ckan = CKAN(address=conf.get('address'),
                apikey=conf.get('apikey'),
                user_agent=conf.get('user_agent'))
    for resource in conf.get('resources', []):
        ckan.resource_create_from_url(
            resource.get('url'),
            input_params=resource.get('input', {}),
            output_params=resource.get('output', {}))


cli.add_command(loaddata)


if __name__ == "__main__":
    cli()
