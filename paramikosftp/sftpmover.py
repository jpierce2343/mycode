#!/usr/bin/env python3
"""Alta3 Research | RZFeeser@alta3.com
   Moving files with SFTP"""

# import paramiko so we can talk SSH
# python3 -m pip install paramiko
import paramiko

# standard library
import os
import getpass

def transfer_to_this_remote_dir():
    """ask user for full path of directory to be created"""
    while True:
        what_dir = input("What directory on the remote host would you like to transfer files to (default: /tmp/)? ")
        if what_dir == "":
            what_dir = "/tmp/"
            break
        elif what_dir[0] == "/" and what_dir[-1] == "/":
            break
        print("You must enter a full path for the remote host. Full paths must begin and end with '/'.")
    return what_dir

def movethemfiles(sftp):
    """a simple function that moves files across an SFTP paramiko channel"""
    what_dir = transfer_to_this_remote_dir()

    for x in os.listdir("/home/student/filestocopy/"):
        if not os.path.isdir("/home/student/filestocopy/"+x):
            sftp.put("/home/student/filestocopy/"+x, what_dir+x)
    return

def main():
    """runtime"""

    # "Where to connect to" - An SSH Transport attaches to a stream (usually a socket), negotiates an encrypted session, authenticates,
    # and then creates stream tunnels, called channels, across the session. 
    t = paramiko.Transport("10.10.2.3", 22) # IP and port

    # "How to connect (see other labs on using id_rsa private/public keypairs)" - Negotiate an SSH2 session, and optionally verify the server’s host key
    # and authenticate using a password or private key. This is a shortcut for start_client, get_remote_server_key, and Transport.auth_password
    # or Transport.auth_publickey. Use those methods if you want more control.
    #
    # You can use this method immediately after creating a Transport to negotiate encryption with a server. If it fails, an exception will be thrown.
    # On success, the method will return cleanly, and an encrypted session exists. 
    t.connect(username="bender", password="alta3")

    ## "Make an sftp connection object" - Setting the window and packet sizes might affect the transfer speed. The default settings in the
    # Transport class are the same as in OpenSSH and should work adequately for both files transfers and interactive sessions.
    sftp = paramiko.SFTPClient.from_transport(t)

    ## iterate across the files within directory
    for x in os.listdir("/home/student/filestocopy/"): # iterate on directory contents
      if not os.path.isdir("/home/student/filestocopy/"+x): # filter everything that is NOT a directory
        sftp.put("/home/student/filestocopy/"+x, "/tmp/"+x) # sftp.put("from_path_local", "to_path_remote") - move file to target location

    ## close the connections
    sftp.close() # close the connection
    t.close()

if __name__ == "__main__":
    main()

