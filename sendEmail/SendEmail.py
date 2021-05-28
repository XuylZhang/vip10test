
import smtplib,time,os
from email.mime.text import MIMEText
from email.header import Header
from logs import logger

def sendEmail():
    sender = '15081860930@163.com'
    receiver = 'forget0930@163.com'
    smtpdsever = 'smtp.163.com'
    username = '15081860930'
    password = 'DTPOWPQMXVDIEVJC'
    t = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
    subject = '自动化测试结果。。。' + t
    content = 'Python 自动化测试发邮件////。。。'

    msg = MIMEText(content,'plain','utf-8')
    msg['Subject'] = Header(subject,'utf-8')
    msg['From'] = sender
    msg['To'] = receiver

    try:
        s = smtplib.SMTP()
        s.connect(smtpdsever)
        s.login(username,password)
        s.sendmail(sender,receiver,msg.as_string())
    except Exception as msg:
        logger.info(f'邮件发送失败：{msg}')
    else:
        logger.info('邮件发送成功')
    finally:
        s.quit()

if __name__ == '__main__':
    sendEmail()
