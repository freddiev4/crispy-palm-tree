# Setup

## Install & Configure Git

If you haven’t done so already, install git (search for “install git” and follow the instructions on git-scm.com). Open your terminal / git bash.

Ensure that you have git installed by typing the following command into your terminal (excluding the $):

```console
$ git --version

# you should see something like the text below
git version 2.24.3
```

Next, configure your name and email address by running:

```console
$ git config --global user.name "Your Name"
$ git config --global user.email your-email@example.com
```


Optionally, set your favorite editor

```console
$ git config --global core.editor code (emacs, vi, etc)
```



# Initializing a repository

A repository contains all of your project's files and each file's revision history. We’re going to create a new repository via our terminal.

Let’s run the following commands:

```console
$ mkdir mygitrepo <-- creates a new directory (folder) for our repository
$ cd mygitrepo    <-- changes our current working directory to mygitrepo
$ git init        <-- initializes the directory as a git repository
```


# .git

Once a repository has been initialized, it will have a hidden directory called .git. This is where all of our version history ends up being stored.

Want to confirm it’s there? Run:

```console
$ ls -a       <-- shows all directories including hidden directories
$ ls -a .git  <-- shows the contents of the .git directory
```


# git status

We’re going to add some files.

```console
$ touch colors.txt numbers.txt
```

Git should pick up these files. To check, run:

```console
$ git status

On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
       colors.txt

       numbers.txt
 ```

You should see output similar to the above (the output might also say `On branch main` which is also valid).

# Anatomy of git status


```console
$ git status

On branch master  ← The current branch we’re working on.
   	  	    A branch is a movable pointer to a series of commits.
 
No commits yet    ← This is saying we have no commits yet.
   	   	    A commit is the basic unit of version control,
 		    and is a snapshot of our files at a specific point in time.

Untracked files:
  (use "git add <file>..." to include in what will be committed)
       colors.txt
       numbers.txt       ← This is saying we have no versions of these files being tracked yet.
       			   The way we can track these files is by first adding them to the staging area.
```


# Git staging area


We’re going to use a common mailing analogy to explain the staging area of Git.


When you’re working with files in git, you add content to the staging area:

```console
$ git add colors.txt numbers.txt (putting a jacket, that you want to mail, in a box)
```

You then record the changes into the git index using git commit:

```
$ git commit -m "Add a colors file and a numbers file" (sealing the box, adding a shipping label)
```

The `-m` flag lets you include a message to go with the commit.


## Why do we need to stage changes?

It is good practice to consider every commit as a *logical unit* of change. If you update 2 files that have independent changes,
it's logical to break up those changes into two commits (or more).

# Viewing our commit

Now that we’ve committed our files, let’s see the commit in our log:

```console
$ git log

commit a2a769b573ecba7a9099530db39c627c7ef347b0 (HEAD -> master)
Author: Freddie Vargus <fjv41995@gmail.com>
Date:   Tue Jan 24 23:43:45 2023 -0500

	Add a colors file and a numbers file
```

Your output should look similar to the above.

The log shows all commits listed from most recent at the top, to least recent at the bottom.

Things that you’ll see here are the name of the author, the email, the date, a random-looking (but not actually random) string known as the commit SHA or commit hash, and the message that is associated with the commit


# Showing the files

One important thing that the log didn’t show us was the files we committed. To see them, we can run:

```console
$ git show

commit a2a769b573ecba7a9099530db39c627c7ef347b0 (HEAD -> master)
Author: Freddie Vargus <fjv41995@gmail.com>
Date:   Tue Jan 24 23:43:45 2023 -0500

	Add a colors file and a numbers file

diff --git a/colors.txt b/colors.txt
new file mode 100644
index 0000000..e69de29
diff --git a/numbers.txt b/numbers.txt
new file mode 100644
index 0000000..e69de29
```

- `diff --git a/colors.txt b/colors.txt`: This line shows the file being compared. `a` and `b` are different versions of the same file. Since the files are empty, there are no changes to show between versions.
- `new file mode 100644`: This says that we added a new file, and `100644` means that it's a regular file.
- `index 0000000..e69de29`: This line shows the hashes being compared.

# More changes, undoing, fixing mistakes


We’ve covered how to take a snapshot of files. We’re now going to make changes those files, and we’re going to purposefully commit mistakes and try to fix them.


This can often one of the more difficult parts of using git, especially as the number of files and number of changes increases, but also being able to undo a set of changes can be one of the biggest benefits.


Continuing... open up `colors.txt` and type in a color you like. Save the file. We’re going to see what we changed:

```console
$ git diff

diff --git a/colors.txt b/colors.txt
index e69de29..08ec89e 100644
--- a/colors.txt
+++ b/colors.txt
@@ -0,0 +1 @@
+purple
```

- Anything between the line that has --- will show us things that we removed from the file, in red (nothing currently).
- Anything after the line that has +++ will show us things that we added to the file, in green.

Add a new file called `food.txt`:

```console
$ touch food.txt
```

You should now have two sets of changes that are unstaged.


# Add and commit again

Add your independent changes and commit them

```console
$ git add food.txt
$ git commit -m "Add food file"

$ git add colors.txt (you can run git status after if you want to check that this file is staged)
$ git commit -m "Add my favorite color"
$ git log
```

Now let’s say you put the wrong color, or you wanted to commit something different from what you had written. How do we undo the commit?

```console
$ git reset HEAD~

Unstaged changes after reset:
M        colors.txt
```

Now take a look at your git log again:

```console
$ git log
```

What do you notice about it? What happens when you run git status?




