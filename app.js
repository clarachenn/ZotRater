document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById("evaluation-form");
    const courseCodeInput = document.getElementById("course-code");
    const resultDiv = document.getElementById("result");
    const optionInput = document.getElementsByName("option");
    const courseCodesContainer = document.getElementById("course-codes-container");


    courseCodeInput.addEventListener("keyup", function(event) {
        if (event.key === "Enter") {
            event.preventDefault();
            displayInput();
        }

        
    });
    
    form.addEventListener("submit", function(event) {
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
                break;
            }
        }
        
        const row = document.createElement("div");
        row.classList.add("course-code-row");
    
        const courseCodeText = document.createElement("span");
        courseCode.className= ".from-group"
        courseCodeText.textContent = "1: " + courseCode + " " + gpa;
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

    function performEvaluation() {
        // Functionality for evaluating the course code goes here
        // This function can be implemented separately
        console.log("Performing evaluation...");
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
});
