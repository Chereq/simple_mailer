# simple_mailer
Simple Python SMTP-mailer class

## Usage:

mailer = Mailer('smtp.DOMAIN.COM', 'LOGIN', 'PASSWORD', 'FROMADDR@DOMAIN.COM')--
mailer.static_addr('TO@ADDR.COM')--
mailer.static_subj('Hello World!')--
mailer.static_sign('send by send_mail.py')--
mailer.send_mail('Hello World!')--
mailer.send_mail(open('simple_mailer.py','r').read(), 'mailer source', 'TO2@ADDR.COM')
