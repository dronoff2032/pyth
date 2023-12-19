import time
import random
import json
import csv

with open('name.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    name = None
    while (name == None):
        name = str(input("Введите свое имя: "))
    writer.writerow(name)

defaultdata = {
        'choice': 0,
        'mayorChoice': 0,
        'demonstrationChoice': 0
}

def readdata():
    with open('save.json', 'r') as file:
        data = json.load(file)
    return data

def writedata(data):
    with open('save.json', 'w') as file:
        json.dump(data, file, indent=4)

choice = readdata()['choice']
demonstrationChoice = readdata()['demonstrationChoice']
mayorChoice = readdata()['mayorChoice']

def newline(text):
    print(text)
    time.sleep(1)

def print_candidates():
    candidates = [
        {
            'number': 1,
            'description': 'Старый политик с многолетним опытом. Всегда готов к жестким мерам и враждебен к критике.',
            'traits': ['Привлекает своим опытом', 'Поддерживает сильную внешнюю политику', 'Не терпит критики']
        },
        {
            'number': 2,
            'description': 'Энергичный и молодой человек, не имеющий опыта в политике. Умеет вдохновлять красочными выступлениями.',
            'traits': ['Предлагает свежий взгляд на проблемы', 'Поддерживает инновации', 'Стремится к открытости и прозрачности']
        },
        {
            'number': 3,
            'description': 'Загадочная личность. Враждебен ко многим и предлагает нестандартные решения.',
            'traits': ['Поддерживает экзотические идеи', 'Против привычных порядков', 'Не привязан к традиционным структурам']
        }
    ]

    print("Список кандидатов: ")
    for candidate in candidates:
        print(f"{candidate['number']}. {candidate['description']}")
        print(f"- {candidate['traits']}")
        print()

def print_outcomes(win):
    outcomes = {
            1: {
                'text': "Первый кандидат победил.",
                'details': [
                    "После того, как он встал на пост мера, город стал более дисциплинированным.",
                    "Он улучшал его, вводил новые законы и правила.",
                    "Однако, он был слишком строг к тем, кто говорит что-то против него.",
                    "Все эти люди сразу отправлялись на исправительные работы."
                ]
            },
            2: {
                'text': "Второй кандидат победил.",
                'details': [
                    "После избрания он придал городу новый взгляд на проблемы.",
                    "Привнес инновации и стал сторонником открытости и прозрачности.",
                    "Его красочные выступления вдохновляли граждан на активное участие в общественной жизни."
                ]
            },
            3: {
                'text': "Третий кандидат победил.",
                'details': [
                    "Город стал местом экзотических идей и нестандартных решений.",
                    "Он противился привычным порядкам и не привязан к традиционным структурам.",
                    "Несмотря на враждебное отношение к многим, его поддерживали те, кто разделял его видение будущего."
                ]
            }
    }

    outcome = outcomes.get(win)
    if outcome:
        print(outcome['text'])
        for detail in outcome['details']:
            newline(detail)


def print_demonstrations_variants():
    variants = [
        {
            'number': 1,
            'description': 'Принять участие в митинге за действующего мера.',
        },
        {
            'number': 2,
            'description': 'Принять участие в митинге против действующего мера.',
        },
        {
            'number': 3,
            'description': 'Остаться дома и понаблюдать за исходом через СМИ',
        }
    ]

    print("Варианты действий: ")
    for solution in variants:
        print(f"{solution['number']}. {solution['description']}")
        print()

def print_demonstrations_outcomes(win):
    outcomes = {
            1: {
                'text': "Вы приняли участие в митинге за действующего мера.",
            },
            2: {
                'text': "Вы приняли участие в митинге против действующего мера.",
            },
            3: {
                'text': "Вы приняли решение остаться дома.",
            }
    }

    outcome = outcomes.get(win)
    if outcome:
        newline(outcome['text'])

if (choice == 0):
    newline("Вы - обычный житель маленького города..")
    newline("Сегодня наступил день важных выборов мэра.")
    choice = None
    while (choice != "Да" and choice != "Нет"):
        choice = input("Хотите ли вы проголосовать? (Да или Нет): ")
    existdata = readdata()
    existdata['choice'] = choice
    writedata(existdata)

if (mayorChoice == 0):
    if (choice == "Да"):
        newline("Вы решаете проголосовать за одного из кандидатов.\n\n")

        print_candidates()

        while (mayorChoice != 1 and mayorChoice != 2 and mayorChoice != 3):
            try:
                mayorChoice = int(input("Выберите кандидата, за которого хотите проголосовать (1-3): "))
            except ValueError:
                print("Пожалуйста, введите число от 1 до 3.")
    else:
        mayorChoice = None
        print("Вы приняли решение воздержаться от своего голоса.")

    mayorChoiceRand = random.randint(1, 3)
    newline("\nВ скором времени вам стали известны результаты голосования.")

    if (mayorChoice != None and mayorChoice != mayorChoiceRand):
        newline("К сожалению, ваше голос ничего не решил.")

    print_outcomes(mayorChoiceRand)

    if (mayorChoice != None and mayorChoice == mayorChoiceRand):
        newline("\n\nВы сделали правильный выбор.")

    print("<= Следующий день =>")

    newline("\nНа следующий день город просыпается под властью нового мэра.")
    newline("Все жители в ожидании перемен.")
    newline("Первые дни проходят под знаком активных реформ и изменений в городской жизни.")

    if mayorChoice == 1:
        print("\nСтарый политик принимает жесткие меры, начиная с борьбы с преступностью и коррупцией.")
        print("Город становится более дисциплинированным, но не все жители одобряют такой подход.")
    elif mayorChoice == 2:
        print("\nМолодой мэр приносит в город свежий взгляд и начинает внедрять инновации.")
        print("Он становится сторонником открытости и прозрачности.")
        print("Граждане вдохновляются его красочными выступлениями и активно участвуют в общественной жизни.")
    else:
        print("\nЗагадочный мэр создает атмосферу экзотики и нестандартных решений.")
        print("Привычные порядки нарушаются, и город становится местом для развития уникальных идей.")
        print("Хотя не все поддерживают его, те, кто разделяет его видение, считают это интересным временем для города.")

    newline("\nС каждым днем мэр продолжает внедрять свои идеи, но сопротивление со стороны оппозиции усиливается.")
    newline("Горожане оказываются втянутыми в волнующие события, и жизнь в городе продолжает меняться.")
    newline("В один день вы узнаете о двух согласованых митингах: в поддержку нового мера и против.\n")
    existdata = readdata()
    existdata['mayorChoice'] = mayorChoice
    writedata(existdata)

if (demonstrationChoice == 0):
    print_demonstrations_variants()
    while (demonstrationChoice != 1 and demonstrationChoice != 2 and demonstrationChoice != 3):
        try:
            demonstrationChoice = int(input("Решите как поступите в данной ситуации (1-3): "))
        except ValueError:
                print("Пожалуйста, введите число от 1 до 3.")

    print_demonstrations_outcomes(demonstrationChoice)

    if (mayorChoice != None and mayorChoice == mayorChoiceRand and demonstrationChoice != None and demonstrationChoice == 1):
        newline("В итоге оппозиция смирилась с курсом действующего мера и признала поражение.")
        newline("В том числе благодаря вашему участию вы сделали город лучше.")
    elif (mayorChoice != None and mayorChoice == mayorChoiceRand and demonstrationChoice != None and demonstrationChoice == 2):
        newline("В конце концов митинг ничего не решил и участники мирно разошлись.")
        newline("Несмотря на ваше участие в городе продолжилась активная политическая жизнь.")
    elif (mayorChoice != None and mayorChoice != mayorChoiceRand and demonstrationChoice != None and demonstrationChoice == 1):
        newline("Хотя это было неожиданным решением, но митинг ничего не решил и участники мирно разошлись.")
        newline("Несмотря на ваше участие в городе продолжилась активная политическая жизнь.")
    elif (mayorChoice != None and mayorChoice != mayorChoiceRand and demonstrationChoice != None and demonstrationChoice == 2):
        newline("В итоге оппозиция вынудила действующего мера и его сторонников пойти к вам на встречу.")
        newline("В том числе благодаря вашему участию вы сделали город лучше.")
    else:
        newline("Хотя вы и решили пронаблюдать со стороны, но в итоге вам стало скучно.")
        newline("В конце концов вы перестали интересоваться политикой и сосредоточились на личной жизни.")
    existdata = readdata()
    existdata['demonstrationChoice'] = demonstrationChoice
    writedata(existdata)

name = []
with open('name.csv', 'r', newline='') as csvfile:
    get = csv.reader(csvfile)
    for row in get:
        name.append(row)
    result = (''.join(name[0]))
    print(f'\n\nИгрок {result}, поздравляем с прохождением игры!')