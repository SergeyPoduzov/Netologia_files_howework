
# первая задача
filename=r'files\recipes.txt'
with open(filename,encoding='utf-8') as file_object:
  indigrients2=file_object.readlines()

for line in indigrients2:
    line=line.rstrip('\n')


dict=[] #промежточный списко

cook_book ={} #итоговй словаь

 #Последовательно удаляем последний элемент списка, проверяя его на длину и на тип, и добавляее его в словарь.
while indigrients2:

    dict_new = {}
    poped_kitchen=indigrients2.pop()
    poped_kitchen=poped_kitchen.split()

    if len(poped_kitchen)>2:

        dict_new = {}
        dict_new['measure']=poped_kitchen[-1]
        dict_new['quantity']=int(poped_kitchen[-3])

        #Удаляем последние у элемента '|', '2', '|', 'шт'
        poped_kitchen.pop()
        poped_kitchen.pop()
        poped_kitchen.pop()
        poped_kitchen.pop()

        dict_new['ingredient_name']=(' '.join(poped_kitchen))

        dict.append(dict_new)
        continue

    if len(poped_kitchen)==1 and (type(int(poped_kitchen[0])==int)):

        popped_name=indigrients2.pop()
        cook_book[popped_name.rstrip('\n')] = dict
        dict = []
        continue
    if len(poped_kitchen)==1 and (type(poped_kitchen)==str):
        continue

#Итоговый результат  cook_book
print("Итоговый результат первой задачи: ")
for elem in  cook_book:
    print (elem,": ",  cook_book[elem])

#Решаем вторую задачу

def get_shop_list_by_dishes(dishes, person_count):
    cook_book_oreder = {}

    elem={}
    for eda in dishes:
        for spisok_eda in cook_book[eda]:# полусили один элемент из списка [{'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},    {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},    {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
            if spisok_eda['ingredient_name'] in cook_book_oreder:

                m=cook_book_oreder[spisok_eda['ingredient_name']]

                m['quantity'] +=spisok_eda['quantity']*person_count

            else:
                elem={}
                elem['measure']=spisok_eda['measure']
                elem['quantity']=spisok_eda['quantity']*person_count
                cook_book_oreder[spisok_eda['ingredient_name']]=elem
                elem={}
    return cook_book_oreder


dishes=['Запеченный картофель', 'Омлет','Утка по-пекински']
cook_book_oreder=get_shop_list_by_dishes(dishes, 10)
# print(cook_book_oreder)

print("\nИтоговый результат второй задачи: ")

for elem in cook_book_oreder:
    print (elem,": ", cook_book_oreder[elem] )



