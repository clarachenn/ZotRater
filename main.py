import json
from pathlib import Path
from planner import Planner
from fastapi import FastAPI
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


def run(courses_list):
    # get course codes and grading option from input - nested list
    planner = Planner(courses_list)

    # set planner attributes
    planner.set_course_obj_list()
    planner.set_average_gpa()
    planner.set_average_rating()
    planner.set_compatibility_word()

    print("planner compatibility:", planner.compatibility_score)
    print("compatibility word:", planner.compatibility_word)
    return planner.compatibility_word


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
            raise CustomException(e)
    else:
        raise CustomException("The path for course.json does not exist")
    return sorted(department_names)


def main():
    courses_list = [["I&C Sci", 35680, "G"], ["I&C Sci", 35610, "G"], ["I&C Sci", 35640, "PNP"]]
    run(courses_list)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=5000)
    main()

