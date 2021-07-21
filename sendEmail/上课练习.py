import smtplib,time
from email.mime.text import MIMEText
from email.header import Header
from logs import logger

def sendtext():
    sender = '15081860930@163.com'
    reciver = ['177416454@qq.com','forget0930@163.com']
    smtpserver = 'smtp.163.com'
    t = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
    subject = '自动化测试结果，，，' + t
    username = '15081860930'
    password = 'DTPOWPQMXVDIEVJC'
    context = 'Python 发送邮件测试。。。'
    msg = MIMEText(context,'plain','utf-8')
    msg['Subject'] = Header(subject,'utf-8')
    msg['From'] = sender
    msg['To'] = ';'.join(reciver)
    try:
        s = smtplib.SMTP()
        s.connect(smtpserver)
        s.login(username,password)
        s.sendmail(sender,reciver,msg.as_string())
    except Exception as msg:
        logger.info(f'邮件发送失败！{msg}')
    else:
        logger.info('邮件发送成功')
    finally:
        s.quit()
        # s.close()

if __name__ == '__main__':
    sendtext()