#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents
of the web_static folder of your AirBnB Clone repo,
using the function do_pacik
"""

from fabric.api import *
from datetime import datetime


def do_pack():
    """
    create an archive on web server
    """

    time = datetime.utcnow()
    arch = 'web_static_{}.tgz'.format(time.strftime("%Y%m%d%H%M%S"))
    local('mkdir -p versions')
    result = local('tar -cvzf versions/{} web_static'.format(arch),
                   capture=True)

    if result.succeeded:
        return arch
    else:
        return None
