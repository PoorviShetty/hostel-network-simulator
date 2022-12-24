from selenium import webdriver

driver = webdriver.Chrome('chromedriver.exe')

driver.set_network_conditions(
    offline=False,
    latency=5000, 
    download_throughput=1024, 
    upload_throughput=1024) 

driver.get("https://jssstuniv.in/")
