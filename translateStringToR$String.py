# -*- coding: utf-8 -*-

import os
import os.path

import re
import codecs

rootDir = "/Users/flyer/Documents/Code/2D/Android/background-rest_phone"
javaCode = rootDir + "/app/src/main/java"

generatedRootDir = "/Users/flyer/Documents/Code/2D/Android/background-rest_phone_trans"
generatedJavaDir = generatedRootDir + "/app/src/main/java"

# 匹配当前行中是否有字符串
pattern = re.compile(ur'(\"[^\"]*[\u4e00-\u9fa5]+[^\"]*\")')
count = 0
# 过滤 log 信息
patternLog = re.compile(ur'Logger|LogUtils|JLog|Log\.+')
# 过滤 comments 信息
patternComments = re.compile(ur'\ *(.)*(\/\/)+|[\*]+|(\/\*)+')

def traverseFile(dir):
    '''
    遍历所有的目录
    :param dir:
    :return:
    '''
    i = 0
    for parent,dirNames,filenames in os.walk(dir):    #三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
        # 当前文件夹下文件内容
        #输出文件信息
        i = i + 1
        for filename in filenames:
            # 文件内容
            # print "parent:" + parent + "\n" + "filename is:" + filename
            if filename.startswith("."):
                continue
            filePath = parent + "/" + filename
            transFilePath = filePath.replace("background-rest_phone","background-rest_phone_trans")
            transParent = parent.replace("background-rest_phone","background-rest_phone_trans")
            translate(transParent,filePath,transFilePath)
        # 文件夹下的文件夹再递归遍历
        # for dirName in  dirNames:                       #输出文件夹信息
        #     # print "dirname is:" + dirName
        #     traverseFile(dirName)

def translate(transParent,oldFilePath,transFilePath):
    '''
    匹配 "" 中的文字，然后进行过滤，最后写入文件
    :param transParent:
    :param oldFilePath:
    :param transFilePath:
    :return:
    '''
    global count
    oldFileOpen = codecs.open(oldFilePath,'r','utf-8')
    if not os.path.exists(transParent):
        os.makedirs(transParent)
    transFileOpen = codecs.open(transFilePath,'w','utf-8')
    lines = oldFileOpen.readlines()
    for line in lines:
        newLine = line.encode('utf-8')
        line.strip('\n')
        strList = pattern.findall(line)
        if not (strList == None or strList.__len__() == 0):
            # 匹配到了，修改line，然后写入文件
            # 过滤 Log comments 返还是 true 表示 需要过滤
            if not filterPattern(line):
                newLine = translateLine(strList,newLine)
                print transFilePath
                count = count + 1
        transFileOpen.write(unicode(newLine, "utf-8"))

def filterPattern(line):
    '''
    过滤掉 log 和 注释
    此处也可以加入其他 pattern 进行过滤
    :param line:
    :return: boolean true 需要过滤，false 不过滤
    '''
    logList = patternLog.findall(line)
    if logList != None and logList.__len__() > 0:
        return True
    # 当前行必然有 string ，正则只需要匹配是 注释类型，
    # 如果是，那么直接返回 true 过滤
    # 否则 返回 false 不过滤
    commentList = patternComments.findall(line)
    if commentList != None and commentList.__len__() > 0:
        return True
    return False

def translateLine(strList,newLine):
    '''
    把字符串变化成 R.string.字符串
    :param strList:
    :param newLine:
    :return:
    '''
    for str in strList:
        strId = str.encode('utf-8')
        newLine = newLine.replace(strId,'R.string.'+ strId.split('\"')[1])
    return newLine

traverseFile(javaCode)
