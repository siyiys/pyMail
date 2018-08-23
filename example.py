# -*- coding: utf-8 -*
import pyMail

#初始化接收邮件类
rml = pyMail.ReceiveMailDealer('mail_address','mail_pwd','imap.gmail.com')
rml.select('INBOX')

#获取所有邮件列表
maillist=rml.getAll()#('OK',['1 2 3 4'])
#遍历最新的一封邮件读邮件，ID最大的一个。
for num in list(maillist)[1][0].split():
    if num != '' and num == max(list(maillist)[1][0].split()):
        mailInfo = rml.getMailInfo(num)
        print mailInfo['subject']
        #print mailInfo['body']
        print mailInfo['html']
        #print mailInfo['from']
        #print mailInfo['to']
        #遍历附件列表
        for attachment in mailInfo['attachments']:
            fileob = open(attachment['name'],'wb')
            fileob.write(attachment['data'])
            fileob.close()


#初始化发送邮件类
sml = mailUtils.SendMailDealer('mail_address','mail_pwd','smtp.gmail.com')
#设置邮件信息
sml.setMailInfo('paramiao@gmail.com','测试','正文','plain','/home/paramiao/resume.html')
#发送邮件
sml.sendMail()
