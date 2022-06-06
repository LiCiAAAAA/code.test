*** Settings ***
Documentation       test anticc protection
Library             WafWebLibrary
Resource            ..${/}config${/}resource.robot
Resource            ..${/}rf_keywords${/}0_common${/}common_keyword.robot
Resource            ..${/}rf_keywords${/}4_rules${/}rules_anticc_keyword.robot
Resource            ..${/}rf_keywords${/}5_config${/}transparent_site_keyword.robot
Resource            ${CURDIR}${/}test_data${/}anticc_variable.robot
Suite Setup         Anticc Setup
Suite Teardown      Anticc Teardown

*** Keywords ***
Anticc Setup
    登录    ${login_config}
    清空保护站点
    添加透明模式保护站点    ${site_config}
    应用更改

Anticc Teardown
    close browser

*** Test Cases ***
验证cc攻击防御
    设置行为分析防护
    创建行为分析规则    ${anticc_cfg}
    应用规则
    Repeater    ${req_params}
    Repeater    ${req_params}
    Repeater    ${block_params}
    [Teardown]    删除规则

验证行为分析规则检测对象遍历
    设置行为分析防护
    创建行为分析规则    ${anticc_cfg}
    应用规则
    Repeater    ${req_params}
    Repeater    ${req_params}
    Repeater    ${block_params}
    [Teardown]    删除规则
