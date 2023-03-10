c.JupyterHub.port = 80

from jupyterhub.auth import DummyAuthenticator
c.JupyterHub.authenticator_class = DummyAuthenticator
c.DummyAuthenticator.admin_users = {'admin'}
c.DummyAuthenticator.allowed_users = {'user'}
c.DummyAuthenticator.password = 'admin'

from jupyterhub.spawner import SimpleLocalProcessSpawner
c.JupyterHub.spawner_class = SimpleLocalProcessSpawner

notebook_dir = '/home'
c.SimpleLocalProcessSpawner.notebook_dir = notebook_dir
