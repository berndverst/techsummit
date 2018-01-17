# Microsoft Tech Summit: Azure on Docker
### Opening the lid on containers

## Examples

### Simple Docker Container
The most basic Docker container image including a simple application binary (in this case compiled from Go) printing the message 'Hello World'.

Source code: [docker-hello-world](./docker-hello-world/)

```bash
.
├── Dockerfile
├── hello-world     # binary compiled for Linux from hello-world.go
└── hello-world.go  # Simple Go application printing 'hello world' to stdout
```

How to build and run:

```bash
docker build docker build -t hello-world docker-hello-world/`
docker run -it hello-world
```

### Python Web Application

This is a simple container image for a basic Python web application based on the minimal and highly performant [Falcon Framework](falconframework.org) for web applications.

This image has already been published to Docker Hub at [`berndverst/techsummit`](https://hub.docker.com/r/berndverst/helloworld)

What is noteworthy here is that we rely on an existing container image ([`berndverst/falcon`](https://hub.docker.com/r/berndverst/falcon)) from Docker hub. This image is already designed for the type of application we want to run and we therefore need not create the necessary runtime environment ourselves.

Source code: [docker-sample-app](./docker-sample-app/)

```
.
├── Dockerfile
└── app
    └── main.py  # Simple Python Falcon Framework web application
```

How to run:
`docker run -it -p8080:80 berndverst/techsummit`

How to build:
`docker build -t techsummit docker-samplea-app/`
