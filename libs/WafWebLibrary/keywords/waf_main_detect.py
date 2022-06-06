#!/usr/bin/env python
# -*- coding:utf-8 -*-

from ..base import keyword, logger
from ..base import WafWebDriver

class WafMainDetectKeywords(WafWebDriver):
    """
        [1] http://robotframework.org/robotframework/#user-guide
        [2] https://robotframework.org/SeleniumLibrary/SeleniumLibrary.html
        [3] https://robotframework.org/robotframework/latest/libraries/BuiltIn.html
        [4] https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html
    """
    __elements = {
        'status': {'type': 'clieck', 'locator': 'link:状态',},
        'site_detect': {'type': 'clieck', 'locator': 'link:站点侦测',},
        'detect_cfg': {'type': 'clieck', 'locator': 'id:detect.config',},
        'detect_status': {'type': 'select', 'locator': 'id:global.enable',},
        'detect_ip': {'type': 'input', 'locator': 'id:global.network',},
        'detect_domain': {'type': 'input', 'locator': 'id:global.domain',},
        'detect_port': {'type': 'input', 'locator': 'id:global.port',},
        'detect_https': {'type': 'click', 'locator': 'id:global.protocol-https',},
        'detect_http': {'type': 'click', 'locator': 'id:global.protocol-http',},
        'detect_ipv4': {'type': 'click', 'locator': 'id:global.protocol-ipv4',},
        'detect_ipv6': {'type': 'click', 'locator': 'id:global.protocol-ipv6',},
        'detect_save': {'type': 'click', 'locator': 'css:#detect\\.save label',},
        # 'user': { 'type': 'input', 'locator': 'id:user_name', 'hide': False, },
        # 'main': { 'type': 'click', 'locator': 'css:span', },
        # 'proxy': { 'type': 'click', 'locator': 'link:纯代理', 'sleep': 2, },
        # 'proxy-alert': {'type': 'alert', 'action': 'ACCEPT', 'check': '切换完成', 'sleep': 6, },
    }
    
    def __init__(self):
        super().__init__()

    @keyword
    def click_status(self):
        self.operate_element(self.__elements['status'])

    @keyword
    def click_site_detect(self):
        self.operate_element(self.__elements['site_detect'])

    @keyword
    def click_detect_cfg(self):
        self.operate_element(self.__elements['detect_cfg'])

    @keyword
    def enable_site_detect(self, **kwargs):
        kwargs = kwargs.get('cfg')
        detect_status = kwargs.get('detect_status')
        detect_ip = kwargs.get('detect_ip')
        detect_domain = kwargs.get('detect_domain')
        detect_port = kwargs.get('detect_port')
        self.operate_element(self.__elements['detect_status'], detect_status)
        self.operate_element(self.__elements['detect_ip'], detect_ip)
        self.operate_element(self.__elements['detect_domain'], detect_domain)
        self.operate_element(self.__elements['detect_port'], detect_port)
        self.operate_element(self.__elements['detect_save'])
        if not (detect_ip or detect_domain):
            self.handle_alert()
