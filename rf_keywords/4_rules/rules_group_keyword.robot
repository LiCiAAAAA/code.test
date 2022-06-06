*** Settings ***
Documentation       rules group keywords
Library             WafWebLibrary

*** Keywords ***
规则组启用
    [Arguments]    ${strategy_cfg}
    click strategy
    click rules group
    rules group enable    strategy_cfg=${strategy_cfg}
    check alert