A simple Hello World app written in Python Flask.

Contains sinagle-stage and multi-stage Dockerfiles.

Build and run using any dockerfile:

```
$ docker build -f [dockerfile] -t python-docker .
$ docker run --rm -it -p 8080:8080 python-docker
```

Uses gunicorn for production build.
