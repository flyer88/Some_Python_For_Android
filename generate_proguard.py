# -*-coding:utf-8

info_msg_list = {
    "Note: ",
    "Warning: "
}

info_type_list = (
    "refers to the unknown class",
    "can't find superclass or interface",
    "can't find referenced class ",
    # "can't find referenced method",
    "can't find dynamically referenced class",
    # "accesses a declared field 'icon' dynamically",
)

# 根据不同类型切出报错的 包名 或者 类名
def chooseType(log_line):
    if log_line.startswith("Note: ") or log_line.startswith("Warning: ") :
        for type_value in info_type_list:
            if (log_line.find(type_value) != -1):
                split_log = log_line.split(type_value)
                if (split_log[-1].find("'") != -1):
                    split_log[-1] = split_log[-1].replace("'", "")
                if split_log[-1].find(" ") != -1:
                    split_log[-1] = split_log[-1].replace(" ", "")
                # print split_log[-1]
                return split_log[-1]
    else:
        return None
        # print log_line


# 清除完全相同的类型
def clearSameClass(clazz_list):
    clear_same_class_list = []
    clear_same_class_list.append(clazz_list[0])
    for clazz in clazz_list:
        if clazz in clear_same_class_list:
            continue
        else:
            clear_same_class_list.append(clazz)
    return clear_same_class_list


# 清除前缀相同的
def clearSameCompany(clear_same_class_list):
    clear_same_company_list = []
    indexI = 0
    for clazz_raw in clear_same_class_list:
        indexJ = 0
        for clazz in clear_same_class_list:
            clear_class = clear(clazz_raw,clazz)
            indexJ = indexJ + 1
        print clear_class
        clear_same_company_list.append(clear_class)
        indexI = indexI + 1


# 判断两个字符串是否相同
# 相同返回两个字符串前缀相同部分
# 不同则返回被比较的字符串
# raw_clazz 为被比较的字符串
# clazz 为参考的字符串
def clear(raw_clazz,clazz):
    index = 0
    clear_clazz = ""
    if clazz == None or raw_clazz == None:
        return None

    for ch in clazz:
        if len(raw_clazz) > index:
            if ch == raw_clazz[index]:
                clear_clazz = clear_clazz + ch
                index = index + 1
                continue
            else:
                clear_clazz = raw_clazz
                break
        else:
            break
    # if clear_clazz != 0:
    #     return clear_clazz
    # else:
    return clear_clazz


# 判断每个两个包名
# 如果第一个和第二个相同,直接返回
# 如果两个不同
# 情况一: 开头三个以上相同,返回三个数据拼凑的包名
# 情况二: 开头三个一下不同,返回第一个原始包名
# 情况三: 包名长度不足 3 ,数组越界,返回第一个原始包名
def compare2List(clazz_a,clazz_b):
    index = 0
    clazz_result = []
    while True:
        if clazz_a == clazz_b:# 相同的情况下,直接返还原数据即可
            return clazz_a
        # 数组越界,返回原数据
        if index + 1 >= len(clazz_b) and index + 1 >= len(clazz_a):
            return clazz_a
        # 两个不完全相同的情况
        if index >= 3: # 已经有3个相同了,返回累计的包名
            return clazz_result
        elif clazz_a[index] == clazz_b[index]:# 累计每个节点名字
            clazz_result.append(clazz_a[index])
        else:# 两个包名四个以内就不相同,或者一开始就不相同,直接返回原来的包名
            return clazz_a
        index = index + 1


# 混淆报错信息
source_log_info = "/Users/flyer/Desktop/source_log_info"

source_log_file = open(source_log_info)

sourc_log_lines = source_log_file.readlines()

# 生成的混淆文件
generated_info = "/Users/flyer/Desktop/generate_log_info"

generated_file = open(generated_info,"w")



clazz_list = []
node_list = []
i = 0
for log_line in sourc_log_lines:
    clazz = chooseType(log_line.strip("\n"))
    if clazz is None:
        "123"
    else:
        node_list = clazz.split(".")
        clazz_list.append(node_list)

clazz_result = [[]]
for i in range(0, len(clazz_list), 1):
    j = i + 1
    clazz_i_list = clazz_list[i]
    for j in range(1,len(clazz_list),1):
        clazz_temp_list = compare2List(clazz_list[i], clazz_list[j])
        if len(clazz_i_list) > len(clazz_temp_list):
            clazz_i_list = clazz_temp_list
    if not clazz_result.__contains__(clazz_i_list):
        clazz_result.append(clazz_i_list)

for class_i in clazz_result:
    s = ""
    for class_j in class_i:
        s = s + class_j + "."
    if s != '':
        generated_file.writelines("-keep class " + s + "**{*;}\n")

generated_file.close()
source_log_file.close()
