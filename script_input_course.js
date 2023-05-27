document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById("evaluation-form");
    const courseCodeInput = document.getElementById("course-code");
    const optionInput = document.getElementsByName("option");
    const courseCodesContainer = document.getElementById("course-codes-container");
    const submitButton = document.getElementById("submit");
    const evaluateButton = document.getElementById("evaluate");
    const totalInput = [];

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
        totalInput.push([courseCode, gpa])
        const row = document.createElement("div");
        row.classList.add("course-code-row");
    
        const courseCodeText = document.createElement("span");
        courseCode.className= ".from-group"
        courseCodeText.textContent = courseCode + "    " + gpa;
        row.appendChild(courseCodeText);
    
        const deleteButton = document.createElement("button");
        deleteButton.textContent = "Remove";
        deleteButton.addEventListener("click", function() {
          row.remove();
        });
        row.appendChild(deleteButton);
    
        courseCodesContainer.appendChild(row);
    
        courseCodeInput.value = "";

          
    }

    function createDepartments() {
        const dropDown = document.getElementById("departments");
        const options = ["Option 1", "Option 2", "Option 3"];

        for (let i = 0; i < options.length; i++)
        {
            const option = document.createElement("option");
            option.text = options[i];
            dropDown.add(option);
        }
    }

    function performEvaluation() {
        // Functionality for evaluating the course code goes here
        // This function can be implemented separately
        console.log("Performing evaluation...");
        console.log(totalInput);
        window.location.href = 'ratings.html';
        totalInput = []
        /*
        let selectedOption = "";
        for (const option of radioOptions) {
            if (option.checked) {
                selectedOption = option.value;
                break;
            }
        }
        const courseCode = courseCodeInput.value;
        $.ajax({
            url: '/evaluate',
            method: 'POST',
            data: { 'course_code': courseCode },
            success: function(response) {
                resultDiv.textContent = 'Evaluation result: ' + response.result;
            },
            error: function() {
                resultDiv.textContent = 'Error occurred during evaluation.';
            }
        });
        */
    }
    createDepartments();
});
