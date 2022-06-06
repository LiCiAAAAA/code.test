*** Settings ***
Documentation       transparent site keywords
Library             WafWebLibrary

*** Keywords ***
添加透明模式保护站点
    [Arguments]    ${site_config}
    click config
    click site
    click add site
    add site config    site_config=${site_config}

https站点配置
    [Arguments]    ${https_site_config}
    click config
    click site
    modify site    https_site_config=${https_site_config}
