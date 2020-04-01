Prerequisites
====

```
pip3 install ansible
ansible-galaxy install grog.user
ansible-galaxy install grog.authorized-key
```

You will also need to copy your ssh public key to the hw-users directory, or update the path in servers.yml

Running the playboards create, remove, and view users
====

```
ansible-playbook -i hosts manage-user.yml view-users.yml
```

