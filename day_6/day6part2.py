with open ('day6data.txt') as data:
    answers = data.read()

total = 0
group_answers = []
group_answers = answers.split('\n\n')



for answers in group_answers:
    people = answers.count("\n")+1
    # freq['people'] = answers.count("\n")+1
    freq = {}
    for ltr in answers.replace("\n",""):
        if ltr in freq:
            freq[ltr] += 1
        else:
            freq[ltr] = 1

    for key,value in freq.items():
        if freq[key] == people:
            total += 1
    # total += len(set(answers.replace("\n","")))

print(total)