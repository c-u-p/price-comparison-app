from flask import Flask, render_template, request
import pandas as pd
import random

app = Flask(__name__)

# Simulated scraping function that returns random prices for demonstration
def get_price(product_name):
    # Simulate fetching prices
    return random.uniform(15.0, 30.0)  # Random price between $15 and $30

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/compare', methods=['POST'])
def compare_prices():
    product_name = request.form.get('product_name')

    # Scrape prices from simulated sources
    price_amazon = get_price(product_name)
    price_ebay = get_price(product_name)

    # Create a DataFrame to store results
    data = {
        'Website': ['Amazon', 'eBay'],
        'Price': [price_amazon, price_ebay]
    }
    df = pd.DataFrame(data)

    # Ensure all values are floats and handle missing prices
    df['Price'] = pd.to_numeric(df['Price'], errors='coerce')  # Convert to numeric, NaN for errors
    df = df.dropna(subset=['Price'])  # Drop rows with missing prices

    # Ensure we have valid prices to compare
    if not df.empty and df['Price'].notna().any():
        best_price_row = df.loc[df['Price'].idxmin()]  # Get the row with the minimum price
        best_price = best_price_row['Price']  # Extract the price
        best_website = best_price_row['Website']  # Extract the corresponding website
    else:
        best_price = None  # Handle the case where no valid prices exist
        best_website = None  # Also set best_website to None

    # Pass the results to the HTML template
    return render_template('results.html', tables=[df.to_html()], best_price=best_price, best_website=best_website)

if __name__ == '__main__':
    app.run(debug=True)
