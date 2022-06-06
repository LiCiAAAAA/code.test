#!/usr/bin/env python
# -*- coding:utf-8 -*-

from ..base import keyword, logger
from ..base import WafWebDriver

class WafConfigGlobalKeywords(WafWebDriver):
    """
        [1] http://robotframework.org/robotframework/#user-guide
        [2] https://robotframework.org/SeleniumLibrary/SeleniumLibrary.html
        [3] https://robotframework.org/robotframework/latest/libraries/BuiltIn.html
        [4] https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html
    """
    __elements = {
        'gloable_cfg': {'type': 'click', 'locator': 'link:全局配置',},
        'analysis_method': {'type': 'select', 'locator': 'id:analysis-method',},
        'xff_key': {'type': 'input', 'locator': 'id:analysis-xff-key',},
        'trusted_ip': {'type': 'input', 'locator': 'id:analysis-url-trustedip',},
        'src_ip_save': {'type': 'click', 'locator': 'id:#global\\.analysis\\.save label',},
        'global_deploy': {'type': 'select', 'locator': 'id:global.deploy',},
        'deploy_save': {'type': 'click', 'locator': 'css:#global\\.deploy\\.save label',},
        # 'user': { 'type': 'input', 'locator': 'id:user_name', 'hide': False, },
        # 'main': { 'type': 'click', 'locator': 'css:span', },
        # 'proxy': { 'type': 'click', 'locator': 'link:纯代理', 'sleep': 2, },
        # 'proxy-alert': {'type': 'alert', 'action': 'ACCEPT', 'check': '切换完成', 'sleep': 6, },
    }
    
    def __init__(self):
        super().__init__()
        
    @keyword
    def click_gloable_cfg(self,):
        self.operate_element(self.__elements['gloable_cfg'])

    @keyword
    def src_ip_enable(self, **kwargs):
        kwargs = kwargs.get('cfg')
        trusted_ip = kwargs.get('trusted_ip')
        analysis_method = kwargs.get('analysis_method')
        xff_key = kwargs.get('xff_key')
        self.operate_element(self.__elements['analysis_method'], analysis_method)
        if xff_key:
             self.operate_element(self.__elements['xff_key'], xff_key)
        self.operate_element(self.__elements['trusted_ip'], trusted_ip)
        self.operate_element(self.__elements['src_ip_save'])

    @keyword
    def global_deploy(self, **kwagrs):
        kwagrs = kwagrs.get(kwagrs)
        global_deploy = kwagrs.get('global_deploy')
        self.operate_element(self.__elements['global_deploy'], global_deploy)
        self.operate_element(self.__elements['deploy_save'], global_deploy)

    