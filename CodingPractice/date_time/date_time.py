'''
@author: Solrac
'''
import time

start_time=time.time()
t=(2014, 12, 9, 2, 30, 0, 2, 338, 0)
print("Current time", time.asctime())
print("Carlitos Bday", time.asctime(t))
print("current day of the week", time.strftime('%A'))
print("current day of the week", time.strftime('%a'))
print("current month of the week", time.strftime('%B'))
print("current month of the week", time.strftime('%b'))
print("current hour/min of the week", time.strftime('%H:%M'))
print("time", time.time())

name=input("Enter your name: ")
print("{} was logged at {}".format(name, time.strftime('%H:%M')))

end_time=time.time()-start_time
print("Running time: ", end_time)