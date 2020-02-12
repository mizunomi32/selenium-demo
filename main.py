import time
import argparse
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def main(url):
    driver = webdriver.Remote(
    command_executor='http://selenium-hub:4444/wd/hub',
    desired_capabilities=DesiredCapabilities.CHROME)
    driver.get(url)
    time.sleep(30)
    driver.close()


parser = argparse.ArgumentParser(description='このプログラムの説明（なくてもよい）')

parser.add_argument('arg1', help='この引数の説明（なくてもよい）')    # 必
args = parser.parse_args()    # 4. 引数を解析

print('arg1='+args.arg1)
main(args.arg1)
