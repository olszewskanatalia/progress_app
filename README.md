# Progress App

Application to track the progress in learning polish with Piotr.

    python piotr.py <command> [<args>]

The available commands are:
- `update` Update the episode(s).
-    `add`      Add the new episode(s) to records.
-    `show`     Show the current status of records.

Positional arguments:
-  `{add,update,show}`  command name

Optional arguments:
-  `-h, --help`         show this help message and exit
-  `-v, --version`      show version and exit

### Add
Add the new episode(s) to records.

    python piotr.py add [-h] episode [episode ...]

The episode should start with the letter `E`, followed by one or more digits.\
Example of usage:
```shell
python piotr.py add E001
```
```shell
python piotr.py add E001 E002
```

Positional arguments:
-  `episode`     single episode (or list) to add to records (default number 1)

Optional arguments:
-  `-h, --help`         show this help message and exit

### Update

Not implemented yet.

### Show

Not implemented yet.
