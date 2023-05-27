from planner import Planner


def run(courses_list):
    # get course codes and grading option from input - nested list
    # courses_list format: [["I&C Sci", 34401, "G"],["COMPSCI", 23344, "G"],["I&C Sci", 89000, "PNP"]]

    planner = Planner(courses_list)

    # set planner attributes
    planner.set_course_obj_list()
    planner.set_average_gpa()
    planner.set_average_rating()
    planner.set_compatibility_score()

    print(planner.compatibility_score)
    # get planner attributes

    compatibility = planner.compatibility
    return compatibility


def main():
    courses_list = [["I&C Sci", 35680, "G"],["COMPSCI", 23344, "G"],["I&C Sci", 89000, "PNP"]]
    run(courses_list)


if __name__ == "__main__":
    main()
