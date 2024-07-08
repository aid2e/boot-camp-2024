# SSH into a Front-End Node Using Proxy Jump

When working with HPC systems, you often need to connect to a front-end node (also known as a login node) through an intermediate server (proxy). This is common in secure environments where direct access to the front-end node is restricted. The `ProxyJump` option in SSH allows you to achieve this. The network diagram for HPC systems at W&M is shown below. 

```{figure} ../../images/intro-to-HPC/WM_HPC_login.png
The Figure is taken from [Lectures on HPC given at W&M by research computing team](https://www.wm.edu/offices/it/services/researchcomputing/using/tutorials/)
```

```{tip}
SSH (Secure Shell) is a protocol used to securely connect to remote servers. In this case, you need to connect to an intermediate server first, and then from there, connect to the front-end node. This is like making a stopover at an intermediate airport before reaching your final destination.
```
## Prerequisites
- SSH client installed on your local machine.
- Access credentials (username and password or SSH key) for both the intermediate server and the front-end node.
- Hostnames or IP addresses of the intermediate server and the front-end node.

## Step-by-Step Guide

### 1. Basic SSH Configuration

First, ensure you can SSH into the intermediate server:

```bash
ssh user@intermediate-server
```

Then, from the intermediate server, ensure you can SSH into the front-end node:

```bash
ssh user@front-end-node
```

### 2. Using ProxyJump

You can use the `-J` option with the ssh command to specify the intermediate server:

```bash
ssh -J user@intermediate-server user@front-end-node
```

### 3. SSH configuration file 

To simplify the process, you can configure your SSH client to use the proxy jump by default. Edit your SSH configuration file (~/.ssh/config) and add the following entries:

```bash
Host intermediate-server
    HostName intermediate-server.example.com
    User your-username

Host front-end-node
    HostName front-end-node.example.com
    User your-username
    ProxyJump intermediate-server
```

Replace `intermediate-server.example.com` and `front-end-node.example.com` with the actual hostnames or IP addresses, and your-username with your actual username. For WM resources, the JumpHost when logging in from outside the campus network is named as `bastion.wm.edu`. Check out the instruction from [here](https://www.wm.edu/offices/it/services/researchcomputing/using/connecting/). 

```bash
ssh -J username@bastion.wm.edu username@bora.sciclone.wm.edu
```

### 4. Using SSH Keys

Some system like the Broohaven National Lab's, The Scientific Data and Computer Center (SDCC), this method is used to [login](https://www.sdcc.bnl.gov/information/ssh/troubleshooting-ssh-connections) to their nodes. SSH keys adds another layer of secutity as it generates an SSH key pair if you don't already have one:

```bash
ssh-keygen -t rsa -b 4096 -C "your-email@example.com"
```

Ensure your SSH configuration file (`~/.ssh/config`) includes the path to your private key:


```bash
Host *
    IdentityFile ~/.ssh/id_rsa
```


