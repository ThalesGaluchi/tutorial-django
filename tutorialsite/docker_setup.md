# How to setup a Docker container

We are going to use the Django tutorial site to run on Docker container


https://docs.docker.com/language/python/

docker run -it --rm --name my-running-script -v "$PWD":/usr/src/myapp -w /usr/src/myapp python:3 python your-daemon-or-script.py

https://code.visualstudio.com/docs/containers/quickstart-python

