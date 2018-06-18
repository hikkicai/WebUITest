var webdriver = require('selenium-webdriver'),  
    By = webdriver.By,  
    until = webdriver.until;  
      
var driver = new webdriver.Builder()  
    .forBrowser('chrome')  
    .build();  
      
driver.get('https://www.baidu.com');  
driver.findElement(By.id('kw')).sendKeys('selenium');  
driver.findElement(By.id('su')).click();  
driver.wait(until.titleIs('selenium_百度搜索'));  

var settings = driver.findElement(By.css('#u > a.pf'));
driver.actions().mouseMove(settings).perform();
driver.findElement(By.css('#wrapper > div.bdpfmenu > a.setpref')).click();

driver.wait(until.elementIsEnabled(driver.findElement(By.id('s1_2'))), 1000);
driver.findElement(By.id('s1_2')).click();

driver.findElement(By.id('nr')).click();
driver.findElement(By.css('#nr > option:nth-child(2)')).click();

driver.sleep(3000);
driver.quit();  