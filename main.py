import json
from pathlib import Path
from planner import Planner
from fastapi import FastAPI, Request
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

@app.post("/run")
def run(courses_list: list[list[str | int]]):
    # get course codes and grading option from input - nested list
    # courses_list format: [["I&C Sci", 34401, "G"],["COMPSCI", 23344, "G"],["I&C Sci", 89000, "PNP"]]
    for code in courses_list:
        code[1] = int(code[1])
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
        except Exception as ex:
            print(ex)
    else:
        print("path doesn't exist")
    return sorted(department_names)


def main():
    print(get_course_directory())

    courses_list = [["I&C Sci", 35680, "G"], ["COMPSCI", 23344, "G"], ["I&C Sci", 89000, "PNP"]]
    run(courses_list)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", port=5000, reload=True)
    # main()

