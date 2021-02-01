curriculum = {}
with open("task_6.txt", encoding="utf-8") as f_obj:
    for line in f_obj:
        subj, hours = line.split(':')
        subj_hours = ("".join([i for i in hours if i == ' ' or '9' >= i >= '0']).split())
        sum_hours = sum(map(int, subj_hours))
        # subj_hours = sum(map(int, "".join([i for i in hours if i == ' ' or '9' >= i >= '0']).split()))
        print(sum_hours)
        curriculum[subj] = sum_hours
print(f"{curriculum}")