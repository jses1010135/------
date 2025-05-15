# Python 基礎程式設計
## 第 17 週：pip 與第三方套件

### 課程目標

本週課程將介紹如何使用 pip 套件管理工具，以及探索幾個實用的第三方 Python 套件（requests、matplotlib、openpyxl）。學生將學習如何安裝、管理和使用這些套件來擴展 Python 的功能。

### 1. pip 套件管理工具

#### 1.1 pip 簡介

pip 是 Python 的標準套件管理系統，用於安裝和管理 Python 套件。Python 3.4+ 版本中已經預裝了 pip。

#### 1.2 確認 pip 是否已安裝

```python
# 在命令提示字元或終端機中輸入以下指令
# pip --version 或 pip3 --version

# 輸出範例:
# pip 23.1.2 from C:\Users\Username\AppData\Local\Programs\Python\Python311\Lib\site-packages\pip (python 3.11)
```

#### 1.3 基本 pip 指令

```
# 安裝套件
pip install package_name

# 安裝特定版本
pip install package_name==1.2.3

# 升級套件
pip install --upgrade package_name

# 解除安裝套件
pip uninstall package_name

# 列出已安裝的套件
pip list

# 查詢特定套件的詳細資訊
pip show package_name

# 從 requirements.txt 文件安裝多個套件
pip install -r requirements.txt
```

#### 1.4 建立與使用虛擬環境

虛擬環境是專案特定的獨立 Python 環境，可避免套件衝突問題。

```
# 使用 venv 模組（Python 3.3+）建立虛擬環境
python -m venv my_project_env

# 在 Windows 上啟動虛擬環境
my_project_env\Scripts\activate

# 在 macOS/Linux 上啟動虛擬環境
source my_project_env/bin/activate

# 停用虛擬環境
deactivate
```

#### 1.5 建立 requirements.txt

```
# 產生 requirements.txt 文件
pip freeze > requirements.txt

# requirements.txt 範例內容:
# requests==2.31.0
# matplotlib==3.7.1
# openpyxl==3.1.2
```

### 2. requests 套件 - HTTP 請求

#### 2.1 安裝 requests

```
pip install requests
```

#### 2.2 發送 GET 請求並處理回應

```python
import requests

# 發送 GET 請求
response = requests.get('https://api.github.com/events')

# 檢查狀態碼
print(f"狀態碼: {response.status_code}")

# 查看回應標頭
print(f"回應標頭: {response.headers}")

# 取得 JSON 格式的回應內容
if response.status_code == 200:
    data = response.json()
    print(f"事件數量: {len(data)}")
    if data:
        print(f"第一個事件的類型: {data[0]['type']}")
else:
    print(f"請求失敗，狀態碼: {response.status_code}")
```

#### 2.3 發送 POST 請求

```python
import requests

# 要發送的資料
payload = {'key1': 'value1', 'key2': 'value2'}

# 發送 POST 請求
response = requests.post('https://httpbin.org/post', data=payload)

# 檢查結果
print(f"狀態碼: {response.status_code}")
if response.status_code == 200:
    data = response.json()
    print("回傳資料:")
    print(data)
```

#### 2.4 使用參數和標頭

```python
import requests

# 查詢參數
params = {
    'q': 'python',
    'sort': 'stars',
    'order': 'desc'
}

# 自訂標頭
headers = {
    'User-Agent': 'Python-Requests-Demo',
    'Accept': 'application/json'
}

# 發送帶有參數和標頭的 GET 請求
response = requests.get(
    'https://api.github.com/search/repositories',
    params=params,
    headers=headers
)

# 處理回應
if response.status_code == 200:
    data = response.json()
    print(f"找到 {data['total_count']} 個 Python 儲存庫")
    print("\n前三個最受歡迎的儲存庫:")
    for i, repo in enumerate(data['items'][:3], 1):
        print(f"{i}. {repo['name']} - ⭐ {repo['stargazers_count']}")
        print(f"   描述: {repo['description']}")
        print(f"   URL: {repo['html_url']}\n")
else:
    print(f"請求失敗，狀態碼: {response.status_code}")
    print(response.text)
```

#### 2.5 練習：抓取網頁內容

```python
import requests
from bs4 import BeautifulSoup  # 需要另外安裝：pip install beautifulsoup4

# 抓取 Python 官網首頁
url = 'https://www.python.org/'
response = requests.get(url)

if response.status_code == 200:
    # 使用 BeautifulSoup 解析 HTML
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # 提取頁面標題
    title = soup.title.string
    print(f"頁面標題: {title}")
    
    # 提取最新消息
    latest_news = soup.select('.blog-widget li')
    print("\n最新消息:")
    for i, news in enumerate(latest_news[:3], 1):
        news_title = news.a.text.strip()
        news_date = news.time.text.strip()
        print(f"{i}. {news_title} ({news_date})")
else:
    print(f"無法抓取頁面，狀態碼: {response.status_code}")
```

### 3. matplotlib 套件 - 資料視覺化

#### 3.1 安裝 matplotlib

```
pip install matplotlib
```

#### 3.2 繪製簡單折線圖

```python
import matplotlib.pyplot as plt
import numpy as np

# 生成資料
x = np.linspace(0, 10, 100)  # 生成 0 到 10 之間的 100 個點
y = np.sin(x)  # 計算 sin(x)

# 建立圖表
plt.figure(figsize=(10, 6))  # 設定圖表大小
plt.plot(x, y, label='sin(x)', color='blue', linewidth=2)  # 畫折線圖

# 添加圖表元素
plt.title('正弦函數圖', fontsize=16)  # 標題
plt.xlabel('x', fontsize=14)  # x 軸標籤
plt.ylabel('sin(x)', fontsize=14)  # y 軸標籤
plt.grid(True)  # 顯示網格
plt.legend(fontsize=12)  # 顯示圖例

# 顯示圖表
plt.tight_layout()  # 自動調整版面
plt.savefig('sine_wave.png')  # 儲存圖表
plt.show()  # 顯示圖表
```

#### 3.3 繪製多個子圖

```python
import matplotlib.pyplot as plt
import numpy as np

# 生成資料
x = np.linspace(0, 2*np.pi, 100)
y_sin = np.sin(x)
y_cos = np.cos(x)

# 建立含有多個子圖的圖表
fig, axs = plt.subplots(2, 1, figsize=(10, 8))

# 第一個子圖：sine 函數
axs[0].plot(x, y_sin, color='blue')
axs[0].set_title('正弦函數')
axs[0].set_ylabel('sin(x)')
axs[0].grid(True)

# 第二個子圖：cosine 函數
axs[1].plot(x, y_cos, color='red')
axs[1].set_title('餘弦函數')
axs[1].set_xlabel('x')
axs[1].set_ylabel('cos(x)')
axs[1].grid(True)

# 調整子圖之間的間距
plt.tight_layout()
plt.savefig('trig_functions.png')
plt.show()
```

#### 3.4 繪製長條圖和圓餅圖

```python
import matplotlib.pyplot as plt
import numpy as np

# 資料
categories = ['A', 'B', 'C', 'D', 'E']
values = [22, 35, 14, 28, 19]
explode = (0, 0.1, 0, 0, 0)  # 只突顯第二個扇形

# 建立一個有兩個子圖的圖表
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# 長條圖
bars = ax1.bar(categories, values, color=['royalblue', 'indianred', 'green', 'orange', 'purple'])
ax1.set_title('長條圖範例')
ax1.set_xlabel('類別')
ax1.set_ylabel('數值')
ax1.grid(axis='y', linestyle='--', alpha=0.7)

# 在長條上顯示數值
for bar in bars:
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2., height + 0.5,
             f'{height}',
             ha='center', va='bottom')

# 圓餅圖
ax2.pie(values, labels=categories, explode=explode, autopct='%1.1f%%',
        shadow=True, startangle=90, colors=['royalblue', 'indianred', 'green', 'orange', 'purple'])
ax2.axis('equal')  # 保持圓形
ax2.set_title('圓餅圖範例')

plt.tight_layout()
plt.savefig('bar_pie_charts.png')
plt.show()
```

#### 3.5 散點圖與趨勢線

```python
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats  # 用於計算趨勢線

# 生成隨機資料
np.random.seed(42)  # 固定隨機數種子，使結果可重現
x = np.random.normal(50, 15, 200)  # 平均值 50，標準差 15 的 200 個隨機數
y = 2*x + 10 + np.random.normal(0, 20, 200)  # 線性關係加上隨機誤差

# 計算趨勢線
slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
line = slope * x + intercept

# 建立圖表
plt.figure(figsize=(10, 6))

# 繪製散點圖
plt.scatter(x, y, color='darkblue', alpha=0.5, label='資料點')

# 繪製趨勢線
plt.plot(x, line, color='red', linewidth=2, label=f'趨勢線 (y = {slope:.2f}x + {intercept:.2f})')

# 添加相關係數資訊
plt.text(0.05, 0.95, f'相關係數 (r): {r_value:.3f}', transform=plt.gca().transAxes,
         fontsize=12, verticalalignment='top')

# 添加圖表元素
plt.title('散點圖與趨勢線範例', fontsize=16)
plt.xlabel('X 值', fontsize=14)
plt.ylabel('Y 值', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()

plt.tight_layout()
plt.savefig('scatter_plot.png')
plt.show()
```

### 4. openpyxl 套件 - Excel 檔案處理

#### 4.1 安裝 openpyxl

```
pip install openpyxl
```

#### 4.2 建立與寫入 Excel 檔案

```python
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

# 建立新的 Excel 工作簿
wb = openpyxl.Workbook()

# 選取預設的工作表（Sheet）
ws = wb.active
ws.title = "銷售報表"

# 定義標題資料
headers = ["產品編號", "產品名稱", "單價", "銷售數量", "總金額"]

# 寫入標題列
for col_idx, header in enumerate(headers, 1):
    cell = ws.cell(row=1, column=col_idx)
    cell.value = header
    
    # 設定標題列樣式
    cell.font = Font(bold=True, size=12, color="FFFFFF")
    cell.fill = PatternFill(fill_type="solid", fgColor="4F81BD")
    cell.alignment = Alignment(horizontal="center")
    cell.border = Border(
        left=Side(style='thin'), 
        right=Side(style='thin'),
        top=Side(style='thin'), 
        bottom=Side(style='thin')
    )

# 範例資料
products = [
    {"id": "P001", "name": "筆記型電腦", "price": 25000, "quantity": 5},
    {"id": "P002", "name": "智慧型手機", "price": 15000, "quantity": 12},
    {"id": "P003", "name": "平板電腦", "price": 12000, "quantity": 8},
    {"id": "P004", "name": "桌上型電腦", "price": 30000, "quantity": 3},
    {"id": "P005", "name": "無線耳機", "price": 3500, "quantity": 20}
]

# 寫入產品資料
for row_idx, product in enumerate(products, 2):  # 從第 2 列開始寫入
    ws.cell(row=row_idx, column=1).value = product["id"]
    ws.cell(row=row_idx, column=2).value = product["name"]
    ws.cell(row=row_idx, column=3).value = product["price"]
    ws.cell(row=row_idx, column=4).value = product["quantity"]
    
    # 計算總金額並寫入
    total = product["price"] * product["quantity"]
    ws.cell(row=row_idx, column=5).value = total
    
    # 設定資料列的基本樣式
    for col_idx in range(1, 6):
        cell = ws.cell(row=row_idx, column=col_idx)
        cell.border = Border(
            left=Side(style='thin'), 
            right=Side(style='thin'),
            top=Side(style='thin'), 
            bottom=Side(style='thin')
        )
        
        # 為數字欄位設定右對齊
        if col_idx >= 3:
            cell.alignment = Alignment(horizontal="right")

# 計算總計
total_row = len(products) + 2
ws.cell(row=total_row, column=4).value = "總計"
ws.cell(row=total_row, column=4).font = Font(bold=True)
ws.cell(row=total_row, column=4).alignment = Alignment(horizontal="right")

# 計算總銷售額並寫入
total_formula = f"=SUM(E2:E{total_row-1})"
ws.cell(row=total_row, column=5).value = total_formula
ws.cell(row=total_row, column=5).font = Font(bold=True)
ws.cell(row=total_row, column=5).alignment = Alignment(horizontal="right")

# 自動調整欄寬
for col_idx in range(1, 6):
    col_letter = get_column_letter(col_idx)
    ws.column_dimensions[col_letter].auto_size = True
    # 因為 auto_size 不一定在所有版本中都有效，我們手動設定一個合理的寬度
    if col_idx == 1:  # 產品編號
        ws.column_dimensions[col_letter].width = 10
    elif col_idx == 2:  # 產品名稱
        ws.column_dimensions[col_letter].width = 15
    else:  # 其他數字欄位
        ws.column_dimensions[col_letter].width = 12

# 為數字欄位設定格式
for row_idx in range(2, total_row + 1):
    # 單價和總金額欄位使用貨幣格式
    ws.cell(row=row_idx, column=3).number_format = "#,##0"
    ws.cell(row=row_idx, column=5).number_format = "#,##0"

# 儲存 Excel 檔案
wb.save("sales_report.xlsx")
print("Excel 檔案已建立：sales_report.xlsx")
```

#### 4.3 讀取 Excel 檔案

```python
import openpyxl

# 開啟 Excel 檔案
wb = openpyxl.load_workbook("sales_report.xlsx")

# 選取工作表
ws = wb["銷售報表"]

# 讀取標題列
headers = []
for col in range(1, 6):
    headers.append(ws.cell(row=1, column=col).value)
print("標題列:", headers)

# 讀取所有的產品資料
products = []
for row in range(2, ws.max_row):
    if ws.cell(row=row, column=1).value:  # 確保非空行
        product = {
            "id": ws.cell(row=row, column=1).value,
            "name": ws.cell(row=row, column=2).value,
            "price": ws.cell(row=row, column=3).value,
            "quantity": ws.cell(row=row, column=4).value,
            "total": ws.cell(row=row, column=5).value
        }
        products.append(product)

# 顯示產品資料
print("\n產品資料:")
for product in products:
    print(f"{product['id']} - {product['name']}: {product['price']} 元 x {product['quantity']} = {product['total']} 元")

# 讀取總計
total_row = len(products) + 2
total_value = ws.cell(row=total_row, column=5).value
print(f"\n總銷售額: {total_value} 元")
```

#### 4.4 修改現有 Excel 檔案

```python
import openpyxl
from openpyxl.styles import Font, PatternFill

# 開啟現有的 Excel 檔案
wb = openpyxl.load_workbook("sales_report.xlsx")
ws = wb["銷售報表"]

# 添加新的產品
next_row = ws.max_row
if ws.cell(row=next_row, column=1).value is None:
    next_row = next_row
else:
    next_row = next_row + 1

# 新產品資料
new_product = {"id": "P006", "name": "行動電源", "price": 1800, "quantity": 15}

# 寫入新產品資料
ws.cell(row=next_row, column=1).value = new_product["id"]
ws.cell(row=next_row, column=2).value = new_product["name"]
ws.cell(row=next_row, column=3).value = new_product["price"]
ws.cell(row=next_row, column=4).value = new_product["quantity"]

# 計算並寫入總金額
total = new_product["price"] * new_product["quantity"]
ws.cell(row=next_row, column=5).value = total

# 更新總計所在的列
total_row = next_row + 1
ws.cell(row=total_row, column=4).value = "總計"
ws.cell(row=total_row, column=4).font = Font(bold=True)

# 更新總計公式
total_formula = f"=SUM(E2:E{total_row-1})"
ws.cell(row=total_row, column=5).value = total_formula

# 高亮顯示新加入的產品
for col in range(1, 6):
    ws.cell(row=next_row, column=col).fill = PatternFill(fill_type="solid", fgColor="E6F0FF")

# 儲存修改後的檔案
wb.save("sales_report_updated.xlsx")
print("Excel 檔案已更新：sales_report_updated.xlsx")
```

#### 4.5 建立圖表

```python
import openpyxl
from openpyxl.chart import BarChart, Reference

# 開啟現有的 Excel 檔案
wb = openpyxl.load_workbook("sales_report_updated.xlsx")
ws = wb["銷售報表"]

# 為圖表建立新的工作表
chart_sheet = wb.create_sheet(title="銷售圖表")

# 建立長條圖
chart = BarChart()
chart.title = "產品銷售金額"
chart.x_axis.title = "產品"
chart.y_axis.title = "銷售金額"

# 定義資料範圍
data = Reference(ws, min_col=5, min_row=2, max_row=ws.max_row-1, max_col=5)
categories = Reference(ws, min_col=2, min_row=2, max_row=ws.max_row-1, max_col=2)

# 添加資料到圖表
chart.add_data(data)
chart.set_categories(categories)

# 設定圖表樣式
chart.shape = 4  # 設定為立體柱狀圖
chart.height = 15  # 圖表高度
chart.width = 20  # 圖表寬度

# 將圖表放入工作表
chart_sheet.add_chart(chart, "A1")

# 儲存含有圖表的檔案
wb.save("sales_report_with_chart.xlsx")
print("含有圖表的 Excel 檔案已建立：sales_report_with_chart.xlsx")
```

### 5. 整合應用範例：資料抓取、分析與視覺化

以下範例結合了 requests、matplotlib 和 openpyxl，模擬一個完整的資料處理流程，從抓取資料、視覺化到匯出 Excel 報表。

```python
import requests
import matplotlib.pyplot as plt
import openpyxl
import json
from datetime import datetime

# 1. 使用 requests 從 API 抓取資料
def fetch_weather_data():
    print("正在從 API 抓取天氣資料...")
    
    # 模擬從 API 獲取天氣資料 (實際上這裡回傳模擬資料)
    # 在實際應用中，這裡應該是真正的 API 呼叫
    # response = requests.get("https://api.weather.com/data")
    
    # 模擬的天氣資料
    weather_data = {
        "city": "台北市",
        "forecast": [
            {"date": "2023-05-12", "temp_max": 32, "temp_min": 26, "humidity": 75, "condition": "晴時多雲"},
            {"date": "2023-05-13", "temp_max": 30, "temp_min": 25, "humidity": 80, "condition": "多雲時晴"},
            {"date": "2023-05-14", "temp_max": 29, "temp_min": 24, "humidity": 85, "condition": "多雲時陣雨"},
            {"date": "2023-05-15", "temp_max": 27, "temp_min": 23, "humidity": 90, "condition": "雨天"},
            {"date": "2023-05-16", "temp_max": 28, "temp_min": 24, "humidity": 85, "condition": "多雲時陣雨"},
            {"date": "2023-05-17", "temp_max": 31, "temp_min": 26, "humidity": 75, "condition": "晴時多雲"},
            {"date": "2023-05-18", "temp_max": 33, "temp_min": 27, "humidity": 70, "condition": "晴天"}
        ]
    }
    
    return weather_data

# 2. 使用 matplotlib 視覺化資料
def visualize_weather_data(weather_data):
    print("正在生成天氣資料視覺化...")
    
    dates = [day["date"] for day in weather_data["forecast"]]
    temp_max = [day["temp_max"] for day in weather_data["forecast"]]
    temp_min = [day["temp_min"] for day in weather_data["forecast"]]
    humidity = [day["humidity"] for day in weather_data["forecast"]]
    
    # 建立圖表
    plt.figure(figsize=(12, 8))
    
    # 子圖 1：溫度曲線圖
    plt.subplot(2, 1, 1)
    plt.plot(dates, temp_max, 'ro-', label='最高溫')
    plt.plot(dates, temp_min, 'bo-', label='最低溫')
    plt.title(f'{weather_data["city"]} 一週溫度預測', fontsize=14)
    plt.ylabel('溫度 (°C)', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    
    # 子圖 2：濕度長條圖
    plt.subplot(2, 1, 2)
    bars = plt.bar(dates, humidity, color='skyblue')
    plt.title(f'{weather_data["city"]} 一週濕度預測', fontsize=14)
    plt.xlabel('日期', fontsize=12)
    plt.ylabel('濕度 (%)', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7, axis='y')
    
    # 在長條上顯示數值
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height + 1,
                 f'{height}%', ha='center', va='bottom')
    
    # 調整版面
    plt.tight_layout()
    
    # 儲存圖表
    plt.savefig("weather_forecast.png")
    print("天氣預測圖表已儲存為：weather_forecast.png")
    plt.close()

# 3. 使用 openpyxl 將資料匯出至 Excel
def export_to_excel(weather_data):
    print("正在將資料匯出至 Excel...")
    
    # 建立新的 Excel 工作簿
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = f"{weather_data['city']}天氣預測"
    
    # 寫入標題
    headers = ["日期", "最高溫 (°C)", "最低溫 (°C)", "濕度 (%)", "天氣狀況"]
    for col_idx, header in enumerate(headers, 1):
        ws.cell(row=1, column=col_idx).value = header
        ws.cell(row=1, column=col_idx).font = openpyxl.styles.Font(bold=True)
    
    # 寫入資料
    for row_idx, day in enumerate(weather_data["forecast"], 2):
        ws.cell(row=row_idx, column=1).value = day["date"]
        ws.cell(row=row_idx, column=2).value = day["temp_max"]
        ws.cell(row=row_idx, column=3).value = day["temp_min"]
        ws.cell(row=row_idx, column=4).value = day["humidity"]
        ws.cell(row=row_idx, column=5).value = day["condition"]
    
    # 調整欄寬
    for col in ws.columns:
        max_length = 0
        column = col[0].column_letter
        for cell in col:
            if cell.value:
                cell_length = len(str(cell.value))
                if cell_length > max_length:
                    max_length = cell_length
        ws.column_dimensions[column].width = max_length + 2
    
    # 儲存檔案
    excel_filename = f"{weather_data['city']}_weather_forecast.xlsx"
    wb.save(excel_filename)
    print(f"天氣預測資料已匯出至：{excel_filename}")
    
    return excel_filename

# 4. 主程式：整合所有功能
def main():
    print("=== 天氣資料處理系統 ===")
    
    # 步驟 1：抓取資料
    weather_data = fetch_weather_data()
    print(f"已獲取 {weather_data['city']} 的天氣預測資料")
    
    # 步驟 2：視覺化資料
    visualize_weather_data(weather_data)
    
    # 步驟 3：匯出資料到 Excel
    excel_file = export_to_excel(weather_data)
    
    print("\n所有處理已完成！")
    print(f"1. 圖表檔案：weather_forecast.png")
    print(f"2. Excel 檔案：{excel_file}")

# 執行主程式
if __name__ == "__main__":
    main()
```

### 6. 課程總結與實作練習

#### 6.1 本週學習重點
- 了解 pip 套件管理工具的基本使用方法
- 學習使用虛擬環境管理 Python 專案
- 掌握常用第三方套件的使用：
  - requests：進行 HTTP 請求與網路資料抓取
  - matplotlib：資料視覺化與圖表生成
  - openpyxl：Excel 檔案的讀取、處理與建立

#### 6.2 實作練習

##### 練習一：使用 requests 抓取資料
從公開 API 抓取資料並進行處理（可選用以下其中一個）：
- 使用 [Open Weather Map API](https://openweathermap.org/api) 獲取天氣資料
- 使用 [JSONPlaceholder](https://jsonplaceholder.typicode.com/) 獲取模擬資料
- 使用 [公開資料平台](https://data.gov.tw/) 獲取台灣開放資料

##### 練習二：使用 matplotlib 視覺化
1. 從任何來源獲取資料（可以使用 CSV 檔案、Excel 檔案、網路 API 等）
2. 使用 matplotlib 繪製至少三種不同類型的圖表（折線圖、長條圖、圓餅圖、散點圖等）
3. 在圖表中加入適當的標題、標籤和圖例

##### 練習三：使用 openpyxl 處理 Excel 檔案
1. 建立一個學生成績管理系統的 Excel 報表
2. 報表應包含：學生資訊、各科成績、平均分數和排名
3. 加入條件格式化，例如：高分標記為綠色，低分標記為紅色
4. 新增圖表顯示班級成績分布

#### 6.3 延伸閱讀
- [PyPI](https://pypi.org/)：Python 套件索引，探索更多有用的 Python 套件
- [Requests 官方文件](https://requests.readthedocs.io/)：深入學習 Requests 套件的更多功能
- [Matplotlib 官方教學](https://matplotlib.org/stable/tutorials/index.html)：更多進階的資料視覺化技巧
- [OpenPyXL 官方文件](https://openpyxl.readthedocs.io/)：Excel 處理的完整資源

下週我們將進行專題製作與展示，請準備好運用本課程所學的知識來完成一個小型專案！