import json
import urllib
from urllib import request, error


class PeterPortalAPI:
    def __init__(self, course_code, grade_option):
        self.course_code = course_code
        self.grade_option = grade_option
        self.professor = None

    def download_url_info(self, url: str) -> dict:
        response_obj = None

        try:
            with request.urlopen(url) as response:
                json_str = response.read()
                response_obj = json.loads(json_str)
        except error.HTTPError as err:
            if err.code == 400:
                print("bad request")
        except urllib.error.URLError:
            print("not connected to the internet")
        return response_obj


    def load_data(self):
        url = f"https://api.peterportal.org/rest/v0/schedule/soc?term=2023 Fall&sectionCode={self.course_code}"
        course_obj = self.download_url_info(url)



