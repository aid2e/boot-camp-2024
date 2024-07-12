# Prerequisities


## Recommendations

* VSCode does a good job with `ssh` and opening remote servers. Hence, working with VSCode is highly recommended. Mainly to visualize `root` files one can simply download them from VS Code.
* Secondly, the software required to use the containers `singularity` works best for linux systems. So if in windows, having WSL2 is highly recommended and is assumed in here. Instructions on how to install WSL2 in windows is shown [here](https://learn.microsoft.com/en-us/windows/wsl/install). If in macOS having a Virtual machines and have singularity installed. The instructions on how to install singularity in macOS is shown [here](https://docs.sylabs.io/guides/3.5/admin-guide/installation.html#mac).
* You can start either by using the HPC account at W&M or have a local installation. The HPC account is recommended.

### Project Directory

The entire tutorial section is going to have the project directory defined in the variable `$EIC_PROJECT_DIR` 

````{tab} bash
```bash
export EIC_PROJECT_DIR="/path/to/ProjectDir"
```
````
````{tab} tcsh
```tcsh
setenv EIC_PROJECT_DIR "/path/to/ProjectDir"
```
````



## Installing Singularity (locally assuming linux)

### Update your installed packages

````{tab} Ubuntu or Debian
```bash
sudo apt-get update && sudo apt-get install -y \
    build-essential \
    uuid-dev \
    libgpgme-dev \
    squashfs-tools \
    libseccomp-dev \
    wget \
    pkg-config \
    git \
    cryptsetup-bin
```
````
````{tab} CentOS or RedHat Enterprise
```bash
sudo yum update -y && \
     sudo yum groupinstall -y 'Development Tools' && \
     sudo yum install -y \
     openssl-devel \
     libuuid-devel \
     libseccomp-devel \
     wget \
     squashfs-tools \
     cryptsetup
```
````

### Install `go`

* download compiled version of `go`
```bash
export VERSION=1.13.5 OS=linux ARCH=amd64 && \
    wget https://dl.google.com/go/go$VERSION.$OS-$ARCH.tar.gz && \
    sudo tar -C /usr/local -xzvf go$VERSION.$OS-$ARCH.tar.gz && \
    rm go$VERSION.$OS-$ARCH.tar.gz
```
*
```bash
echo 'export GOPATH=${HOME}/go' >> ~/.bashrc && \
echo 'export PATH=/usr/local/go/bin:${PATH}:${GOPATH}/bin' >> ~/.bashrc && \
source ~/.bashrc
```
### Install `singularity`

* download `singularity`
```bash
export VERSION=3.5.3 && # adjust this as necessary \
    wget https://github.com/sylabs/singularity/releases/download/v${VERSION}/singularity-${VERSION}.tar.gz && \
    tar -xzf singularity-${VERSION}.tar.gz && \
    cd singularity
```

* Check out a version of `singularity`
```bash
 git clone https://github.com/sylabs/singularity.git && \
    cd singularity && \
    git checkout v3.5.3
```

* compile `singularity`. if needed can give `--prefix=/path/to/install` for install in custom directory else, it will get installed in `/usr/local/`
```bash
./mconfig && \
    make -C ./builddir && \
    sudo make -C ./builddir install
```

* check your installation as `singularity --version`

