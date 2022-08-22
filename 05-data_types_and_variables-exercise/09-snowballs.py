number_of_snowballs = int(input())

best_value = 0
best_value_weight = 0
best_value_speed = 0
best_value_quality = 0

for snowball in range(number_of_snowballs):
    weight_of_snowball = int(input())
    time_needed_to_hit_target = int(input())
    quality_of_snowball = int(input())
    value = (weight_of_snowball / time_needed_to_hit_target) ** quality_of_snowball

    if value > best_value:
        best_value = value
        best_value_weight = weight_of_snowball
        best_value_speed = time_needed_to_hit_target
        best_value_quality = quality_of_snowball

print(f"{best_value_weight} : {best_value_speed} = {int(best_value)} ({best_value_quality})")
