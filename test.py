import random
import csv     
def generate_rebuy_num(count=(10,2000),avg=(0,500), std_dev=(0,50)):# 設定重買次數的範圍和平均值、標準差
   avg= random.uniform(*avg)
   std_dev = random.uniform(*std_dev)
   R = []
   for _ in range(random.randint(*count)):
    rate =(random.gauss(avg, std_dev))  # 使用高斯分布生成重買次數
    rate = round(max(10, min(2000, rate)))  # 確保重買次數在10到2000之間
    R.append(rate)
   return R

def generate_rebuy_frequency(count=(1,50), avg=(0,20), std_dev=(0,5)):# 設定重買率的範圍和平均值、標準差
    avg = random.uniform(*avg)
    std_dev = random.uniform(*std_dev)
    F = []
    for _ in range(random.randint(*count)):
        freq = random.gauss(avg, std_dev)
        freq = round(max(1, min(50, freq)))  # 確保頻率至少為1
        F.append(freq)

    return F

def generate_consumer_value(count=(100, 3000), avg=(0,10000), std_dev=(0,2000)):  # 設定消費者價值的範圍和平均值、標準差
    avg = random.uniform(*avg)
    std_dev = random.uniform(*std_dev)
    M = []
    for _ in range(random.randint(*count)):
        value = random.gauss(avg, std_dev)
        value = round(max(1000, min(3000, value)))  # 消費者價值在1000到3000之間
        M.append(value)

    return M
def write_to_csv(R, F, M, filename='rebuy_data.csv'):
    filed_name=['重買次數', '重買頻率', '消費者價值']
    try:
        with open(filename, mode='w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=filed_name)
            writer.writeheader()
            for r, f, m in zip(R, F, M):
                writer.writerow({'重買次數': r, '重買頻率': f, '消費者價值': m})
        print("✅ 已寫入檔案")
    except Exception as e:
        print("❌ 寫入檔案失敗:", e)
            

            



def main():
    rebuy_num = generate_rebuy_num()
    rebuy_freq= generate_rebuy_frequency()
    consumer_value = generate_consumer_value()
    write_to_csv(rebuy_num, rebuy_freq, consumer_value)

if __name__ == "__main__":
    main()

    