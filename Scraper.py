import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

# Read zip codes from an Excel file
zip_codes_df = pd.read_excel(r'Zip codes.xlsx', header=0)
print(zip_codes_df)

# Set up Chrome options to run headless
chrome_options = Options()
chrome_options.add_argument('--headless')  # Run Chrome in headless mode (without opening a browser window)

# Add headers to the Chrome options
chrome_options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36')

# Create a WebDriver instance
driver = webdriver.Chrome(options=chrome_options)

# Create empty lists to store Housing Units and Fiber Ratio values
housing_units_list = []
fiber_ratio_list = []

# Loop through each row in the DataFrame
for index, row in zip_codes_df.iterrows():
    state = row['State']
    zip_code = str(row['ZIP_Code'])

    # Convert 4-digit zip codes to string and add a leading '0'
    if len(zip_code) == 4:
        zip_code = '0' + zip_code

    # Construct the URL with the state and zip code
    url = f"https://zipatlas.com/us/{state.lower()}/zip-code-{zip_code}.htm"

    # Open the page in the WebDriver
    driver.get(url)

    # Wait for JavaScript to execute (you may need to adjust the time based on the complexity of the page)
    driver.implicitly_wait(1)

    # Get the page content
    page_content = driver.page_source

    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(page_content, 'html.parser')

    # Find the specific <td> element with the text "Total Occupied Housing Units"
    target_td = soup.find('td', text='Total Occupied Housing Units')

    # Find the next <td> element after the target_td
    next_td = target_td.find_next('td')

    # Extract the text content of the next <td> element
    if next_td:
        total_occupied_housing_units = next_td.text.strip()
        print(f"State: {state}, Zip Code: {zip_code}, Total Occupied Housing Units: {total_occupied_housing_units}")

        # Convert Housing Units to numbers
        housing_units = int(total_occupied_housing_units.replace(',', ''))  # Remove commas and convert to int
        housing_units_list.append(housing_units)

        # Calculate Fiber Ratio and append to the list
        total_available_fiber = row['Total Available Fiber']
        fiber_ratio = (total_available_fiber / housing_units) * 100  # Calculate ratio and convert to percentage
        fiber_ratio_list.append(f'{fiber_ratio:.2f}%')  # Format as string with two decimal places and add %

    else:
        print(f"State: {state}, Zip Code: {zip_code}, Next <td> element not found")
        housing_units_list.append(None)  # Append None if data is not found
        fiber_ratio_list.append(None)  # Append None for Fiber Ratio if data is not found

# Add 'Housing Units' and 'Fiber Ratio' columns to the DataFrame
zip_codes_df['Housing Units'] = housing_units_list
zip_codes_df['Fiber Ratio'] = fiber_ratio_list

# Save the updated DataFrame to the Excel file
zip_codes_df.to_excel(r'Output.xlsx', index=False)

# Close the WebDriver
driver.quit()

