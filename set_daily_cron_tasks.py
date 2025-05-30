from crontab import CronTab

# 初始化当前用户的 cron
cron = CronTab(user=True)

# 清除已有的同名任务，防止重复添加
cron.remove_all(comment='update_weather_html')
cron.remove_all(comment='peer_dutch_feedback')
cron.remove_all(comment='peer_asian_feedback')

# 设置三个 .py 脚本的路径（❗不是 .html）
scripts = {
    "update_weather_html": "/Users/kqin/Downloads/uv-feedback-pages/professional_day1_doctor_feedback.html.py",
    "peer_dutch_feedback": "/Users/kqin/Downloads/uv-feedback-pages/peer_day1_dutch_feedback.html.py",
    "peer_asian_feedback": "/Users/kqin/Downloads/uv-feedback-pages/peer_day1_asian_feedback.html.py"
}

# 每天 07:55 运行三个脚本
for comment, path in scripts.items():
    job = cron.new(command=f'python3 "{path}"', comment=comment)
    job.setall("55 07 * * *")

# 写入任务
cron.write()

print("✅ 每天 07:55 的定时任务已设置完成！")
