#Author: Xinnan SHEN
#Student ID: 1051380
#File Name: crawl.py
#Usage: Drawing the figure of results
import matplotlib.pyplot as plt
def main():
	name_list = ['2 hidden layers','3 hidden layers','4 hidden layers']
	pre_list = [0.800,0.847,0.762]
	rec_list=[0.960,1.000,0.960]
	f1_list=[0.873,0.917,0.849]
	total_width, n = 0.7, 3
	width = total_width / n
	x =[0,1,2]
	plt.bar(x, pre_list, width=width, label='Precision',fc = 'g')
	for i in range(len(x)):
 		x[i] = x[i] + width
	plt.bar(x, rec_list, width=width, label='Recall',tick_label = name_list,fc = 'r')
	for i in range(len(x)):
 		x[i] = x[i] + width
	plt.bar(x, f1_list, width=width, label='F1-score',tick_label = name_list,fc = 'b')
	plt.legend()
	plt.show()
	return
if __name__ == '__main__':
	main()
