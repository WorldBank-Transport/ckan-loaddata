# -*- coding: utf-8 -*-

import io
import logging
from datetime import datetime
from ckanapi import RemoteCKAN
from .collection import Collection


logging.basicConfig(format='%(levelname)s: %(asctime)s: %(message)s',
                    level=logging.DEBUG)


class CKAN(object):

    def __init__(self, address, apikey=None,
                 user_agent='ckan-loaddata/0.1.0'):
        self.address = address
        self.apikey = apikey
        self.user_agent = user_agent
        self.client = RemoteCKAN(self.address, apikey=self.apikey,
                                 user_agent=self.user_agent)
        self.format_mappings = {
            'csv': {
                'loader': 'load_csv_from_url',
                'output_formater': 'to_csv_stream'},
            'excel': {
                'loader': 'load_excel_from_url',
                'output_formater': 'to_excel'},
            'html': {
                'loader': 'load_html_from_url'},
        }

    def resource_create_from_url(self, url, input_params={},
                                 output_params={}):
        """Create CKAN resource using data from URL.
        """
        input_format = input_params.pop('format', 'csv')
        output_format = output_params.pop('format', 'csv')
        rename_columns = input_params.pop('rename_columns', {})
        drop_columns = input_params.pop('drop_columns', [])
        drop_duplicates = input_params.pop('drop_duplicates', [])
        name_format = output_params.pop('name_format', '')
        data = output_params.pop('metadata', {})
        logging.info('Create resource from url: %s', url)
        if input_format.lower() in self.format_mappings.keys():
            collection = Collection()
            getattr(collection,\
                    self.format_mappings[input_format]['loader'])\
                    (url, **input_params)
            if rename_columns:
                collection.rename(url, columns=rename_columns)
            if drop_duplicates:
                collection.drop_duplicates(url, subset=drop_duplicates)
            if drop_columns:
                collection.drop(url, labels=drop_columns)
            if name_format:
                _name = name_format.format(**data)
                data['name'] = datetime.now().strftime(_name)
            resource_buffer = getattr(
                collection,
                self.format_mappings[output_format]['output_formater'])\
                (url, **output_params)
            data['upload'] = resource_buffer
            created = self.client.action.resource_create(**data)
            logging.info(str(created))
            logging.info(
                'Create resource from url:\t%s:\t%s:\t%s',
                url, self.address, data.get('package_id', ''))
            return created
