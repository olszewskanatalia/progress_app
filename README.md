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


All the progress is saved under file `records.json`. If the file is not found, the new one is created.

### Add
Add the new episode(s) to the records.

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

Update the episode(s).

    python piotr.py update [-h] [-n NUMBER | -s SET_UP | -r] episode [episode ...]

The episode should start with the letter `E`, followed by one or more digits.
Example of usage:
```shell
    python piotr.py update E001
```
```shell
    python piotr.py update E001 E002 -n 2
```
```shell
    python piotr.py update E001 -s 76
```
```shell
    python piotr.py update E001 E002 E003 -r
```
Positional arguments:
-  `episode`               single episode (or list) to update (default updated by 1)

Optional arguments:
-  `-h, --help`                  show this help message and exit
-  `-n NUMBER, --number NUMBER`  update episodes by N number
-  `-s SET_UP, --set-up SET_UP`  set records to N
-  `-r, --reset`                 reset progress on episodes. These records will be set to 0

### Show
Show the current status of the records.

    python piotr.py show [-h] [-a | -t N | -b N] [-s [WHAT | HOW | WHAT-HOW]]

Without any paramenters the program will show all the values without sorting. \
For the `[-t | -b]` parameters `N` should have a positive integer value. \
The possible options for sorting are:
- `ep`        - sort by episode name (default asc)
- `num`       - sort by number (default asc)
- `asc`       - sort ascending (default by numer)
- `desc`      - sort descending (default by numer)
- `ep-asc`    - sort ascending by episode name
- `ep-desc`   - sort decending by episode name
- `num-asc`   - sort ascending by number
- `num-desc`  - sort descending by number
Default sort is ascending by number.

Example of usage:
```shell
    python piotr.py show
```
```shell
    python piotr.py show -a
```
```shell
    python piotr.py show -t 5
```
```shell
    python piotr.py show -b 10
```
```shell
    python piotr.py show -a -s ep
```
```shell
    python piotr.py show -t 5 -s num
```
```shell
    python piotr.py show -b 1 -s asc
```
```shell
    python piotr.py show -s ep-desc
```

Optional arguments:
-  `-h, --help`            show this help message and exit
-  `-a, --all`             show all records
-  `-t N, --top N`         show top N records
-  `-b N, --bottom N`      show bottom N records
-  `-s [WHAT | HOW | WHAT-HOW], --sort [WHAT | HOW | WHAT-HOW]` sort displayed records
