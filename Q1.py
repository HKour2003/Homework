#write a python code to find index containing string :input:['Navya',98,'Hema','Siroj','Tarun',78,90,'Ramya']  ,output: 0 2 3 4 7

input_list = ['Navya', 98, 'Hema', 'Siroj', 'Tarun', 78, 90, 'Ramya']
output_indices = [str(i) for i, item in enumerate(input_list) if isinstance(item, str)]
output = ' '.join(output_indices)
print(output)
