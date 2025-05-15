# Python 基礎程式設計
## 第 18 週：專題製作與發表

### 課程目標

本週為課程的最後一週，將專注於專題製作與發表。學生將結合之前所學知識，完成一個小型 Python 專案，並在課堂上進行展示。同時，我們會對整個學期所學內容進行回顧與總結，並解答學生的問題。

### 1. 專題製作指南

#### 1.1 專題目標與要求

專題目的是應用課程中所學的 Python 知識，解決實際問題或創建有用的應用程式。

**基本要求**：
- 必須使用 Python 作為主要程式語言
- 必須應用至少 5 個我們在課程中學過的主題/概念
- 程式碼必須有適當的註解和文件說明
- 必須包含使用介面（命令列或簡單的 GUI）
- 專題展示時間為每組 10-15 分鐘

**專題主題建議**：以下是一些可能的專題方向，但學生可以提出自己的想法：
1. 數據分析與視覺化應用
2. 網路爬蟲與資料處理
3. 檔案管理與自動化工具
4. 簡易的遊戲或互動式應用
5. 資料庫應用（如學生成績管理系統）
6. 文字處理工具（如文字統計、格式轉換等）

#### 1.2 專題開發流程

1. **規劃階段**：
   - 明確定義專題目標
   - 列出需要實現的功能
   - 設計程式架構與模組

2. **開發階段**：
   - 根據規劃分步驟實現功能
   - 定期測試已完成的部分
   - 解決遇到的問題

3. **測試與完善階段**：
   - 全面測試程式的各項功能
   - 修復發現的錯誤
   - 優化使用者體驗

4. **展示準備**：
   - 準備演示文稿和演示流程
   - 練習專題講解
   - 預期可能的問題與解答

#### 1.3 專題文件要求

每個專題應包含以下文件：

1. **README.md**：包含專題概述、功能說明、使用方法、安裝指南等
2. **需求文件**：requirements.txt，列出專題所需的第三方套件
3. **源代碼**：所有 Python 檔案，含適當註解
4. **簡報文件**：用於專題展示的簡報（如 PowerPoint）

### 2. 專題範例

以下提供幾個專題範例，學生可以參考或擴展這些範例：

#### 2.1 個人記帳系統

這是一個基於命令列的個人記帳系統，可以記錄收入和支出、查詢歷史紀錄、生成報表等。

```python
import os
import json
import datetime
import matplotlib.pyplot as plt
from collections import defaultdict

class ExpenseTracker:
    def __init__(self, data_file="expenses.json"):
        self.data_file = data_file
        self.records = self.load_data()
    
    def load_data(self):
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                print("資料檔案損壞，建立新的資料檔。")
                return {"income": [], "expense": []}
        else:
            return {"income": [], "expense": []}
    
    def save_data(self):
        with open(self.data_file, 'w', encoding='utf-8') as f:
            json.dump(self.records, f, ensure_ascii=False, indent=2)
    
    def add_record(self, record_type, amount, category, description, date=None):
        if date is None:
            date = datetime.datetime.now().strftime("%Y-%m-%d")
        
        record = {
            "date": date,
            "amount": amount,
            "category": category,
            "description": description
        }
        
        self.records[record_type].append(record)
        self.save_data()
        print(f"已新增{record_type}紀錄：{amount} 元 - {description}")
    
    def view_records(self, record_type, start_date=None, end_date=None):
        if record_type not in ["income", "expense", "all"]:
            print("錯誤：記錄類型必須是 'income', 'expense' 或 'all'")
            return
        
        records_to_show = []
        if record_type == "all" or record_type == "income":
            for record in self.records["income"]:
                if self._in_date_range(record["date"], start_date, end_date):
                    records_to_show.append({"type": "收入", **record})
        
        if record_type == "all" or record_type == "expense":
            for record in self.records["expense"]:
                if self._in_date_range(record["date"], start_date, end_date):
                    records_to_show.append({"type": "支出", **record})
        
        # 依日期排序
        records_to_show.sort(key=lambda x: x["date"])
        
        if not records_to_show:
            print("沒有符合條件的記錄")
            return
        
        print("\n{:<10} {:<8} {:<10} {:<12} {:<20}".format("日期", "類型", "金額", "分類", "描述"))
        print("-" * 60)
        
        for record in records_to_show:
            print("{:<10} {:<8} {:<10.2f} {:<12} {:<20}".format(
                record["date"], 
                record["type"], 
                record["amount"], 
                record["category"], 
                record["description"]
            ))
    
    def _in_date_range(self, date_str, start_date, end_date):
        if start_date is None and end_date is None:
            return True
        
        date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        
        if start_date is not None:
            start = datetime.datetime.strptime(start_date, "%Y-%m-%d").date()
            if date < start:
                return False
        
        if end_date is not None:
            end = datetime.datetime.strptime(end_date, "%Y-%m-%d").date()
            if date > end:
                return False
        
        return True
    
    def generate_monthly_report(self, year, month):
        # 獲取指定月份的資料
        start_date = f"{year}-{month:02d}-01"
        
        # 計算月末日期
        if month == 12:
            next_year = year + 1
            next_month = 1
        else:
            next_year = year
            next_month = month + 1
        
        end_date = (datetime.datetime(next_year, next_month, 1) - datetime.timedelta(days=1)).strftime("%Y-%m-%d")
        
        # 統計資料
        total_income = 0
        total_expense = 0
        income_by_category = defaultdict(float)
        expense_by_category = defaultdict(float)
        
        for record in self.records["income"]:
            if self._in_date_range(record["date"], start_date, end_date):
                total_income += record["amount"]
                income_by_category[record["category"]] += record["amount"]
        
        for record in self.records["expense"]:
            if self._in_date_range(record["date"], start_date, end_date):
                total_expense += record["amount"]
                expense_by_category[record["category"]] += record["amount"]
        
        # 顯示報表
        print(f"\n===== {year}年{month}月收支報表 =====")
        print(f"總收入: {total_income:.2f} 元")
        print(f"總支出: {total_expense:.2f} 元")
        print(f"淨收入: {total_income - total_expense:.2f} 元")
        
        print("\n收入類別統計:")
        for category, amount in income_by_category.items():
            print(f"  {category}: {amount:.2f} 元 ({amount/total_income*100:.1f}%)")
        
        print("\n支出類別統計:")
        for category, amount in expense_by_category.items():
            print(f"  {category}: {amount:.2f} 元 ({amount/total_expense*100:.1f}%)")
        
        # 繪製支出圓餅圖
        self._plot_expense_pie_chart(expense_by_category, year, month)
    
    def _plot_expense_pie_chart(self, expense_by_category, year, month):
        # 如果沒有支出資料，則不繪圖
        if not expense_by_category:
            print("沒有支出資料可供繪圖")
            return
        
        labels = list(expense_by_category.keys())
        values = list(expense_by_category.values())
        
        plt.figure(figsize=(10, 6))
        plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)
        plt.axis('equal')  # 使圓餅圖為正圓形
        plt.title(f'{year}年{month}月支出分佈')
        
        # 儲存圖片
        output_file = f"expense_report_{year}_{month:02d}.png"
        plt.savefig(output_file)
        plt.close()
        
        print(f"\n支出分佈圖已儲存為：{output_file}")

def main():
    tracker = ExpenseTracker()
    
    while True:
        print("\n===== 個人記帳系統 =====")
        print("1. 添加收入")
        print("2. 添加支出")
        print("3. 查看所有記錄")
        print("4. 查看收入記錄")
        print("5. 查看支出記錄")
        print("6. 生成月度報表")
        print("0. 退出程式")
        
        choice = input("\n請選擇操作: ")
        
        if choice == "1":
            try:
                amount = float(input("收入金額: "))
                category = input("收入類別 (例如: 薪資、獎金、投資): ")
                description = input("收入描述: ")
                date = input("日期 (YYYY-MM-DD，留空為今天): ")
                
                if date.strip() == "":
                    tracker.add_record("income", amount, category, description)
                else:
                    tracker.add_record("income", amount, category, description, date)
            except ValueError:
                print("錯誤：請輸入有效的金額")
        
        elif choice == "2":
            try:
                amount = float(input("支出金額: "))
                category = input("支出類別 (例如: 食物、交通、娛樂): ")
                description = input("支出描述: ")
                date = input("日期 (YYYY-MM-DD，留空為今天): ")
                
                if date.strip() == "":
                    tracker.add_record("expense", amount, category, description)
                else:
                    tracker.add_record("expense", amount, category, description, date)
            except ValueError:
                print("錯誤：請輸入有效的金額")
        
        elif choice in ["3", "4", "5"]:
            record_type = {"3": "all", "4": "income", "5": "expense"}[choice]
            start_date = input("開始日期 (YYYY-MM-DD，留空表示不限): ")
            end_date = input("結束日期 (YYYY-MM-DD，留空表示不限): ")
            
            if start_date.strip() == "":
                start_date = None
            if end_date.strip() == "":
                end_date = None
                
            tracker.view_records(record_type, start_date, end_date)
        
        elif choice == "6":
            try:
                year = int(input("年份 (YYYY): "))
                month = int(input("月份 (1-12): "))
                
                if 1 <= month <= 12:
                    tracker.generate_monthly_report(year, month)
                else:
                    print("錯誤：月份必須在 1 到 12 之間")
            except ValueError:
                print("錯誤：請輸入有效的年份和月份")
        
        elif choice == "0":
            print("感謝使用本系統，再見！")
            break
        
        else:
            print("無效的選擇，請重新輸入")

if __name__ == "__main__":
    main()
```

#### 2.2 簡易網路爬蟲與天氣預報

這個專題使用 requests 和 BeautifulSoup 爬取天氣資訊，並提供命令列介面查詢各地天氣預報。

```python
import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import os
import json
from datetime import datetime
import time

class WeatherApp:
    def __init__(self):
        self.cache_file = "weather_cache.json"
        self.cache_duration = 3600  # 1小時的快取時間（秒）
        self.cache = self.load_cache()
        
        # 城市代碼對照表（示例）
        self.city_codes = {
            "台北": "Taipei",
            "新北": "NewTaipei",
            "桃園": "Taoyuan",
            "台中": "Taichung",
            "高雄": "Kaohsiung",
            "基隆": "Keelung",
            "台南": "Tainan",
            "新竹市": "HsinchuCity",
            "新竹縣": "HsinchuCounty",
            "苗栗": "MiaoliCounty",
            "彰化": "ChanghuaCounty",
            "南投": "NantouCounty",
            "雲林": "YunlinCounty",
            "嘉義市": "ChiayiCity",
            "嘉義縣": "ChiayiCounty",
            "屏東": "PingtungCounty",
            "宜蘭": "YilanCounty",
            "花蓮": "HualienCounty",
            "台東": "TaitungCounty",
            "澎湖": "PenghuCounty",
            "金門": "KinmenCounty",
            "連江": "LienchiangCounty"
        }
    
    def load_cache(self):
        if os.path.exists(self.cache_file):
            try:
                with open(self.cache_file, 'r', encoding='utf-8') as f:
                    cache = json.load(f)
                return cache
            except:
                return {}
        return {}
    
    def save_cache(self):
        with open(self.cache_file, 'w', encoding='utf-8') as f:
            json.dump(self.cache, f, ensure_ascii=False, indent=2)
    
    def get_weather(self, city):
        # 檢查是否有快取且是否過期
        now = time.time()
        if city in self.cache and now - self.cache[city]["timestamp"] < self.cache_duration:
            print(f"使用快取的資料（{city}）")
            return self.cache[city]["data"]
        
        # 沒有快取或快取過期，重新獲取資料
        print(f"獲取最新天氣資料（{city}）...")
        
        # 這裡用一個模擬的資料，實際應用中應該使用真實的 API 或網頁爬蟲
        # 例如：使用 OpenWeatherMap API 或中央氣象局資料
        
        # 模擬的請求過程（實際專案應該從真實 API 獲取資料）
        if city in self.city_codes:
            city_code = self.city_codes[city]
            # 這裡只是示例，實際專案應使用真實的 URL
            url = f"https://example.com/weather/{city_code}"
            
            # 模擬從 API 獲取資料
            # response = requests.get(url)
            # data = response.json()
            
            # 以下是模擬的天氣資料，實際應用應替換為實際 API 資料
            weather_data = self._generate_mock_weather_data(city)
            
            # 快取資料
            self.cache[city] = {
                "timestamp": now,
                "data": weather_data
            }
            self.save_cache()
            
            return weather_data
        else:
            return {"error": "不支援的城市"}
    
    def _generate_mock_weather_data(self, city):
        """生成模擬的天氣資料（供演示使用）"""
        import random
        
        today = datetime.now()
        forecast = []
        
        # 生成未來 7 天的天氣預報
        for i in range(7):
            date = (today.replace(hour=0, minute=0, second=0, microsecond=0) + 
                    pd.Timedelta(days=i)).strftime("%Y-%m-%d")
            
            temp_high = random.randint(22, 32)
            temp_low = temp_high - random.randint(3, 8)
            
            weather_types = ["晴天", "多雲", "陰天", "小雨", "大雨", "雷陣雨"]
            weather_weights = [0.3, 0.3, 0.2, 0.1, 0.05, 0.05]  # 權重
            weather = random.choices(weather_types, weights=weather_weights)[0]
            
            humidity = random.randint(50, 90)
            wind_speed = round(random.uniform(1, 15), 1)
            
            forecast.append({
                "date": date,
                "temp_high": temp_high,
                "temp_low": temp_low,
                "weather": weather,
                "humidity": humidity,
                "wind_speed": wind_speed
            })
        
        return {
            "city": city,
            "forecast": forecast
        }
    
    def display_weather(self, city):
        weather_data = self.get_weather(city)
        
        if "error" in weather_data:
            print(weather_data["error"])
            return
        
        print(f"\n===== {city} 七日天氣預報 =====")
        print("{:<12} {:<6} {:<6} {:<8} {:<8} {:<8}".format(
            "日期", "最高溫", "最低溫", "天氣", "濕度", "風速(m/s)"
        ))
        print("-" * 60)
        
        for day in weather_data["forecast"]:
            print("{:<12} {:<6}℃ {:<6}℃ {:<8} {:<8}% {:<8}".format(
                day["date"],
                day["temp_high"],
                day["temp_low"],
                day["weather"],
                day["humidity"],
                day["wind_speed"]
            ))
    
    def plot_temperature_forecast(self, city):
        weather_data = self.get_weather(city)
        
        if "error" in weather_data:
            print(weather_data["error"])
            return
        
        # 準備資料
        dates = [day["date"].split("-")[2] + "日" for day in weather_data["forecast"]]
        temp_high = [day["temp_high"] for day in weather_data["forecast"]]
        temp_low = [day["temp_low"] for day in weather_data["forecast"]]
        
        # 畫圖
        plt.figure(figsize=(10, 6))
        plt.plot(dates, temp_high, 'ro-', label='最高溫')
        plt.plot(dates, temp_low, 'bo-', label='最低溫')
        plt.fill_between(dates, temp_high, temp_low, color='gray', alpha=0.2)
        
        plt.title(f'{city} 七日溫度預報', fontsize=16)
        plt.xlabel('日期', fontsize=12)
        plt.ylabel('溫度 (℃)', fontsize=12)
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.legend()
        
        # 在溫度點上標示數值
        for i in range(len(dates)):
            plt.text(i, temp_high[i] + 0.5, f'{temp_high[i]}℃', ha='center')
            plt.text(i, temp_low[i] - 1, f'{temp_low[i]}℃', ha='center')
        
        plt.tight_layout()
        
        # 儲存圖表
        output_file = f"{city}_temperature_forecast.png"
        plt.savefig(output_file)
        plt.close()
        
        print(f"\n溫度預報圖表已儲存為：{output_file}")
    
    def compare_cities(self, cities):
        if len(cities) < 2:
            print("至少需要兩個城市進行比較")
            return
        
        plt.figure(figsize=(12, 6))
        
        for city in cities:
            weather_data = self.get_weather(city)
            
            if "error" in weather_data:
                print(f"無法獲取 {city} 的天氣資料")
                continue
            
            # 準備資料
            dates = [day["date"].split("-")[2] + "日" for day in weather_data["forecast"]]
            temp_avg = [(day["temp_high"] + day["temp_low"]) / 2 for day in weather_data["forecast"]]
            
            # 畫平均溫度線
            plt.plot(dates, temp_avg, 'o-', label=f'{city} 平均溫度')
        
        plt.title('城市溫度比較', fontsize=16)
        plt.xlabel('日期', fontsize=12)
        plt.ylabel('平均溫度 (℃)', fontsize=12)
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.legend()
        
        plt.tight_layout()
        
        # 儲存圖表
        city_names = '_'.join(cities)
        output_file = f"city_comparison_{city_names}.png"
        plt.savefig(output_file)
        plt.close()
        
        print(f"\n城市溫度比較圖表已儲存為：{output_file}")

def main():
    app = WeatherApp()
    
    while True:
        print("\n===== 天氣預報系統 =====")
        print("1. 查詢城市天氣")
        print("2. 生成溫度預報圖表")
        print("3. 比較多個城市")
        print("4. 顯示支援的城市")
        print("0. 退出程式")
        
        choice = input("\n請選擇操作: ")
        
        if choice == "1":
            city = input("請輸入城市名稱: ")
            app.display_weather(city)
        
        elif choice == "2":
            city = input("請輸入城市名稱: ")
            app.plot_temperature_forecast(city)
        
        elif choice == "3":
            cities_input = input("請輸入要比較的城市（以逗號分隔）: ")
            cities = [city.strip() for city in cities_input.split(",")]
            app.compare_cities(cities)
        
        elif choice == "4":
            print("\n支援的城市:")
            for city in sorted(app.city_codes.keys()):
                print(f"- {city}")
        
        elif choice == "0":
            print("感謝使用本系統，再見！")
            break
        
        else:
            print("無效的選擇，請重新輸入")

if __name__ == "__main__":
    main()
```

#### 2.3 檔案管理助手

這個專題提供文件分類、重命名、搜尋等實用功能，幫助使用者管理檔案。

```python
import os
import shutil
import datetime
import re
import hashlib
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt

class FileManager:
    def __init__(self):
        self.current_dir = os.getcwd()
    
    def list_files(self, path=None, show_hidden=False, file_type=None):
        """列出目錄中的檔案"""
        if path is None:
            path = self.current_dir
        
        try:
            files = os.listdir(path)
            
            if not show_hidden:
                files = [f for f in files if not f.startswith('.')]
            
            if file_type:
                files = [f for f in files if f.endswith(file_type)]
            
            # 獲取檔案詳細資訊
            file_info = []
            for file in files:
                file_path = os.path.join(path, file)
                stats = os.stat(file_path)
                size = stats.st_size
                modified = datetime.datetime.fromtimestamp(stats.st_mtime).strftime("%Y-%m-%d %H:%M:%S")
                file_type = "目錄" if os.path.isdir(file_path) else "檔案"
                
                file_info.append({
                    "名稱": file,
                    "類型": file_type,
                    "大小": self._format_size(size),
                    "修改時間": modified
                })
            
            # 使用 pandas 格式化顯示
            if file_info:
                df = pd.DataFrame(file_info)
                print(f"\n目錄 '{path}' 的內容:")
                print(df.to_string(index=False))
            else:
                print(f"\n目錄 '{path}' 中沒有符合條件的檔案")
                
        except Exception as e:
            print(f"錯誤：{e}")
    
    def change_directory(self, path):
        """變更當前目錄"""
        try:
            # 處理相對路徑和絕對路徑
            if not os.path.isabs(path):
                path = os.path.join(self.current_dir, path)
            
            path = os.path.normpath(path)
            
            if os.path.isdir(path):
                self.current_dir = path
                print(f"當前目錄已變更為：{self.current_dir}")
            else:
                print(f"錯誤：'{path}' 不是有效的目錄")
        except Exception as e:
            print(f"錯誤：{e}")
    
    def create_directory(self, path):
        """建立新目錄"""
        try:
            # 處理相對路徑和絕對路徑
            if not os.path.isabs(path):
                path = os.path.join(self.current_dir, path)
            
            if not os.path.exists(path):
                os.makedirs(path)
                print(f"目錄已建立：{path}")
            else:
                print(f"錯誤：'{path}' 已存在")
        except Exception as e:
            print(f"錯誤：{e}")
    
    def move_file(self, source, destination):
        """移動檔案或目錄"""
        try:
            # 處理相對路徑
            if not os.path.isabs(source):
                source = os.path.join(self.current_dir, source)
            
            if not os.path.isabs(destination):
                destination = os.path.join(self.current_dir, destination)
            
            # 確認來源存在
            if not os.path.exists(source):
                print(f"錯誤：來源 '{source}' 不存在")
                return
            
            # 如果目的地是目錄，將檔案移至該目錄中
            if os.path.isdir(destination):
                destination = os.path.join(destination, os.path.basename(source))
            
            # 移動檔案或目錄
            shutil.move(source, destination)
            print(f"已將 '{source}' 移動至 '{destination}'")
        except Exception as e:
            print(f"錯誤：{e}")
    
    def copy_file(self, source, destination):

            shutil.copy2(source, destination)
            print(f"已將 '{source}' 複製至 '{destination}'")
        except Exception as e:
            print(f"錯誤：{e}")

    def search_files(self, keyword, path=None):
        """根據關鍵字搜尋檔名"""
        if path is None:
            path = self.current_dir

        try:
            matches = []
            for root, dirs, files in os.walk(path):
                for file in files:
                    if keyword.lower() in file.lower():
                        matches.append(os.path.join(root, file))

            if matches:
                print(f"找到 {len(matches)} 個符合的檔案：")
                for match in matches:
                    print(f"- {match}")
            else:
                print("未找到符合的檔案")

        except Exception as e:
            print(f"錯誤：{e}")

    def _format_size(self, size):
        """將位元組轉為人類可讀格式"""
        for unit in ['B', 'KB', 'MB', 'GB']:
            if size < 1024:
                return f"{size:.2f} {unit}"
            size /= 1024
        return f"{size:.2f} TB"

def main():
    fm = FileManager()

    while True:
        print("\n===== 檔案管理助手 =====")
        print("1. 顯示目前目錄檔案")
        print("2. 變更目錄")
        print("3. 建立新目錄")
        print("4. 移動檔案")
        print("5. 複製檔案")
        print("6. 搜尋檔案")
        print("0. 離開程式")

        choice = input("請選擇操作：")

        if choice == "1":
            fm.list_files()
        elif choice == "2":
            path = input("輸入要前往的目錄路徑：")
            fm.change_directory(path)
        elif choice == "3":
            path = input("輸入要建立的資料夾名稱：")
            fm.create_directory(path)
        elif choice == "4":
            source = input("來源檔案/資料夾：")
            destination = input("目的地路徑：")
            fm.move_file(source, destination)
        elif choice == "5":
            source = input("來源檔案/資料夾：")
            destination = input("目的地路徑：")
            fm.copy_file(source, destination)
        elif choice == "6":
            keyword = input("輸入要搜尋的檔名關鍵字：")
            fm.search_files(keyword)
        elif choice == "0":
            print("感謝使用，再見！")
            break
        else:
            print("請輸入有效的選項")

if __name__ == "__main__":
    main()

        """複製檔案或目錄"""
        try:
            # 處理相對路徑
            if not os.path.isabs(source):
                source = os.path.join(self.current

---

## 3. 專題撰寫輔助資源

### 3.1 專題企劃書範本（建議於第 15～16 週撰寫）

請學生於專題開發初期撰寫一份 `proposal.md`，格式如下：

```markdown
# 專題名稱：個人記帳系統

## 一、專題簡介
說明本專題的目標與用途。

## 二、功能列表
- 新增收入與支出
- 列出所有記帳紀錄
- 生成月份報表與圓餅圖
- 匯出為 JSON 格式

## 三、使用技術與對應課程主題
- Dictionary：用於資料儲存
- 函式與模組：封裝邏輯
- 檔案處理：儲存/載入資料
- 第三方套件 matplotlib：生成圖表
- CLI 使用介面：input / print

## 四、預期挑戰
1. 如何整理大量資料？
2. 如何畫出統計圖？
```

---

### 3.2 GUI 專題範例：簡易記事本（使用 `tkinter`）

```python
import tkinter as tk
from tkinter import filedialog, messagebox

class SimpleNoteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("記事本")

        self.text = tk.Text(root, wrap='word')
        self.text.pack(fill='both', expand=True)

        self._build_menu()

    def _build_menu(self):
        menu = tk.Menu(self.root)
        file_menu = tk.Menu(menu, tearoff=0)
        file_menu.add_command(label="開啟", command=self.open_file)
        file_menu.add_command(label="儲存", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="離開", command=self.root.quit)
        menu.add_cascade(label="檔案", menu=file_menu)
        self.root.config(menu=menu)

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, 'r', encoding='utf-8') as file:
                self.text.delete(1.0, tk.END)
                self.text.insert(tk.END, file.read())

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt")
        if file_path:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(self.text.get(1.0, tk.END))
            messagebox.showinfo("儲存成功", f"已儲存至 {file_path}")

if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleNoteApp(root)
    root.mainloop()
```

---

### 3.3 專題評分指標（總分 100 分）

| 項目                         | 比例 | 說明 |
|------------------------------|------|------|
| 專案功能完整性               | 30%  | 是否達成企劃目標，邏輯清晰、無重大錯誤 |
| 程式碼品質與結構             | 25%  | 使用函式、模組、註解完整，結構良好 |
| 使用者介面與互動性           | 15%  | 命令列/GUI 友善性、操作清楚 |
| 專題展示與說明               | 15%  | 投影片、表達能力、Q&A 應對 |
| 創意與應用價值               | 10%  | 專題選題具特色、具實用性 |
| 團隊合作                     | 5%   | 小組協作與分工明確 |

---

### 3.4 展示簡報與報告建議結構

簡報可包含以下部分：
1. 專題簡介與動機
2. 使用技術與對應課程主題
3. 系統功能與展示（建議錄製畫面或現場操作）
4. 問題與挑戰
5. 總結與未來發展

---

### 3.5 範例專題所使用的課程主題對應表

| 範例名稱       | 對應主題                                               |
|----------------|--------------------------------------------------------|
| 個人記帳系統   | list/dict、檔案處理、函式、模組、matplotlib、例外處理 |
| 天氣查詢系統   | requests、json、dict、文字處理、資料可視化、GUI       |
| 檔案管理助手   | os/pathlib、函式、迴圈與條件判斷、Exception、CLI 操作 |
| GUI 記事本     | tkinter、文字處理、檔案操作、事件驅動與例外處理       |

