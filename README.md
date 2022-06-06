# 基于RF的WEB自动化测试设计

## 代办
```shell
  # 1. 用python封装产品 和 用 RF语法 封装产品有什么优劣  # python 的灵活性/通用性/稳定性
  2. 全局配置管理
  3. 测试数据管理
  # 4. python包导入
  5. 配置文件 licence
  # 6. 变量类型  @$&
  # 7. robot 指定python库环境变量 -P 
  # 8. 文件作用域 库作用域 库导入 相对路径
  9. 并发执行问题
  10. 文件结构问题
  # 11. 用例标签 Default Tags | Force Tags | Tags  Tags会重写Default
  # 12. 用例执行
  # 13. 区分生效的用例/作废的用例  使用tag区分
  # 14. 用例ID  数字+__ 01__  02__
  # 15. 允许在工程内任意路径下执行任何robot脚本  已在run.sh 中实现 ./run.sh robot $args
  # 16. 编码格式 中文关键字 字典处理 @keyword 
  # 17. python库结构确认 
  # 18. from . import utils  和 import .utils 区别
  # 19. 为什么 __init__.py  中导入包确不用它   
  # 20. from .keywords.WafLogin import Wa fLogin  和 from .keywords import WafLogin , 导入一个py文件和导入一个类的区别
  # 21. 为什么要写一堆只有pass的类 
  # 22. 调整keywords文件夹结构，适配 
  # 23. robot命名规范确认
  # 24. 活动日志记录
  # 25. rf文件结构规范
  # 26. rf工程结构规范
  # 27. *** Comments ***  Comments Comment 关键字  # Additional comments or data. Ignored by Robot Framework.
  # 28. 变量声明 变量赋值 ${invoice}=
  29. json yaml 读取  pyyaml 原生支持情况  json.loads
  # 30. robot 命令行常用方法
  # 31. 注释编写规范
  # 32. 换行连接符  ...
  # 33. 重复关键字是否会报错，是否易识别 已写脚本处理 ./run.sh check
  # 34. _Libdoc 文档自动生成  已处理 libdoc.exe WafWebLibrary  haha.html
  # 35. requirement.txt 库自动安装 文件作用
  36. 用例执行失败后的处理动作？
  37. ${LIBRARY}  ${RESOURCES}  用途，是否可以实现任意路径执行
  38. 用例依赖的问题  ${PREV TEST STATUS}
  # 39. webdriver切换为selenium中自带的 未搞定
  40. 失败后重新执行失败的用例？ 
  # 41. 异常抛出问题  使用 builtin 类抛出异常
  42. 动态创建变量 py文件 (数据库 ，计算，时间等)
  43. LIST__或DICT__ 前缀 ,RF会校验是否为对应的属性
  # 44. reStructuredText 文档语法 帮助文档语法  `` 反引号 链接 关键字  5.1.6参考文档
  # 45. 接口处理方式 url处理方式 获取 cookie 获取 user-agent 已获取
  # 46. linux 系统 robotframework---chrome headless模式不能最大化window  采用 Set Window Size    ${2200}   ${1400}
  # 47. linux 环境 Google 浏览器中文显示乱码  已解决  修改编码类型为zh_CN.utf8
  #     yum -y groupinstall "X Window System"
  #     yum -y groupinstall Fonts
  48. 显示等待偶尔无法获取到元素
  49. robot for 循环用法
  
```

## 遗留问题分类
```shell
  # RF 工程结构规范  目录/文件
    25. rf文件结构规范
    26. rf工程结构规范
    23. robot命名规范确认
    10. 文件结构问题
    2. 全局配置管理
    3. 测试数据管理
    5. 配置文件 licence
    # 6. 变量类型  @$&
    # 28. 变量声明 变量赋值 ${invoice}=
    29. json yaml 读取  pyyaml 原生支持情况  json.loads
    42. 动态创建变量 py文件 (数据库 ，计算，时间等)
    43. LIST__或DICT__ 前缀 ,RF会校验是否为对应的属性
    
    
  
  # for语法
    FOR  ${index}  IN RANGE  [start  stop  loop]
      Exit For Loop IF
      Continue For Loop IF
      LOG  ${index}  END
    FOR  ${item}  IN  @{LIST}
    FOR  ${index}  ${item}  IN ENUMERATE  @{LIST}
    FOR  ${index}  ${item}  IN ENUMERATE  @{LIST}  start=1
  
  # 用例依赖问题
    38. 用例依赖的问题
    40. 失败后重新执行失败的用例？ 
    36. 用例执行失败后的处理动作？
    9. 并发执行问题
    
  # 引用路径问题
    8. 文件作用域 库作用域 库导入 相对路径
    37. ${LIBRARY}  ${RESOURCES} ${EXECDIR}  用途，是否可以实现任意路径执行
```

## WAF_RF工程结构
```shell
WAF_RF/
  cases/
    防护面/
    转发面/
    控制面/
      转发/
        部署模式/
          透明代理cesi_testsuit.robot
  datas/  # ??
    
  libs/
    WafWebLibrary/  # 详见库结构
  docs/             # 存放相关帮助文档
  test/             # 存放相关debug工具
  .gitignore        # 
  Readme.md         # 
  requirements.txt  # 
  run.sh            # 启动脚本封装

```

## WAF_RF编码规范
```shell
  # 编码规范
    命名      单词首字母大写, 单词间用'_'分割
    分隔符    参数间用 2个或以上空格分隔
    系统变量  ${SPACE} ${EMPTY}
    标签      Force Tags | Default Tags | [Tags]  [Tags]会重写Default
    顺序      01__ 02__  用数字+两个下划线 表示 套件ID 和 用例ID
    中英文    py库文件中关键字使用英文，RF中关键字可以使用中文
    文件编码  LF UTF-8 空格缩进:2
    注释      单行注释使用 #
    换行连接  换行连接符使用  ...开头
    空值      RF中 空值使用 NONE 表示
    文档      RF关键字文档中， ``链接关键字
    异常      RF中，调用BuiltIn类中的fail方法抛出异常
  
  # 工程约定
    目录中含有 10-15个测试套, 1个suit中含有15个以内用例
    测试套之间没有依赖关系  测试套内部可以存在依赖关系
    lib  bin  case  data  ，测试套 和 测试数据不要放在一起? 
    三类文件添加 testsuit resource variable 后缀
    每个测试套的 Documentation 中写 背景/场景/用户故事 ，而不是 环境/步骤/要求
    
  # 常用命令 
    关键字检查  ./run.sh check
    库文档生成  libdoc.exe WafWebLibrary  haha.html
    报告处理    rebot --name HAHA haha.html hehe.html
    
    # robot 常用命令参数说明
      -T            # 输出文件添加时间戳
      -N <name>     # 设置顶级测试套件名称
      -P <libs>     # 追加库搜索路径
      -L TRACE      # 调试
      -i <tag>      # 指定tag
      -e <tag>      # 排除tag
      -t <case>     # 按名称选择用例
      -s <suit>     # 指定suit
      --skip <tag>  # 跳过指定tag
      -G <tag>          # 给所有执行的用例添加标签 - 分布式用
      -d <dir>          # 设置 output file 目录
      -o <file>         # 设置 output file 路径
      -l <file>         # 设置 log file 路径
      -r <file>         # 设置 report file 路径
      -v <name:value>   # 设置单个变量
      -V <path:args>    # 设置变量文件
      --dryrun          # 不执行，验证语法
      -X                # 失败即停
      -A <path>         # 讲robot参数存放在文本中
      -R                # 多次执行合并结果 rebot用
      --tagstatinclude tag   # 指定报告中要显示的标签
      --tagstatexclude tag   # 指定报告中要排除的标签
      --logtitle <title>     # 设置日志标题
      --reporttitle <title>  # 设置报告标题
      --splitlog             # 拆分日志文件
      --maxerrorlines NONE   # 错误日志行数不限制

```

## WafWebLibrary 库结构
```shell
# WafWebLibrary 库目录结构
libs/WafWebLibrary/
  __init__.py     # 初始化库
    class WafWebLibrary      # 继承全部关键字库
      ROBOT_LIBRARY_SCOPE    # 库作用域
      ROBOT_LIBRARY_VERSION  # 库版本号
    
  base/
    __init__.py   # 导入关键字
    utils.py      # 实用工具
    compat.py     # 兼容性处理
    
    webdriver.py  # webdriver公共类
      class WafWebDriver(SeleniumLibrary)
        open_new_browser
        open_url
        operate_element
  
  keywords/
    __init__.py   # 导入关键字
    waf_login.py  # waf产品的关键字
      class WafLoginKeywords(WafWebDriver):
        __elements    # 前端元素 page object
        waf_login     # keyword
        login_error   # keyword
```

## RF文件类型说明
```shell

# 文件类型
_Variable.robot
  variable

__init__.robot
  *** Settings ***
    Documentation
    Library
    Resource
    Variables
    Force Tags
    Suite Setup
    Suite Teardown
    Test Setup
    Test Teardown

  *** Variables ***
  *** Keywords ***
  
_TestSuite.robot 
  *** Settings ***
    Documentation
    Library
    Resource
    Variables
    Force Tags
    Default Tags
    Suite Setup
    Suite Teardown
    Test Setup
    Test Teardown
    Test Template
    Test Timeout
    
  *** Variables ***
  *** Test Cases ***
  *** Keywords ***
  
_Resource.robot
  *** Settings ***
    Documentation
    Library
    Resource
    Variables

  *** Variables ***
  *** Keywords ***

# 参数类别
  *** Variables ***
  ${var}
  @{list}
  &{dict}
  
  *** Test Cases ***
  Testcase_Name
    [Documentation]
    [Tags]
    [Setup]
    [Teardown]
    [Template]
    [Timeout]
  
  *** Keywords ***
  Keyword_Name
    [Documentation]
    [Tags]
    [Teardown]
    [Arguments]
    [Return]
    [Timeout]

```

## 分布式执行设计方案
```shell
# 结论: 可行 易实现
  # jenkin 用于分布式执行管理
  # rebot  用于合成报告
  [1] http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#post-processing-outputs
```


## 活动日志

```shell
# 背景
0. 21Q4核心目标: 解放生产力
1. 基线回归用例不全, 没有用例，只有测试点
2. 不同部署模式, 不同平台(信创/云)，回归成本巨大
3. 手工执行的天然的复杂性、不确定性、不可靠性
4. 借本次天池/飞腾/海光测试之机，实施自动化测试

# 活动日志
10-08 ??
结论:
    1. 立项 - 康廷峰负责

11-05 ??
结论:
  1. 调整策略，不干预具体实施
  2. 仅在需要帮助时提供支持
  
11-10 ??
结论:
  1. 上库，lib库初步成型
  2. 新增10条用例自动化

11-11 ?? 
  
```

## 预期

```shell
# 预期
1. 执行
  一键执行
  多参数，可配置
  执行效率高
  执行简单
  单平台全模式，百条用例从5~10人天降至0.5~1人天
  降低投入，降低遗漏，降低判断偏差
2. 维护
  用例管理 - 数据
  方法 - 易扩展
  公共函数 - 代码复用性高
  注释
  培训2h，可以迅速新增用例
3. 结果展示 - 报表
4. 问题重现
5. 过程日志
6. 有效文档说明
7. 支持测试类型
  配置测试
  业务测试
8. 落地时间
  框架 
    3-7 可用
    30-70 好用
```

# 基于V460的WEB自动化 - 失败

## 活动日志 

```shell
#  WEB自动化的一次失败尝试
## 背景
	0. 舍不得花时间
	1. 自动化的原始诉求 价值
	2. WEB自动化 外界认知中能够做到的部分
	3. 选用例 - 手工用例 - 典型用例 3*3
	4. 思考: 用例 -> 自动化
	5. 用户怎么用这个框架

## 活动日志
0630 09:30 ~ 11:30
结论：
    1. 首次讨论，初步确定问题/预期/框架
    2. 赵昊负责实现一个demo，0630完成
    3. 周天负责调研相关测试框架selenium/RF
    4. demo实现后，确定详细设计，痛点，里程碑
风险：
    1. 没有软件设计的经验，很多细节没有讨论清楚
    2. 故事的形式落地还是不理想，影响讨论积极程度

0702 19:00 ~ 19:40
结论：
  1. 提出详细设计
  2. 明确接下来任务
      1. 今天这个调通 / 稳定
      2. 选择手工用例 3*3
      3. 数据补完后，代码精简优化
      4. 补充数据 各种情况，加 减情况 
      # 5. 新架构调整

0706 19:30 ~ 20:30
结论: 
  1. 及时止损
  2. 现阶段缺失的是基线用例
  3. 需要补齐测试用例，然后转换为自动化测试
  4. 后续再投入自动化测试

    
```

## 设计方案

```shell
# 实施基于V460的WEB自动化
# 架构设计
  执行文件 
    传参
      单步/全部
        退出/停住
  用例层/
    datacase/
      配置/
        消息通知/
          直接发送.yml
          SMTP发送.yml
            唯一id '' '' '' '' '' '' 
          syslog通知.yml
            唯一id '' '' '' '' '' '' '' '' '' 
    业务用例
  方法层/
    datafunc/
      配置/
        消息通知/
          直接发送.py
            //*[@id="dialog-method-config"]/table/tbody/tr[3]/td[2]/span[1]/input # 注释
          SMTP发送.py
            唯一id
          syslog通知.py
    业务方法
  公共层
    config.py
      系统配置 
    common.py
      查列表
      选择器
      解释器
    校验
    动作
      webaction.py
        click
        text
      wafaction.py
        应用更改
        保存
        关闭
        清除
    流 - 环境复原
  日志
  报表

```



# RF安装指南

```shell
## python pip 指定源 默认源
  # python 安装
    https://www.python.org/downloads/release/python-379/ 
  
  # pip 升级
    python -m pip install --upgrade pip

  # 备注 指定源安装  
    pip install urllib3==1.25.11 -i http://pypi.douban.com/simple --trusted-host pypi.douban.com

  # 生成pip文件
    # pip config set global.index-url http://pypi.douban.com/simple
  
  配置文件内容 pip 安装目录下 pip.ini
  # linux ~/.pip/pip.conf
    [global]
    index-url = http://pypi.douban.com/simple

    [install]
    trusted-host = pypi.douban.com
  
  # linux 安装 setuptools-rust
    pip install setuptools-rust
  
  # robotframework 安装
    # pip install robotframework-ride==2.0b1 robotframework-seleniumlibrary psutil
    pip install -r requirements.txt
  # linux 安装Google浏览器
  #   下载：
  #     wget https://dl.google.com/linux/direct/google-chrome-stable_current_x86_64.rpm
  #   本地安装：
  #     sudo yum localinstall google-chrome-stable_current_x86_64.rpm
```

# 官方文档

```shell
[0] http://robotframework.org/robotframework/#user-guide
[1] https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html
[2] https://robotframework.org/robotframework/latest/libraries/BuiltIn.html
[3] https://robotframework.org/SeleniumLibrary/SeleniumLibrary.html
[4] https://marketsquare.github.io/robotframework-requests/doc/RequestsLibrary.html
[5] https://github.com/robotframework/RobotDemo  # data-driver demo

```

# 参考文档

```shell
[1] http://www.python3.vip/  "python学习 白月黑羽"
[2] https://www.programiz.com/  "python学习 Learn to Code for Free "
[3] https://www.geeksforgeeks.org  "python学习 geeksforgeeks"
[4] https://www.jianshu.com/p/2c5c622b5442  "从零开始UI自动化测试框架搭建 有架构图"
[5] https://www.jianshu.com/p/882d2c57f040  "Robot Framework 分层测试"
[6] https://www.cnblogs.com/-wenli/p/11343451.html "Python super用法"
[7] https://blog.csdn.net/fjswcjswzy/article/details/105637400 "Python中如何只执行一次初始化init工作"

```
