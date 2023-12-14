# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных

def add_contact(phonebook):
    name=input("Введите имя контакта: ")
    last_name=input("Введите фамилию контакта: ")
    phone_number=input("Введите номер телефона контакта: ")
    
    if name in phonebook or last_name in phonebook: 
        print("Контакт уже существует") 
    else: 
        phonebook[name] =phone_number
        phonebook[last_name] =phone_number
        print("Контакт успешно добавлен")
def update_contact(phonebook): 
    name_or_last_name=input("Введите имя или фамилию контакта: ")
    
    if name_or_last_name in phonebook: 
        new_phone_number=input("Введите новый номер телефона: ")
        phonebook[name_or_last_name] =new_phone_number
        print("Контакт успешно обновлен") 
    else: 
        print("Контакт не найден")
def remove_contact(phonebook):
    name_or_last_name=input("Введите имя или фамилию контакта: ")
    if name_or_last_name in phonebook: 
        phone_number=phonebook.pop(name_or_last_name) 
        print(f"Контакт {name_or_last_name}с номером телефона {phone_number}успешно удален") 
    else: 
        print("Контакт не найден")
def main():
    phonebook={}
    while True: 
        print("1. Добавить контакт") 
        print("2. Изменить контакт") 
        print("3. Удалить контакт") 
        print("0. Выход")
        
        choice = input("Выберите операцию: ")
        if choice=="1": 
            add_contact(phonebook)
        elif choice=="2":
            update_contact(phonebook) 
        elif choice=="3":
            remove_contact(phonebook)
        elif choice=="0":
            break
        else: 
            print("Некорректный выбор")
if __name__== "__main__": 
    main()
