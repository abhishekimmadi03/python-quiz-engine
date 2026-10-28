# Algorithm: Python Quiz Engine

## Step 1: Start
1. Import the `random` module.
2. Initialize `correct`, `incorrect`, and `score` to 0.
3. Set the passing percentage to 70%.
4. Initialize an empty `responses` list and set `interrupted` to `False`.

## Step 2: Initialize Questions
1. Create a list of quiz questions.
2. For each question, store:
   - Question text
   - Multiple-choice options
   - Correct answer
   - Hint
   - Difficulty level
   - Points assigned to the question
3. Calculate the total number of questions.
4. If there are no questions, display "Add Questions" and stop the quiz.
5. Otherwise, calculate the maximum possible score by adding the points of all questions.

## Step 3: Randomize Questions
1. Create a copy of the original question list.
2. Shuffle the copied list using `random.shuffle()`.
3. Present the questions in the shuffled order.

## Step 4: Display and Validate Answers
For each question in the shuffled list:

1. Display the question text.
2. Display its difficulty level and point value.
3. Display all available options.
4. Ask the user to enter an answer.
5. Convert the answer to lowercase and remove surrounding whitespace.
6. If the answer is not `a`, `b`, `c`, or `d`, display an error message and ask again.
7. Compare the validated answer with the correct answer key.

## Step 5: Calculate the Score
1. If the answer is correct:
   - Increase `correct` by 1.
   - Add the question's points to `score`.
2. Otherwise:
   - Increase `incorrect` by 1.
3. Store the user's answer and its correctness status in the `responses` list.

## Step 6: Handle Keyboard Interruption
1. Monitor the quiz for a `KeyboardInterrupt`, such as when the user presses Ctrl+C.
2. If an interruption occurs:
   - Set `interrupted` to `True`.
   - Display a termination message.
3. Display the quiz status.
4. If the quiz was interrupted, show the number of questions answered, correct answers, incorrect answers, and points earned.

## Step 7: Display Final Results
If the quiz finishes normally:

1. Display the number of correct answers.
2. Display the number of incorrect answers.
3. Display the points earned and maximum possible points.
4. Calculate the weighted percentage:

   **Weighted Percentage = (Points Earned / Maximum Possible Points) × 100**

5. If the percentage is at least 70%, display "Passed".
6. Otherwise, display "Failed".

## Step 8: Review Missed Questions
1. Examine each recorded response.
2. If the answer was incorrect:
   - Display the question.
   - Display its options.
   - Show the user's answer.
   - Show the correct answer.
   - Display the difficulty, point value, and hint.
3. If no questions were missed and the quiz was completed, display "No Missed Questions".

## Step 9: Display Unanswered Questions
If the quiz was interrupted:

1. Identify questions that were not answered.
2. Display each unanswered question and its options.
3. Display "Not Answered" as the user's answer.
4. Display the correct answer, difficulty, point value, and hint.

## Step 10: End
Terminate the quiz after displaying the applicable results and question reviews.
