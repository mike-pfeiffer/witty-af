# gnomes

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

The primary function in collect_underpants.py is collect_underpants(). The function
takes one argument: a valid URL. All supporting functions are called as a result of
running collect_underpants(). If used in other applications, this would be the
function to import. A simple argparse has been written in __main__ and a shebang for
Python3 is included in the file.

### Basic Usage

You can collect underpants by executing collect_underpants.py and supplying a URL.

```shell
python3 collect_underpants.py https://webscraper.io/test-sites/e-commerce/allinone
```

After all possible URLs have been parsed from the seed URL, a set is output to
folder **underpants**. If this folder does not exist, the program will create it
for you and store the output in a file named after the seed URL. The example
below will show you the created folder and file. The output in the file is empty
as the target URL provides no new URLs from the seed.

```shell
ls underpants/
```

```shell
more underpants/webscraper.io_test-sites_e-commerce_allinone
```

### Raised Exceptions

The first exception relies on validators to determine if the supplied URL is
valid or not. If an invalid URL is provided, then a **ValueError** is raised
indicating the input URL should match the provided regex. Basically, the URL
should begin with http:// or https:// and contain a valid domain.

```shell
ValueError: Input URL should match regex https?://[^.]*.[a-z]*/?.*
```

If the target has already been collected, then a **FileExistsError** is raised.
In the event you wish to refresh the contents of this file, simply rename or
delete the existing file.

```shell
FileExistsError: These underpants have already been collected!
```

Another **ValueError** is raised when the supplied URL returns 0 new links. This
exception ensures no empty data is stored.

```shell
ValueError: No additional links were discovered!
```
