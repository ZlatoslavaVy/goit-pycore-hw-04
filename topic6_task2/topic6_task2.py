from pathlib import Path


def get_cats_info(path: str):
    cats_list = []    
    try:
        with open(path, mode='r', encoding='utf-8') as file:
            for line in file:
                clean_line = line.strip() 
                if not clean_line:
                    continue   
                try:
                    clean_line = clean_line.split(',') 
                    cat_dict = {
                        "id": clean_line[0],
                        "name": clean_line[1],
                        "age": clean_line[2]
                        }
                    cats_list.append(cat_dict)
                except IndexError:
                    print(f"Попередження: Рядок '{clean_line}' має неправильний формат і буде пропущений.")
        return cats_list 
    except FileNotFoundError:
        print(f"Помилка: Файл за шляхом '{path}' не знайдено.")
        return []

cats_info = get_cats_info(r"D:\My_repo\goit-pycore-hw-04\topic6_task2\cats_file.txt")
print(cats_info)
