# TripAdvisor Scraper

This project is a Python script that scrapes data from TripAdvisor using its GraphQL API to collect detailed information on various locations around the world. Users can specify the type of data they want to scrape (e.g., hotels, restaurants, tourist spots) and the location (e.g., New York, London, Paris) to extract valuable insights like ratings, reviews, descriptions, and more.

## Features

- Scrapes data from multiple TripAdvisor categories:
    - **ACCOMMODATION** (Hotels)
    - **EATERY** (Restaurants)
    - **ATTRACTION** (Tourist Spots)
    - **FLIGHT** (Flight options)
    - **VACATION_RENTAL** (Vacation Rentals)
- Supports multiple popular locations (e.g., New York, Los Angeles, Tokyo, Paris, London, etc.).
- Extracts detailed information such as:
    - Location ID
    - Name of the place
    - Rating
    - Number of reviews
    - URL and Image URL
    - Description
- Saves the scraped data in both CSV, Excel and JSON formats.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/abdullah-shaheer/tripadvisor-scraper.git

## Usage

### Step 1: Set Up

Before running the script, make sure to check the available locations and their corresponding location IDs, which are stored in the `lo_cat` dictionary.

### Step 2: Run the Script

You will be prompted to:

1. Choose a location from the available list (or add a new location to the `lo_cat` dictionary if not listed).
2. Select the type of data you want to scrape (hotels, restaurants, tourist spots, etc.).
3. Choose the keyword to filter your query.

The script will then begin scraping data from TripAdvisor and save it as CSV, Excel and JSON files with the name `tripadvisor_{query}_{location}.csv`, `tripadvisor_{query}_{location}.xlsx` and `tripadvisor_{query}_{location}.json`.

### Step 3: Add Custom Locations

If you want to scrape data from locations not listed in the predefined dictionary, you can add them to the `lo_cat` dictionary by specifying the location name and its corresponding TripAdvisor location ID. Example:

lo_cat["New Location"] = <Location_ID>

### Step 4: View Your Data

Once the scraping process is complete, the results will be saved as:

*   `tripadvisor_{query}_{location}.csv`
*   `tripadvisor_{query}_{location}.xlsx`
*   `tripadvisor_{query}_{location}.json`

Open these files to view the scraped data.

## Example Output

For example, if you choose to scrape hotel data for New York, the output CSV/Excel file will contain columns such as:

*   **Location ID**
*   **Name**
*   **Rating**
*   **Number of Reviews**
*   **Description**
*   **Image URL**
*   **Default URL**

