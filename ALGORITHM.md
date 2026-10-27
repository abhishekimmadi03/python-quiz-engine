# Algorithm and Pseudocode — Python Quiz Engine

## Algorithm

1. Initialize the correct-answer count, incorrect-answer count, response list, and interruption flag.
2. Store the quiz questions in a list. Each question contains the question text, four choices, the correct choice key, and a hint.
3. Count the questions in the question bank.
4. If the question bank is empty, display a message and do not start scoring.
5. Otherwise, visit the questions in order:
   - Display the question and its choices.
   - Ask the user for an answer.
   - Remove surrounding whitespace and convert the answer to lowercase.
   - While the answer is not one of `a`, `b`, `c`, or `d`, display an invalid-input message and ask again.
   - Compare the valid answer with the correct answer key.
   - Increase the correct or incorrect counter accordingly.
   - Store the user's answer and whether it was correct.
6. If the user interrupts the quiz with `Ctrl+C`, set the interruption flag and display a termination message.
7. Display the quiz status and answer counts.
8. If the quiz completed normally, calculate the percentage and display the score and pass/fail result.
9. Review stored responses and display each missed question, the user's answer, the correct answer, and the hint.
10. If interrupted, list questions that were not answered.

## Pseudocode

```text
START

SET correct = 0
SET incorrect = 0
SET pass_percent = 70
SET responses = empty list
SET interrupted = false
LOAD questions
SET total = number of questions

IF total equals 0
    DISPLAY "Add Questions."
ELSE
    TRY
        FOR each question in questions, in order
            DISPLAY question text
            DISPLAY all choices
            INPUT answer
            CONVERT answer to lowercase and trim surrounding whitespace

            WHILE answer is not a, b, c, or d
                DISPLAY "Invalid answer"
                INPUT answer again
                NORMALIZE answer
            END WHILE

            COMPARE answer with the question's answer key
            IF answer is correct
                INCREMENT correct
                SET status = true
            ELSE
                INCREMENT incorrect
                SET status = false
            END IF

            APPEND answer and status to responses
        END FOR
    CATCH KeyboardInterrupt
        SET interrupted = true
        DISPLAY termination message
    END TRY

    DISPLAY summary

    IF interrupted is false
        SET percentage = (correct / total) * 100
        DISPLAY score and percentage
        IF percentage >= pass_percent
            DISPLAY pass result
        ELSE
            DISPLAY fail result
        END IF
    ELSE
        DISPLAY incomplete result
    END IF

    FOR each recorded response, in order
        IF response status is false
            DISPLAY missed question, user's answer, correct answer, and hint
        END IF
    END FOR

    IF interrupted is true
        DISPLAY questions from index equal to number of responses through the final question as unanswered
    END IF
END IF

END
```
