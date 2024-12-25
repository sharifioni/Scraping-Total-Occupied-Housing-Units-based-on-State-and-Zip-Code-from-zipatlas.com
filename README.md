# Instructions for Running the Python Script

This Python script scrapes housing unit data for various zip codes and calculates the fiber ratio based on the available fiber data. The script uses Selenium and BeautifulSoup for web scraping, along with Pandas to manage and process data.

## Prerequisites

Before running the script, ensure you have the following installed:

1. **Python 3.x**: You can download it from [python.org](https://www.python.org/downloads/).
2. **Required Libraries**: The script uses the following Python libraries:
   - `pandas`
   - `selenium`
   - `beautifulsoup4`

To install these libraries, you can use `pip`:

```bash
pip install pandas selenium beautifulsoup4
```

3. **Chrome WebDriver**: Ensure that the Chrome WebDriver is installed and accessible from your system’s PATH. You can download the appropriate version for your system from [here](https://sites.google.com/a/chromium.org/chromedriver/).

## Script Overview

1. **Reading Data**: The script reads zip codes and related data (including "Total Available Fiber") from an Excel file (`Zip codes.xlsx`).
2. **Web Scraping**: It uses Selenium to open each page associated with the zip codes and scrapes the total number of occupied housing units from the page.
3. **Fiber Ratio Calculation**: The script calculates the fiber ratio by dividing the "Total Available Fiber" by the number of occupied housing units.
4. **Saving Results**: The results (housing units and fiber ratio) are added as new columns in the DataFrame and saved to a new Excel file (`Frontier Fiber Zip Codes, 05.01.2023_updated.xlsx`).

## Instructions for Running the Script

1. **Prepare the Input File**: 
   - Ensure you have an Excel file (`Zip codes.xlsx`) with the following columns:
     - `State`: The state code (e.g., `CA`, `NY`, etc.)
     - `ZIP_Code`: The zip code (can be 5 digits or 4 digits, 4-digit codes will be padded with leading zeroes)
     - `Total Available Fiber`: The total available fiber for the corresponding zip code.

2. **Update the File Paths**:
   - Replace `r'Zip codes.xlsx'` with the path to your input Excel file.
   - Replace `r'Output.xlsx'` with the desired path to save the updated file.

3. **Run the Script**:
   - Run the script in your Python environment.

```bash
python your_script.py
```

4. **Check the Output**: 
   - The updated Excel file will include two new columns:
     - `Housing Units`: The total number of occupied housing units for each zip code.
     - `Fiber Ratio`: The percentage of the fiber ratio (calculated as `Total Available Fiber / Total Occupied Housing Units * 100`).

## Troubleshooting

- **Web Scraping Issues**: If the script does not scrape data properly, ensure that the webpage structure has not changed and that the `find` method is correctly targeting the HTML elements.
- **Selenium Errors**: If Selenium does not work properly, check that your Chrome WebDriver version matches the version of Chrome you have installed.
- **Excel File Issues**: Ensure the Excel file is properly formatted with the correct column names and data.


