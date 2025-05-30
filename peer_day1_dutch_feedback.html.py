import requests

print("⚠️ 脚本开始运行...")

# ✅ 替换成你自己的 OpenWeather API 密钥
API_KEY = "9d770d00e9cb32e8bf84fcd9cb6b39fd"  # ← 别忘了填入！
url = f"https://api.openweathermap.org/data/3.0/onecall?lat=51.4416&lon=5.4697&exclude=minutely,hourly,daily,alerts&units=metric&appid={API_KEY}"

response = requests.get(url)
data = response.json()
temp = round(data["current"]["temp"])
uvi = round(data["current"]["uvi"], 1)
weather_main = data["current"]["weather"][0]["main"]

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
            background-image: url("Dutch (1).png");
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
            Yesterday after biking all day, I noticed my scalp felt kind of dry, reddish, and tight around my hairline. My girlfriend sent me a UV-protective shampoo she saw trending on Instagram — honestly, it might be worth a try. I’m planning to do the same: apply some sunscreen and throw on a cap when I’m out for a while. Same advice for you, hopefully it saves us both from a weird peeling scalp this summer.
        </div>
    </div>
</body>
</html>"""

# ✅ 保存 HTML 到 Downloads
output_path = "/Users/kqin/Downloads/peer_day1_dutch_feedback_live3.html"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(html_template)

print("✅ Dutch peer HTML 文件已成功保存！路径：", output_path)

