def generte_buy_count(count=(10,2000), min_mean=0, max_mean=500, min_dev=0, max_dev=50): #設定買入次數的範圍和平均值、標準差
    import random
    mean = random.uniform(min_mean, max_mean)
    std_dev = random.uniform(min_dev, max_dev)
    
    buy_counts = []
    for _ in range(count):
        buy_count = random.gauss(mean, std_dev)
        buy_count = round(max(0, buy_count))
        buy_counts.append(buy_count)
    
    return buy_counts
    
def generte_rate(count=(0,50), min_mean=0.1, max_mean=20, min_dev=0.05, max_dev=5):
    import random
    mean = random.uniform(min_mean, max_mean)
    std_dev = random.uniform(min_dev, max_dev)
    
    rates = []
    for _ in range(count):
        rate = random.gauss(mean, std_dev)
        rate = round(max(0, min(1, rate)), 2)
        rates.append(rate)
    
    return rates