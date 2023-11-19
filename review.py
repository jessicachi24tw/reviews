review = []
with open ('reviews.txt', 'r')as f:
	for line in f:
		review.append(line)
print(len(review))
print(review[0])

print('-------')

review = []
count = 0
with open ('reviews.txt', 'r')as f:
	for line in f:
		review.append(line)
		count += 1
		if count % 10000 == 0: #求餘數% 意即是10000的倍數
			print(len(review))