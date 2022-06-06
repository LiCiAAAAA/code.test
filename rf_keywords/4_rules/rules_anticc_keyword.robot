*** Settings ***
Documentation       anticc keywords
Library             WafWebLibrary

*** Keywords ***
设置行为分析防护
    click strategy
    click anticc
    anticc config
    enable anticc    始终运行
    check anticc save

创建行为分析规则
    [Arguments]    ${anticc_cfg}
    click anticc
    create_new_anticc
    anticc_rule    anticc_cfg=${anticc_cfg}
    check anticc rule save

应用规则
    apply_rule

删除规则
    del anticc rule
    apply_rule