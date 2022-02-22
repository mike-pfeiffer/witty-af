# collect-underpants

Gnomes is a collection of programs to aid in web scraping. The project is inspired by the South Park episode, “Gnomes.” Expect more modules inspired by the Gnomes’ three-phased business plan.

## Getting Started

This project is being developed on the server edition of [Ubuntu 20.04.3
LTS](https://releases.ubuntu.com/20.04/) and written in Python3.

### Direct on Host

Install the required packages.

```shell
pip install -r requirements.txt
```

### Virtual Environment

Create a virtual environment, activate the environment, and install the required packages.

```shell
python3 -m venv env
```

```shell
. env/bin/activate
```

```shell
pip install -r requirements.txt
```

## collect_underpants.py

The primary function in collect_underpants.py is collect_underpants(). The function takes one argument: a valid URL. All supporting functions are called as a result of running collect_underpants(). If used in other applications, this would be the function to import. A simple argparse has been written in __main__ and a shebang for Python3 is included in the file. You can collect underpants by executing collect_underpants.py and supplying a URL.

```shell
(env) $ ./collect_underpants.py https://realpython.github.io/fake-jobs/
(env) $ python3 collect_underpants.py https://realpython.github.io/fake-jobs/
```

After all possible URLs have been parsed from the seed URL, a set is output to
folder **underpants**. If this folder does not exist, the program will create it
for you and store the output in a file named after the seed URL. The example
below will show you the created folder and file. The output in the file is empty
as the target URL provides no new URLs from the seed.

```shell
(env) $ ls underpants/
realpython.github.io

(env) $ cat underpants/realpython.github.io
set()
```
