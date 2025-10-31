def total_salary(path: str): 
    with open(path, mode='w', encoding='utf-8') as file:
        file.write("""Alex Korp,3000
Nikita Borisenko,2000 
Sitarama Raju,1000""" )
        
    total = 0
    developers = 0  
    with open(path, mode='r', encoding='utf-8') as file:

        for line in file:
            clean_line = line.strip() 
            clean_line = clean_line.split(',') 
            print(clean_line)
            salary = int(clean_line[1])
            total += salary
            developers += 1
        print(developers)
        average = total // developers
        print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
    return total, average

total_salary('salary_file.txt')