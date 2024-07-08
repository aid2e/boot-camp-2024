# Advanced exercises

## `git reset`

The `git reset` command is used to undo changes in your working directory and staging area. It can be a powerful tool for correcting mistakes and managing your commit history. There are three main modes of `git reset`: `--soft`, `--mixed`, and `--hard`.

### Step 1: Understanding the Modes

1. **`--soft`**:
   - Moves the HEAD pointer to a specified commit.
   - Does not change the working directory or the staging area.
   - Useful for undoing commits but keeping changes staged.

2. **`--mixed`** (default):
   - Moves the HEAD pointer to a specified commit.
   - Resets the staging area to match the specified commit.
   - Does not change the working directory.
   - Useful for undoing commits and un-staging changes.

3. **`--hard`**:
   - Moves the HEAD pointer to a specified commit.
   - Resets the staging area and the working directory to match the specified commit.
   - Discards all changes in the working directory.
   - Useful for completely discarding changes.

### Step 2: Using `git reset`

#### Example Scenario

Let's say you have the following commit history that you print from our example
```bash
git log
```

which produces

```bash
git log origin0/main
commit ba4d5381ae88542f557d5a855f687a14c6bcd792 (HEAD -> main, origin0/new-bramch, origin0/main, new-bramch)
Author: karthik18495 <karthik18495@gmail.com>
Date:   Mon Jul 8 04:01:25 2024 -0400

    second commit

commit dd1a49bc774cdd74e7116a6cf49b89c5832917e8 (origin_new/main)
Author: karthik18495 <karthik18495@gmail.com>
Date:   Sun Jul 7 21:41:18 2024 -0400

    added hello.txt
```

you can revert back to previous commits in a few ways

#### `--soft` Reset

```bash
git reset --soft <commit-hash>
```
In this case 

```bash
git reset --soft HEAD~1
```
This moves the HEAD pointer to commit by `2` positions before (index starts from `0`), but keeps the changes from recent commit  staged.

#### --mixed Reset

```bash
git reset --mixed HEAD~1
```
This moves the HEAD pointer to commit `2` positions before (index starts from `0`), but unstages the recent commits but keeps them in the working directory.

#### --hard Reset

```bash
git reset --hard HEAD~1
```
This moves the HEAD pointer to commit `2` positions before (index starts from `0`), and discards all changes from the recent commit.

## `git merge`

The `git merge` command is used to combine the changes from one branch into another. This is a common operation when you want to integrate changes from a feature branch into the main branch.

When you merge branches, Git tries to automatically combine the changes. If there are conflicts (i.e., changes that cannot be automatically resolved), Git will prompt you to resolve them manually.

### An example

From our previous exercises we have two branches namely
```bash
* main
  new-feature
```

You want to merge the changes from `new-feature` into `main`.

* Switch to the main branch
```bash
git checkout main
```

* Now, merge the `new-feature` branch into `main`:
```bash
git merge new-feature
```

If there are no conflicts, the merge will complete automatically. You will see a message like:

```bash
Updating a1b2c3d..d4e5f6g
Fast-forward
 feature1.txt | 1 +
 1 file changed, 1 insertion(+)
 create mode 100644 feature1.txt
``` 

And finally, you can push these changes to the remote repository.

```bash
git push -u origin main
```

## `git merge conflict`

But what if there are conflicts?

Consider the branch `new-feature`

```bash
git checkout new-feature
```

* Let us edit the file `first_file.txt` such that the second line is something other than what is currently in there. 
* Now try to merge it
```bash
git checkout main && git merge new-feature
```
* Since there are conflicts, Git will prompt you to resolve them. For example:
```bash
Auto-merging file.txt
CONFLICT (content): Merge conflict in file.txt
Automatic merge failed; fix conflicts and then commit the result.
```
To resolve conflicts:

1. Open the conflicting file(s) in your text editor. In this case it is `first_file.txt`
2. Look for conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`). In this case it will be like
```bash
<<<<<<< HEAD
Main branch changes
=======
new-feature changes
>>>>>>> new-feature
```
3. Edit the file to resolve the conflict.
4. Once resolved, stage the changes:
```bash
git add first_file.txt
git commit -m "resolved conflicts"
```

And finally, you can push these changes to the remote repository.

```bash
git push -u origin main
```