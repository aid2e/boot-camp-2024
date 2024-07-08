# Exercise 2: Commits, push and branches

In this exercise, you will learn how commits can be reset and the idea of branching. We will be using the repo that you had created from our previous exercise.

## `git commit`

* Navigate to the repository in your terminal and list the contents in the directory.
```bash
cd my-first-git-repo && ls
```
* Before making any changes, it's a good practice to check the status of your repository to see which files are tracked and which are not.
```bash
git status
```

* Check out the commit history of your git repo
```bash
git log
```

* Let us try to add more files and modify the exisiting files
```bash
echo "This is another file. I am ${USER} and I am doing great in learning about git" > second_file.txt
cat second_file.txt
```

* Add this to staging in your the git repo
```bash
git add second_file.txt
```

* Now that the file is staged, you can commit the changes. A commit is a snapshot of your repository at a specific point in time.
```bash
git commit -m "Add second_file.txt with initial content"
```

* Oh... but now say we need to modify the file `first_file.txt`. So lets do add another line to it. 
```bash
echo " This is another line of content in the first_file.txt " >> first_file.txt
cat first_file.txt
```

```{admonition} Try this
:class: tip
Can you add and commit these changes?
```

* Lets check out the commit logs
```bash
git log
```

```{note}
The commits we make here are local commits. These may not neccesarily transalte to remote repository. The remote repository gets updated with all commit history only when you do push it.
```

## `git push`

Now let us push these changes to the remote repository. 

* Check the remote repository that and how its corresponding alias naming and past actions so far. You can do `git remote --help` to get the a detailed manual on its usage.

```bash
git remote -v
```
* Now let us push these changes to the remote repository. The git push command uploads your local commits to the remote repository.
```bash
git push --set-upstream origin main
```
 - `--set-upstream`: This option sets the upstream (tracking) reference for the branch.
 - `origin`: This is the name of the remote repository.
 - `main`: This is the name of the branch you want to push. In this case the name of the branch is `main`

* After pushing, you can verify that your changes are on the remote repository by visiting the repository URL in your web browser or by using:
```bash
git log origin/main
```

## Branches

A branch in Git is a lightweight movable pointer to a commit. The default branch in a new repository is called `main`. When you create a new branch, you're creating a new pointer to a specific commit.

* You can list exisiting branches in the repo using the following command. The current branch will be highlighted with an asterisk (*).
```bash
git branch
```

* To create a new branch, use the git branch command followed by the name of the new branch. For eg. To cerate a new branch with the name new-feature
```bash 
git branch new-feature
```

* To switch to the new branch, use the git checkout command followed by the branch name:
```bash
git checkout new-feature. 
```

```{note}
One can also simply do `git checkout -b <branch-name>` to switch to the new branch. This command will create the branch if it is not exisiting already.
```

* Now that you're on the new branch, you can make changes and commit them. These changes will only affect the feature-1 branch.

```bash
echo "Some new feature" > feature.txt
git add feature.txt
git commit -m "Add feature.txt with some new feature"
```

* You can push this branch to the remote repository as well as 

```bash
git push --set-upstream origin new-feature
```

Great!!! These are the functionalities that are widely used in `git`. If you still have time you can proceed to the advanced exercises as well.