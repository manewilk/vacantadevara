import time

n= 100000

start_time = time.time()
l = []
for i in range(n):
    l.append(i * 2)
print(time.time() - start_time)


# In the following example, we will compare the different approaches and calculate their run times. To understand the following program, you need to know that time.time() returns a float number, the time in seconds since the so-called ,,The Epoch''1. time.time() - start_time calculates the time in seconds used for the for loops:


# import time

# n= 100000

# start_time = time.time()
# l = []
# for i in range(n):
#     l = l + [i * 2]
# print(time.time() - start_time)


# start_time = time.time()
# l = []
# for i in range(n):
#     l += [i * 2]
# print(time.time() - start_time



# start_time = time.time()
# l = []
# for i in range(n):
#     l.append(i * 2)
# print(time.time() - start_time)