import random


def delete_surnames(group, skip):
    for surname in skip:
        if surname not in group:
            continue
        group.remove(surname)
    
    return group

def create_queue_random(group: list, skip: list = []):
    group_set = set()
    
    group = delete_surnames(group=group, skip=skip)

    while len(group_set) != len(group):
        surname = random.choices(group)
        group_set.add(surname[0])
    
    return group_set

def output(group_set: list):
    for index in range(len(group_set)):
        print(f"{index+1}. {group_set[index]}")


if __name__ == "__main__":
    group = [
        "Бакалина",
        "Бакуткин",
        "Бойко",
        "Бояркин",
        "Водянов",
        "Глебов",
        "Гриднев",
        "Иванцов",
        "Коноплева",
        "Коняева",
        "Лунякова",
        "Медведев А",
        "Медведев М",
        "Мишин",
        "Песков",
        "Пономарев",
        "Проскурякова",
        "Пчелинцев",
        "Синякина",
        "Толстоухова",
        "Федоров",
        "Филинов",
        "Фомин",
        "Чернецов",
        "Шадчина",
        "Шепелев",
    ]
    skip = list(map(str, input("Введите фамилия для пропуска через пробел: ").split()))

    group_set = create_queue_random(group=group, skip=skip)
    output(group_set=list(group_set))
    input("нажмите ENTER чтобы закрыть")