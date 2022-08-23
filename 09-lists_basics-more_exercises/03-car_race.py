times_as_str = input()
times_str = times_as_str.split(" ")
times = [int(time) for time in times_str]

left_racer_time = 0

for i in range(int(len(times) / 2)):
    if times[i] == 0:
        left_racer_time *= .8
    else:
        left_racer_time += times[i]

right_racer_time = 0

for i in range(1, int(len(times) / 2) + 1):
    if times[i * -1] == 0:
        right_racer_time *= .8
    else:
        right_racer_time += times[i * -1]
    # print(times[i*-1], i*-1)
    # print(i)

if left_racer_time < right_racer_time:
    print(f'The winner is left with total time: {left_racer_time:.1f}')
else:
    print(f'The winner is right with total time: {right_racer_time:.1f}')