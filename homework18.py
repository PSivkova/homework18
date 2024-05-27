# Создайте новый класс Buiding с атрибутом total
# Создайте инициализатор для класса Buiding, который будет увеличивать атрибут
# количества созданных объектов класса Building total (по примеру класса Lemming из урока)
# В цикле создайте 40 объектов класса Building и выведите их на экран командой print

class Buiding:
    total = 0

    def __init__(self):
        Buiding.total += 1


objec = []
while len(objec) < 40:
    new_objec = Buiding()
    objec.append(new_objec)
print(Buiding.total)
print(objec)
