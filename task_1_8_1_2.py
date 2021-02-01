from task_1_8_1 import Pet

pets = [
    {
    "name": "Сем",
    "gender": "Мальчик",
    "age": 2
    }
    ,
    {
    "name": "Борис",
    "gender": "Мальчик",
    "age": 2
    }
]

for pet in pets:
    pet_obj = Pet()
    pet_obj.init_from_dict(pet)
    print( pet_obj.name, pet_obj.gender, pet_obj.age, sep = "\n" )
    

