from pytest import UsageError

# Django url validation
import re

regex = re.compile(
    r"^(?:http|)s?://"  # http:// or https://
    r"(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|"  # domain...
    r"localhost|"  # localhost...
    r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"  # ...or ip
    r"(?::\d+)?"  # optional port
    r"(?:/?|[/?]\S+)$",
    re.IGNORECASE,
)


def validate_url(url: str) -> str:
    """
    Uses Djangos built in url regex validation for urls
    raises a InvalidUrl exception if it is considered invalid
    :param url: the url to be checked
    """
    matches = re.match(pattern=regex, string=url)
    if matches is None:
        raise UsageError(f"url: {url} was not a valid url")
    return url
