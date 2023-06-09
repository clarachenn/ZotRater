import json
from urllib import request, error, parse
from fastapi import HTTPException

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
            with request.urlopen(decoded_url) as response:
                json_str = response.read()
                response_obj = json.loads(json_str)
        except error.HTTPError as err:
            if err.code == 400:
                raise HTTPException(status_code =400, detail="Bad request")
        except error.URLError as e:
            raise HTTPException(status_code=400, detail= e)

        return response_obj


    def set_proper_format(self, url):
        url = parse.quote(url)
        return url
