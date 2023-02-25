import customtkinter
import time
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver


# Function for Crawling
def crawler():
    driver = webdriver.Chrome(ChromeDriverManager().install())

    user_entry = entry.get()
    driver.get(user_entry)

    car_names = driver.find_elements(By.CSS_SELECTOR, ".stories-wrap h2")
    mailage = driver.find_elements(By.CSS_SELECTOR, ".wp-block-table")
    image_list = driver.find_elements(By.CSS_SELECTOR, '.wp-block-image img')

    car_list = car_names[:-2]

    # Using list comprehension for getting car information
    name_list = [car_list[name].text for name in range(len(car_list))]
    mileage_list = [mailage[mile].text.split()[6] for mile in range(len(car_list))]
    fuel_list = [mailage[fuel].text.split()[5] for fuel in range(len(car_list))]
    gear_list = [mailage[gear].text.split()[4] for gear in range(len(car_list))]
    img_list = [image_list[image].get_attribute('src') for image in range(len(car_list))]

    # print(name_list)
    # print(mileage_list)
    # print(fuel_list)
    # print(gear_list)
    # print(img_list)

    for i in range(len(mileage_list)):
        google_form_link = 'https://forms.gle/EyMhMoSDurFYq77x9'
        driver.get(google_form_link)

        time.sleep(2)
        car_name = driver.find_element(By.XPATH,
                                       '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        car_name.click()
        car_name.send_keys(name_list[i])

        time.sleep(2)

        car_mileage = driver.find_element(By.XPATH,
                                          '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
        car_mileage.click()
        car_mileage.send_keys(f'{mileage_list[i]} kmpl')

        time.sleep(2)

        car_image = driver.find_element(By.XPATH,
                                        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        car_image.click()
        car_image.send_keys(img_list[i])

        time.sleep(2)

        car_gear = driver.find_element(By.XPATH,
                                       '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input')
        car_gear.click()
        car_gear.send_keys(gear_list[i])

        time.sleep(2)

        car_fuel = driver.find_element(By.XPATH,
                                       '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input')
        car_fuel.click()
        car_fuel.send_keys(fuel_list[i])

        time.sleep(2)

        submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')
        submit_button.click()

        time.sleep(2)


# GUI Part
FONT = ('Rubrik', 15, 'bold')

# Screen Setup
window = customtkinter.CTk()
window.geometry('500x500')
window.title('Custom Web Crawler')
window.configure(fg_color='#C780FA', padx=20, pady=20)

title_label = customtkinter.CTkLabel(text='Web Crawler', master=window, text_color='black', font=('Rubrik', 30, 'bold'))
title_label.grid(column=0, row=0, padx=20, pady=20)

# Input filled setup
entry = customtkinter.CTkEntry(placeholder_text="Enter url", text_color='black',
                               placeholder_text_color='gray', master=window, font=('Rubrik', 15, 'normal'), height=30,
                               width=410,
                               border_color='black')
entry.grid(column=0, row=1, padx=20, pady=20)

# Button
button = customtkinter.CTkButton(text='Start Crawling', master=window, text_color='black', font=FONT,
                                 border_color='black', fg_color='white', hover_color='#F16767', command=crawler)
button.grid(column=0, row=2, padx=20, pady=20)

window.mainloop()
