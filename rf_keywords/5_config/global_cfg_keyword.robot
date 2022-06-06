*** Settings ***
Documentation       global config keywords
Library             WafWebLibrary

*** Keywords ***
开启源ip解析
    [Arguments]    ${cfg}
    click config
    click gloable cfg 
    src ip enable    cfg=${cfg}