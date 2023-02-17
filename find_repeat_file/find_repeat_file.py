import os

# 定义一个函数，递归查找目录中所有文件和文件夹中的文件
def find_files(folder, files_dict):
    for root, dirs, files in os.walk(folder):
        for filename in files:
            filepath = os.path.join(root, filename)
            if filename not in files_dict:
                files_dict[filename] = []
            files_dict[filename].append(filepath)
 
# 将文件字典输出到txt文件中
def output_files_to_txt(files_dict, filename):
    with open(filename, 'w') as f:
        for k, v in files_dict.items():
            if len(v) > 1:
                f.write(k + ':\n')
                for filepath in v:
                    f.write(filepath + '\n')
                f.write('\n')

# 调用函数
folder = 'F:\\'
files_dict = {}
find_files(folder, files_dict)
output_files_to_txt(files_dict, 'output.txt')
