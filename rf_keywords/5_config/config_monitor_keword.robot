*** Settings ***
Documentation       monitor manager keywords
Library             WafWebLibrary

*** Keywords ***
snmp开启
    [Arguments]    ${cfg}
    click config 
    click cfg monitor
    enable snmp    ${cfg}[snmp_v]
    config_snmp    cfg=${cfg}

snmp关闭
    [Arguments]    ${cfg}
    click config 
    click cfg monitor
    enable snmp    ${cfg}[snmp_v]

snmp结果
    [Arguments]    ${cfg}    ${oid}
    ${msg}    check snmp cmd result    cfg=${cfg}    oid=${oid}
    [Return]    ${msg}
