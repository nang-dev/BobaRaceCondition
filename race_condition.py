
# Example of a race condition with a shared variable
from threading import Thread
 
def set_one(amount, repeats):
    global value
    for _ in range(repeats):
        value = amount
 
def set_two(amount, repeats):
    global value
    for _ in range(repeats):
        value = amount
 
# define the global variable
value = 0
# start a thread making the value 1
set_one_thread = Thread(target=set_one, args=(1, 10000000))
set_one_thread.start()
# start a thread making the value 2
set_two_thread = Thread(target=set_two, args=(2, 10000000))
set_two_thread.start()
# wait for both threads to finish
# print('Waiting for threads to finish...')
set_one_thread.join()
set_two_thread.join()
# report the value
print(f'Value: {value}')

# Result, some of the times, the shared value is 1, sometimes its 2.