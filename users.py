#!/usr/local/bin/python3

import argparse
import paramiko
import os

def view_user(args):
    print("Getting user information for", args.view, "\n")
    
    ssh_target = os.environ['SSH_TARGET']
    client = paramiko.client.SSHClient()
    client.load_system_host_keys()
    client.connect(ssh_target)

    command = "getent passwd %s" % args.view
    stdin, stdout, stderr = client.exec_command(command)
    user_details = stdout.readlines()
    
    if user_details:
        print(user_details[0])

        print("Authorized Keys:\n")
        my_keys_command = "cat ~/.ssh/authorized_keys"
        stdin, stdout, stderr = client.exec_command(my_keys_command)
        my_keys = stdout.readlines()
        print(my_keys)

    if not user_details:
        print(args.view, "not found on", ssh_target)

def upload_key(key_file):

    ssh_target = os.environ['SSH_TARGET']
    client = paramiko.client.SSHClient()
    client.load_system_host_keys()
    client.connect(ssh_target)

    ftp_client=client.open_sftp()
    ftp_client.put(key_file, "/tmp/authorized_keys")
    ftp_client.close()

def create_user(args):
    username = args.create
    local_file_path = args.key_file
    print("Creating user", username)
    print("Key file: %s" % local_file_path)
    
    ssh_target = os.environ['SSH_TARGET']
    client = paramiko.client.SSHClient()
    client.load_system_host_keys()
    client.connect(ssh_target)

    # Create user including home and .ssh dir
    command = """sudo useradd -s /bin/bash -d /home/%s -m %s; 
                 sudo mkdir /home/%s/.ssh; """ % (username, username, username) 

    stdin, stdout, stderr = client.exec_command(command)
    output = stdout.readlines()

    upload_key(local_file_path)

    command2 = """sudo mv /tmp/authorized_keys /home/%s/.ssh/; sudo chown -R %s:%s /home/%s/.ssh""" % (username, username, username, username) 
    stdin2, stdout2, stderr2 = client.exec_command(command2)
    output = stdout2.readlines()

def confirm_delete(username):
    if username == 'bhenerey':
        print("%s can not be deleted." % username)
        exit()
    else:
        double_check = input("Please type %s to confirm account deletion:  " % username)
        if double_check == username:
            # TODO: Might want to protect accounts where UID < 1000
            print("Deleting %s .." % username)
            return
        else:
            print("Confirmation of deletion failed")
            exit()


def delete_user(args):
    
    username = args.delete 
    print("Deleting user", username, "\n")
    
    confirm_delete(args.delete)

    ssh_target = os.environ['SSH_TARGET']
    client = paramiko.client.SSHClient()
    client.load_system_host_keys()
    client.connect(ssh_target)

    # Delete user
    command = "sudo userdel -rf %s" % username
    stdin, stdout, stderr = client.exec_command(command)
    output = stdout.readlines()


def main():

    # create the top-level parser
    parser = argparse.ArgumentParser(prog='users.py')
    subparsers = parser.add_subparsers(help='users.py [view|create] <USERNAME> <KEY_FILE>')

    # create the parser for the "view" command
    parser_a = subparsers.add_parser('view', help='users.py view <USERNAME>')
    parser_a.add_argument('view', type=str, help='users.py view <USERNAME>')
    parser_a.set_defaults(func=view_user)

    # create the parser for the "create" command
    parser_b = subparsers.add_parser('create', help='users.py create <USERNAME> <KEY_FILE>')
    parser_b.add_argument('create', type=str, help='users.py create <USERNAME> <KEY_FILE>')
    parser_b.add_argument('key_file', type=str, help='users.py create <USERNAME> <KEY_FILE>')
    parser_b.set_defaults(func=create_user)

    # create the parser for the "delete" command
    parser_c = subparsers.add_parser('delete', help='users.py delete <USERNAME>')
    parser_c.add_argument('delete', type=str, help='users.py delete <USERNAME>')
    parser_c.set_defaults(func=delete_user)

    args = parser.parse_args()
    args.func(args)



if __name__ == "__main__":
    main()

    # TODO: needs plenty of error handling
    # TODO: I'm aware the functions aren't very DRY and the ssh connection could be moved to it's own function. 
