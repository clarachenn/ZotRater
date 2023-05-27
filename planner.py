from course import Course


class Planner:
    def __init__(self, courses_list):
        self.courses_list = courses_list
        self.course_obj_list = []

        # self.prof_list = prof_list
        # self.prof_obj_list = []

        self.course_prof_list = []
        self.num_courses = len(courses_list)
        self.all_courses_gpa = 0
        self.course_load_time = 0
        self.average_rating = 0
        self.compatibility_score = 0

        self.compatibility = ""

    def set_course_obj_list(self):
        """
        creates course objects and appends them to the planner's course_obj_list attribute
        :return:
        """
        for course in self.courses_list:
            course_code = course[0]
            grading_opt = course[1]
            course_obj = Course(course_code, grading_opt)
            course.load_course_data()
            course.set_grade()
            course.set_prof_obj()
            course.set_course_rating()
            self.course_obj_list.append(course_obj)

    """
    def set_prof_obj_list(self):
        for prof in self.prof_list:
            prof_obj = ""
            self.prof_obj_list.append(prof_obj)
    """

    def set_average_gpa(self):
        """
        calculates the average gpa of all the courses combined
        :return:
        """
        all_gpa_sum = 0
        for course_obj in self.course_obj_list:
            current_course_gpa = course_obj.grade_obj.course_gpa
            all_gpa_sum += current_course_gpa
        self.all_courses_gpa = all_gpa_sum / self.num_courses

    """
    def set_course_prof_list(self):
        for i in range(self.num_courses):
            self.course_prof_list.append([self.course_obj_list[i], self.prof_obj_list[i]])
    """

    def set_average_rating(self):
        """
        calculates the average rating of all the courses' ratings combined
        :return:
        """
        rating_sum = 0
        for course in self.course_obj_list:
            rating_sum += course.course_rating
        self.average_rating = rating_sum / self.num_courses

    def set_compatibility_score(self):
        """
        sets the compatibility score depending on the average rating of all courses
        :return:
        """
        if self.average_rating >= 9:
            self.compatibility = "perfect"
        elif self.average_rating >= 8:
            self.compatibility = "excellent"
        elif self.average_rating >= 6:
            self.compatibility = "good"
        elif self.average_rating >= 4:
            self.compatibility = "ok"
        elif self.average_rating >= 2:
            self.compatibility = "poor"
