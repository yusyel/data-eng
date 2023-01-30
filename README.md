# Data Engineering Zoomcamp Notes


## 1. Introducing Docker

Docker is type of virtualization separates host from guest. Virtualizations delivery packages and called container. Containers are isolated from host.

### 1.1 Why should we care about docker

* Local experiments
* Integration tests (CI/CD)
* Reproducibility
* Running pipelines on the cloud (AWS Batch, Kubernetes Jobs)
* Spark
* Serverless (AWS Lambda, Google functions, Azure functions)


### 1.2 Installing Docker

Docker is already in most popular linux distributions. Installing docker on Debian based distros:

```bash
sudo apt install docker.io
```

### 1.2.1 Running docker without sudo

Create the docker group.
```bash
sudo groupadd docker
```
Add your user to the docker group.

```bash
sudo usermod -aG docker $USER
```

Log out and log back in so that your group membership is re-evaluated.

For testing

```bash
docker run hello-world
```

Output should starting with this:

```bash
Hello from Docker!
This message shows that your installation appears to be working correctly.
```

### 1.2.2 Docker Commands

* Docker Run: Run a command in a new container

```bash
docker run hello-world
```

* Interactive Mod: Interactive mods mean after running docker images, docker allow us for use terminal.

```bash
docker run -it ubuntu bash
```
We want to use ubuntu image with interactive mod and using bash.

```bash
docker run -it python:3.9 bash
```

Starting python image with bash mod

```bash
docker run -it python:3.9 python
```

Starting python image with python mod.

### 1.2.3 Building Docker Image


