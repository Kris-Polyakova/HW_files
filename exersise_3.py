files = ['1.txt', '2.txt','3.txt']    

def merge_files(files_list = list, final_file_name = str):
    result_list = []
    for file_name in files_list:
        with open (file_name, 'r', encoding = 'utf-8') as file:
            file_list = [line.strip() for line in file]
            file_list = [file.name] + [len(file_list)] + file_list
            result_list += [file_list]
            
    result_list.sort(key=len)
    
    with open (final_file_name, 'a', encoding = 'utf-8') as result_file:
        for lines in result_list:
            for line in lines:
                write_str = str(line) + '\n'
                result_file.writelines(write_str)
    
merge_files(files, 'result.txt')