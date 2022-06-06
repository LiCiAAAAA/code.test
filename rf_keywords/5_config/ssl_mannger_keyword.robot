*** Settings ***
Documentation       ssl manager keywords
Library             WafWebLibrary

*** Keywords ***
上传ssl证书
    [Arguments]    ${file_path}
    click config
    click cer manager
    add cer    file_path=${file_path}
    check ssl save
