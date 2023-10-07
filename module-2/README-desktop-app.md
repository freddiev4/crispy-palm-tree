# Setup Part 1 (on your machine)

Create new SSH keys for GitHub for secure access and repository writes

```console
ssh-keygen -t ed25519 -C "your_email@example.com"

# OR, if your machine doesn’t support ed25519

ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
```

Press `Enter` to accept the default file location. When asked, type a secure passphrase (or leave it empty).
**NOTE**: When you type a passphrase, you will not see it appear in the terminal. This is a general terminal security measure. Type carefully.


```console
> Enter passphrase (empty for no passphrase): [Type a passphrase]
> Enter same passphrase again: [Type passphrase again]
```

Start the ssh-agent

```console
eval "$(ssh-agent -s)"
```

Add the ssh key to the agent

```console
ssh-add ~/.ssh/id_ed25519

# OR, if you used rsa in the ssh-keygen step

ssh-add ~/.ssh/id_rsa
```

# Setup Part 2 (on your GitHub account)

Add your public SSH key (ends in .pub) from the file to your clipboard from your terminal

```console
pbcopy < ~/.ssh/id_ed25519.pub <-- if this doesn’t work, then open the file in a text editor and copy it
```

Go to github.com/settings, click `SSH and GPG keys`, and then click `New SSH key`.

Paste the key into the text box and click Add SSH key

Test your connection in your terminal with `ssh -T git@github.com` (might take a second). Type `Yes` if prompted. You should see similar text to the below.

```console
Hi freddiev4! You've successfully authenticated, but GitHub does not provide shell access.
```


# Fork a repository

1. Go to `https://github.com/freddiev4/silver-carnival`
2. Click the Fork button
3. Check that you now have a copy of the repository on your GitHub account (go to github.com/yourusername and look at the `repositories` tab)

![forking a repo](forkingrepo.png)


# git clone your fork

From your GitHub Desktop app, click the top left `Current repository` dropdown, then click `Add` and `Clone repository`:

![clone a repo](clone-repo.png)

Find the name of your repository `yourusername/silver-carnival`, click it, and then click clone.


# Make a branch

Click the `current branch` dropdown, then click `New branch`.

![new branch](new-branch.png)

Give your branch a name and click `Create branch`.

# Make changes to the fork

Using some familiar commands (check the actions from module 1), add a `.txt` file with your username: `yourusername.txt`

And commit the file.


# Push your changes

Click on the `Repository` tab in top menu bar, and click `Push`.

# See your changes on GitHub

Go to `github.com/yourusername/silver-carnival`, click the `branch` dropdown, and then your branch name to see your changes

![viewing branches](viewingbranches.png)

And we'll continue back to the main workshop.
