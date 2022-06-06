*** Settings ***
Documentation       test snmp monitor
Library             WafWebLibrary
Resource            ..${/}config${/}resource.robot
Resource            ..${/}rf_keywords${/}0_common${/}common_keyword.robot
Resource            ..${/}rf_keywords${/}5_config${/}transparent_site_keyword.robot
Resource            ..${/}rf_keywords${/}4_rules${/}rules_group_keyword.robot
Resource            ..${/}rf_keywords${/}2_logs${/}alarms_log_keyword.robot
Resource            ${CURDIR}${/}test_data${/}log_variable.robot
Suite Setup         Alarms Setup
Suite Teardown      Alarms Teardown

*** Keywords ***
Alarms Setup
    登录    ${login_config}
    规则组启用  ${strategy_cfg}
    清空保护站点
    添加透明模式保护站点    ${site_config}
    应用更改

Alarms Teardown
    close browser

*** Test Cases ***
特殊攻击报文日志记录验证
    # 1. 使用poc报文攻击保护站点
    # 2. 查看防护日志
    ${msg}    Custom Repeater    ${site_config}[site_ip]    ${datagram1}
    Run Keyword If    '${datagram1}[rps_code]' not in '''${msg}'''    Fail    实际结果:${msg}
    校验日志内容    ${alarms_log1}

    ${msg}    Custom Repeater    ${site_config}[site_ip]    ${datagram2}
    Run Keyword If    '${datagram2}[rps_code]' not in '''${msg}'''    Fail    实际结果:${msg}
    校验日志内容    ${alarms_log2}

应用防护日志攻击特征串验证
    # 1. SQL注入攻击？id=1 and 1=1，文件限制.mdb
    # 2. 查看防护日志攻击特征串
    ${msg}    Custom Repeater    ${site_config}[site_ip]    ${datagram3}
    Run Keyword If    '${datagram3}[rps_code]' not in '''${msg}'''    Fail    实际结果:${msg}
    校验日志内容    ${alarms_log3}

    ${msg}    Custom Repeater    ${site_config}[site_ip]    ${datagram4}
    Run Keyword If    '${datagram4}[rps_code]' not in '''${msg}'''    Fail    实际结果:${msg}
    校验日志内容    ${alarms_log4}