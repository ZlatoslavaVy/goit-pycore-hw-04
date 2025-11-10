def total_salary(path: str): 
    total = 0
    developers = 0 
    average = 0
    try: 
        with open(path, mode='r', encoding='utf-8') as file:

            for line in file:
                clean_line = line.strip() 
                clean_line = clean_line.split(',') 
                salary = int(clean_line[1])
                total += salary
                developers += 1
            print(total, developers)
            average = total // developers
            print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
    except FileNotFoundError:
        print("Помилка: Файл не знайдено.")
    except UnicodeDecodeError:
        print("Помилка: Проблема з кодуванням символів.")
    return total, average

total_salary(r'D:\My_repo\goit-pycore-hw-04\topic6_task1\salary_file.txt')