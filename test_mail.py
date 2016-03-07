#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
from email.mime.text import MIMEText
import smtplib

class Mailer:
	def __init__(self, smtp_server, login, password, from_addr, sign=None):
		self.smtp_server = smtp_server
		self.login = login
		self.password = password
		self.from_addr = from_addr
		self.sign = sign
	
	def static_addr(self, static_to):
		self.static_to = static_to

	def static_subj(self, static_subj):
		self.static_subj = static_subj

	def __date_time__(self):
		return time.strftime('%Y.%m.%d %H:%M:%S', time.localtime(time.time()))

	def send_mail(self, msg=None, dyn_subj=None, dyn_to=None):
		if not msg:
			msg = 'There was a terrible error that occured and I want you to know!'
		msg += '\n\nTime: ' + self.__date_time__()
		if self.sign: msg += '\n'+str(self.sign)
		to_addr = dyn_to if dyn_to else self.static_to
		msg = MIMEText(msg)
		msg['Subject'] = dyn_subj if dyn_subj else self.static_subj
		msg['From'] = self.from_addr
		msg['To'] = to_addr
		server = smtplib.SMTP(self.smtp_server)
		server.starttls()
		server.login(self.login, self.password)
		server.sendmail(self.from_addr, to_addr, msg.as_string())
		server.quit()
