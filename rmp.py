import requests
from bs4 import BeautifulSoup
import json
import urllib.parse


class Professor:
    def __init__(self, professor_name):
        self.professor_name = professor_name
        self.prof_rating = None
        self.prof_diff = None

    def rate_my_professor(self):
        f_and_l = self.professor_name.split(", ")
        f_name = f_and_l[1]
        l_name = f_and_l[0]
        link_name = f"{f_name}%20{l_name}"
        return link_name

    def obtain_data(self):
        #name = urllib.parse.quote(self.professor_name)
        name = self.rate_my_professor()
        url = f"https://www.ratemyprofessors.com/search/professors/1074?q={name}"
        response = requests.get(url)
        content = response.text
        string = str(content)
        ind = string.find("avgRating")
        val = string[ind:ind+14]
        part = val.split(":")
        if "," in part[1]:
            self.prof_rating = part[1][0]
        else:
            self.prof_rating = part[1]
        ind2 = string.find("avgDifficulty")
        val2 = string[ind2:ind2+18]
        part2 = val2.split(":")
        if "," in part2[1]:
            self.prof_diff = part2[1][0]
        else:
            self.prof_diff = part2[1]