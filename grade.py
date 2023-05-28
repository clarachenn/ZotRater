import json
from WebAPI import WebAPI
from urllib import parse


class Grade(WebAPI):
    def __init__(self, department, number, course_type, professor):
        self.department = department
        self.number = number
        self.course_type = course_type
        self.professor = professor
        self.course_gpa = 0
        self.pass_count = 0
        self.no_pass_count = 0
        self.past_courses_length = 0

    def extract_json(self, json_msg):
        try:
            json_obj = json.loads(json_msg)
            self.past_courses_length = len(json_obj)
            gpa_sum = 0
            for i in range(self.past_courses_length):
                gpa_sum += json_obj[i]["averageGPA"]
                self.pass_count += json_obj[i]["gradePCount"]
                self.no_pass_count += json_obj[i]["gradeNPCount"]
            try:
                self.course_gpa = gpa_sum / self.past_courses_length
            except ZeroDivisionError:
                print("no grades for this course")

        except json.JSONDecodeError:
            return "JSON cannot be decoded."

    def load_grade_data(self):
        """
        downloads info from the url and updates the object's attributes with the data
        :return:
        """
        f_string_url = f"https://api.peterportal.org/rest/v0/grades/raw?"
        parameters = {
            "instructor": self.professor,
            "department": self.department,
            "number": self.number,
            "type": self.course_type
        }
        encoded_parameters = parse.urlencode(parameters)
        f"instructor={self.professor}&department={self.department}&number={self.number}&type={self.course_type}"
        url = f"{f_string_url}?{encoded_parameters}"
        grade_info_obj = self.download_url_info(url)

        if grade_info_obj is not None:
            json_obj = json.dumps(grade_info_obj)
            self.extract_json(json_obj)

