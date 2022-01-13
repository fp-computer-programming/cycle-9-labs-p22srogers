# Author: SMR (AMDG) 1/11/21
def add_foods(lst):
    sixth_letter=[]
    not_foods=[]
    short_foods=[]
    for x in lst:
        try:
            sixth_letter.append(x[5])
        except TypeError:
            not_foods.append(x)
        except IndexError:
            short_foods.append(x)

    print("sixth_letter: ", sixth_letter)
    print("not_foods: ", not_foods)
    print("short_foods: ", short_foods)
    
    add_foods(['potatoes','salsa','cherries','banana','apple'])
    add_foods(['naan','celery','buckwheat',7,'clementine'])
    add_foods(['cheeseburger',True,'chicken','rice','radish'])
    