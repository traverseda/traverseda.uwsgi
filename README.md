Deploy django/php apps with ansible and uwsgi.

```yaml
roles:
  - traverseda.uwsgi:
    name: app #This names the user account, postgres database, etc
    type: django #custom settings for a particular app
```
