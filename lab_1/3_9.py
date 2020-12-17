# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
print("3.9")
num_list = [10, 2, 30, 100, 10, 50, 11, 30, 15, 7]
word_list = ['python', 'ruby', 'perl', 'ruby', 'perl', 'python', 'ruby', 'perl']
print(num_list)
num_list.reverse()
var1 = input('Your value = ')
var1 = int(var1)
index = num_list.index(var1)
print('Last index {}'.format(len(num_list)-index))
print('_'*50)
print(word_list)
word_list.reverse()
var2 = input('Your word = ')
index = word_list.index(var2)
print('Last index{}'.format(len(word_list)-index))