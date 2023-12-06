"""
Є список, кожен елемент якого є словником з контактами користувача наступного виду:

    {
    "name": "Allen Raymond",
    "email": "nulla.ante@vestibul.co.uk",
    "phone": "(992) 914-3792",
    "favorite": False,
}
Словник містить ім'я користувача name, його email, телефонний номер phone та властивість favorite - обраний контакт чи ні.

Розробіть дві функції для серіалізації та десеріалізації списку контактів за допомогою пакету csv та зберігання отриманих даних у текстовому файлі.

Перша функція write_contacts_to_file приймає два параметри: filename - ім'я файлу, contacts - список контактів. Вона зберігає вказаний список у файлі формату csv.

Структура csv файлу має бути такою:

name,email,phone,favorite
Allen Raymond,nulla.ante@vestibul.co.uk,(992) 914-3792,False
Chaim Lewis,dui.in@egetlacus.ca,(294) 840-6685,False
Kennedy Lane,mattis.Cras@nonenimMauris.net,(542) 451-7038,True
Wylie Pope,est@utquamvel.net,(692) 802-2949,False
Cyrus Jackson,nibh@semsempererat.com,(501) 472-5218,True
Зверніть увагу, першим рядком у файлі йдуть заголовки – це назви ключів.

Друга функція read_contacts_from_file читає, виконує перетворення даних та повертає вказаний список contacts із файлу filename,
збереженого раніше функцією write_contacts_to_file.

Примітка: При читанні файлу csv ми отримуємо властивість словника favorite у вигляді рядка, тобто. наприклад favorite='False'.
Необхідно його привести до логічного виразу назад, щоб стало favorite=False.
"""

import csv


def write_contacts_to_file(filename, contacts):
    with open(filename, 'w', newline='') as fh:
        field_names = ['name', 'email', 'phone', 'favorite']
        writer = csv.DictWriter(fh, fieldnames=field_names)
        writer.writeheader()

        for item in contacts:
            writer.writerow({'name': item['name'], 'email': item['email'], 'phone': item['phone'], 'favorite': item['favorite']})


def read_contacts_from_file(filename):

    result = []

    with open(filename, 'r', newline='') as fh:
        reader = csv.DictReader(fh)
    
        for row in reader:
            favorite = False if row['favorite'] == 'False' else True
            result.append({'name':row['name'], 'email':row['email'], 'phone':row['phone'], 'favorite':favorite})

    return result


if __name__ == "__main__":

    contacts = [
        {
            "name": "Allen Raymond",
            "email": "nulla.ante@vestibul.co.uk",
            "phone": "(992) 914-3792",
            "favorite": False,
        },
        {
            "name": "Chaim Lewis",
            "email": "dui.in@egetlacus.ca",
            "phone": "(294) 840-6685",
            "favorite": False,
        }
    ]

    # write_contacts_to_file('ex_03.csv', contacts)

    print(read_contacts_from_file('ex_03.csv'))
