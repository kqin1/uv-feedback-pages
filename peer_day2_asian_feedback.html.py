import requests
import os
import subprocess
print("⚠️ 脚本开始运行...")

# ✅ 替换为你的 OpenWeather API 密钥
API_KEY = "9d770d00e9cb32e8bf84fcd9cb6b39fd"  # ← 填上你的 key
url = f"https://api.openweathermap.org/data/3.0/onecall?lat=51.4416&lon=5.4697&exclude=minutely,hourly,daily,alerts&units=metric&appid={API_KEY}"

response = requests.get(url)
data = response.json()
temp = round(data["current"]["temp"])
uvi = round(data["current"]["uvi"], 1)
weather_main = data["current"]["weather"][0]["main"]

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
            background-image: url("https://kqin1.github.io/uv-feedback-pages/Asian (2).png");
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
            My brother is an active outdoor person who just turned 23, and he recently noticed some hair thinning on the top of his head. After learning in a university lecture that acid rain is common in low-lying areas like the Netherlands, Denmark, and Belgium, he started wearing caps and using waterproof UV spray, which really helped with flaking and irritation. He says if he’d known earlier, he would’ve acted sooner—and now that he’s tried it, he realizes it’s not a hassle at all and hopes others can learn from it too.
        </div>
    </div>
</body>
</html>"""

# ✅ 保存 HTML 文件
output_path = "/Users/kqin/Downloads/uv-feedback-pages/peer_day1_asian_feedback_live4.html"

with open(output_path, "w", encoding="utf-8") as f:
    f.write(html_template)

print("✅ Asian HTML 文件已成功保存！路径：", output_path)

# ✅ 自动推送到 GitHub
print("🚀 开始同步到 GitHub...")
os.chdir("/Users/kqin/Downloads/uv-feedback-pages")
try:
    subprocess.run(["git", "add", "."], check=True)
    subprocess.run(["git", "commit", "-m", "✅ 修复 Asian 页面空白"], check=True)
    subprocess.run(["git", "push", "origin", "main"], check=True)
    print("✅ GitHub 同步成功！")
except subprocess.CalledProcessError:
    print("❌ GitHub 推送失败，请检查网络或凭证")
    print("温度2A:", temp)
    print("UV2A:", uvi)
    print("天气2A:", weather_main)
    from datetime import datetime
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# 替换 feedback 内容中加入时间，或作为注释
html_template += f"\n<!-- Last updated: {timestamp} -->\n"

