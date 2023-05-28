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

    def find_prof(self, name):
        url = f"https://www.ratemyprofessors.com/search/professors/1074?q={name[5:]}"
        
        response = requests.get(url)
        content = response.text
        string = str(content)
        new_name = ""
        first_ind = find_all(str(content), 'firstName')
        for i in first_ind:
            start_of_first = string.find(':', i)
            firstName = string[start_of_first+2:string.find(',', start_of_first)-1]
            print(firstName)
            if firstName[0] == name[0]:
                new_name += firstName
                break
        new_name += "%20" + name[5:]
        print(new_name)


    def load_prof_data(self):
        name = self.rate_my_professor()
        print(name)
        name = self.find_prof(name)
        url = f"https://www.ratemyprofessors.com/search/professors/1074?q={name}"
        
        response = requests.get(url)
        content = response.text
        string = str(content)
        print(string)
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
        print(f'{val2} from professor.py')
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

def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub)