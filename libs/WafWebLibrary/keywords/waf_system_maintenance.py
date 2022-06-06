#!/usr/bin/env python
# -*- coding:utf-8 -*-

import time
import telnetlib
from ..base import keyword, logger
from ..base import WafWebDriver

class WafSystemMaintenanceKeywords(WafWebDriver):
    """
        [1] http://robotframework.org/robotframework/#user-guide
        [2] https://robotframework.org/SeleniumLibrary/SeleniumLibrary.html
        [3] https://robotframework.org/robotframework/latest/libraries/BuiltIn.html
        [4] https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html
    """
    __elements = {
        'system': {'type': 'click', 'locator': 'link:系统'},
        'system_maintenance': {'type': 'click', 'locator': 'link:系统维护'},
        'reboot': {'type': 'click', 'locator': 'css:#system-device-restart label'},
        # 'user': { 'type': 'input', 'locator': 'id:user_name', 'hide': False, },
        # 'main': { 'type': 'click', 'locator': 'css:span', },
        # 'proxy': { 'type': 'click', 'locator': 'link:纯代理', 'sleep': 2, },
        # 'proxy-alert': {'type': 'alert', 'action': 'ACCEPT', 'check': '切换完成', 'sleep': 6, },
    }
    
    def __init__(self):
        super().__init__()
        self.telnet = telnetlib.Telnet()
        
    @keyword
    def dev_reboot(self):
        self.operate_element(self.__elements['reboot'])
        self.handle_alert()

    @keyword
    def click_system(self):
        self.operate_element(self.__elements['system'])

    @keyword
    def click_system_maintenance(self):
        self.operate_element(self.__elements['system_maintenance'])

    @keyword
    def dev_connectivity(self, **kwargs):
        kwargs = kwargs.get('cfg')
        timeout = kwargs.get('timeout')
        ip_addr = kwargs.get('master')
        port = kwargs.get('port')
        start_time = time.time()
        end_time = start_time + int(timeout)
        while start_time < end_time:
            start_time = time.time()
            try:
                time.sleep(10)
                telnetlib.Telnet(ip_addr, port)
                self.handle_alert()
                break
            except (ConnectionRefusedError, TimeoutError):
                if start_time < end_time:
                    pass
                else:
                    logger.error("设备重启超时, IP: %s" % ip_addr)
                    raise