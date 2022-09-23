queue = int(input())
state_of_lift = input().split(" ")
state_of_lift = [int(number) for number in state_of_lift]

capacity_per_wagon = 4

for i, wagon in enumerate(state_of_lift):
    if wagon < capacity_per_wagon:
        if queue - (capacity_per_wagon - wagon) >= 0:
            state_of_lift[i] += capacity_per_wagon - wagon
            queue -= capacity_per_wagon - wagon
        else:
            state_of_lift[i] += queue
            queue -= queue

if queue == 0 and sum(state_of_lift) < len(state_of_lift) * 4:
    print("The lift has empty spots!")
elif queue > 0:
    print(f"There isn't enough space! {queue} people in a queue!")

state_of_lift = [str(x) for x in state_of_lift]
print(" ".join(state_of_lift))

# Write a program that finds a place for the tourist on a lift.
# Every wagon should have a maximum of 4 people on it. If a wagon is
# full, you should direct the people to the next one with space available.
# Input
# •	On the first line, you will receive how many people are waiting to get on the lift
# •	On the second line, you will receive the current state of the
# lift separated by a single space: " ".
# Output
# When there is no more available space left on the lift, or there are
# no more people in the queue, you should print on the console the final
# state of the lift's wagons separated by " " and one of the following messages:
# •	If there are no more people and the lift have empty spots, you should print:
# "The lift has empty spots!
# {wagons separated by ' '}"
# •	If there are still people in the queue and no more available space, you should print:
# "There isn't enough space! {people} people in a queue!
# {wagons separated by ' '}"
# •	If the lift is full and there are no more people in the queue, you should
# print only the wagons separated by " "
