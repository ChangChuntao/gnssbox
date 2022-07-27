
def batchRename(path, oldStr, newStr):
    from gnssbox.lib.filePy import getFileInPath
    import os
    fileList = getFileInPath(path)
    for file in fileList:
        newFile = str(file).replace(oldStr, newStr)
        os.rename(file, newFile)
