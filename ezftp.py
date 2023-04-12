import pyftpdlib.authorizers as pa
import pyftpdlib.handlers as ph
import pyftpdlib.servers as ps
import time
import os

# Create authenticated user, specify server ip, specify directory
def auth():
    username = input('Enter username :')
    password = input('Enter password :') 
    print('The PC port must be linked up and IP enabled.')
    svip = input('Enter Server ip :')

    # Default directory D:\FTP
    dir = ('D:\FTP')
    os.makedirs(dir, exist_ok=True)

    auth = pa.DummyAuthorizer()
    auth.add_user(username, password, 'D:\FTP', perm='elradfmw')
    
    handler(svip, auth)

# Creating a connection management handler
def handler(svip, auth):
    handler = ph.FTPHandler
    handler.authorizer = auth
    
    server(svip, handler)
    
# Start FTP Server
def server(svip, handler):
    try:
        server = ps.FTPServer((svip, 21), handler)
        server.serve_forever()
    except:
        print('Error. Please restart the app. 10 seconds later the app will close.')
        time.sleep(10)

def main():
    auth()

if __name__ == '__main__':
    main()