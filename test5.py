import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.annotations.AfterMethod;
import org.testng.annotations.BeforeMethod;
import org.testng.annotations.Test;

import org.testng.Assert.assertTrue;


class FirstAutomatedTest():

    @BeforeMethod
    def beforeTest():
            # System.setProperty("webdriver.chrome.driver", "C:/drivers/chromedriver.exe");
            # driver = ChromeDriver()

            driver = webdriver.Chrome(r'C:\Users\kszpo\Downloads\chromedriver_win32 (2)/chromedriver.exe')

    @Test
    def myFirstTest():
        driver.navigate().to("https://duckduckgo.com/")

        driver.findElement(By.id("search_form_input_homepage")).sendKeys("JavaStart")
        driver.findElement(By.id("search_form_input_homepage")).submit()

        pageTitle = driver.getTitle()

        assertTrue(pageTitle.contains("JavaStart"))

    @AfterMethod
    def afterTest():
            driver.close()
            driver.quit()