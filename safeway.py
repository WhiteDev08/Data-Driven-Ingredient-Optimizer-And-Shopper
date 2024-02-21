import requests
from bs4 import BeautifulSoup
import pandas as pd
import input as ip
ingredients_list = []
ingredients_list=ip.ip1()
print(ingredients_list)
# Define a global list of ingredients
#ingredients_list = ["salt", "sugar", "flour"]  # Example list, you can modify it as needed

base_url = "https://www.ocado.com/search?entry="

def scrape_ocado_prices(ingredients):
    # Initialize an empty list to store the results
    results = []

    for ingredient in ingredients:
        full_url = base_url + ingredient
        response = requests.get(full_url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            
            li_elements = soup.find_all('li', class_=lambda x: x and ('fops-item--featured' in x or 'fops-item--cluster' in x))
            
            for li in li_elements:
                fop_item = li.find('div', class_='fop-item')
                if fop_item:
                    fop_content_wrapper = fop_item.find('div', class_='fop-contentWrapper')
                    if fop_content_wrapper:
                        # Price extraction
                        price_group_wrapper = fop_content_wrapper.find('div', class_='price-group-wrapper')
                        if price_group_wrapper:
                            price_span = price_group_wrapper.find('span', class_='fop-price')
                            price = price_span.text.strip() if price_span else "Price not found"
                        else:
                            price = "Price not found"
                        
                        # Link extraction
                        a_tag = fop_content_wrapper.find('a')
                        href = a_tag['href'] if a_tag and 'href' in a_tag.attrs else None
                        full_href = f'www.ocado.com{href}' if href else 'Link not found'

                        # Rating extraction
                        review_wrapper = fop_content_wrapper.find('div', class_='review-wrapper')
                        if review_wrapper:
                            rating_span = review_wrapper.find('span', class_='fop-rating-inner')
                            rating = rating_span['title'].split()[1] if rating_span and 'title' in rating_span.attrs else "Rating not found"
                            
                            # Count extraction
                            count_span = review_wrapper.find('span', class_='fop-rating__count')
                            count_text = count_span.text.strip() if count_span else "Count not found"
                            count = count_text[count_text.find("(")+1:count_text.find(")")] if "(" in count_text and ")" in count_text else "Count not found"
                        else:
                            rating = "Rating not found"
                            count = "Count not found"
                        
                        # Append the collected data
                        results.append({
                            "Ingredient": ingredient, 
                            "Price": price, 
                            "Link": full_href, 
                            "Rating": rating, 
                            "Count": count
                        })

        else:
            # In case the page request fails, log the ingredient with a failure notice
            results.append({"Ingredient": ingredient, "Price": "Failed to fetch data", "Link": "Link not found", "Rating": "Rating not found", "Count": "Count not found"})

    # Convert the results list to a pandas DataFrame
    return pd.DataFrame(results)

# Call the function and store the result in a variable
df_prices = scrape_ocado_prices(ingredients_list)

# Display the DataFrame
print(df_prices)
df_prices.to_csv("result.csv")
