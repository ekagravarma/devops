A simple Hello World app written in Python Flask.

Contains single-stage and multi-stage Dockerfiles.

Build and run using any dockerfile:

```
$ docker build -f [dockerfile] -t python-docker .
$ docker run --rm -it -p 8080:8080 python-docker
```

Uses gunicorn for production build.


Multistage Dockerfile helps in reducing the space of image and also enhances the security.
In the below image by implementation of Multistage Dockerfile, image size reduced by 900 - 1000 % 

![multi_stage_docker](https://github.com/ekagravarma/devops/assets/40314122/9a82e69d-f282-4d7e-b60f-3ee6ce78f1f1)
