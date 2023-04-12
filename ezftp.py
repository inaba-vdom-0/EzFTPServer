"""EzFTPServer"""

from tkinter import filedialog as fd
import time
import os
import pyftpdlib.authorizers as pa
import pyftpdlib.handlers as ph
import pyftpdlib.servers as ps

def serverauth():
    """Create authenticated user, specify server ip, specify directory"""
    dfdir = 'C:\\'
    dirselect = fd.askdirectory(initialdir=dfdir)
    username = input('Enter username :')
    password = input('Enter password :')
    svip = '0.0.0.0'

    # directory is "dirselect"
    dirname = dirselect
    os.makedirs(dir, exist_ok=True)

    auth = pa.DummyAuthorizer()
    auth.add_user(username, password, dirname, perm='elradfmw')

    connectionhandler(svip, auth)

def connectionhandler(svip, auth):
    """Creating a connection management handler"""
    handler = ph.FTPHandler
    handler.authorizer = auth

    startserver(svip, handler)

def startserver(svip, handler):
    """Start FTP Server"""
    try:
        server = ps.FTPServer((svip, 21), handler)
        server.serve_forever()
    except: # pylint: disable=bare-except
        print('Error. Please restart the app. 10 seconds later the app will close.')
        time.sleep(10)

def main():
    """python main"""
    serverauth()

if __name__ == '__main__':
    main()
