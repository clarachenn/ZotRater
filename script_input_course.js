document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById("evaluation-form");
    const courseCodeInput = document.getElementById("course-code");
    const optionInput = document.getElementsByName("option");
    const courseCodesContainer = document.getElementById("course-codes-container");
    const submitButton = document.getElementById("submit");
    const evaluateButton = document.getElementById("evaluate");
    const dropDown = document.getElementById("departments");
    var totalInput = [];

    form.addEventListener("submit", function(event) {
        event.preventDefault();
        
        displayInput();
        evaluateButton.removeAttribute("disabled");

    });
    
    evaluateButton.addEventListener("click", function(event) {
        event.preventDefault();
        performEvaluation();
    });


    function displayInput() {
        courseCode = courseCodeInput.value;
        var gpa = ""
        for (i = 0; i < optionInput.length; i++)
        {
            if (optionInput[i].checked)
            {
                gpa = optionInput[i].value;
                optionInput[i].checked = false;
                break;
            }

        }
        totalInput.push([dropDown.value, courseCode, gpa.toUpperCase()]);
        const row = document.createElement("div");
        row.classList.add("course-code-row");
    
        const courseCodeText = document.createElement("span");
        courseCode.className= ".from-group"
        courseCodeText.textContent = courseCode + "    " + gpa;
        row.appendChild(courseCodeText);
    
        const deleteButton = document.createElement("button");
        deleteButton.textContent = "X";
        deleteButton.addEventListener("click", function() {
          row.remove();
        });
        row.appendChild(deleteButton);
    
        courseCodesContainer.appendChild(row);
    
        courseCodeInput.value = "";          
    }

    function createDepartments() {
        fetch("http://localhost:5000/get_course_directory")
          .then(response => response.json())
          .then(result => {
            const dropDown = document.getElementById("departments");
            for (let i = 0; i < result.length; i++) {
              const option = document.createElement("option");
              option.text = result[i];
              dropDown.add(option);
            }
          })
          .catch(error => {
            console.error("Error: ", error);
          });
      }

    function performEvaluation() {
        console.log("Performing evaluation...");
        const test = [["I&C Sci", "35680", "G"], ["COMPSCI", "23344", "G"], ["I&C Sci", "89000", "PNP"]];
        const encodedTest = JSON.stringify(totalInput);
        while (courseCodesContainer.firstChild)
        {
            courseCodesContainer.removeChild(courseCodesContainer.firstChild);
        }
        fetch('http://localhost:5000/run', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body : encodedTest
        })
          .then(response => {
            if (!response.ok) {
            }
            return response.json();
        })
          .then(result => {
            
            if (result.details != null)
            {
                alert(result.detail);
                
                return;
            }
            console.log(result);
            //console.log(result.detail);
            
            const data = 3.5;
            //window.location.href = `ratings.html?data=${data}`;
            
          })
          .catch(error => {
            console.error("Error: ", error);
          });
        
        totalInput = []
        
    }
    createDepartments();
});
