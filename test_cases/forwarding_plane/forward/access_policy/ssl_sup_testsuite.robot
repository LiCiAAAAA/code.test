*** Settings ***
Documentation       test ssl support
Library             WafWebLibrary
Resource            ..${/}config${/}resource.robot
Resource            ..${/}rf_keywords${/}0_common${/}common_keyword.robot
Resource            ..${/}rf_keywords${/}5_config${/}transparent_site_keyword.robot
Resource            ..${/}rf_keywords${/}5_config${/}ssl_mannger_keyword.robot
Resource            ..${/}rf_keywords${/}4_rules${/}rules_group_keyword.robot
Resource            ${CURDIR}${/}test_data${/}access_policy_variable.robot
Suite Setup         SLL Setup
Suite Teardown      SLL Teardown

*** Keywords ***
SLL Setup
    登录    ${login_config}
    规则组启用  ${strategy_cfg}
    清空保护站点
    上传ssl证书  ${file_path}
    添加透明模式保护站点    ${site_config}
    https站点配置    ${https_site_config}
    应用更改

SLL Teardown
    close browser

*** Test Cases ***
OpenSSL-版本验证
    # 1. 升级后查看OpenSSL版本"/waf/system_service/haproxy/haproxy -vvv"【check1】
    # 2. 创建https站点
    # 3. 访问/攻击站点【check2】
    
    [Setup]    开启ssh  ${reserved_cfg}
    结果校验  ${login_config}  ${ssl_cfg}[cmd]  ${ssl_cfg}   ${ssl_cfg}[judg]
    Repeater    ${https_req_params}
    Repeater    ${https_attack_params}
    [Teardown]    关闭ssh  ${reserved_cfg}

