# log_to_proguard_rules
此脚本用于处理，Android Studio 开启混淆后，输出的log信息，过滤大部分内容，将其转为混淆规则
此脚本只能过滤大部分信息，不能处理所有的

####使用方式
修改这两个目录即可，前者是log信息，后者是输出的最终proguar的规则
```
  source_log_info = "/Users/flyer/Desktop/source_log_info"
  generated_info = "/Users/flyer/Desktop/generate_log_info"
```

####最后
脚本问题多多，python写的很菜

