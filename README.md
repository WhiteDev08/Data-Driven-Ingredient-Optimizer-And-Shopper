# Data-Driven-Ingredient-Optimizer-And-Shopper
This Python project tailored to simplify the grocery shopping process for home cooking enthusiasts. By simply entering the name of a dish, users can access a detailed ingredient list. Additionally, the project integrates with Ocado to recommend optimal purchasing options based on factors such as price, customer ratings, and review counts. Leveraging techniques like web scraping, data cleaning, and analysis, this tool offers valuable insights to enhance the efficiency and cost-effectiveness of grocery shopping for homemade meals.

## Features
- Utilizes OpenAI's language model to fetch ingredients for a specified dish.
- Scrapes Ocado for price, link, rating, and review count of each ingredient.
- Analyzes and filters data to select the best product options.
- Outputs a clean and concise summary for easy decision-making.

### Prerequisites
- Python 3.6+
- OpenAI API Key
- Required Python packages: `requests`, `beautifulsoup4`, `pandas`

### Configuration
Create a `.env` file in the project directory. Add your OpenAI API key to the `.env` file as follows:

```
OPENAI_API_KEY=your_api_key_here
```

### Usage
To use Automated Ingredient Analyzer and Shopper, follow these steps: Run the script:
```
python script.py
```
When prompted, enter the dish name that you wish to make. The program will then output a summary of the best options for each ingredient based on the scraped data.


### Contribution
To contribute to Automated Ingredient Analyzer and Shopper, follow these steps:
```
1. Fork this repository.
2. Create a new branch: git checkout -b branch_name.
3. Make your changes and commit them: git commit -m 'commit_message'.
4. Push to the original branch: git push origin Automated Ingredient Analyzer and Shopper/branch_name.
5. Create the pull request.
```
### License
This project is licensed under the MIT License - see the LICENSE file for details.
