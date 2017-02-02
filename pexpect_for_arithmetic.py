import pexpect
import sys
m = pexpect.spawn('python arithmetic_pexpect.py')
m.logfile_read = sys.stdout#to see the execution
m.expect("Enter the first input")
m.sendline("10")
m.expect("Enter the second input")
m.sendline("20")
m.expect('\n')
m.close()

