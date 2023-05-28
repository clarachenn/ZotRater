import json
from WebAPI import WebAPI
from grade import Grade
from professor import Professor
from fastapi import HTTPException


class CustomException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f"CustomException: {self.message}"


class Course(WebAPI):
    def __init__(self, department, course_code, grade_option):
        self.course_code = course_code
        self.grade_option = grade_option
        self.department = department
        self.number = None
        self.course_type = None
        self.professor = None
        self.grade_obj = None
        self.prof_obj = None
        self.course_rating = None
        self.units = None

    def extract_json(self, json_msg):
        try:
            json_obj = json.loads(json_msg)
            self.number = json_obj["schools"][0]["departments"][0]["courses"][0]["courseNumber"]
            self.professor = json_obj["schools"][0]["departments"][0]["courses"][0]["sections"][0]["instructors"][0]
            self.course_type = json_obj["schools"][0]["departments"][0]["courses"][0]["sections"][0]["sectionType"]
            self.units = json_obj["schools"][0]["departments"][0]["courses"][0]["sections"][0]["units"]
        except IndexError:
            raise HTTPException(status_code = 400, detail =  "The department and the course code don't match")
        except json.JSONDecodeError:
            raise HTTPException (status_code = 400, detail =  "The JSON cannot be decoded")

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
        else:
            raise HTTPException(status_code=400, detail="Error fetching data from url")

    def set_grade(self):
        """
        creates a grade object and stores it as an attribute
        :return:
        """
        try:
            self.grade_obj = Grade(self.department, self.number, self.course_type, self.professor)
            self.grade_obj.load_grade_data()
        except Exception as e:
            return HTTPException(status_code = 400, detail = e) 

    def set_prof_obj(self):
        """
        creates a professor object and stores it as an attribute
        :return:
        """
        if self.professor is not None:
            try:
                self.prof_obj = Professor(self.professor)
                self.prof_obj.load_prof_data()
            except IndexError:
                raise HTTPException(status_code = 400, detail = f"The department and the course code don't match for: {self.department} and "
                                      f"{self.course_code}")
        else:
            raise HTTPException(status_code = 400, detail = f"No professor associated with the course: {self.course_code}")

    def set_course_rating(self):
        """
        calculates the rating for each course
        :return:
        """
        if self.grade_obj.course_gpa is not None and self.units is not None and self.prof_obj.prof_rating is not None \
                and self.prof_obj.prof_diff is not None:

            grade = self.grade_obj.course_gpa
            units = int(self.units)
            prof_rating = float(self.prof_obj.prof_rating)
            prof_difficulty = float(self.prof_obj.prof_diff)

            if self.grade_option == "G":
                self.course_rating = 1.40253911*grade + 1.02 * prof_rating - (prof_difficulty * 0.46961778) - (0.06482668 * units)
            elif self.grade_option == "PNP":
                self.course_rating = 1.57253911 * grade + 1.02 * prof_rating - (prof_difficulty * 0.46961778) - (0.06482668 * units)


def main():
    n = Course("I&C Sci", "35610", "PNP")
    n.load_course_data()
    n.set_grade()
    n.set_prof_obj()
    n.set_course_rating()


if __name__ == "__main__":
    main()
