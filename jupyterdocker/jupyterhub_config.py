# cd jupyterdocker/
# pip install dockerspawner jupyterhub-nativeauthenticator oauthenticator
from dockerspawner import DockerSpawner
from nativeauthenticator import NativeAuthenticator
import os

c.JupyterHub.authenticator_class = NativeAuthenticator
c.JupyterHub.log_level = 'DEBUG'
c.JupyterHub.hub_ip = '0.0.0.0'
c.JupyterHub.spawner_class = DockerSpawner
# Persistence
c.JupyterHub.db_url = "sqlite:///data/jupyterhub.sqlite"

c.DockerSpawner.network_name = 'jupyterhub'
c.DockerSpawner.remove = True

notebook_dir = os.environ.get('DOCKER_NOTEBOOK_DIR') or '/home/jovyan/work'
c.DockerSpawner.notebook_dir = notebook_dir
c.DockerSpawner.volumes = { 'jupyterhub-user-{username}': notebook_dir }
c.DockerSpawner.image = "jupyter/datascience-notebook:latest"

#c.DockerSpawner.image = "jupyter/datascience-notebook:latest"
## docker pull jupyter/datascience-notebook:latest ## ist groß einmal vorher ausführen

c.Spawner.http_timeout = 300

c.GenericOAuthenticator.enable_auth_state = True
# Enable user registration
c.Authenticator.allowed_users = set()
c.NativeAuthenticator.create_system_users = True ## dem Host bekannte Benutzer

c.Authenticator.admin_users = {'stefan'}
c.NativeAuthenticator.open_signup = True

