from django.db import models
import datetime
import logging

from test_creator import TestGenerator


logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)




class Teacher:
    def __init__(self):
        print("Welcome! Run create_full_test() to create a test.")


    def create_full_test(self):

        topic = input("What topic would you like to create a test on? ")
        num_possible_answers = int(input("How many possible answers would you like to have? "))
        num_questions = int(input("How many possible answers per question would you like to have? "))

        self.test_creator = TestGenerator(topic, num_possible_answers, num_questions)
        test = self.test_creator.run()
    
        #logging.info(test)
        student_view = self.create_student_view(test, num_questions)
        answers = self.extract_answers(test, num_questions)
        return student_view, answers

    def create_student_view(self, test, num_questions):
        student_view = {1 : ""}
        question_number = 1
        for line in test.split("\n"):
            if not line.startswith("Correct Answer:"):
                student_view[question_number] += line+"\n"
            else:
                
                if question_number < num_questions:
                    question_number+=1
                    student_view[question_number] = ""
        return student_view

    def extract_answers(self, test, num_questions):
        answers = {1 : ""}
        question_number = 1
        for line in test.split("\n"):
            if line.startswith("Correct Answer:"):
                answers[question_number] += line+"\n"

                if question_number < num_questions:
                    question_number+=1
                    answers[question_number] = ""
        return answers

        

if __name__ == "__main__":
    teacher = Teacher()
    student_view, answers = teacher.create_full_test()
    print(student_view)
    print(answers)

from teacher import Teacher
/ .
class Exam(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    passing_score = models.IntegerField(default=70)
    tech_stack = models.CharField(max_length=100)
        
    def __str__(self):
        return self.name
    
    def __init__(self, student_view, answers, store_test=False, topic=""):
        self.student_view = student_view
        self.answers = answers

        if store_test:
            self.store_test(topic)

    
    def take(self):
        answers = {}
        for question, question_view in self.student_view.items():
            print(question_view)
            answer = input("Enter your answer: ")
            answers[question] = answer
        return answers

    def grade(self, answers):
        correct_answers = 0
        for question, answer in answers.items():
            if answer.upper() == self.answers[question].upper()[16]:
                correct_answers+=1
        grade = 100 * correct_answers / len(answers)

        if grade < 60:
            passed = "Not passed!"
        else:
            passed = "Passed!"
        return f"{correct_answers} out of {len(answers)} correct! You achieved: {grade} % : {passed}"


    def store_test(self, topic):
        with open(f'Test_{topic}_{datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.txt', "w") as file:
            for question, question_view in self.student_view.items():
                file.write(question_view)
                file.write("\n")
                file.write(self.answers[question])
                file.write("\n")


""" if __name__ == "__main__":
    teacher = Teacher()
    student_view, answers = teacher.create_full_test()

    exam = Exam(student_view, answers, store_test=True, topic=teacher.test_creator.topic)
    student_answers = exam.take()
    print(student_answers)
    grade = exam.grade(student_answers)
    print(grade) """


# Create your models here.
class PracticeExam(Exam):
    number_of_questions = models.IntegerField(default=10)
    
    def __str__(self):  
        return f"{self.name} - {self.number_of_questions} questions"
