import json
from urllib import request, error, parse


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
                print("bad request")
        except error.URLError as e:
            print(e)

        return response_obj

    def set_proper_format(self, url):
        url = parse.quote(url)
        return url
