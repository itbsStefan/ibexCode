FROM jupyterhub/jupyterhub:latest

RUN pip install --no-cache \
    oauthenticator \
    dockerspawner \
    jupyterhub-nativeauthenticator

WORKDIR /home/jovyan/work 

# Kopiere einzelne Dateien
# adds files from your Docker clients current directory.
COPY README.md ./README.md 
#COPY jupyterhub_config.py /srv/hub/jupyterhub_confing.py # per volume im compose
RUN mkdir -p /home/jovyan/work/readonly
RUN mkdir -p /home/jovyan/builfiles/ibexCode

# Kopie Ordner zum Serverimage
# eins von beiden Quellen aus dem online Repository oder lokal vom Entwicklungsrechner
RUN cd /home/jovyan/builfiles/ibexCode
ADD gitOnline .
# alternativ copy the source-scripts to a folder
#RUN git clone https://github.com/itbsStefan/ibexCode.git # (dafür muss git im Image installiert sein)
RUN cd ~

#optional on build pc call
# pip install jupyterhub
# jupyterhub --generate-config #if you need it
# pip install dockerspawner jupyterhub-nativeauthenticator
## docker build . ## um imageteile local zu laden

# COPY jupyterhub_config.py /srv/jupyterhub/jupyterhub_config.py #ist in compose volumes

#    FROM creates a layer from the ubuntu:22.04 Docker image.
#    COPY adds files from your Docker client's current directory.
#    RUN builds your application with make.
#    CMD specifies what command to run within the container.
