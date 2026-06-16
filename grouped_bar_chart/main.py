import matplotlib.pyplot as plt
import numpy as np

questions = ['question_1', 'question_2', 'question_3']
positions = np.arange(len(questions))

yes_answers = np.array([500, 240, 726])
no_answers = np.array([432, 618, 101])
answers = np.array([yes_answers, no_answers])

width = 0.3

# Iterate over the indices of the correct array
for i in range(len(answers)):
	# Create bars for each category with the correct arguments
    plt.bar(positions + width * i, answers[i], width)
  
plt.xticks(positions + width * (len(answers) - 1) / 2, questions)

plt.show()