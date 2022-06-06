*** Settings ***
Documentation       alarms log keywords
Library             WafWebLibrary

*** Keywords ***
校验日志内容
    [Arguments]    ${cfg}
    sleep    10
    click log
    click alarms log
    check alarms log    cfg=${cfg}