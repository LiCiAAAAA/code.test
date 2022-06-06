*** Settings ***
Documentation       test Protect protection
Library             WafWebLibrary
Resource            ..${/}config${/}resource.robot
Resource            ..${/}rf_keywords${/}0_common${/}common_keyword.robot
Resource            ..${/}rf_keywords${/}5_config${/}transparent_site_keyword.robot
Resource            ..${/}rf_keywords${/}5_config${/}network_cfg_keyword.robot
Resource            ${CURDIR}${/}test_data${/}net_cfg_variable.robot
Suite Setup         Protect Setup
Suite Teardown      Protect Teardown

*** Keywords ***
Protect Setup
    登录    ${login_config}
    开启ssh    ${reserved_cfg}
    清空保护站点
    应用更改

Protect Teardown
    关闭ssh    ${reserved_cfg}
    close browser

*** Test Cases ***
验证删除网桥
    删除网桥
    应用更改
    结果校验    ${login_config}    ip a | grep Protect1    ${net_check_var}    ${net_check_var}[judg1]

验证创建网桥
    创建网桥    ${net_cfg}
    应用更改
    结果校验    ${login_config}    ip a    ${net_check_var}    ${net_check_var}[judg2]