import smtplib
import pexpect
m_p=pexpect.spawn('python gmail.py')
m_p.timeout=60
m_p.expect('gamil')
m_p.sendline('yadav.pankit9894@gmail.com')
m_p.expect('Password:')
m_p.sendline('')
m_p.expect('to')
m_p.sendline('shivamchourasiya190@gmail.com')
m_p.expect('sub')
m_p.sendline('hello C')
m_p.expect('mes')
m_p.sendline('hellllooo shivam')
m_p.close()
