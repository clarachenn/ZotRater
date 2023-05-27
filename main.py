from course import Course


def get_course_obj_list(courses_list):
    course_obj_list = []
    for course in courses_list:
        course_code = course[0]
        grading_opt = course[1]
        course_obj = Course(course_code, grading_opt)
        course_obj_list.append(course_obj)
    return course_obj_list


def calc_compatibility(course_obj_list):
    for course_obj in course_obj_list:
        pass


def main():
    # get course codes and grading option from input - list
    courses_list = []
    course_obj_list = get_course_obj_list(courses_list)
    calc_compatibility(course_obj_list)


if __name__ == "__main__":
    main()
