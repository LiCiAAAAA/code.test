*** Settings ***
Documentation       rf_keywords
Library             WafWebLibrary


*** Keywords ***
登录
    [Arguments]    ${login_config}
    open new browser
	# Set Window Size    ${2200}   ${1400}
    maximize browser window
    open url    ${login_config}[login_url]
    waf login    ${login_config}[user]   ${login_config}[pwd]

再次登录
    [Arguments]    ${login_config}
    open url    ${login_config}[login_url]
    waf login    ${login_config}[user]   ${login_config}[pwd]

清空保护站点
    click config
    click site
    clear site

应用更改
    click apply changes
    confirm apply
    handle alert
    check apply changes

反代应用更改
    click apply changes
    confirm apply
    handle alert
    handle alert
    check apply changes

Repeater
    [Arguments]    ${req_params}
    get    req_params=${req_params}

开启ssh
    [Arguments]    ${reserved_cfg}
    open url    ${reserved_cfg}[ssh_url]
    system reserved    ${reserved_cfg}[dev_kye]
    ssh on

关闭ssh
    [Arguments]    ${reserved_cfg}
    open url    ${reserved_cfg}[ssh_url]
    system reserved    ${reserved_cfg}[dev_kye]
    ssh off

结果校验
    [Arguments]    ${login_config}    ${cmd}    ${check_var}   ${judg}
    waf ssh login    ${login_config}[ssh_user]    ${login_config}[ssh_pwd]
    ${msg}   waf ssh exec    ${cmd}
    Run Keyword If    '${check_var}[check_value]' ${judg} '''${msg}'''    Fail    实际结果:${msg}

开启tw_recycle
    [Arguments]    ${cfg}    ${reserved_cfg}
    open url    ${reserved_cfg}[ssh_url]
    system reserved    ${reserved_cfg}[dev_kye]
    tw recycle on    cfg=${cfg}
    check success

判断设备重启
    [Arguments]    ${cfg}
    dev connectivity    cfg=${cfg}

Custom Repeater
    [Arguments]    ${cfg1}    ${cfg2}
    ${msg}    new custom request    ip=${cfg1}    cfg2=${cfg2}
    [Return]    ${msg}

WAF Request
    [Arguments]    ${cfg1}    ${cfg2}
    ${msg}    waf req    ip=${cfg1}    cfg2=${cfg2}
    [Return]    ${msg}