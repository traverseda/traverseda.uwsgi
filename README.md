Deploy django/php apps with ansible and uwsgi.

This role is a bit odd, in that it tries to push as much as possible onto
the user account. Most notably, the uwsgi daemon itself is run as a systemd user
service.

It's designed to run under nginx, systemd, and postgres.

It makes the uwsgi apps available at `<yoursite>/~<name>`.

```yaml
vars:
  default_nginx_site: /etc/nginx/sites-enabled/default #Needed for
  #enabling home-dir apps

roles:
  - role: traverseda.uwsgi
    name: app #This names the user account, postgres database, etc
    type: django #custom settings for a particular app type
    source: git@github.com:example/example.git
    branch: master #Defaults to master, you can leave this out.
    domain: app.example.com #This just sets facts for later
  - role: traverseda.uwsgi
  #...
```

During setup, it templates any file starting with `ansible_`. So if you wanted
to use some of these ansible variables in your config, `ansible_config.py` would
become `config.py` after templating.

The postgres user/db are both `{{name}}` and you can access the password with
`{{lookup('password', '~'+name+'/postgresPassword.txt length=32')}}`. Or just
look at the `postgresPassword.txt` file in your app's home dir.
