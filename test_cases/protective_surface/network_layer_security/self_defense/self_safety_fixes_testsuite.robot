*** Settings ***
Documentation       test self safety fixes problem
Library             WafWebLibrary
Resource            ..${/}config${/}resource.robot
Resource            ..${/}rf_keywords${/}0_common${/}common_keyword.robot
Resource            ${CURDIR}${/}test_data${/}self_defense_variable.robot
Suite Setup         Self_safety Setup
Suite Teardown      Self_safety Teardown

*** Keywords ***
Self_safety Setup
    登录    ${login_config}

Self_safety Teardown
    关闭ssh  ${reserved_cfg}
    close browser

*** Test Cases ***
命令注入漏洞
    [Setup]    开启ssh    ${reserved_cfg}
    WAF Request    ${login_config}[ip]    ${inject_cfg}
    结果校验  ${login_config}  ${inject_cfg}[cmd]  ${inject_cfg}  ${inject_cfg}[judg]
    [Teardown]    再次登录    ${login_config}

cas认证漏洞
    # 1. 访问https://ip/cas.m 和 https://ip/main.m?m=_cas.m 【check1】

    ${msg}    WAF Request    ${login_config}[ip]    ${cas_cfg1}
    Run Keyword If    '${cas_cfg1}[rsp_code]' not in '''${msg}'''    Fail    实际结果:${msg}
    ${msg}    WAF Request    ${login_config}[ip]    ${cas_cfg2}
    Run Keyword If    '${cas_cfg2}[rsp_code]' not in '''${msg}'''    Fail    实际结果:${msg}
