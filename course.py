import json
from WebAPI import WebAPI
from grade import Grade
from professor import Professor


class Course(WebAPI):
    def __init__(self, department, course_code, grade_option):
        self.course_code = course_code
        self.grade_option = grade_option
        self.department = department
        self.number = 0
        self.course_type = ""
        self.professor = ""
        self.grade_obj = None
        self.prof_obj = None
        self.course_rating = 0
        self.units = 0

    def extract_json(self, json_msg):
        try:
            json_obj = json.loads(json_msg)
            self.number = json_obj["schools"][0]["departments"][0]["courses"][0]["courseNumber"]
            self.professor = json_obj["schools"][0]["departments"][0]["courses"][0]["sections"][0]["instructors"][0]
            self.course_type = json_obj["schools"][0]["departments"][0]["courses"][0]["sections"][0]["sectionType"]
            self.units = json_obj["schools"][0]["departments"][0]["courses"][0]["sections"][0]["units"]
        except IndexError:
            return "dept + course code don't match"
        except json.JSONDecodeError:
            return "JSON cannot be decoded"

    def load_course_data(self):
        """
        downloads data with from the PeterPortal API with the course code and term.
        sets the object's attributes to the data
        :return:
        """
        self.department = self.set_proper_format(self.department)
        term = "Fall"
        url = self.set_proper_format(f"https://api.peterportal.org/rest/v0/schedule/soc?term=2023%20{term}&"
                                     f"department={self.department}&sectionCodes={self.course_code}")
        course_obj = self.download_url_info(url)

        if course_obj is not None:
            json_obj = json.dumps(course_obj)
            self.extract_json(json_obj)

    def set_grade(self):
        """
        creates a grade object and stores it as an attribute
        :return:
        """
        self.grade_obj = Grade(self.department, self.number, self.course_type, self.professor)
        self.grade_obj.load_grade_data()

    def set_prof_obj(self):
        """
        creates a professor object and stores it as an attribute
        :return:
        """
        self.prof_obj = Professor(self.professor)
        self.prof_obj.load_prof_data()


    def set_course_rating(self):
        """
        calculates the rating for each course
        :return:
        """
        gpa = self.grade_obj.course_gpa
        units = self.units
        prof_rating = self.prof_obj.prof_rating
        prof_difficulty = self.prof_obj.prof_diff

        if gpa >= 3.5:
            gpa_input = gpa * 2.25
        elif gpa >= 3:
            gpa_input = gpa * 2.3
        elif gpa >= 2:
            gpa_input = gpa * 2.4
        elif gpa >= 0:
            gpa_input = gpa * 2.5

        if prof_rating >= 4:
            prof_rating_input = prof_rating * 0.9
        elif prof_rating >= 0:
            prof_rating_input = prof_rating * 1

        if prof_difficulty >= 4:
            prof_input = prof_difficulty * 0.95
        elif prof_difficulty >= 0:
            prof_input = prof_difficulty * 0.85

        res = gpa_input + prof_rating_input - (units * 0.4) - prof_input

        # res = (gpa * 2.25) + (prof_rating * 1.0) - (units * 0.4) - (prof_difficulty * .95)
        # res = (gpa * 2.4) + (prof_rating * 1.05) - (units * 0.3) - (prof_difficulty * 1)

        print(res)


def main():
    n = Course("I&C SCI", "35680", "P")
    n.load_course_data()
    n.set_grade()


if __name__ == "__main__":
    main()
