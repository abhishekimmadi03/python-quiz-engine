correct = 0
incorrect = 0
pass_percent=70
responses=[]
interrupted=False
questions = [
    {
           "question": "1. Which Python function returns the number of items in a list?",
           "options": {
               "a": "count()",
               "b": "size()",
               "c": "len()",
               "d": "length()"
           },
           "answer": "c",
           "hint": "This function can tell you how many elements a list contains."
       },
       {
           "question": "2. Which data structure stores information as key-value pairs?",
           "options": {
               "a": "List",
               "b": "Dictionary",
               "c": "Tuple",
               "d": "Set"
           },
           "answer": "b",
           "hint": "Think of a structure where you access a value using a key."
       },
       {
           "question": "3. Which keyword is used to define a function in Python?",
           "options": {
               "a": "function",
               "b": "define",
               "c": "fun",
               "d": "def"
           },
           "answer": "d",
           "hint": "It is a three-letter keyword used before a function name."
       },
       {
           "question": "4. What is the output of this code: print(2 ** 3)?",
           "options": {
               "a": "6",
               "b": "8",
               "c": "9",
               "d": "5"
           },
           "answer": "b",
           "hint": "The double asterisk is Python's exponentiation operator."
       },
       {
           "question": "5. Which operator checks whether two values are equal?",
           "options": {
               "a": "=",
               "b": "!=",
               "c": "==",
               "d": ">="
           },
           "answer": "c",
           "hint": "It uses two equal signs, unlike the operator used for assignment."
       }
]
total=len(questions)
if total==0:
    print("Add Questions.")
else:
    try:
        for j in range(total):
            question = questions[j]
            print(question["question"])
            for choice,option in question["options"].items():
                print(choice +")"+ option)
            answer = input("Enter your answer (a/b/c/d): ")
            user_answer=answer.lower().strip()
            while user_answer not in ['a','b','c','d']:
                print("Invalid answer")
                answer = input("Enter your answer (a/b/c/d): ")
                user_answer=answer.lower().strip()
            status=user_answer == question["answer"]
            if status==True:
                correct += 1
            else:
                incorrect += 1
        
            responses.append({
            "user_answer": user_answer,"status":status
            })

    except KeyboardInterrupt:
        interrupted=True
        print("\nQuiz Terminated By User")
    print("\n---- Quiz Status------")
    if interrupted:
     print("Quiz Status: Incomplete")
     print("Questions Answered:",len(responses),"/",total)
     print("Correct Answers: ",correct)
     print("Wrong Answers: ",incorrect)
    else:   
        print("\nQuiz Completed!")
        print("No.of Correct Answers:",correct)
        print("No.of Wrong Answers:",incorrect)
        print("Your Score is"+str(correct)+"/"+str(total))
        percentage=(correct/total)*100
        print(f"Your Accuracy is {percentage:.2f}%")
        if percentage >= pass_percent:
            print("Passed")
        else:
            print("Failed Try Again Later")
    print("--- Your Missed Questions ---")
    missed=False
    for i in range(len(responses)):
        if responses[i]['status'] == False:
            missed=True
            print("Question: "+questions[i]['question'])
            for choice,option in questions[i]["options"].items():
                print(choice +")"+ option)
            print("Your Answer: "+responses[i]['user_answer'])
            print("Correct Answer: "+ questions[i]['answer'])
            print("Hint: "+ questions[i]["hint"])
    if not missed and not interrupted:
        print("No Missed Questions")
    if interrupted:
        print("\n Unanswered Questions")
        for i in range(len(responses),total):
            print(questions[i]["question"])
            for choice,option in questions[i]["options"].items():
                print(choice,")"," ",option)
            print("Your Answer: Not Answered")
            print("Correct Answer: "+questions[i]["answer"])
            print("Hint:"+questions[i]["hint"])
