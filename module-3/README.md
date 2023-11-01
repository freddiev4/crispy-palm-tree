# Testing out `git rebase -i`

## Setup

In this module, we have a `main` branch that has some commits on it. Each commit has a snapshot of changes made to some Python files.

First, fork this repository (click the fork button in the top right) and then clone your forked copy of the repository from your GitHub account to your machine.

## Working with your local copy

Now that you have a local copy, checkout to a new branch using:

```
git checkout -b mynewbranch
```

And take a look at the commit log using:

```
git log
```

You should see some commits made on November 1st. You're going to interactively fix each commit, because the last three commits have bugs in the code.

```console
Author: Freddie Vargus <fjv41995@gmail.com>
Date:   Wed Nov 1 20:13:28 2023 +0000

    Add test suite

commit 739984afef2b78d2c9095d9654ab8a2bcc4789f7
Author: Freddie Vargus <fjv41995@gmail.com>
Date:   Wed Nov 1 20:10:46 2023 +0000

    Add subtract() function

commit 6938c90e9d0c1ba6353d8b7972bb8f9388bfc5df
Author: Freddie Vargus <fjv41995@gmail.com>
Date:   Wed Nov 1 20:09:51 2023 +0000

    Add add() function
```


Start by running

```
git rebase -i HEAD~3
```

This tells git we want to interactively fix the last 3 commits from `HEAD`. You should see a file pop up in your editor that looks something like:


```console
pick 6938c90 Add add() function
pick 739984a Add subtract() function
pick c64789f Add test suite

# Rebase 12da376..c64789f onto 12da376 (3 commands)
#
# Commands:
# p, pick <commit> = use commit
# r, reword <commit> = use commit, but edit the commit message
# e, edit <commit> = use commit, but stop for amending
# s, squash <commit> = use commit, but meld into previous commit
# f, fixup [-C | -c] <commit> = like "squash" but keep only the previous
#                    commit's log message, unless -C is used, in which case
#                    keep only this commit's message; -c is same as -C but
#                    opens the editor
# x, exec <command> = run command (the rest of the line) using shell
# b, break = stop here (continue rebase later with 'git rebase --continue')
# d, drop <commit> = remove commit
# l, label <label> = label current HEAD with a name
# t, reset <label> = reset HEAD to a label
# m, merge [-C <commit> | -c <commit>] <label> [# <oneline>]
#         create a merge commit using the original merge commit's
#         message (or the oneline, if no original merge commit was
#         specified); use -c <commit> to reword the commit message
# u, update-ref <ref> = track a placeholder for the <ref> to be updated
#                       to this position in the new commits. The <ref> is
#                       updated at the end of the rebase
#
# These lines can be re-ordered; they are executed from top to bottom.
#
# If you remove a line here THAT COMMIT WILL BE LOST.
#
# However, if you remove everything, the rebase will be aborted.
#
```

Replace each word `pick` with the word `edit`. Then save and close the file.

What will happen next is git will bring you back to the oldest commit, and then allow you to make any changes to the commit.

To undo the changes to the Python file made in this commit run:

```console
git reset --mixed HEAD~1
```

Run `git status` and check that the file was still modified.

Then fix what's wrong with the file, save it, and add and commit your changes.

```console
git add .
```

```console
git commit -m "<your message here>"
```

Then run `git rebase --continue` to move on to the next commit, and then repeat this process until you've fixed every commit.

# Testing out `git reflog`

Let's add a new file here called `mygithubusername.txt`. Add your username to it, and then save the file, add, and commit it with a message.

Now run `git reflog` to see what has happened over the last few commits. You will see a list of every thing you've done in git. Each change has an index shown as `HEAD@{index}`.

Pick a commit where you changed something and run (while replacing the index number):

```console
git reset HEAD@{index}
```

# Testing out `git revert`

Now that you're on a new commit, check where you are in the log, using `git log`.

Find the commit hash, and undo it with `git revert <hash>`.

Follow the instructions that git showd to you in a new file.

