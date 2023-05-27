from WebAPI import WebAPI
from grade import Grade


class Course(WebAPI):
    def __init__(self, course_code, grade_option):
        self.course_code = course_code
        self.grade_option = grade_option
        self.department = None
        self.number = None
        self.course_type = None
        self.professor = None
        self.grade_obj = None
        self.units = 0

    def load_data(self):
        term = "Fall"
        url = f"https://api.peterportal.org/rest/v0/schedule/soc?term=2023%20{term}&sectionCode={self.course_code}"
        course_obj = self.download_url_info(url)
        print(course_obj)


        """
        if course_obj is not None:
            self.course_name = course_obj[]
            self.professor = course_obj[]
            self.course_type = course_obj[]
            self.units = course_obj[]
        """

    def set_grade(self):
        self.grade_obj = Grade(self.department, self.number, self.course_type, self.professor)


def main():
    n = Course("35530", "P")
    n.load_data()
    n.set_grade()


if __name__ == "__main__":
    main()
