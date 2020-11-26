import socket
import threading
import getopt
import subprocess
import sys

listen        = False
command       = False
upload        = False
execute       = ""
target        = ""
upload_dest   = ""
port          = 0

def start_client(buffer):

    cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

   #try:
    cli.connect((target,port))
    cli.send(buffer)
    #except:
    #    print('* Error while connecting, exiting\n')
    #    sys.exit(1)
    
def start_server():
    global target

    cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    cli.bind((target,port))
    cli.listen()

    while True:

        host, addr = cli.accept()
        print(f'Connection established with {addr}!\n')

def gather():
    global listen
    global command
    global execute
    global target
    global upload_dest
    global port

    if not(len(sys.argv[1:])):
        print('* ERROR\n')
        sys.exit(1)
    
    try:
        opts, arg = getopt.getopt(sys.argv[1:],"hle:t:p:cu:",["help","listen","execute","target","port","command","upload"])
    except getopt.GetoptError as err:
        print(err)
        sys.exit(1)
    
    for a,b in opts:
        
        if a in ['-l','--listen']:
            listen = True
        elif a in ['-e','--execute']:
            execute = b
        elif a in ['-c','--commandshell']:
            command = True
        elif a in ['-u','--upload']:
            upload_dest = b
        elif a in ['-t','--target']:
            target = b
        elif a in ['-p','--port']:
            port = int(b)
        # no need for else
        
        if not listen and len(target) and port > 0:
            
            for line in sys.stdin:
                start_client(line)
        if listen:

            start_server()

gather()
