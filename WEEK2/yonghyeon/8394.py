#1명이면 안하는 경우 밖에 없음 : 1
#2명이면 안하는 경우, 둘이서 하는 경우 : 2
#3명이면 1,2번 악수. 2,3,번 악수, 1,3번 악수 :3
#4명이면  4번이 안하는 경우 1,2 3번이 안하는 경우 1,4 2번이 안하는 경우 3,4 1번이 안하는 경우 2,3, 다 안하는 경우 X
# -> 5가지
#5명이면  1번x 2,3 3,4 5,4 2번x 5,1 3번x 1,2 4번x 5,3 5번x 4,1 다 안함 1 -> 8가지

n = int(input())

li = [1,2,3]

for i in range(3, n):
    li.append(li[i-1]+li[i-2])

print(str(li[-1]))
