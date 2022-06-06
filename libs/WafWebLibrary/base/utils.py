#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re
import time 
import sys
from requests import request
import urllib3

from robot.api.deco import keyword
from robot.api import logger
from robot.libraries.BuiltIn import BuiltIn

from selenium import webdriver
from urllib.parse import urlparse

"""
    用于存放实用工具
"""

builtin = BuiltIn()

def time_wait(secs):
    """
        默认sleep 1s
    """
    if secs:
        time.sleep(float(secs))
    else:
        time.sleep(1)

def check_msg(check, msg):
    """
    用于校验check是否在msg中
    如果不存在，则动作为 fail
    """
    if check:
        if not re.findall(check, msg):
            logger.error('Check: \'' + check + '\', but got: ' + msg)
            return builtin.fail('CheckMsg Not in Msg')
        else:
            logger.info('Check: \'' + check + '\', and got: ' + msg)
  
def get_chrome_options():
    """
    设置chrome浏览器默认选项
    返回选项
    """
    os_type = sys.platform
    options = webdriver.ChromeOptions()
    options.add_argument("ignore-certificate-errors")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_experimental_option('detach', True)
    if os_type == 'linux':
        options.add_argument('--no-sandbox')
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
    return options
  
def url_parse(url):
    """
    url likes: scheme://host[:post][/path]
    return: {'scheme': xx, 'host': xx, 'post': xx, 'url': xx}
    """
    d_port = {
        'ssh': '22' ,
        'http': '80' , 
        'https': '443' ,
    }
  
    dict_url = {}
    parsed=urlparse(url)

    dict_url['scheme'] = parsed.scheme
    dict_url['host'] = parsed.hostname
  
    if not parsed.port:
        dict_url['port'] = d_port[dict_url['scheme']]
    else:
        dict_url['port'] = str(parsed.port)
    
    dict_url['url'] = str(dict_url['scheme'] + '://' + dict_url['host'] + ':' + dict_url['port'])
  
    return dict_url
  
def custom_req(method, url, cookies=None, **kwargs):
    urllib3.disable_warnings()
    try:
        rsp = request(method, url, cookies=cookies, **kwargs)
    except Exception as e:
        logger.error(e)
        raise
    return rsp
  
def main():
    time_wait(str(0.2))

if __name__ == "__main__":
    main()

