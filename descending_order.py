user_data = [9,4,8,1,3,7,2,6,5,0]
for i in range(0, len(user_data)):
    for j in range(0, i):
        if user_data[i] > user_data[j]:
            user_data[i],user_data[j] = user_data[j], user_data[i]
print(user_data)

