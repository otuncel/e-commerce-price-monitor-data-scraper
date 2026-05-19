import pandas as pd
from bs4 import BeautifulSoup

# Simulated HTML content from the client's competitor website
html_content = """
<html>
    <head><title>Mock Coffee Store - Competitor Products</title></head>
    <body>
        <h1>Our Organic Coffee & Equipment</h1>
        <div class="product-list">
            <div class="product-card" data-id="101">
                <h2 class="product-title"><a href="/products/ethiopia-yirgacheffe">Ethiopia Yirgacheffe Organic Coffee (250g)</a></h2>
                <span class="price">$14.99</span>
                <p class="stock-status in-stock">In Stock</p>
            </div>
            <div class="product-card" data-id="102">
                <h2 class="product-title"><a href="/products/colombia-supremo">Colombia Supremo Dark Roast (500g)</a></h2>
                <span class="price">$22.50</span>
                <p class="stock-status out-of-stock">Out of Stock</p>
            </div>
            <div class="product-card" data-id="103">
                <h2 class="product-title"><a href="/products/hario-v60-starter">Hario V60 Ceramic Starter Set</a></h2>
                <span class="price">$35.00</span>
                <p class="stock-status in-stock">In Stock</p>
            </div>
            <div class="product-card" data-id="104">
                <h2 class="product-title"><a href="/products/guatemala-huehuetenango">Guatemala Huehuetenango Medium Roast (250g)</a></h2>
                <span class="price">$16.25</span>
                <p class="stock-status in-stock">In Stock</p>
            </div>
        </div>
    </body>
</html>
"""

# 1. Initialize the BeautifulSoup object
soup = BeautifulSoup(html_content, 'html.parser')
print("BeautifulSoup object successfully initialized!")

# --- DATA EXTRACTION ---

# Select all product container cards
product_cards = soup.find_all('div', class_='product-card')

# Master list to store structured product dictionaries
all_products = []

# Iterate through each product card to extract specific data fields
for card in product_cards:
    # 1. Extract Product Name (strip whitespace for clean text)
    name = card.find('h2', class_='product-title').text.strip()
    
    # 2. Extract Current Price
    price = card.find('span', class_='price').text.strip()
    
    # 3. Extract Stock Status
    stock = card.find('p', class_='stock-status').text.strip()
    
    # 4. Extract Product URL and build the absolute link
    relative_url = card.find('h2', class_='product-title').find('a')['href']
    full_url = f"https://www.mock-coffeestore-competitor.com{relative_url}"
    
    # Map the extracted variables to a structured dictionary layout
    product_data = {
        "Product Name": name,
        "Current Price": price,
        "Stock Status": stock,
        "Product URL": full_url
    }
    
    # Append the dictionary to the master data list
    all_products.append(product_data)

# --- PANDAS DATA CONVERSION & EXPORT ---

# Convert the list of dictionaries into a Pandas DataFrame
df = pd.DataFrame(all_products)

# Export the DataFrame to a CSV file as requested by the client
# index=False ensures that auto-generated Pandas row numbers are omitted from the final file
df.to_csv('competitor_prices.csv', index=False, encoding='utf-8')

print("\n🚀 Success! Data has been successfully exported to 'competitor_prices.csv'.")
print("\nPreview of the extracted dataset:")
print(df)