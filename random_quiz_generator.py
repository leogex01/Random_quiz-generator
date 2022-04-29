""" Random Quiz Generator - Creates quizes
with questions and answers in random order"""

import random

from quiz_data import capitals
from quiz_data import elements
import re


class Quest_gen:
    def __init__(self, subject, number_of_tests, number_of_questions):

        self.subject = subject
        self.number_of_tests = num_of_tests
        self.number_of_questions = num_of_quests

        # self.format = format

        # get number of questions, subject, and form
        # if format == 'txt':
        # Generate quiz text files.
        for quizNum in range(num_of_tests):
            # Create the quiz and answer key files.
            try:
                quizFile = open('%s_quiz%s.txt' % (subject, quizNum + 1), 'w')
            except FileNotFoundError:
                print("File not open")
                raise
            answerKeyFile = open('%s_quiz_answers%s.txt' % (subject, quizNum + 1), 'w')
            # Write out headers
            quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
            quizFile.write((' ' * 20) + '%s Quiz (Form %s)' % (subject, quizNum + 1))
            quizFile.write('\n\n')

            # Shuffle the order of the questions.
            # Topic is either capitals or elements
            if subject == 'cap':
                topic = list(capitals.keys())  # get all questions in a list
                random.shuffle(topic)
                list_title = capitals
            else:
                topic = list(elements.keys())
                random.shuffle(topic)
                list_title = elements

        # Loop through dictionary, making required number of question for each.
        # def dict_loop(num, subject)
        for questionNum in range(num_of_quests):
            # Get right and wrong answers.
            correctAnswer = list_title[topic[questionNum]]  # ex. capitals[capital.keys]
            wrongAnswers = list(list_title.values())  # get a complete list of answers
            del wrongAnswers[wrongAnswers.index(correctAnswer)]  # remove the right answer
            wrongAnswers = random.sample(wrongAnswers, 3)  # pick 3 random ones
            answerOptions = wrongAnswers + [correctAnswer]
            random.shuffle(answerOptions)  # randomize the order of the answers

            # Write the question and answer options to the quiz file.
            quizFile.write('%s. What is the capital of %s?\n' % (questionNum + 1, topic[questionNum]))
            for i in range(4):
                quizFile.write('    %s. %s\n' % ('ABCD'[i], answerOptions[i]))
                quizFile.write('\n')

            # Write out the answer key to a file.
            answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))
        quizFile.close()
        answerKeyFile.close()


if __name__ == "__main__":
    title = input("Please enter a name for the test/quiz: ")

    subject = input("Please enter 'atomic' for elements or 'cap' state capitals: ")
    while subject != 'atomic' and subject != 'cap':
        subject = input("Please enter 'atomic' for elements or 'cap' state capitals.")
        if subject == 'atomic' or subject == 'cap':
            break
    while True:

        try:
            num_of_tests = int(input("Please enter number of tests:"))
        except ValueError:
            print("Not an integer! Try again.")
            continue
        else:
            break


    while True:
        try:
            num_of_quests = int(input("Please enter number of questions: "))
        except ValueError:
            print("Not an integer! Try again.")
            continue
        else:
            break
    title = Quest_gen(subject, num_of_tests, num_of_quests)
    # TODO
    # form = input("Please enter format: 'txt' for printable quizzes or 'quiz' for self-check quiz. ")
