class Pet:
    def __init__(self, name = "", gender = "", age = 0):
        self.name = name
        self.gender = gender
        self.age = age

    def init_from_dict(self, event_dict):
        self.name = "Имя котейки: " + event_dict.get("name")
        self.gender = "Пол котейки: " + event_dict.get("gender")
        if event_dict.get("age") > 0 and isinstance(event_dict.get("age"), int):
            self.age = "Возраст котейки: " + str(event_dict.get("age"))
        else:
            print( "Некорректный ввод характеристики age", (event_dict.get("age")) )
    

