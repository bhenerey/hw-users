# hw-users

## Requirements / Background

Create a command line application that when provided with user information and a public ssh key would create the user on a specified host.

Assume that the user running the program has the rights to manage users on that host.

Create a command line application that can list users on a host, reporting their username, userid, and comment fields.

Create a command line application that can remove a user from a host.

### Step 1 - Build a set of programs in python to manage the users on a Linux system

1. create user
   - include setting their ssh key
2. view user
3. delete user

### Step 2 - Select any configuration management tool that you're comfortable with and do the same as

### Step 3 - Discuss the differences between the two solutions including Pros/Cons

## Examples

### Help

```
➜  hw-users git:(master) ✗ python3 users.py -h
usage: users.py [-h] {view,create,delete} ...

positional arguments:
  {view,create,delete}  users.py [view|create] <USERNAME> <KEY_FILE>
    view                users.py view <USERNAME>
    create              users.py create <USERNAME> <KEY_FILE>
    delete              users.py delete <USERNAME>

optional arguments:
  -h, --help            show this help message and exit
```

### Create User

```
➜  hw-users git:(master) ✗ python3 users.py create bhenerey4 id_rsa.pub
Creating user bhenerey4
Key file: id_rsa.pub
```

### View User

```
➜  hw-users git:(master) ✗ python3 users.py view bhenerey4
Getting user information for bhenerey4

bhenerey4:x:1001:1002::/home/bhenerey4:/bin/bash

Authorized Keys:

['ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDVnj3vmbhwjzRIeYCl7VeEkGIz+zZKcm42UPCdAzZALzBFCXKMef72ONKclSN5LWEJ//ZvRqcDtQEA5oEr4ahg/jdVboBcavuY3Mt7OGepACnnNV+puOCv55EFcx/qBQ5JeAYnX0WLuVR4yAQRk6AcQA5l2cZ42I01fMx6UR+zGkMUIyAdGJ9PVCtNYIOqXJcPpLJ2FQ98VaYgYRB5bbWh37SUkEAdRgsH0qOUzoKNpI61wtRhxyYFjflzH6z1oX0iOB/1wnGio5aZuZNuXB7WhQmAo8+6MyO+tSc8PxVvpOk8CGn0ewgh+bX/7VrAgw7FquxrnhQNNHcAbLrmVWxH bhenerey@bch-asus-linux\n']
```

### Delete User

```
➜  hw-users git:(master) ✗ python3 users.py delete bhenerey4
Deleting user bhenerey4

Please type bhenerey4 to confirm account deletion:  bhenerey4
Deleting bhenerey4 ..
```
