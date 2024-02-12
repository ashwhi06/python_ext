def hello():
    print("Hello from inside the function!")

hello()

def pack(age,name,sign):
    return [age,name,sign]

print(pack(20,"John","Virgo"))

def eat_lunch(food_list):
    if not food_list:
        print("My lunchbox is empty!")
    else: 
        print("First I eat",food_list[0])
        for food in food_list[1:]:
            print("Next I eat",food)
foods=["pizza","pasta","salad"]
eat_lunch(foods)