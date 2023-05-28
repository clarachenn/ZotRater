import json
from urllib import request, error, parse


class CustomException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f"CustomException: {self.message}"


class WebAPI:
    def download_url_info(self, url: str) -> dict:
        response_obj = None
        try:
            decoded_url = parse.unquote(url)
            print("link:", decoded_url)
            with request.urlopen(decoded_url) as response:
                json_str = response.read()
                response_obj = json.loads(json_str)
        except error.HTTPError as err:
            if err.code == 400:
                raise CustomException("Bad request")
        except error.URLError as e:
            raise CustomException(e)

        return response_obj


    def set_proper_format(self, url):
        url = parse.quote(url)
        return url
