===============================
CKAN Loaddata
===============================

A utility for loading data into CKAN from remote sources based on
Python `Pandas <http://pandas.pydata.org/>`_ and `ckanapi <https://github.com/ckan/ckanapi>`_.

Installation
--------------

Installation is similar to most of other Python packages
as a global python package or within a virtual enviroment.


    NOTE: Using a **Python virtual environment** is not mandatory but it **is highly recommended**.

Using pip

::

    pip install git+https://github.com/WorldBank-Transport/ckan-loaddata


Or by downloading or clonnning the source code then directly using setup.py

::

    git clone https://github.com/WorldBank-Transport/ckan-loaddata.git
    cd ckan-loaddata
    python setup.py install


Or for development installation

::

    git clone https://github.com/WorldBank-Transport/ckan-loaddata.git
    cd ckan-loaddata
    python setup.py develop


Usage
-------

::

   ckan_loaddata <path-to-your-yaml-task-file>


In order to automate periodic publishing of new dataset resources using
the ``ckan_loaddata`` command a `CRON <https://en.wikipedia.org/wiki/Cron>`_ job can be used.

Your yaml task file can be in this format

::

    ---
    
    address: <your-ckan-host>
    apikey: <your-api-key>

    resources:
        - url: '<your-data-source-url>'
          input:
            format: '<input-file-format>'
            # other input parameters
          output:
            format: <output-file-format>
            # other output parameters
            metadata:
                package_id: 'your-ckan-package-id'
                # resource-metadata


For example:

::

    ---
    
    address: http:ckan.example.com
    apikey: 'your-api-key'
    
    resources:
        - url: 'http://remote.example.com/remote-data-source-file-url.xls'
          input:
            format: excel
          output:
            format: csv
            filename: '%Y-%m-your-target-resource-file-name.csv'
            metadata:
                package_id: 'your-package-id'
                name: '%Y-%m: Your target resource title'
                url: ''
                format: csv


For more information about YAML file syntax you can check online


Task parameters
________________


:address:
    A root URL of the target CKAN instance.

:apikey:
    A CKAN API key.

    **default**: ``None``

:user_agent:
    The User Agent string.

    **default**: ``'ckan-loaddata/0.1.0'``

:resources:
    a collection/list of resources that to be loaded.

    **default**: ``[]``


Each resource item in the resources collection may contain the following
arguments


:url:
    A full URL of the resource file to be loaded.

:input:
    Arguments to be use in processing the input resource file

    :format: file format: csv, excel, json or html
    
    :rename_columns:
        a dictionary of ``original_name: new_name`` for fields to be renamed

        **default**: `{}`

    :drop_columns:
        A list of field labels to be removed from resource file
        
        **default**: `[]`

    :drop_duplicates:
        A list of field labels to used in identifying duplicate entries
        which are going to be droped.

        **default**: `[]`
    :other parameters:
        other parameters which are going to be passed to the
        *Pandas IO reader functions* for the respective file format
        http://pandas.pydata.org/pandas-docs/stable/io.html

:output:
    Arguments to be use in uploading the resource to CKAN

    :format: file format: csv or excel.

    :name:
            How the dataset resource file should be titled.
           
            This can also include placeholder for date/time in Python
            `stftime` format:
            https://docs.python.org/2/library/datetime.html#strftime-and-strptime-behavior

    :filename:
            How the target resource file should be named.
            
            This can also include placeholder for date/time in Python
            `stftime` format:
            https://docs.python.org/2/library/datetime.html#strftime-and-strptime-behavior

    :metadata:
        Resource metadata to be posted to CKAN including the
        target ``package_id``.

        For more information about acceptable fields can be found in
        CKAN resource creating API documentation
        http://docs.ckan.org/en/latest/api/index.html#ckan.logic.action.create.resource_create
