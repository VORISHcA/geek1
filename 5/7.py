import json
profit = {}
pr = {}
prof = 0
prof_aver = 0
i = 0
with open('file8.txt', 'r') as file:
    for line in file:
        name, firm, earning, damage = line.split()
        profit[name] = int(earning) - int(damage)
        if profit.setdefault(name) >= 0:
            prof = prof + profit.setdefault(name)
            i += 1
    if i != 0:
        prof_aver = prof / i
    pr = {'average_profit': round(prof_aver)}
    profit.update(pr)
with open('file8.json', 'w') as write_js:
    json.dump(profit, write_js)
    js_str = json.dumps(profit)
    print(js_str)