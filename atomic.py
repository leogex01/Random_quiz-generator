from quiz_data import elements
from random_quiz_generator import *


def elements():
    atoms = list(elements.keys())  # get all questions in a list
    random.shuffle(atoms)  # randomize the order of the states

    # Loop through dictionary, making required number of question for each.
    # def dict_loop(num, subject)
    for questionNum in range(num_of_quests):
        # Get right and wrong answers.
        correctAnswer = elements[atoms[questionNum]]
        wrongAnswers = list(elements.values())  # get a complete list of answers
        del wrongAnswers[wrongAnswers.index(correctAnswer)]  # remove the right answer
        wrongAnswers = random.sample(wrongAnswers, 3)  # pick 3 random ones
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)  # randomize the order of the answers

        # Write the question and answer options to the quiz file.
        quizFile.write('%s. What is the weight of %s?\n' % (questionNum + 1, atoms[questionNum]))
        for i in range(4):
            quizFile.write('    %s. %s\n' % ('ABCD'[i], answerOptions[i]))
            quizFile.write('\n')

        # Write out the answer key to a file.
        answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))
    quizFile.close()
    answerKeyFile.close()
