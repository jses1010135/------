import random
import csv
import os     
def generate_rebuy_num(count=(10,2000),avg=(0,500), std_dev=(0,50)):# 設定重買次數的範圍和平均值、標準差
   avg= random.uniform(*avg)# 隨機生成平均值
   # 隨機生成標準差
   std_dev = random.uniform(*std_dev)
   R = []
   for _ in range(random.randint(*count)):# 隨機生成重買次數的數量
    # 使用高斯分布生成重買次數
    rate =(random.gauss(avg, std_dev))  # 使用高斯分布生成重買次數
    rate = round(max(10, min(2000, rate)),2)  # 確保重買次數在10到2000之間
    R.append(rate)
   return R

def generate_rebuy_frequency(count=(1,50), avg=(0,20), std_dev=(0,5)):# 設定重買率的範圍和平均值、標準差
    avg = random.uniform(*avg)
    std_dev = random.uniform(*std_dev)
    F = []
    for _ in range(random.randint(*count)):# 隨機生成重買頻率的數量
        # 使用高斯分布生成重買頻率
        freq = random.gauss(avg, std_dev)
        freq = round(max(1, min(50, freq)),2)  # 確保重買頻率至少為1~50
        F.append(freq)

    return F

def generate_consumer_value(count=(100, 3000), avg=(0,10000), std_dev=(0,2000)):  # 設定消費者價值的範圍和平均值、標準差
    avg = random.uniform(*avg) #隨機生成平均值
    std_dev = random.uniform(*std_dev) #隨機生成標準差
    M = []
    for _ in range(random.randint(*count)):# 隨機生成消費者價值的數量
        # 使用高斯分布生成消費者價值
        value = random.gauss(avg, std_dev)
        value = round(max(1000, min(3000, value)),2)  # 消費者價值在1000到3000之間
        M.append(value)

    return M
def write_to_csv(R, F, M, filename='rebuy_data.csv'):
    filed_name=['重買次數', '重買頻率', '消費者價值']
    try:
        directory = os.path.dirname(filename)  # 獲取檔案所在目錄
        if directory and not os.path.exists(directory):  # 如果目錄不存在，則創建它
            os.makedirs(directory)
            print(f"✅ 已創建目錄:", {directory})
        with open(filename, mode='w', newline='', encoding='utf-8') as csvfile:#with open(檔案名稱, 模式='寫入', newline='', encoding='UTF-8編碼') 在Python中打開一個CSV檔案進行寫入操作
            # 使用 DictWriter 寫入 CSV 檔案
            writer = csv.DictWriter(csvfile, fieldnames=filed_name)
            writer.writeheader()
            
            
            
            min_length = min(len(R), len(F), len(M))# 獲取最小長度，確保每個列表的長度相同
            
            for i in range(min_length):# 確保每個列表的長度相同
                writer.writerow({# 將每一行的數據寫入 CSV 檔案
                    '重買次數': R[i],
                    '重買頻率': F[i], 
                    '消費者價值': M[i]
                })
        print("✅ 已寫入檔案")
    except Exception as e:
        print("❌ 寫入檔案失敗:", e)

def read_from_csv(filename='rebuy_data.csv'):
    """從 CSV 檔案讀取數據"""
    data = []
    try:
        with open(filename, mode='r', newline='', encoding='utf-8') as csvfile:#as csvfile: 打開CSV檔案進行讀取操作
            reader = csv.DictReader(csvfile)# # 使用 DictReader 讀取 CSV 檔案
            for row in reader:# 遍歷每個row
                # 將數據轉換為 float
                row['重買次數'] = float(row['重買次數'])
                row['重買頻率'] = float(row['重買頻率'])
                row['消費者價值'] = float(row['消費者價值'])
                data.append(row)
                print(f"讀取資料: 重買次數={row['重買次數']}, "
                      f"重買頻率={row['重買頻率']}, "
                      f"消費者價值={row['消費者價值']}")
            return data
    except Exception as e:
        print("❌ 讀取檔案失敗:", e)
        directory = os.path.dirname(filename)  # 獲取檔案所在目錄
        if directory and not os.path.exists(directory):  # 如果目錄不存在，則創建它
            os.makedirs(directory)
            print(f"✅ 已創建目錄:", {directory})
        return data
            

            



def main():
    rebuy_num = generate_rebuy_num()
    rebuy_freq = generate_rebuy_frequency()
    consumer_value = generate_consumer_value()
    write_to_csv(rebuy_num, rebuy_freq, consumer_value)
    data = read_from_csv()
    if not data:
        print("❌ 沒有讀取到任何數據")
   

if __name__ == "__main__":
    main()

