#!/usr/bin/env python
# -*- coding:utf-8 -*-

from ..base import keyword, logger
from ..base import WafWebDriver

class WafRulesGroupMainKeywords(WafWebDriver):
    """
        [1] http://robotframework.org/robotframework/#user-guide
        [2] https://robotframework.org/SeleniumLibrary/SeleniumLibrary.html
        [3] https://robotframework.org/robotframework/latest/libraries/BuiltIn.html
        [4] https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html
    """
    __elements = {
        'strategy': { 'type': 'click', 'locator': 'link:策略',},
        'rules_group': { 'type': 'click', 'locator': 'link:规则组',},
        'rules_group_config': { 'type': 'click', 'locator': 'css:tr:nth-child(1) > .column-group-operation > span:nth-child(1) label',},
        'rules_group_enable': { 'type': 'select', 'locator': 'css:#rule\.info\.field td > span > select',},
        'rules_save': { 'type': 'click', 'locator': 'xpath://td[2]/span/a/span/span/label',},
        'check_alert': {'type': 'alert', 'action': 'ACCEPT', 'sleep': 60, 'check': '成功' },
        # 'main': { 'type': 'click', 'locator': 'css:span', },
        # 'proxy': { 'type': 'click', 'locator': 'link:纯代理', 'sleep': 2, },
        # 'proxy-alert': {'type': 'alert', 'action': 'ACCEPT', 'check': '切换完成', 'sleep': 6, },
    }
    
    def __init__(self):
        super().__init__()
        
    @keyword
    def click_strategy(self, **kwargs):
        self.operate_element(self.__elements['strategy'])

    @keyword
    def click_rules_group(self, **kwargs):
        self.operate_element(self.__elements['rules_group'])

    @keyword
    def rules_group_enable(self, **kwargs):
        kwargs = kwargs.get('strategy_cfg')
        rules_group_enable = kwargs.get('rules_group_enable')
        
        self.operate_element(self.__elements['rules_group_config'])
        self.operate_element(self.__elements['rules_group_enable'], rules_group_enable)
        self.operate_element(self.__elements['rules_save'])

    @keyword
    def check_alert(self, **kwargs):
        self.operate_element(self.__elements['check_alert'])
