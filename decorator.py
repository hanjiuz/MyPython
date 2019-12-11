#decorator in python

import time

def timer(func):
	def decorator(*args, **kwds):
		t1 = time.time()
		func(*args, **kwds)
		t2 = time.time()
		print('time eclipse between func: %0.4f'%(t2-t1))
	return decorator

@timer
def do_something(delay):
	print("start to do_something")
	time.sleep(delay)
	print("stop from do_something")

do_something(3)


def want_sleep(delay):
	assert isinstance(delay, (int, float)), "sleep time need to be int or float! - "+repr(delay)
	time.sleep(delay)

want_sleep(2)
want_sleep(3.4)
want_sleep('2.3')
print("can you see me?")
