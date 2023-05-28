import requests


class Professor:
    def __init__(self, professor_name):
        self.professor_name = professor_name
        self.prof_rating = None
        self.prof_diff = None
        self.top_tags = None

    def rate_my_professor(self):
        f_and_l = self.professor_name.split(", ")
        f_name = f_and_l[1]
        l_name = f_and_l[0]
        link_name = f"{f_name}%20{l_name}"
        return link_name

    def load_prof_data(self):
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
        ind3 = string.find("legacyId")
        val3 = string[ind3:ind3+17]
        if ',"' in val3:
            val3 = val3[:-2]
        elif "," in val3:
            val3 = val3[:-1]
        else:
            pass
        part3 = val3.split(":")
        url2 = f"https://www.ratemyprofessors.com/professor/{part3[1]}"
        response2 = requests.get(url2)
        content2 = response2.text
        string2 = str(content2)
        ind4 = string2.find("Top Tags")
        val4 = string2[ind4+10:ind4+1000]
        ind5 = val4.find("</div>")
        val5 = val4[:ind5]
        part4 = val5.split("Tag-bs9vf4-0 hHOVKF")
        mod = part4[1:]
        lst = []
        for val in mod:
            index = val.find("<")
            element = val[2:index]
            if "&#x27;" in element:
                element = element.replace("&#x27;", "'")
            lst.append(element.strip())
        self.top_tags = lst