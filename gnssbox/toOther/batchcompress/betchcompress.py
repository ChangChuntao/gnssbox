# 获取文件夹内所有文件目录
def getFileInPath(path): 
    import os
    all_file = []
    for f in os.listdir(path): 
        f_name = os.path.join(path, f)
        all_file.append(f_name)
    return all_file

def batchcompress(path, compressType):
    import subprocess
    filelist = getFileInPath(path)
    if compressType == 'Z':
        for file in filelist:
            args = 'compress ' + file
            subprocess.Popen(args=args, shell=True)
            
            
batchcompress('/mnt/d/Project/NOW/NSOAS/NSOAS/AUX_CACHE/gnsswhu', 'Z')