from WebAPI import WebAPI
from grade import Grade
from rmp import Professor


class Course(WebAPI):
    def __init__(self, course_code, grade_option):
        self.course_code = course_code
        self.grade_option = grade_option
        self.department = ""
        self.number = 0
        self.course_type = ""
        self.professor = ""
        self.grade_obj = None
        self.prof_obj = None
        self.course_rating = 0
        self.units = 0

    def load_course_data(self):
        """
        downloads data with from the PeterPortal API with the course code and term.
        sets the object's attributes to the data
        :return:
        """
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

    def set_course_rating(self):
        """
        calculates the rating for each course
        :return:
        """
        pass


def main():
    n = Course("35530", "P")
    n.load_course_data()
    n.set_grade()


if __name__ == "__main__":
    main()
