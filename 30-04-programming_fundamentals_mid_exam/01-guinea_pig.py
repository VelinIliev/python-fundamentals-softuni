food_per_month = float(input()) * 1000
hay = float(input()) * 1000
cover = float(input()) * 1000
weight = float(input()) * 1000

everythingOK = True

for day in range(1, 31):
    food_per_month -= 300
    if day % 2 == 0:
        hay -= food_per_month * .05
    if day % 3 == 0:
        cover -= weight / 3
    if food_per_month <= 0 or hay <= 0 or cover <= 0:
        print("Merry must go to the pet store!")
        everythingOK = False
        break

if everythingOK:
    print(f"Everything is fine! Puppy is happy! Food: {food_per_month/1000:.2f}, Hay: {hay/1000:.2f}, Cover: {cover/1000:.2f}.")