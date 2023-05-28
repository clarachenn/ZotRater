import json
from pathlib import Path
from urllib import parse
from planner import Planner
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
origins = [
    "http://127.0.0.1:5500",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)


class CustomException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f"CustomException: {self.message}"


@app.post("/run")
def run(courses_list: list[list[str | int]]):
    # get course codes and grading option from input - nested list
    for code in courses_list:
        code[1] = int(code[1])

    planner = Planner(courses_list)

    # set planner attributes
    planner.set_course_obj_list()
    planner.set_average_gpa()
    planner.set_average_rating()
    planner.set_compatibility_word()

    course_name_list = []
    prof_name_list = []
    course_rating_list = []
    course_gpa_list = []
    pass_rate_list = []
    prof_rating_list = []
    prof_difficulty_list = []
    prof_keywords_list = []
    for course in planner.course_obj_list:
        decoded_str = parse.unquote(course.department)
        course_name_list.append(f"{decoded_str} {course.number}")
        prof_name_list.append(course.professor)
        course_rating_list.append(course.course_rating)
        course_gpa_list.append(f"{course.grade_obj.course_gpa:.2f}")
        pass_rate = course.grade_obj.pass_count / (course.grade_obj.pass_count + course.grade_obj.no_pass_count)
        pass_rate_list.append(f"{pass_rate:.2f}")
        prof_rating_list.append(course.prof_obj.prof_rating)
        prof_difficulty_list.append(course.prof_obj.prof_diff)
        prof_keywords_list.append(course.prof_obj.top_tags)
    return [f"{planner.average_rating:.2f}", planner.compatibility_word, course_rating_list, course_gpa_list, pass_rate_list, prof_rating_list, prof_difficulty_list, prof_keywords_list]


@app.get("/get_course_directory")
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
        except Exception as e:
            raise HTTPException(status_code = 400, detail = e)
    else:
        raise HTTPException(status_code = 400, detail = "The path for course.json does not exist")
    return sorted(department_names)


def main():
    courses_list = [["I&C Sci", 35680, "G"], ["I&C Sci", 35610, "G"], ["I&C Sci", 35640, "PNP"]]
    run(courses_list)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app",  port=5001, reload = True)
    main()
