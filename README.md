# Wee-Scraper

## Overview

Wee-Scraper is a Python-based web scraper that allows you to extract text, images, and links from any webpage. Built with Streamlit for a user-friendly interface, it also features a filtering system to target specific HTML classes or types.

## Features

- **Text Extraction**: Scrape all visible text from a webpage.
- **Image Extraction**: Download and display all images from the webpage.
- **Hyperlink Extraction**: Retrieve and list all hyperlinks.
- **Filtering System**: Optionally filter elements by HTML class/type.

## Usage

1. **Installation**:
   Ensure you have Python installed. Install the necessary libraries by running:
   ```bash
   pip install requests beautifulsoup4 streamlit
   ```

2. **Running the Scraper**:
   - Save the provided code into a Python file, for example, `wee_scraper.py`.
   - Run the script using Streamlit:
     ```bash
     streamlit run wee_scraper.py
     ```

3. **Interface**:
   - **URL Input**: Enter the URL of the webpage you want to scrape.
   - **Filtering**: Enable or disable filtering by HTML class/type.
   - **Scrape**: Click the "Scrape" button to start extracting data.

4. **Example**:
   - To scrape weather information from a site like `at.wetter.com`, enter the URL and use the class `rtw_temp` to filter.
   - **Output**:
     ```text
     15 C°
     ```

## Screenshots

- **Interface Example**:
  ![Image Example](https://cdn.discordapp.com/attachments/1280252232209530894/1283417678593265802/image.png?ex=66e2eb5b&is=66e199db&hm=7effafc4d7ecbc9aae4a8e4714470d355d69108ccdffce2c856c641114248343&)

- **Scraping Example**:
  ![Screenshot Example](https://cdn.discordapp.com/attachments/1280252232209530894/1283417306742915132/image.png?ex=66e2eb02&is=66e19982&hm=567bb3f149d17edc87f9475401fae6f9760b8ec239963208eb63417be0baec32&)

## Contributing

Contributions are welcome! If you have suggestions or improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
