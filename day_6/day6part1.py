with open ('day6data.txt') as data:
    answers = data.read()

total = 0
group_answers = []
group_answers = answers.split('\n\n')

for answers in group_answers:
    total += len(set(answers.replace("\n","")))

print(total)
