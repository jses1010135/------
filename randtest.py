import random as r
import time as t
r.seed(t.time())
#r.gauss(mu,sigma)
#data=[[int(r.gauss(mu=65,sxdigma=15)) for _ in range(4)] for _ in range(1000)]
def random():
    rand=[r.randint(1, 6) for _ in range(10000)]
    return rand

def random2():
    rand1=random()
    count = {i:0  for i in range(1,7)}
    for rr in rand1:
        count[rr]+=1
    print(count)
    return count


def random3():
    students = []
    for i in range(1000):
        name = f"Student_{i+1}"
        chinese = r.randint(40, 90)
        english = r.randint(40, 90)
        math = r.randint(40, 90)
        physics = r.randint(40, 90)
        students.append([name, chinese, english, math, physics])
    return students
def random4():
    students = random3()
    result = []
    for student in students:
        name, chinese, english, math, physics = student
        total = sum([chinese,english,math,physics]) 
        avg = total / 4
        result.append([name, total, avg])
    return result
def random5():
    result = random4()
    total_scores = [item[1] for item in result]
    w_avg_scores = [item[2] for item in result]

    stats = {
        'total': {
            'avg': sum(total_scores) / len(total_scores),
            'var': sum((x - (sum(total_scores) / len(total_scores))) ** 2 for x in total_scores) / len(total_scores),
            'stddev': (sum((x - (sum(total_scores) / len(total_scores))) ** 2 for x in total_scores) / len(total_scores)) ** 0.5
        },
        'w_avg': {
            'avg': sum(w_avg_scores) / len(w_avg_scores),
            'var': sum((x - (sum(w_avg_scores) / len(w_avg_scores))) ** 2 for x in w_avg_scores) / len(w_avg_scores),
            'stddev': (sum((x - (sum(w_avg_scores) / len(w_avg_scores))) ** 2 for x in w_avg_scores) / len(w_avg_scores)) ** 0.5
        }
    }
    return stats

if __name__ == "__main__":
    stats = random5()
    students = random4()

    print(f"總分:{students}")
    print(f"  平均值：{stats['total']['avg']:.2f}")
    print(f"  變異數：{stats['total']['var']:.2f}")
    print(f"  標準差：{stats['total']['stddev']:.2f}")



