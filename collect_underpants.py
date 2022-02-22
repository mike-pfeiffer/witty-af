#!/usr/bin/env python3
"""
collect_underpants.py gathers more URLs from a single seed URL.
Copyright (C) 2022 Mike Pfeiffer

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import os
import requests
import argparse
import validators
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urlunparse

FORMAT = "https?://[^.]*.[a-z]*/?.*"
FOLDER = "underpants"
USER_AGENT = (
    "Mozilla/5.0 (X11; CrOS x86_64 14324.80.0) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/97.0.4692.102 Safari/537.36"
)

HEADERS = {
    "User-Agent": USER_AGENT
}


def is_url_valid(url):

    is_valid = validators.url(url)

    if is_valid:
        return True
    else:
        return False


def repair_href(href, target):
    ignore = ["", "/", "#"]

    test = urlparse(href)
    base = urlparse(target)

    # Avoid links that point back to the same page.
    if href in ignore:
        return None
    # A valid scheme and netloc equals a valid page.
    elif (
        test.scheme == base.scheme and
        test.netloc == base.netloc
    ):
        return href
    # Repair scheme for use in requests.get.
    elif (
        test.scheme != base.scheme and
        test.netloc == base.netloc
    ):
        repaired = urlunparse(
            (
                base.scheme, test.netloc,
                test.path, test.params,
                test.query, test.fragment
            )
        )
        return repaired
    # Add scheme and netloc to path only.
    elif (
        not test.scheme and
        not test.netloc and
        test.path
    ):
        repaired = urlunparse(
            (
                base.scheme, base.netloc,
                test.path, test.params,
                test.query, test.fragment
            )
        )
        return repaired
    else:
        return None


def parse_links(url, target):
    links = set()

    try:
        page = requests.get(url, headers=HEADERS)
        response_status = page.status_code

        if response_status == 404:
            return links

        content = page.content

        html = BeautifulSoup(content, "html.parser")
        a_tags = html.find_all("a", href=True)
        for a_tag in a_tags:
            link = repair_href(a_tag["href"], target)
            if link is None:
                continue
            else:
                links.add(link)
    except requests.exceptions.ConnectionError:
        return links
    except requests.exceptions.Timeout:
        return links
    except requests.exceptions.TooManyRedirects:
        return links
    except requests.exceptions.RequestException:
        return links
    except AttributeError:
        return links

    return links


def store_underpants(underpants, target):
    base = urlparse(target)
    netloc = base.netloc
    folder = f"{os.getcwd()}/{FOLDER}"
    filename = f"{folder}/{netloc}"
    folder_exists = os.path.exists(folder)

    if not folder_exists:
        os.mkdir(folder)

    with open(filename, "w") as f:
        f.write(str(underpants))


def is_collected(target):
    base = urlparse(target)
    netloc = base.netloc
    folder = f"{os.getcwd()}/{FOLDER}"
    filename = f"{folder}/{netloc}"
    file_exists = os.path.isfile(filename)

    if file_exists:
        return True
    else:
        return False


def collect_underpants(target):

    if not is_url_valid(target):
        errmsg = f"Input URL should match regex {FORMAT}"
        raise ValueError(errmsg)

    if is_collected(target):
        return "These underpants have been collected!"

    links = set()
    urls = parse_links(target, target)

    def gnomes(urls):

        if urls.issubset(links):
            return

        for url in urls:
            new_links = parse_links(url, target)
            links.update(new_links)

        temp = set()
        temp.update(links)
        gnomes(temp)

    gnomes(urls)
    store_underpants(links, target)

    return links


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("url")
    args = parser.parse_args()
    url = args.url
    collect_underpants(url)
