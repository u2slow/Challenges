import random

unsort_list = []

for i in range(10):
    unsort_list.append(random.randint(0,100))

print(unsort_list)

for n in range(len(unsort_list)):

    for i in range(len(unsort_list)):
        if i + 1 + n >= len(unsort_list):
            break
        
        if unsort_list[i] > unsort_list[i+1]:
            mem = unsort_list[i]
            unsort_list[i] = unsort_list[i+1]
            unsort_list[i+1] = mem

print(unsort_list)