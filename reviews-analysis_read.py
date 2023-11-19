review = []
sum_len = 0
with open ('reviews.txt', 'r')as f:
	for line in f:
		review.append(line)
		sum_len += len(line)
print(sum_len)
print('每一筆留言的平均長度為', sum_len/len(review))