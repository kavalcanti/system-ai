# system-ai
A simple chatGPT implementation to assist with using the terminal. 

### Sistem Manual Submind

The script generates a more or less stateless instance of chatGPT, prompted to assist the user with terminal usage.
You will need an openAI API key.

Just hit "Enter" on an empty MSG: or use a keyboard interrupt (Ctrl+C) to finish.

Install:

You will need a working python environment first.
Use [mamba](https://mamba.readthedocs.io/en/latest/installation.html) to manage environments:

```
mamba create -n sys-ai
mamba activate sys-ai
```

Clone the repository and navigate to the folder.

```
git clone https://github.com/kavalcanti/system-ai
cd system-ai
```

To start a conversation just type `sms`. 

Run 
```
bash add_alias.sh
bash remove_alias.sh
```

to add or remove an alias from ~/.bashrc so it can be called from anywhere in the shell.
