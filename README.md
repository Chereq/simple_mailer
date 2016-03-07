# simple_mailer
Simple Python SMTP-mailer class

## Usage:

mailer = simple_mailer('smtp.DOMAIN.COM', 'LOGIN', 'PASSWORD', 'FROMADDR@DOMAIN.COM')<br />
mailer.static_addr('TO@ADDR.COM')<br />
mailer.static_subj('Hello World!')<br />
mailer.static_sign('send by send_mail.py')<br />
mailer.send_mail('Hello World!')<br />
mailer.send_mail(open('simple_mailer.py','r').read(), 'mailer source', 'TO2@ADDR.COM')
