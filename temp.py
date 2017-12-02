import pigpio
from time import sleep
for i in range(100):
    pi=pigpio.pi()
    import DHT22
    s=DHT22.sensor(pi,4)
    s.trigger()
    sleep(2)
    print('{:3.2f}'.format(s.humidity()/1.))
    print('{:3.2f}'.format(s.temperature()/1.))
    s.cancel()
    pi.stop()