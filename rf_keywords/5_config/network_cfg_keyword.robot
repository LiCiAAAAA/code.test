*** Settings ***
Documentation       network cfg keywords
Library             WafWebLibrary

*** Keywords ***
删除网桥
    click config
    click net config
    del protect
    check del protect

创建网桥
    [Arguments]    ${net_cfg}
    click config
    click net config
    click create interface
    select inteface type    ${net_cfg}[inteface_type]
    create protect    brif1=${net_cfg}[brif1]    brif2=${net_cfg}[brif2]
