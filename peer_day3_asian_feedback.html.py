import requests
import os
import subprocess
from datetime import datetime
print("⚠️ 脚本开始运行...")

# ✅ 替换为你的 OpenWeather API 密钥
API_KEY = "9d770d00e9cb32e8bf84fcd9cb6b39fd"  # ← 填上你的 key
url = f"https://api.openweathermap.org/data/3.0/onecall?lat=51.4416&lon=5.4697&exclude=minutely,hourly,daily,alerts&units=metric&appid={API_KEY}"
response = requests.get(url)
data = response.json()
temp = round(data["current"]["temp"])
uvi = round(data["current"]["uvi"], 1)
weather_main = data["current"]["weather"][0]["main"]

# ✅ 打印天气信息（在拿到数据之后）
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(f"🕒 脚本运行时间: {timestamp}")
print("🌡️ 温度:", temp)
print("🌞 UV Index:", uvi)
print("🌥️ 天气状态:", weather_main)

# ✅ HTML 模板 + 实时天气数据
html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <style>
        @font-face {{
            font-family: 'SF Pro Display';
            src: local('SF Pro Display'), local('SFProDisplay-Regular'), sans-serif;
        }}

        body {{
            margin: 0;
            font-family: 'SF Pro Display', sans-serif;
            background: #1C1B33;
        }}

        .container {{
            position: relative;
            width: 377px;
            height: 816px;
            margin: 0 auto;
            background-image: url("https://kqin1.github.io/uv-feedback-pages/Asian3.png");
            background-size: cover;
            background-repeat: no-repeat;
        }}

        .weather-info {{
            position: absolute;
            top: 95px;
            width: 100%;
            text-align: center;
            color: white;
        }}

        .weather-info h1 {{
            margin-bottom: 10px;
            font-size: 32px;
            margin: 0;
        }}

        .weather-info .temperature {{
            margin-top: 10px;
            margin-bottom: 10px;
            font-size: 92px;
            margin: 0;
            line-height: 67.68px;
            letter-spacing: 0.36px;
        }}

        .weather-info .details {{
            margin-top: 10px;
            font-size: 19.34px;
            font-weight: 500;
            line-height: 23.2px;
            letter-spacing: 0.37px;
            color: rgba(235, 235, 245, 0.60);
        }}

        .weather-info .uv {{
            font-size: 19.34px;
            font-weight: 500;
            line-height: 23.2px;
            letter-spacing: 0.37px;
            color: white;
        }}

        .feedback-box {{
            position: absolute;
            top: 695px;
            left: 10px;
            width: 342px;
            height: 66px;
            padding: 7px 8px;
            overflow-y: scroll;
            background: linear-gradient(136deg, rgba(46, 51, 90, 0.26) 0%, rgba(28, 27, 51, 0.26) 100%);
            box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25) inset;
            border-radius: 10px;
            color: white;
            font-size: 13px;
            line-height: 16px;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="weather-info">
            <h1>Eindhoven</h1>
            <div class="temperature">{temp}°</div>
            <div class="details">{weather_main}</div>
            <div class="uv">UV Index: {uvi}</div>
        </div>
        <div class="feedback-box">
            I’ve noticed that my hair starts thinning around April, especially after going hiking with friends on the weekends. What surprised me more was that it didn’t grow back as quickly as I expected. I looked it up and saw that the WHO actually recommends wearing a wide-brimmed hat for better sun protection. I can share the link if you’re curious [https://www.amazon.nl/-/en/Home-Prefer-Mens-Protection-Fisherman/dp/B01CAGGLK4?th=1&psc=1] Honestly, I was a bit worried people might judge how I looked. But once I realized something wasn’t right, I felt it was more important to take care of my health and do what I could early on. Funny enough, some of my hiking group friends ended up getting the same sunhat too after I shared my experience. We’re planning to go hiking again after finals :)
        </div>
    </div>
</body>
</html>"""

# 添加更新时间（注意顺序要早于保存）
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
html_template += f"\n<!-- Last updated: {timestamp} -->\n"

# ✅ 保存 HTML 文件
output_path = "/Users/kqin/Downloads/uv-feedback-pages/peer_day3_asian_feedback_live5.html"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(html_template)

print("✅ Asian HTML 文件已成功保存！路径：", output_path)
print("温度2A:", temp)
print("UV2A:", uvi)
print("天气2A:", weather_main)

# ✅ 自动推送到 GitHub
print("🚀 开始同步到 GitHub...")
# Git 提交和推送部分
os.chdir("/Users/kqin/Downloads/uv-feedback-pages")

# 先 add
subprocess.run(["git", "add", "."], check=True)

# 再 commit（并捕捉返回码）
commit_result = subprocess.run(["git", "commit", "-m", "✅ 修复 Asian 页面空白"])
if commit_result.returncode == 0:
    subprocess.run(["git", "push", "origin", "main"], check=True)
    print("✅ GitHub 同步成功！")

    # ✅ 自动生成唯一版本参数（避免缓存）
    version = datetime.now().strftime("%Y%m%d%H%M")  # e.g., 202506012308
    final_url = f"https://kqin1.github.io/uv-feedback-pages/peer_day3_asian_feedback_live5.html?v={version}"

    print("🔗 请使用以下链接查看最新内容（防止缓存）:")
    print(final_url)
else:
    print("⚠️ 没有内容变更，无需提交！")

    


