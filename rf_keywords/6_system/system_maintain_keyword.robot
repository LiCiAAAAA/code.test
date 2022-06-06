*** Settings ***
Documentation       system maintain keywords
Library             WafWebLibrary

*** Keywords ***
重启设备
    [Arguments]    ${cfg}
    click system
    click system maintenance
    dev_reboot
    判断设备重启    ${cfg}