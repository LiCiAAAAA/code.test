*** Settings ***
Documentation       sys situation keywords
Library             WafWebLibrary

*** Keywords ***
获取系统概况
    click status
    click sys situation
    ${msg}    obtain situation
    [Return]    ${msg}