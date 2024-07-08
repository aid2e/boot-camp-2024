
# Configuring your `git`

````{margin}
```{important}
Note this could be your GitHub username or other services like [GitLab](https://GitLab.com), [Bitbucket](https://bitbucket.org/) etc. Check out the 10 alternatives to `GitHub` [here](https://www.softwaretestinghelp.com/github-alternatives/). We will look closely into GitHub for this tutorial.
```
````

We shall try to configure your credentials to git. Note that we are using GitHub for hosting for remote repository. Make sure to have your an account created and signed up at [GitHub](https://github.com).

1. Open your terminal.
2. Set your username💻: 
```bash
git config --global user.name "Your username"
```
3. Set your email📧:  
```bash
git config --global user.email "your.email@example.com"
```
3. Check your configuration using 
```bash
git config --global --list
```
4. **Personal Access Tokens (PAT)**: In order to use password in GitHub Command Line Interface (CLI), one have to use tokens.
    * Go to [https://github.com/settings/tokens](https://github.com/settings/tokens), Login is required for this step. 
    * Click on "Generate new token" -> "Generate new token (classic)".
    * Give your token a descriptive name. For eg. one could use a token for performing pushes to certain respository. 
    * Select the scopes or permissions you'd like to grant this token. For typical Git operations, the following scopes are recommended: `repo`, `write:packages`, `workflow`, `read:packages`, `delete:packages`, `admin:repo_hook`.
    * Click on "Generate token"
    * You will see a token has been generated with. Usually it looks like `ghp_*`. Copy this as this will be used as `passwords` when prompted. 
    * In order to securely store the credentials you can store it in the global configuration file. The next time you perform an action that requires authentication, Git will prompt you for your PAT and store it in plaintext in a file under your home directory (~/.git-credentials).
```bash
git config --global credential.helper store
```

## A few alternatives to store PAT

`````{tab} Using environemental variables

1. Open your terminal 
2. Set your PAT as an environmental variable
````{tab} bash 

```bash
export GITHUB_TOKEN=your_personal_access_token
```
````
````{tab} tcsh 

```tcsh
setenv GITHUB_TOKEN your_personal_access_token
```
````

3. Use the environment variable in your Git commands:
```bash
git clone https://$GITHUB_TOKEN@github.com/username/repo.git
```
`````

`````{tab} Using Git Credential Manager
````{tab} Windows and macOS
1. Git for Windows includes the Git Credential Manager by default. On macOS, you can install it using Homebrew:
```bash
brew tap microsoft/git
brew install --cask git-credential-manager-core
```
````
````{tab} Linux
1. Install the Git Credential Manager Core:
```bash
sudo apt-get update
sudo apt-get install git-credential-manager-core
```
2. Configure Git to use the Credential Manager:
```bash
git config --global credential.helper manager-core
```
````
`````

Now, let us proceed to exercises now.