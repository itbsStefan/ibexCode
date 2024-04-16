## Beschereibung

diese README.md Datei sollte im DockerHub Image per 

''git clone https://github.com/itbsStefan/ibexCode.git  /srv/hubdateien/gitOnline''

benutzt werden. TODO Dateien in jupyterdocker Ordner müssen angepasst werden!

cd gitOnline
cd jupyterdocker
(base) @ibex:$ cp docker-compose.yml ../..
(base) @ibex:$ cp Dockerfile ../..
(base) @ibex:$ cp jupyterhub_config.py ../..

Kommentare aus der jupyterhub_config.py einmal vor dem Docker build ausführen

pip install dockerspawner jupyterhub-nativeauthenticator oauthenticator
docker pull jupyter/datascience-notebook:latest
docker compose up -d


# JupyterHub mit DockerSpawner

Dieses Projekt enthält eine Beispielkonfiguration für einen JupyterHub-Server, der in Docker ausgeführt wird. Der JupyterHub ermöglicht es dir, Jupyter-Notebooks zu starten und gemeinsam mit anderen Nutzern zu bearbeiten.

## Dateien

- `docker-compose.yml`: Docker Compose-Datei, die den JupyterHub-Server startet
- `Dockerfile`: Dockerfile, das das Image für den Jupyter Notebook Server definiert
- `jupyterhub_config.py`: Konfigurationsdatei für den JupyterHub-Server

## Verwendung

1. Stelle sicher, dass Docker installiert ist
2. Lade das Repository herunter oder klonen es von Github
3. Navigiere in das Projektverzeichnis
4. Führe `docker-compose up -d` aus, um den JupyterHub-Server zu starten
5. Öffne `http://localhost:8000` in deinem Browser und melde dich an

## Hinweise

- Die Jupyter-Notebooks werden standardmäßig im Verzeichnis `/home/jovyan/work` im Container gespeichert.
- Die Nutzer-Notebooks werden in separaten Docker-Volumes gespeichert, die nach dem Schema `jupyterhub-user-{username}` benannt sind. 
- In der Datei `jupyterhub_config.py` können weitere Konfigurationen vorgenommen werden, z.B. das Hinzufügen von Nutzern oder das Ändern des Anmeldebildschirms.
- Weitere Informationen findest du in der [JupyterHub-Dokumentation](https://jupyterhub.readthedocs.io/en/stable/index.html).

Viel Spaß :-)

http://wiki.itbs.selfhost.co/doku.php?id=ibex:kursinhalte:kursteil2:start

http://wiki.itbs.selfhost.co/doku.php?id=playground:about:coworking:jupyterhub



