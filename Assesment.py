#Assesment1 25/7/23
sentence = ['Goodday My name is john and im here for a job offer.', 'Today is indeed a great day and we all are happy ']
def longest_word(sentence):
    print(max(sentence))
longest_word(sentence)
    
    
# #Assesment2 25/7/23
list = [1, 'Mark', 367.23, 'jake', 90, 'fred', 3.554, 'Hen', 23]
new_list = []
def to_find_strings(list):
    for i in list:
        if i is str(i):
            new_list.append(i)
to_find_strings(list)
print(new_list)

#OR

random_stuffs = ['1', 'Mark', '367.23', 'jake', '90', 'fred', '3.554', 'Hen', '23']
def get_only_string_with_characters(lst):
    return [value for value in lst if value.isalpha()]
print(get_only_string_with_characters(random_stuffs))

#testing git taskbar

#2 Classwork
def find_common_elements(*d1):
    d1 = [1,2,3,4,5,6,9]
    d2 = [8,7,4,3,2,9,1]
    d3 = []
    for i in d1:
        if i in d2:
            d3.append(i)
    return d3
result = find_common_elements()
print(result)