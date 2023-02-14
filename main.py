import subprocess
import multiprocessing as mp

host_LinkedIn = 'linkedin.com'
host_gitHub = 'github.com'
host_Reddit = 'reddit.com'
host_Google = 'google.com'

def ping(host):
    command = ['ping', host]
    return subprocess.call(command)

if __name__ == '__main__':

    p1 = mp.Process(target=ping, args=(host_LinkedIn,))
    p2 = mp.Process(target=ping, args=(host_gitHub,))
    p3 = mp.Process(target=ping, args=(host_Reddit,))
    p4 = mp.Process(target=ping, args=(host_Google,))

    p1.start()
    p2.start()
    p3.start()
    p4.start()

    print(ping(host_LinkedIn))
    print(ping(host_gitHub))
    print(ping(host_Reddit))
    print(ping(host_Google))




