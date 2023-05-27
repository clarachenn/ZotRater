from WebAPI import WebAPI


class Grade(WebAPI):
    def __init__(self, department, number, course_type, professor):
        self.department = department
        self.number = number
        self.course_type = course_type
        self.professor = professor
        self.average_gpa = None
        self.pass_count = None
        self.no_pass_count = None

    def load_data(self):
        self.department = self.set_proper_format(self.department)
        self.number = self.set_proper_format(self.number)
        self.professor = self.set_proper_format(self.professor)
        url = f"https://api.peterportal.org/rest/v0/grades/raw?instructor={self.professor}&" \
              f"department={self.department}&number={self.number}&type={self.course_type}"
        grade_info_obj = self.download_url_info(url)
        print(grade_info_obj)

        """
        if grade_info_obj is not None:
            # check if course type is the same as the json file course type first
            self.average_gpa = grade_info_obj[]
            self.pass_count = grade_info_obj[]
            self.no_pass_count = grade_info_obj[]
        """


def main():
    pass


if __name__ == "__main__":
    main()
