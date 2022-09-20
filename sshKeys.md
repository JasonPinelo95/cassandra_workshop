# Generate your ssh keys

## Windows 
On your Windows machine, open up the Git Bash terminal. You can do this by searching for Git Bash in the Windows search bar. Once you have opened up the terminal, run the following command:

```$ ssh-keygen -t rsa -b 4096 -C "youremail@example.com"```

Click enter to anything that is prompted. This will generate your ssh keys. Then, run the following command:

```$ eval $(ssh-agent -s)```

```$ ssh-add ~/.ssh/id_rsa```

You can find your public key in the following location:

```C:\Users\<USERNAME>\.ssh\id_rsa.pub```

## Linux
The same process as Windows :-)

## Mac OS X

The same as in Windows. After you have generated your ssh keys, run the following command:

```$ vim ~/.ssh/config```

Add the following lines to the file:

```
Host *
  AddKeysToAgent yes
  UseKeychain yes
  IdentityFile ~/.ssh/id_rsa
```

And Finally, run the following command:

```$ ssh-add -K ~/.ssh/id_rsa```