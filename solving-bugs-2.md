#MAJOR BUGS (That to took me a while to solve)

####FLASK API TEMPLATE
```no module named shared libs``` while running alembic: **virtualenv for web app must have not been started.**

```rfc code url error``` while running alembic: **Its either the url at local_config.ini is wrong or theres not local_config.ini to begin with.**

While running endpoints ```sqlalchemy.orm.exc.DetachedInstanceError: Instance <LinkedInAccount at 0x7fa6e6f4ded0> is not bound to a Session; attribute refresh operation cannot proceed```: **include expire_on_commit=False on the backend functions.**

```no module named <any>```: **Normally this is caused when the virtualenv for the project was not activated. The command `python setup.py develop` initialized PYTHONPATH within the virtualenv and not on your local.**
