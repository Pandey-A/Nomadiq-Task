import ssl
# BYPASS CERTIFICATE ERRORS (Fixes specific for Mac )
ssl._create_default_https_context = ssl._create_unverified_context

import time
import pandas as pd
import random
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from datetime import date, timedelta

ROUTES = [
    {"origin": "DEL", "dest": "DXB"},
    {"origin": "BOM", "dest": "LHR"},
    {"origin": "DEL", "dest": "SIN"},
    {"origin": "BOM", "dest": "DOH"},
    {"origin": "DEL", "dest": "JFK"}
]

class UltimateFlightScraper:
    def __init__(self):
        options = uc.ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-popup-blocking")
        self.driver = uc.Chrome(options=options)
        self.data_list = []

    def scrape_route(self, origin, dest):
        print(f"\n✈️  Scraping All Flights: {origin} -> {dest}")
        today = date.today()
        

        for i in range(1,31): 
            flight_date = today + timedelta(days=i)
            date_str = flight_date.strftime("%Y-%m-%d")
            
            url = f"https://www.google.com/travel/flights?q=Flights%20to%20{dest}%20from%20{origin}%20on%20{date_str}%20one-way"
            
            self.driver.get(url)
            time.sleep(random.uniform(3, 5)) 
            
            try:
               
                print(f"   Day {i}: Loading all flight results...")
                for _ in range(5):
                    self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
                    time.sleep(1)
                try:
                    more_buttons = self.driver.find_elements(By.XPATH, "//button[contains(., 'more flights')]")
                    for btn in more_buttons:
                        btn.click()
                        time.sleep(2)
                except: pass

                flights = self.driver.find_elements(By.CLASS_NAME, "pIav2d")
                print(f"   Found {len(flights)} listings.")

                for flight in flights:
                    try:
                        try:
                            airline = flight.find_element(By.CLASS_NAME, "sSHqwe").text
                        except:
                            try:
                                airline = flight.find_element(By.TAG_NAME, "img").get_attribute("alt")
                            except:
                                airline = "Unknown Airline"

                        try:
                            full_text = flight.text.split('\n')
                            price = 0
                            for line in full_text:
                                if '₹' in line or '$' in line:
                                    clean_price = ''.join(filter(str.isdigit, line))
                                    if clean_price:
                                        price = int(clean_price)
                                        break
                        except: price = 0

                        text_content = flight.text
                        stops = "Non-stop" if "Non-stop" in text_content or "Direct" in text_content else "1+ Stops"
                        if "stop" in text_content and "Non-stop" not in text_content:
                            for line in text_content.split('\n'):
                                if "stop" in line:
                                    stops = line
                                    break
                        
                        duration = "N/A"
                        for line in text_content.split('\n'):
                            if "hr" in line and "min" in line:
                                duration = line
                                break
                        if price > 0: 
                            self.data_list.append({
                                "route": f"{origin}-{dest}",
                                "flight_date": date_str,
                                "days_to_departure": i,
                                "airline": airline,     
                                "price": price,
                                "duration": duration,
                                "stops_count": stops
                            })

                    except Exception as e:
                        continue 

            except Exception as e:
                print(f"   Skipping date due to error: {e}")

    def save_data(self):
        if self.data_list:
            df = pd.DataFrame(self.data_list)
            df = df.sort_values(by=['route', 'flight_date', 'price'], ascending=[True, True, True])
            
            filename = "final_flight_data_all.csv"
            df.to_csv(filename, index=False)
            print(f"\n✅ SUCCESS! Data saved to '{filename}'")
            print(f"   Total Flights Scraped: {len(df)}")
        else:
            print("⚠️ No data collected. Google might be blocking. Try running later.")

    def close(self):
        self.driver.quit()

if __name__ == "__main__":
    bot = UltimateFlightScraper()
    for route in ROUTES:
        bot.scrape_route(route['origin'], route['dest'])
    bot.save_data()
    bot.close()