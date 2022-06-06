*** Settings ***
Documentation       test snmp monitor
Library             WafWebLibrary
Resource            ..${/}config${/}resource.robot
Resource            ..${/}rf_keywords${/}0_common${/}common_keyword.robot
Resource            ..${/}rf_keywords${/}5_config${/}config_monitor_keword.robot
Resource            ..${/}rf_keywords${/}1_status${/}sys_situaton_keyword.robot
Resource            ${CURDIR}${/}test_data${/}dev_manager_variable.robot
Suite Setup         SNMP Setup
Suite Teardown      SNMP Teardown

*** Keywords ***
SNMP Setup
    登录    ${login_config}

SNMP Teardown
    close browser

*** Test Cases ***
SNMPv2-自定义oid准确性
    # 1. 点击配置->监控管理->snmp开启v2
    # 2. 获取CPU使用率oid:.1.3.6.1.4.1.2021.11.18.3.1.1.3.99.112.117【check1】
    # 3.获取内存使用率oid:.1.3.6.1.4.1.2021.4.18.3.1.2.3.109.101.109【check2】
    snmp开启    ${snmpv2_cfg}
    ${sys_situation}    获取系统概况
    ${msg}    snmp结果    ${snmpv2_cfg}  ${oid}[cpu]
    Run Keyword If    '${sys_situation}[cpu_percent]' not in '''${msg}'''    Fail    实际结果:${msg}
    ${sys_situation}    获取系统概况
    ${msg}    snmp结果    ${snmpv2_cfg}  ${oid}[mem]
    Run Keyword If    '${sys_situation}[mem_percent]' not in '''${msg}'''    Fail    实际结果:${msg}
    [Teardown]    snmp关闭    ${snmpv2_cfg}

SNMPv3-自定义oid准确性
    # 1. 点击配置->监控管理->snmp开启v3
    # 2. 获取CPU使用率oid:.1.3.6.1.4.1.2021.11.18.3.1.1.3.99.112.117【check1】
    # 3.获取内存使用率oid:.1.3.6.1.4.1.2021.4.18.3.1.2.3.109.101.109【check2】
    snmp开启    ${snmpv3_cfg}
    ${sys_situation}    获取系统概况
    ${msg}    snmp结果    ${snmpv3_cfg}  ${oid}[cpu]
    Run Keyword If    '${sys_situation}[cpu_percent]' not in '''${msg}'''    Fail    实际结果:${msg}
    ${sys_situation}    获取系统概况
    ${msg}    snmp结果    ${snmpv3_cfg}  ${oid}[mem]
    Run Keyword If    '${sys_situation}[mem_percent]' not in '''${msg}'''    Fail    实际结果:${msg}
    [Teardown]    snmp关闭    ${snmpv3_cfg}