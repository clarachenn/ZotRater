from course import Course
from fastapi import HTTPException

class CustomException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f"CustomException: {self.message}"


class Planner:
    def __init__(self, courses_list):
        self.courses_list = courses_list
        self.course_obj_list = []
        self.course_prof_list = []
        self.num_courses = len(courses_list)
        self.all_courses_gpa = 0
        self.course_load_time = 0
        self.average_rating = 0
        self.compatibility_word = ""

    def set_course_obj_list(self):
        """
        creates course objects and appends them to the planner's course_obj_list attribute
        :return:
        """
        for course in self.courses_list:
            course_dept = course[0]
            course_code = course[1]
            grading_opt = course[2]
            course_obj = Course(course_dept, course_code, grading_opt)
            course_obj.load_course_data()
            course_obj.set_grade()
            course_obj.set_prof_obj()
            course_obj.set_course_rating()
            self.course_obj_list.append(course_obj)

    def set_average_gpa(self):
        """
        calculates the average gpa of all the courses combined
        :return:
        """
        all_gpa_sum = 0
        for course_obj in self.course_obj_list:
            current_course_gpa = course_obj.grade_obj.course_gpa
            all_gpa_sum += current_course_gpa
        try:
            self.all_courses_gpa = all_gpa_sum / self.num_courses
        except ZeroDivisionError:
            raise HTTPException(status_code=400, detail= "No courses entered")

    def set_average_rating(self):
        """
        calculates the average rating of all the courses' ratings combined
        :return:
        """
        rating_sum = 0
        course_count = 0
        for course in self.course_obj_list:
            if course.course_rating is not None:
                rating_sum += course.course_rating
                course_count += 1
            else:
                raise HTTPException(status_code=400, detail="Error generating course rating")
        self.average_rating = rating_sum / course_count
        if course_count != self.num_courses:
            raise HTTPException(status_code=400, detail="Some courses do not have a rating")

    def set_compatibility_word(self):
        """
        sets the compatibility word depending on the average rating of all courses
        :return:
        """
        if self.average_rating >= 9:
            self.compatibility_word = "perfect"
        elif self.average_rating >= 8:
            self.compatibility_word = "excellent"
        elif self.average_rating >= 6:
            self.compatibility_word = "great"
        elif self.average_rating >= 5:
            self.compatibility_word = "good"
        elif self.average_rating >= 3:
            self.compatibility_word = "ok"
        else:
            self.compatibility_word = "poor"
