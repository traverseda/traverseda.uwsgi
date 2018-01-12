# traverseda.uwsgi

[![CLA assistant](https://cla-assistant.io/readme/badge/traverseda/traverseda.uwsgi)](https://cla-assistant.io/traverseda/traverseda.uwsgi) 

Deploy django/php apps with ansible and uwsgi.

This role is a bit odd, in that it tries to push as much as possible onto
the user account. Most notably, the uwsgi daemon itself is run as a systemd user
service.

It's designed to run under nginx, systemd, and postgres.

It makes the uwsgi apps available at `<yoursite>/~<name>`, without needing to
use a subdomain!

## Quickstart

```yaml
---
#~/server.yml
- hosts: any
  vars:
    default_nginx_site: /etc/nginx/sites-enabled/default
  pre_tasks:
  - name: Install required packages
    become: True
    apt:
      name: "{{item}}"
      state: present
      update_cache: yes
    with_items: ["nginx","python3","virtualenv","uwsgi","uwsgi-plugin-python3",]

  roles:
    - role: traverseda.uwsgi
      become: True
      name: example-app
      source: git@github.com/example/example.git
      type: django
      django_settings: Settings/settings.py
      wsgi_file: Settings/wsgi.py
      wsgi_module: Settings.wsgi:application
      allowed_hosts: ['localhost', 'ec2-XX-XX-XXX-XX.compute-1.amazonaws.com']
      debug: True
```

You could then deploy using something like

`sudo ansible-playbook -i "localhost," -c local server.yml`
