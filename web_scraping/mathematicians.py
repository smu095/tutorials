from collections import defaultdict
from contextlib import closing
from pprint import pprint
from typing import Dict, List

from bs4 import BeautifulSoup
from requests import Response, get
from requests.exceptions import RequestException


def simple_get(url: str, is_json: bool = False):
    """Return GET request from URL.

    Parameters
    ----------
    url : str
        Target URL.
    is_json : bool, optional
        Flag indicating if expected return value is a JSON, by default False

    Returns
    -------
    A JSON or string, depending on value of `is_json`.
    """
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.json() if is_json else resp.content
            else:
                return None
    except RequestException as e:
        print(f"Error during request to {url} : {str(e)}")
        return None


def is_good_response(resp: Response) -> bool:
    """Return True if valid response, else False.

    Parameters
    ----------
    resp : Response
        A Response object resulting from a get request.

    Returns
    -------
    is_good : bool
        Boolean indicating if response is good or not.
    """
    content_type = resp.headers["content-type"].lower()
    is_good = (
        resp.status_code == 200
        and content_type is not None
        and (content_type.find("json") > -1 or content_type.find("html") > -1)
    )
    return is_good


def get_names(url="http://www.fabpedigree.com/james/mathmen.htm") -> List[str]:
    """Return list of 100 mathematician names.

    Parameters
    ----------
    url : str, optional
        URL to scrape mathematician names from, by default "http://www.fabpedigree.com/james/mathmen.htm"

    Returns
    -------
    names : List[str]
        A list of mathematician names.

    Raises
    ------
    Exception
        Thrown when response is NoneType.
    """
    response = simple_get(url, is_json=False)
    if response is not None:
        html = BeautifulSoup(response, "html.parser")
        names = set()
        for li in html.select("li"):
            for name in li.text.split("\n"):
                if len(name) > 0:
                    names.add(name.strip())
        return list(names)
    else:
        raise Exception(f"Error retrieving contents at {url}")


def _url(name: str) -> str:
    """Return URL for given mathematician.

    Parameters
    ----------
    name : str
        Name of mathematician.

    Returns
    -------
    url : str
        URL to scrape.
    """
    base_url = "https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia.org/"
    api_request = f"all-access/user/{name}/monthly/2020010400/2020060100"
    url = base_url + api_request
    return url


def print_result(dictionary: Dict, name: str, rjust: int = 30) -> None:
    """Prettify print output of result for individual mathematician."""
    name_length = len(name)
    add_rjust = rjust - name_length
    output = name + str(dictionary[name]).rjust(add_rjust)
    print(output)


def print_output(dd: Dict) -> None:
    """Prettify print output of generated results."""
    header = "Name" + "Views".rjust(30 - len("Name"))
    ruler = "=" * len(header)
    print(header)
    print(ruler)
    for mathematician in sorted(dd, key=dd.get, reverse=True):
        print_result(dd, mathematician)


def get_results() -> None:
    """Return top 100 most popular mathematicians ranked by Wikipedia page views."""
    names = get_names()
    dd = defaultdict(int)
    for name in names:
        url_name = "_".join(name.split())
        url = _url(url_name)
        resp = simple_get(url, is_json=True)
        if resp:
            for item in resp["items"]:
                dd[name] += item["views"]
        else:
            dd[name] = -1
    return dd


if __name__ == "__main__":
    results = get_results()
    print_output(results)
