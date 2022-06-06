*** Settings ***
Documentation       reverse site keywords
Library             WafWebLibrary

*** Keywords ***
添加反代模式保护站点
    [Arguments]    ${cfg}
    click config
    click site
    click add site
    add site config    cfg=${cfg}
