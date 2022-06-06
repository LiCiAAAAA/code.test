*** Settings ***
Variables         .${/}ssl_sup_cfg.yml
Variables         .${/}xff_policy_cfg.yml

*** Variables ***
&{file_path}    cer_path=${CURDIR}${/}test.cer    key_path=${CURDIR}${/}test.key
