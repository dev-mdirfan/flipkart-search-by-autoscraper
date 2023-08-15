from autoscraper import AutoScraper
import pandas as pd

search = "realme"
url = "https://www.flipkart.com/search?q={}".format(search)

wanted_list = ["realme C53 (Champion Gold, 128 GB)",
                "₹9,999",
                "₹11,999",
                "16%% off",
                "4.1",
                "1,940 Ratings",
                "174 Reviews",
                "4 GB RAM | 128 GB ROM | Expandable Upto 2 TB",
                "17.12 cm (6.74 inch) HD Display",
                "108MP + 2MP | 8MP Front Camera",
                "5000 mAh Battery",
                "T612 Processor",
                "1 Year Manufacturer Warranty for Phone and 6 Months Warranty for In the Box Accessories",
                "https://rukminim2.flixcart.com/image/312/312/xif0q/mobile/h/h/d/-original-imags487gaqqhcea.jpeg?q=70"
                ]

scraper=AutoScraper()
result=scraper.build(url, wanted_list)
data = scraper.get_result_similar(url, grouped=True)

keys = list(data.keys())

scraper.set_rule_aliases({str(keys[0]):'ImageUrl',str(keys[1]):'Title',str(keys[3]):'Price',str(keys[5]):'Reviews'})

scraper.save("amazon_in.json")

amazon_scraper = AutoScraper()
amazon_scraper.load('search_result.json')

