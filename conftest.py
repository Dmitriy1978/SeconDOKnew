import sys
import platform
import os
global path
#path = os.path.dirname(os.path.realpath(__file__))
#sys.path.append("{0}\\Test".format(path))
import pytest

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    # ======= Add cell to report ========

    # ======= Extra ==================
    extra = getattr(report, 'extra', [])
    if report.when == 'call':
        #driver.save_screenshot('C:\\Users\\John\\PycharmProjects\\SeconDOKnew\\Test_result\\log_screen.png')
        driver.save_screenshot('C:\\Program Files (x86)\\Jenkins1\\workspace\\SeconDOK\\default\\log_screen.png')
        #from selenium import webdriver
        #screen = driver.get_screenshot_as_base64()
        #extra.append(pytest_html.extras.image(screen, mime_type='image/png', extension='png'))
        #url = driver.current_url
        #extra.append(pytest_html.extras.url(url))
        xfail = hasattr(report, 'wasxfail')
        #if (report.skipped and xfail) or (report.failed and not xfail):
            #only add additional html on failure
            #extra.append(pytest_html.extras.html('<div>Additional HTML</div>'))
        report.extra = extra
'''
@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
    Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
    :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_")+".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)
    '''

@pytest.fixture(scope="class")
def start(request):
    system = platform.platform()
    global driver
    if "Windows" in system:
        from selenium import webdriver
        driver = webdriver.Chrome()
        driver.implicitly_wait(5)
        #driver = webdriver.Firefox()
        request.cls.driver = driver
        driver.maximize_window()
        def fin():
            driver.delete_all_cookies()
            driver.close()
            driver.quit()
        request.addfinalizer(fin)


    elif "Linux" in system:
        from selenium import webdriver
        from pyvirtualdisplay import Display                       #Enaible for run on Linux systems
        display = Display(visible=0, size=(1366, 720))             #Enaible for run on Linux systems
        display.start()                                            #Enaible for run on Linux systems
        driver = webdriver.Chrome()
        request.cls.driver = driver
        driver.maximize_window()
        #print(system)

        def fin():
            driver.quit()
            display.stop()                                         # Enaible for run on Linux systems

        request.addfinalizer(fin)

    else:
        print("Unknown platform")
    return driver




    '''
    fixture(scope="session", autouse=True)
    def stop(request):
        def fin():
            driver.delete_all_cookies()
            driver.quit()
            driver.destroy()
        request.addfinalizer(fin)
        return driver

    '''

    '''
    def pytest_addoption(parser):
    parser.addoption("--browser", action="", default="ff")
    browser = request.config.getoption("--browser")
    from selenium import webdriver
    driver = webdriver.Chrome()
    return driver
    from selenium import webdriver
    if browser == "chrome":
          driver = webdriver.Chrome()
     elif browser == "ff":
        driver = webdriver.Firefox()
     else: ValueError ("Unrecognised browser %s" %browser)
    '''
    '''
        #driver.session = sessionHelper
        driver.regHelperPersonal = regHelperPersonal
        driver.regHelperEducation = regHelperEducation
        driver.regHelperProfession = regHelperProfession
        driver.regHelperAddinform = regHelperAddinform
        driver.regHelperBillInfo = regHelperBillInfo
        driver.regHelperMail = regHelperMail
        driver.regHelperDB = regHelperDB
        driver.wait = wait
    '''