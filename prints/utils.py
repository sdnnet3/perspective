import requests
from bs4 import BeautifulSoup
import re

def scrape_product_details(url):
    """Scrapes product details from the given URL."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        html_content = response.text

        soup = BeautifulSoup(html_content, 'html.parser')

        # Extract name from the <title> tag
        title_tag = soup.find('title')
        name = title_tag.get_text(strip=True) if title_tag else 'N/A'

        # Extract image URL
        image_tag = soup.select_one('meta[property="og:image"]')
        image_url = image_tag['content'].strip() if image_tag else 'N/A'

        # Extract price from <h2> tag within <aside>
        aside_tag = soup.find('aside')
        price_tag = aside_tag.find('h2') if aside_tag else None
        price_text = price_tag.get_text(strip=True) if price_tag else 'N/A'
        price = re.search(r'\$\d+(\.\d{2})?', price_text).group() if price_text != 'N/A' else 'N/A'

        # Extract type
        type_tag = soup.find('h3')
        type_of_print = type_tag.get_text(strip=True) if type_tag else 'N/A'

        # Initialize variables
        size = paper = surface = mounting = 'N/A'

        # Extract product details based on type
        product_details = soup.find('div', class_='productDetails')
        if product_details:
            details = product_details.find_all('dt')
            for detail in details:
                term = detail.get_text(strip=True)
                description = detail.find_next_sibling('dd').get_text(strip=True)

                if term == 'Size':
                    size = description.encode('latin1').decode('utf-8')
                elif term == 'Paper' and type_of_print == 'Fine Art Print':
                    paper = description.encode('latin1').decode('utf-8')
                elif term == 'Surface' and type_of_print == 'Photo Print':
                    surface = description.encode('latin1').decode('utf-8')
                elif term == 'Mounting' and type_of_print == 'Photo Print':
                    mounting = description.encode('latin1').decode('utf-8')

        # Construct the type field and logic for each type
        type_field = 'N/A'
        if type_of_print == 'Fine Art Print':
            type_field = f"{type_of_print}\nPaper: {paper}"
        elif type_of_print == 'Photo Print':
            type_field = f"{type_of_print}\nSurface: {surface}\nMounting: {mounting}"

        # Return the extracted data
        return {
            'name': name,
            'price': price,
            'image_url': image_url,
            'size': size,
            'type': type_field,
        }

    except requests.RequestException as e:
        return {'error': str(e)}
