import random as r

num_videos = [28, 48, 19]
total = sum(num_videos)
order = []

while total > 0:
    i = r.randint(0, 2)
    if num_videos[i] > 0:
        num_videos[i] -= 1
    # print(i)
    order.append(i)
    total = sum(num_videos)

print(order)
