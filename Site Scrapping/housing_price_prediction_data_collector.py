import selenium
from msedge.selenium_tools import Edge, EdgeOptions
import time
import xlwt as excel

file = excel.Workbook()
w1 = file.add_sheet('Dataset')
w1.write(0, 0, "Location")
w1.write(0, 1, "Rooms")
w1.write(0, 2, "Bedrooms")
w1.write(0, 3, "Additional_Rooms")
w1.write(0, 4, "Bathrooms")
w1.write(0, 5, "Balconies")
w1.write(0, 6, "Area")
w1.write(0, 7, "Garden")
w1.write(0, 8, "Floor")
w1.write(0, 9, "Price")

options = EdgeOptions()
options.use_chromium = True
prefs = {"profile.managed_default_content_settings.images": 2}
options.add_experimental_option("prefs", prefs)
path = 'drivers/edge88.exe'
driver = Edge(path, options=options)

p = 1
for j in range(1, 90):
    driver.get("https://www.makaan.com/dehradun-residential-property/buy-property-in-dehradun-city?page={}".format(j))
    time.sleep(1)
    print("------------------------------------------------------------------------")
    print("\nPage: ", j, "\n")
    print("------------------------------------------------------------------------")
    for i in range(1, 21):
        rooms = 0
        house = driver.find_element_by_xpath('//*[@id="mod-listing-{}"]/div/div[3]/table/tbody/tr[1]'.format(i))
        house.click()
        driver.switch_to.window(driver.window_handles[1])
        location = driver.find_element_by_xpath(
            '/html/body/div[1]/main/div/div[1]/div[2]/div[1]/div[2]/div[1]/h1/div/span[1]')
        location = location.text
        bedrooms = driver.find_element_by_xpath(
            '/html/body/div[1]/main/div/div[1]/div[2]/div[1]/div[2]/div[1]/h1/span[1]')
        bedrooms = bedrooms.text
        try:
            additionalRooms = driver.find_element_by_xpath(
                '//*[@id="Additional Rooms"]')
            additionalRooms = additionalRooms.text
        except selenium.common.exceptions.NoSuchElementException:
            additionalRooms = 'zzz'
        try:
            bathrooms = driver.find_element_by_xpath(
                '//*[@id="Bathrooms"]')
            bathrooms = bathrooms.text
        except selenium.common.exceptions.NoSuchElementException:
            bathrooms = 0
        if bedrooms[0] != 'R' and int(bedrooms[0]) >= int(bathrooms):
            additionalRooms = str(additionalRooms.replace('zzz', str(int(bedrooms[0]) - int(bathrooms))))
            additionalRooms = str(additionalRooms.replace('-', str(int(bedrooms[0]) - int(bathrooms))))
            bedrooms = str(bathrooms)
            rooms = int(additionalRooms[0]) + int(bedrooms[0])
        else:
            additionalRooms = str(additionalRooms.replace('zzz', '0'))
            additionalRooms = str(additionalRooms.replace('-', '0'))
            bedrooms = str(bedrooms)
            bedrooms = bedrooms.replace('R', '0')
            rooms = int(additionalRooms[0]) + int(bedrooms[0])
        try:
            balconies = driver.find_element_by_xpath('//*[@id="Balconies"]')
            balconies = balconies.text
        except selenium.common.exceptions.NoSuchElementException:
            balconies = 0
        try:
            floor = driver.find_element_by_xpath(
                '//*[@id="Floor"]')
            floor = floor.text
        except selenium.common.exceptions.NoSuchElementException:
            floor = 'zzz'
        try:
            garden = driver.find_element_by_xpath(
                '//*[@id="Overlooking"]')
            garden = garden.text
        except selenium.common.exceptions.NoSuchElementException:
            garden = 'no'
        if 'Garden' in garden:
            garden = 1
        else:
            garden = 0
        area = driver.find_element_by_xpath('/html/body/div[1]/main/div/div[1]/div[2]/div[1]/div[2]/div[1]/h1/span[2]')
        area = area.text
        price = driver.find_element_by_xpath(
            '/html/body/div[1]/main/div/div[1]/div[2]/div[1]/div[2]/div[3]/div[1]/div[1]/span[1]/span[1]')
        price = price.text
        value = driver.find_element_by_xpath(
            '/html/body/div[1]/main/div/div[1]/div[2]/div[1]/div[2]/div[3]/div[1]/div[1]/span[1]/span[2]')
        value = value.text
        if 'Cr' in value:
            price = float(price) * 10000000
        elif 'L' in value:
            price = float(price) * 100000
        if ' sq ft' in area:
            area = str(area)
            area = area.replace(' sq ft', '')
            area = area.replace(',', '')
        if 'zzz' or 'G' in floor:
            floor = str(floor.replace('zzz', '1'))
            floor = str(floor.replace('G', '1'))
        print(i,'.','|', location, '|, ', rooms, '|,', bedrooms[0], '|, ', additionalRooms[0], '|, ', bathrooms, '|, ',
              balconies, '|, ', floor[0], '|, ',
              garden, '|, ', area, '|, ', price, '|')
        rooms = int(rooms)
        bedrooms = int(bedrooms[0])
        additionalRooms = int(additionalRooms[0])
        bathrooms = int(bathrooms)
        balconies = int(balconies)
        floor = int(floor[0])
        garden = int(garden)
        area = int(area)
        price = int(price)

        w1.write(p, 0, location)
        w1.write(p, 1, rooms)
        w1.write(p, 2, bedrooms)
        w1.write(p, 3, additionalRooms)
        w1.write(p, 4, bathrooms)
        w1.write(p, 5, balconies)
        w1.write(p, 6, area)
        w1.write(p, 7, garden)
        w1.write(p, 8, floor)
        w1.write(p, 9, price)
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        p += 1
        file.save('Dataset.xls')
file.save('Dataset.xls')
