## wikipedia_scraper_world_leaders

This project was created to learn about scrapers.
The program scrapes a given API for information about world leaders. It then structures this data into a dictionary of countries, each of which is a list containing leader dictionaries.

From the data gathered the program extracts wikipedia links to each world leader's page.
The wikipedia pages are then scraped for the first paragraph. Excess characters are removed using regular expression.
This paragraph is added to our leader dictionaries. Bottleneck network calls are sped up with use of a session and caching.

In the end a function saves the output to a new json file.
