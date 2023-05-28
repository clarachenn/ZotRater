import json
from pathlib import Path
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


def get_course_directory():
    path = "courses.json"
    my_path = Path(path)

    department_names = set()

    if my_path.exists():
        try:
            with open(my_path, 'r', encoding='utf-8') as my_file:
                j_obj = json.load(my_file)
                for item in j_obj:
                    department_names.add(item['department'])
        except Exception as ex:
            print(ex)
    else:
        print("path doesn't exist")
    return sorted(department_names)


def main():
    gpa = 3.828
    prof_rating = 4.4
    units = 4
    prof_difficulty = 3

    res = (gpa * 2) + (prof_rating * 1.25) - (units * 0.3) - (prof_difficulty * 0.75)
    print(res)

    print(get_course_directory())

    courses_list = [["I&C Sci", 35680, "G"], ["COMPSCI", 23344, "G"], ["I&C Sci", 89000, "PNP"]]
    run(courses_list)


if __name__ == "__main__":
    main()

