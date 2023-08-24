import requests
from bs4 import BeautifulSoup
import re

# Define a function to detect technologies
def detect_technology(url, patterns):
    
    response = requests.get(url)

    
    if response.status_code == 200:
        
        soup = BeautifulSoup(response.text, 'html.parser')

        
        detected_technologies = {}

        
        for tech, pattern in patterns.items():
            if re.search(pattern, str(soup), re.IGNORECASE):
                detected_technologies[tech] = True
            else:
                detected_technologies[tech] = False

        return detected_technologies

    else:
        print("Failed to fetch the web page.")
        return None

# Define the regex patterns for each technology
patterns = {
    "jQuery": r'<script\s+src=["\'](.*?/jquery.*?\.js)["\']',
    "React.js": r'react(\.production)?\.min\.js',
    "WooCommerce": r'woocommerce',
    "Bootstrap": r'bootstrap(\.min)?\.css',
    "Shopify": r'myshopify\.com',
    "Next.js": r'next(\.min)?\.js',
    "Materialize CSS": r'materialize(\.min)?\.css',
    "PHP": r'php',
    "Python": r'python',
    "Google Maps": r'maps\.googleapis\.com',
}
sample_websites = {
    "jQuery": "https://jquery.com/",
    "React.js": "https://reactjs.org/",
    "WooCommerce": "https://woocommerce.com/",
    "Bootstrap": "https://getbootstrap.com/",
    "Shopify": "https://www.shopify.com/",
    "Next.js": "https://nextjs.org/",
    "Materialize CSS": "https://materializecss.com/",
    # PHP and Python are server-side technologies, so no specific URL provided
    "PHP": "https://Facebook.com/",  # Replace with a real PHP website
    "Python": "https://uber.com/",  
    "Google Maps": "https://developers.google.com/maps/documentation/javascript/overview",
}

# Detect technologies on sample websites
for tech, url in sample_websites.items():
    detected = detect_technology(url, patterns)
    print(f"Detected technologies on {url}: {detected}")
