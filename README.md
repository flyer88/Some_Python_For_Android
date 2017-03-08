## `Android` 开发中用到的一些脚本

### log_to_proguard_rules
此脚本用于处理，`Android Studio` 开启混淆后，输出的 `log` 信息，过滤大部分内容，将其转为混淆规则
此脚本只能过滤大部分信息，不能处理所有的

####使用方式
修改这两个目录即可，前者是 `log` 信息，后者是输出的最终 `proguar` 的规则
```
  source_log_info = "/Users/flyer/Desktop/source_log_info"
  generated_info = "/Users/flyer/Desktop/generate_log_info"
```

### translate_string_to_R$String 
此脚本用于批量替换 `android` 项目下 `java` 代码中中文字符串的硬编码，并同意替换成 R.string.xx


####使用方式
修改这两个四个目录值即可，前两者是原项目的根目录和 `java` 代码目录，后者是输出的文件根目录和 `java` 代码目录
```
  rootDir = "/Users/flyer/Documents/Code/2D/Android/background-rest_phone"
  javaCode = rootDir + "/app/src/main/java"

  generatedRootDir = "/Users/flyer/Documents/Code/2D/Android/background-rest_phone_trans"
  generatedJavaDir = generatedRootDir + "/app/src/main/java"
```



####最后
脚本问题多多，python写的很菜

