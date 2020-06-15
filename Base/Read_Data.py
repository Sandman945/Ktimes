import os
import yaml


# def ret_yaml_data(file_name):
#     file_path = os.getcwd() + os.sep + "Data" + os.sep + file_name + ".yaml"
#     with open(file_path, "r", encoding='UTF-8') as f:
#         return yaml.load(f)

def yml_data_with_filename_and_key(file_name, key):
    file_path = "./Data/" + file_name + ".yaml"
    with open(file_path, "r", encoding='UTF-8') as f:
        data = yaml.load(f)[key]
        case_data_list = list()
        for case_data in data.values():
            case_data_list.append(case_data)
        return case_data_list
