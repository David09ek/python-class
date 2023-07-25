# #Assessment:
names_list = ['james Mark', 'Fredrick Logan', 'Marcus Her-lin', 'Ekeleme David', 'isaballe Mon-tel']
num_names = len(names_list)
first_names = []
last_names = []
def process_names(names_list : list)->tuple:
    for i in names_list:
        first_names.append(i.split(' ')[0])
        last_names.append(i.split(' ')[1])
        
process_names(names_list)
print(f'Num:{num_names}, first: {first_names}, last: {last_names}')

