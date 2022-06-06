*** Settings ***
Documentation     A resource file with reusable keywords and variables.
...
...               The system specific keywords created here form our own
...               domain specific language. They utilize keywords provided
...               by the imported SeleniumLibrary.
# Library           yaml
Variables         .${/}global_config.yml
Variables         .${/}run_cfg.yml
# *** Variables ***
# ${MASTER}         10.20.192.54
# ${BROWSER}        Chrome
# ${DELAY}          0
# ${VALID USER}     admin
# ${VALID PASSWORD}    adminadmin
# ${LOGIN URL}      https://${MASTER}/user.m?a=login
# ${WELCOME URL}    https://${MASTER}/main.m
# ${USER}           admin
# ${PWD}            adminadmin