# import smtplib
# from email.mime.text import MIMEText
#
# # 设置服务器所需信息
# # 163邮箱服务器地址
# mail_host = 'smtp.qq.com'
# # qq用户名
# mail_user = '873064448@qq.com'
# # 密码(部分邮箱为授权码)
# mail_pass = 'ggymkdiryklbbcdc'
# # 邮件发送方邮箱地址
# sender = '873064448@qq.com'
# # 邮件接受方邮箱地址，注意需要[]包裹，这意味着你可以写多个邮件地址群发
# receivers = ['1904662739@qq.com']
#
# # 设置email信息
# # 邮件内容设置
# attr = (open(r'D:\day08\day13【单元测试】\代码\day13\计算器测试报告.html', 'rb').read())
# message = MIMEText(attr, 'plain', 'utf-8')
# # 邮件主题
# message['Subject'] = '计算器测试报告'
# # 发送方信息
# message['From'] = sender
# # 接受方信息
# message['To'] = receivers[0]
#
# # 登录并发送邮件
# try:
#     smtpObj = smtplib.SMTP()
#     # 连接到服务器
#     smtpObj.connect(mail_host, 25)
#     # 登录到服务器
#     smtpObj.login(mail_user, mail_pass)
#     # 发送0
#     smtpObj.sendmail(
#         sender, receivers, message.as_string())
#     # 退出
#     smtpObj.quit()
#     print('success')
# except smtplib.SMTPException as e:
#     print('error', e)  # 打印错误




import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

# 邮件内容配置
msg = MIMEText("约吗","html","utf-8")
msg["From"] = formataddr(["黄石市","873064448@qq.com"])
msg["Subject"] = "邮件主题"

# 发送邮件
server = smtplib.SMTP_SSL("smtp.qq.com")
server.login("873064448@qq.com","ggymkdiryklbbcdc")
server.sendmail("873064448@qq.com","1904662739@qq.com",msg.as_string())
server.quit()