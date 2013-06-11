import random

def monty_hall(num):
    orig_data = range(num)
    right = random.choice(orig_data)

    first_choice = random.choice(orig_data)
    if first_choice == right:
        cur_data = range(num)
        cur_data.remove(right)
        deleted = random.choice(cur_data)
    else:
        cur_data = range(num)
        cur_data.remove(right)
        cur_data.remove(first_choice)
        deleted = random.choice(cur_data)


    cur_data = range(num)
    cur_data.remove(deleted)
    cur_data.remove(first_choice)
    second_choice = random.choice(cur_data)
    return second_choice == right


num = 0
total_exp_num = 10000
for i in xrange(total_exp_num):
    if monty_hall(3):
        num += 1

print float(num) / total_exp_num
