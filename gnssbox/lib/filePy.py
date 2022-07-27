# 获取文件夹内所有文件目录
def getFileInPath(path):
    import os
    all_file = []
    for f in os.listdir(path):
        f_name = os.path.join(path, f)
        all_file.append(f_name)
    return all_file


# 新建文件目录
def mkdir(path, isdel=False):
    'If the folder exists and isdel is true, the folder is emptied'
    import os
    # 去除首行空格
    path = path.strip()
    # 去除尾部\符号
    path = path.rstrip('\\')
    if path == '':
        path = '.'
    # 判断路径是否存在
    isExists = os.path.exists(path)
    if not isExists:
        print(path + ' created successfully')
        os.makedirs(path)
        return True
    else:
        print(path + ' already exists')
        return False


def batchcompress(path, compressType):
    import subprocess
    filelist = getFileInPath(path)
    if compressType == 'Z':
        for file in filelist:
            args = 'compress ' + file
            subprocess.Popen(args=args, shell=True)
