# Exercise 1: Basic Git Commands

In this exercise, you will learn the basic Git commands. you will be creating your own private repository. 

## Steps

### Create a New Repository on GitHub
This is going to be our remote repository to which we will be uploading our projects.
* Go to GitHub and create a new repository named `my-first-git-project`.

* **Do not** initialize it with a README, .gitignore, or license. We will be creating a private repository so that we will be using the personal access tokens as well.

![creating repo](../../images/intro-to-git/create-repo.png)

### Initialize a new `git` repository

* In your terminal, let us create new directory 
```bash 
mkdir my-first-git-repo
```
* To align with GitHub naming scheme, the default branch is named as `main`. Hence, lets configure it. 
```bash
git config --global init.defaultBranch main
```
* Initialize a `git` repository
```bash
git init
```

2. Let us add this to git repo
   ```bash
   echo "Hello, Git!" > hello.txt
   git add hello.txt
   ```
3. Commit this file 
   ```bash
   git commit -m "Add hello.txt"
   ```

```{raw} html
<script
   type="text/javascript"
   src="https://utteranc.es/client.js"
   async="async"
   repo="executablebooks/jupyter-book"
   issue-term="git-course-exercise-1"
   theme="github-dark"
   label="💬 git-ex-1"
   crossorigin="anonymous"
/>
```