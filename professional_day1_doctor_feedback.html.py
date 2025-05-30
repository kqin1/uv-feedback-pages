import requests
import os
import subprocess

print("⚠️ 脚本开始运行...")

# 获取天气数据
API_KEY = "9d770d00e9cb32e8bf84fcd9cb6b39fd"
url = f"https://api.openweathermap.org/data/3.0/onecall?lat=51.4416&lon=5.4697&exclude=minutely,hourly,daily,alerts&units=metric&appid={API_KEY}"
response = requests.get(url)
data = response.json()
temp = round(data["current"]["temp"])
uvi = round(data["current"]["uvi"], 1)
weather_main = data["current"]["weather"][0]["main"]

# 创建 HTML 内容（不要有 ...）
html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <style>
        body {{
            margin: 0;
            font-family: sans-serif;
            background: #1C1B33;
        }}
        .container {{
            position: relative;
            width: 377px;
            height: 816px;
            margin: 0 auto;
            background-image: url("https://kqin1.github.io/uv-feedback-pages/doctor_bg4.png");
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
            font-size: 32px;
            margin: 0;
        }}
        .temperature {{
            font-size: 92px;
            margin: 0;
        }}
        .details, .uv {{
            font-size: 20px;
            margin-top: 10px;
        }}
        .feedback-box {{
            position: absolute;
            top: 695px;
            left: 10px;
            width: 342px;
            height: 66px;
            padding: 7px 8px;
            overflow-y: scroll;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 10px;
            color: white;
            font-size: 13px;
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
            A new patient of mine went surfing during break without sunscreen on scalp and came back with brittle, less elastic hair and scalp issues. With summer coming, more people doing outdoor sports are applying sunscreen to thinning areas, wearing caps or using UV-protective shampoo. If your scalp feels dry, reddish, or tight after sun exposure, that’s an early sign worth paying attention to.
        </div>
    </div>
</body>
</html>
"""

# 保存 HTML 文件
output_path = "/Users/kqin/Downloads/uv-feedback-pages/professional_day1_doctor_feedback_live3.html"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(html_template)

print("✅ Doctor HTML 文件已成功保存！路径：", output_path)

# 推送到 GitHub
print("🚀 开始同步到 GitHub...")
os.chdir("/Users/kqin/Downloads/uv-feedback-pages")
try:
    subprocess.run(["git", "add", "."], check=True)
    subprocess.run(["git", "commit", "-m", "✅ 修复 doctor 页面空白"], check=True)
    subprocess.run(["git", "push", "origin", "main"], check=True)
    print("✅ GitHub 同步成功！")
except subprocess.CalledProcessError:
    print("❌ GitHub 推送失败，请检查网络或凭证")

