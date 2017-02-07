===============================
CKAN Loaddata
===============================

Installation
--------------

Installation is similar to most of other Python packages
as a global python package or within a virtual enviroment.

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
            filename: 'your-target-resource-file-Name.csv'
            name_format: '%Y-%m: {name}'
            metadata:
                package_id: 'your-package-id'
                name: 'Your target resource title'
                url: ''
                format: csv


For more information about YAML file syntax you can check online
