*** Settings ***
Documentation       test tcp parame support
Library             WafWebLibrary
Resource            ..${/}config${/}resource.robot
Resource            ..${/}rf_keywords${/}0_common${/}common_keyword.robot
Resource            ..${/}rf_keywords${/}5_config${/}transparent_site_keyword.robot
Resource            ..${/}rf_keywords${/}4_rules${/}rules_group_keyword.robot
Resource            ..${/}rf_keywords${/}6_system${/}system_maintain_keyword.robot
Resource            ${CURDIR}${/}test_data${/}traffic_variable.robot
Suite Setup         TCP Setup
Suite Teardown      TCP Teardown

*** Keywords ***
TCP Setup
    登录    ${login_config}
    规则组启用  ${strategy_cfg}
    清空保护站点
    添加透明模式保护站点    ${site_config}
    应用更改

TCP Teardown
    close browser

*** Test Cases ***
tw_recycle参数-配置恢复
    # 1. 进入隐藏界面/system.m?a=reserved
    # 2. 设置tw_recycle参数为“1”并保存【check1】
    # 3. 点击系统->系统维护->重启设备【check2】
    # 4. 设备启动后，进入隐藏界面/system.m?a=reserved，查看tw_recycle参数【check3】
    
    [Setup]    开启ssh    ${reserved_cfg}
    开启tw_recycle    ${tcp_cfg}    ${reserved_cfg}
    结果校验    ${login_config}    ${tcp_cfg}[cmd]    ${tcp_cfg}    ${tcp_cfg}[judg]
    Repeater    ${req_params}
    Repeater    ${http_attack_params}
    重启设备    ${login_config}
    再次登录    ${login_config}
    结果校验    ${login_config}    ${tcp_cfg}[cmd]    ${tcp_cfg}    ${tcp_cfg}[judg]
    [Teardown]    关闭ssh  ${reserved_cfg}

