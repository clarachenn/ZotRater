from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

def get_department_names():
    # Your logic to retrieve the department names
    department_names = ['Department 1', 'Department 2', 'Department 3']
    return department_names

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
# API endpoint to retrieve the list of department names
@app.get('/get_course_directory')
def get_course_directory():
    # Call the function to get the department names
    department_names = get_department_names()

    # Return the department names as JSON response
    return department_names

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='localhost', port=5000)
