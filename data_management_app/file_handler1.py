code_set = set()
new_data_list = [] # list with dictionaries 

def retrieve_code_set():
    try:
        with open("code_set.txt", 'r') as code_setfile:
            lines = code_setfile.readlines()
            for line in lines:
                code_set.add(int(line.strip()))
    except:
        print("Code Set not retrieved")


def retrieve_data_by_code(code):
    data_dict = {"Name":'error',"Surname":"error","City":"error","Number":"error"}
    try:
        data_file = open("save.txt",'r')
        data_lines = data_file.readlines()
        for line in data_lines:
            data_list = line.split(',')
            temp_code = data_list[4].split(':')
            if (line.find(code) >0 and code == temp_code[1].replace(" ", "")):
                data_list = data_list[:-2]
                for i in range(len(data_list)):
                    sublist = data_list[i].split(':')
                    data_dict[sublist[0]] = sublist[1]
                break
            
            data_file.close()
    
    except:
        print("Error in Retrieving saved data")
    return data_dict

def empty_list():
    new_data_list = []

def add_new_data(data):
    new_data_list.append(data)
    
def add_code_to_set(code):
    code_set.add(code)

def code_in_set(code):
    return code in code_set

def save_code_set():
    codefile = open("code_set.txt",'w')
    for code in code_set:
        codefile.write(str(code)+"\n")
    codefile.close()
    
def save_new_data():
    try:
        global new_data_list
        save_file = open("save.txt",'a')
        line = ""
        for data in new_data_list:
            for key in data:
                line = line + key + ': ' + data[key] + ' ,'
                
            line += "\n"
            save_file.write(line)
            line = ""
        save_file.close()
    except:
        print("Data not Saved")