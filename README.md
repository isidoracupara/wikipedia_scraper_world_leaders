## wikipedia_scraper_world_leaders

This project was created to learn about scrapers.
In this exercise, the program sceapes a given API for information about world leaders. It then structures this data into a dictionary of countries, each of which is a list containing leader dictionaries.

From the data gathered the program extracts wikipedia links to each world leader's page.
These pages are then scraped for the first paragraph. Excess characters are removed using regular expression.
This paragraph is added to our leader dictionaries. Errors and slow process are resolved by session and requesting cookies in case of status error.

In the end a function that saves the output to a new text file.
