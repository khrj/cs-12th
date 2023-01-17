seconds = int(input("seconds: "))
mins = seconds // 60
seconds_without_mins = seconds % 60
print(f"{seconds} seconds is {mins}min {seconds_without_mins}sec")