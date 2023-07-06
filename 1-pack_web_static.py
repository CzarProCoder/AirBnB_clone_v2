#!/usr/bin/python3
'''
Fabric script that generates a .tgz archive from the contents
    of the web_static folder
'''
from fabric.api import local
from datetime import datetime


def do_pack():
    '''
    Function to compress files within the directory

    Return:
        Path to archive upon success
        else fail
    '''
    now = datetime.now()
    now = now.strftime('%Y%m%d%H%M%S')
    archive_path = 'versions/web_static_' + now + '.tgz'

    local('mkdir -p versions/')
    result = local('tar -cvzf {} web_static/'.format(archive_path))

    # Check if archiving was successful
    if result.succeeded:
        return archive_path
    return None
