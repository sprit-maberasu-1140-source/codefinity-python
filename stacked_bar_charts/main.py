import matplotlib.pyplot as plt
import numpy as np
questions = ['question_1', 'question_2', 'question_3']
yes_answers = np.array([500, 240, 726])
no_answers = np.array([432, 618, 101])
# Create the lower bars
plt.bar(questions, yes_answers)
# Create the upper bars
plt.bar(questions, no_answers, bottom=yes_answers)
plt.show()