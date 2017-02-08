# -*- coding: utf-8 -*-

import io
import tempfile
from datetime import datetime
import requests
import pandas as pd


class Collection(object):

    def __init__(self):
        self.data_frames = {}

    def load_csv(self, in_file, key=None, **kwargs):
        """Read CSV file from path and add it to Collection data_frames.
        """
        if not key:
            key = in_file
        self.data_frames[key] = pd.read_csv(in_file, **kwargs)

    def load_excel(self, in_file, key=None, **kwargs):
        """Read excel file from path and add it to Collection
        data_frames.
        """
        if not key:
            key = in_file
        self.data_frames[key] = pd.read_excel(in_file, **kwargs)

    def load_json(self, in_file, key=None, **kwargs):
        """Read json file from path or buffer and add it to Collection
        data_frames.
        """
        if not key:
            key = in_file
        self.data_frames[key] = pd.read_json(in_file, **kwargs)

    def load_html(self, in_file, key=None, **kwargs):
        """Read HTML file from path and add it to Collection
        data_frames.
        """
        if not key:
            key = in_file
        self.data_frames[key] = pd.read_html(in_file, **kwargs)[0]

    def load_csv_from_url(self, url, key=None, **kwargs):
        """Read CSV file from URL and add it to Collection data_frames.
        """
        if not key:
            key = url
        s = requests.get(url).text
        self.load_csv(io.StringIO(s), key, **kwargs)

    def load_excel_from_url(self, url, key=None, **kwargs):
        """Read excel file from URL and add it to Collection
        data_frames.
        """
        if not key:
            key = url
        s = requests.get(url).text
        self.load_excel(io.StringIO(s), key, **kwargs)

    def load_html_from_url(self, url, key=None, **kwargs):
        """Read HTML file from URL and add it to Collection
        data_frames.
        """
        if not key:
            key = url
        s = requests.get(url).text
        self.load_html(io.StringIO(s), key, **kwargs)

    def rename(self, data_frame, columns=None, inplace=True, **kwargs):
        """Rename columns in a specified data frame."""
        return self.data_frames[data_frame].rename(
            columns=columns,  inplace=inplace, **kwargs)

    def drop(self, data_frame, labels=None, inplace=True, axis=1,
             **kwargs):
        """Delete columns with given labels in a specified data frame.
        """
        return self.data_frames[data_frame].drop(
            labels=labels, inplace=inplace, axis=axis, **kwargs)

    def drop_duplicates(self, data_frame, subset, inplace=True,
                        **kwargs):
        """Drop duplicate rows based on columns in a dataframe."""
        self.data_frames[data_frame].drop_duplicates(
            subset, inplace=inplace, **kwargs)

    def to_csv_stream(self, data_frame, index=False, **kwargs):
        """Convert data frame to CSV file object."""
        if not kwargs.get('encoding'):
            kwargs['encoding'] = 'UTF-8'
        outfile = tempfile.SpooledTemporaryFile()
        outfile.name = datetime.now()\
            .strftime(kwargs.pop('filename', '')) or data_frame + '.csv'
        outfile.write(
            self.data_frames[data_frame].to_csv(index=index, **kwargs))
        outfile.seek(0)
        return outfile

    def to_excel(self, data_frame, excel_writer, index=False, **kwargs):
        """Convert data frame to excel file."""
        return self.data_frames[data_frame].to_excel(
            excel_writer, index=index, **kwargs)
