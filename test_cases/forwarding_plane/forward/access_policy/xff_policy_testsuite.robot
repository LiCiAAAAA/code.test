*** Settings ***
Documentation       test ssl support
Library             WafWebLibrary
Resource            ..${/}config${/}resource.robot
Resource            ..${/}rf_keywords${/}0_common${/}common_keyword.robot
Resource            ..${/}rf_keywords${/}5_config${/}reverse_site_keyword.robot
Resource            ..${/}rf_keywords${/}5_config${/}global_cfg_keyword.robot
Resource            ..${/}rf_keywords${/}4_rules${/}rules_group_keyword.robot
Resource            ${CURDIR}${/}test_data${/}access_policy_variable.robot
Suite Setup         XFF Setup
Suite Teardown      XFF Teardown

*** Keywords ***
XFF Setup
    登录    ${login_config}
    规则组启用  ${strategy_cfg}
    清空保护站点
    反代应用更改

XFF Teardown
    close browser

*** Test Cases ***
反代客户端ip不透明-源IP解析功能验证
    # 1. 点击配置->全局配置->开启源ip解析
    # 2. 应用更改
    # 3. 可信任代理ip列表中ip，不包含client ip
    # 4. 发起header中携带xff攻击请求【check1】
    # 5. 查看应用防护日志客户端ip【check2】
    # 6. 重复3-5步，可信任代理ip列表中添加client ip【check3】
    
    [Setup]    添加反代模式保护站点  ${reverse_site_cfg}
    开启源ip解析    ${src_ip_parse1}
    反代应用更改
    ${msg}    Custom Repeater    ${reverse_site_cfg}[frontend_ip]    ${attack_cfg}
    Run Keyword If    '${attack_cfg}[rps_code]' not in '''${msg}'''    Fail    实际结果:${msg}
    校验日志内容    ${alarms_log1}
    开启源ip解析    ${src_ip_parse2}
    反代应用更改
    ${msg}    Custom Repeater    ${reverse_site_cfg}[frontend_ip]    ${attack_cfg}
    Run Keyword If    '${attack_cfg}[rps_code]' not in '''${msg}'''    Fail    实际结果:${msg}
    校验日志内容    ${alarms_log2}


