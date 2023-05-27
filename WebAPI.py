import json
import urllib
from urllib import request, error


class WebAPI:
    def download_url_info(self, url: str) -> dict:
        response_obj = None

        try:
            with request.urlopen(url) as response:
                print("t")
                json_str = response.read()
                response_obj = json.loads(json_str)
        except error.HTTPError as err:
            if err.code == 400:
                print("bad request")
        except urllib.error.URLError:
            print("error with url")

        return response_obj

    def set_proper_format(self, original_str):
        original_str.replace(" ", "%20")
        original_str.replace("&", "%26")
        original_str.replace(".", "%2E")
        original_str.replace("/", "%2F")
        return original_str
