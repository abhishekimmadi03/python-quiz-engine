# Python Quiz Engine — Test Case Report

**Project:** Python Quiz Engine  
**Program file:** `quiz.py`  
**Passing threshold:** 70%  
**Test documentation status:** All cases documented; outcomes below are based on review of the submitted program logic and should be confirmed by running the program.

## Test cases

# Python Quiz Engine - Test Cases

| Test ID | Test Scenario | Input / Action | Expected Result | Actual Result |
|---|---|---|---|---|
| TC-01 | All answers correct | Answer all 5 questions correctly. | Score 5/5, accuracy 100%, Passed, no missed questions. |  verified |
| TC-02 | All answers incorrect | Answer all 5 questions incorrectly using valid options. | Score 0/5, accuracy 0%, Failed, all 5 questions appear in the missed-question review. | verified |
| TC-03 | Passing threshold met | Answer 4 questions correctly and 1 incorrectly. | Score 4/5, accuracy 80%, Passed, 1 missed question reviewed. |  verified |
| TC-04 | Passing threshold not met | Answer 3 questions correctly and 2 incorrectly. | Score 3/5, accuracy 60%, Failed, 2 missed questions reviewed. |  verified |
| TC-05 | Uppercase input | Enter B instead of b. | Input is normalized to lowercase and accepted. | verified |
| TC-06 | Invalid input | Enter e, then 9, then a valid option. | Invalid inputs are rejected, and the program prompts again. |  verified |
| TC-07 | Empty input | Press Enter without entering an answer. | Program rejects the blank input and prompts again. | verified |
| TC-08 | Early termination | Press Ctrl+C at the first question. | Quiz reports Incomplete and lists all 5 questions as unanswered. | verified |
| TC-09 | Partial completion | Answer 2 questions, then press Ctrl+C at question 3. | Quiz reports Incomplete, preserves the first 2 responses, and lists 3 unanswered questions. | verified |
| TC-10 | Empty question bank | Temporarily set questions = [] and run the program. | Program displays Add Questions. without dividing by zero. | verified |