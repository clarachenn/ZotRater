from grade import Grade
from course import Course


class Planner:
    def __init__(self, courses_list, prof_list):
        self.courses_list = courses_list
        self.course_obj_list = []

        self.prof_list = prof_list
        self.prof_obj_list = []

        self.course_prof_list = []
        self.num_courses = len(courses_list)
        self.all_courses_gpa = 0
        self.course_load_time = 0

    def set_course_obj_list(self):
        for course in self.courses_list:
            course_code = course[0]
            grading_opt = course[1]
            course_obj = Course(course_code, grading_opt)
            self.course_obj_list.append(course_obj)

    def set_prof_obj_list(self):
        for prof in self.prof_list:
            prof_obj = ""
            self.prof_obj_list.append(prof_obj)

    def set_average_gpa(self):
        all_gpa_sum = 0
        for course_obj in self.course_obj_list:
            current_course_gpa = course_obj.grade_obj.course_gpa
            all_gpa_sum += current_course_gpa
        self.all_courses_gpa = all_gpa_sum / self.num_courses

    def set_course_prof_list(self):
        for i in range(self.num_courses):
            self.course_prof_list.append([self.course_obj_list[i], self.prof_obj_list[i]])



    def calc_compatibility(self):
        pass