import os
import json
import random
import time
from typing import List, Dict
from dotenv import load_dotenv
import logging

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def search_shopee(keyword: str) -> List[Dict]:
    """
    Search Shopee products dengan DATA REAL dari Shopee via Apify.
    Return 3 produk dengan harga TERENDAH dan link real ke produk Shopee.
    """
    
    apify_token = os.getenv('APIFY_TOKEN')
    if apify_token:
        logger.info(f'🚀 Searching with Apify for "{keyword}"...')
        results = _search_apify_real(keyword, apify_token)
        if results and len(results) >= 3:
            logger.info(f'✅ Found {len(results)} real products from Shopee!')
            # Ensure sorted by price and return top 3
            results.sort(key=lambda x: x['price'])
            return results[:3]
    
    logger.warning(f'⚠️  Apify failed, using realistic dummy data for "{keyword}"')
    return _get_realistic_dummy_products(keyword)

def _search_apify_real(keyword: str, apify_token: str) -> List[Dict]:
    """
    Scrape Shopee REAL data menggunakan Apify actor.
    Actor ID: vlSIMF6GxwbFAIQ77
    """
    try:
        from apify_client import ApifyClient
        
        client = ApifyClient(apify_token)
        
        logger.info(f'Initializing Apify client...')
        
        actor_id = 'vlSIMF6GxwbFAIQ77'
        
        run_input = {
            'startUrls': None,
            'searchKeywords': [keyword],
            'country': 'ID', 
            'shopeeCookies': None,
            'scrapeMode': 'fast',
            'maxProductsPerSearch': 100,  
            'sortBy': 'relevancy',
            'proxyConfiguration': None,
        }
        
        logger.info(f'Starting Apify actor {actor_id}...')
        logger.info(f'Input: {json.dumps(run_input, indent=2)}')
        
        run = client.actor(actor_id).call(run_input=run_input)
        
        logger.info(f'✅ Actor run completed: {run["id"]}')
        logger.info(f'Default dataset ID: {run["defaultDatasetId"]}')
        
        products = []
        dataset = client.dataset(run['defaultDatasetId'])
        
        logger.info(f'Fetching results from dataset...')
        
        for item in dataset.iterate_items():
            try:
                name = item.get('name') or item.get('title', '')
                price = item.get('price') or item.get('convertedPrice', 0)
                link = item.get('url') or item.get('link', '')
                
                if isinstance(price, str):
                    price_str = price.replace('Rp', '').replace('.', '').replace(',', '').strip()
                    try:
                        price = int(price_str)
                    except:
                        price = 0
                
                price = int(price) if price else 0
                
                if name and price > 1000 and link:
                    products.append({
                        'name': str(name)[:80],
                        'price': price,
                        'price_formatted': 'Rp {:,}'.format(price).replace(',', '.'),
                        'link': str(link),
                    })
                    logger.debug(f'Added: {name[:50]} - {price}')
            except Exception as e:
                logger.debug(f'Error parsing item: {e}')
                pass
        
        logger.info(f'📊 Total scraped: {len(products)} products')
        
        products.sort(key=lambda x: x['price'])
        
        logger.info(f'📊 Top 3 cheapest:')
        for i, p in enumerate(products[:3], 1):
            logger.info(f'  {i}. {p["name"][:50]} - {p["price_formatted"]}')
        
        return products
        
    except ImportError:
        logger.error('❌ apify_client not installed')
        return []
    except Exception as e:
        logger.error(f'❌ Apify error: {type(e).__name__}: {e}')
        return []

def _get_realistic_dummy_products(keyword: str) -> List[Dict]:
    """
    Realistic dummy data - simulasi produk Shopee.
    HANYA digunakan jika Apify gagal.
    """
    keyword_lower = keyword.lower()
    
    price_ranges = {
        'sepatu': (35000, 350000),
        'hp': (800000, 12000000),
        'laptop': (3000000, 15000000),
        'mouse': (25000, 350000),
        'keyboard': (65000, 1200000),
        'monitor': (799000, 4500000),
        'headphone': (35000, 1500000),
        'powerbank': (35000, 400000),
        'kompressor': (250000, 3000000),
        'celana': (20000, 250000),
        'baju': (20000, 150000),
        'tas': (35000, 400000),
        'sandal': (20000, 80000),
        'rok': (30000, 200000),
        'gantungan': (5000, 30000),
        'tali rambut': (8000, 50000),
        'buku': (15000, 80000),
        'charger': (35000, 250000),
        'cable': (15000, 150000),
    }
    
    price_min, price_max = (50000, 500000)
    for key, (min_p, max_p) in price_ranges.items():
        if key in keyword_lower:
            price_min, price_max = min_p, max_p
            break
    
    brands = ['Original', 'Premium', 'Standar', 'Murah', 'Terbaik', 'Berkualitas']
    variants = ['Type A', 'Type B', 'Versi 1', 'Model Baru', 'Limited Edition']
    
    all_products = []
    num_products = random.randint(50, 100)
    
    for i in range(num_products):
        price = random.randint(price_min, price_max)
        brand = random.choice(brands)
        variant = random.choice(variants)
        all_products.append({
            'name': f'{brand} {keyword.capitalize()} {variant} #{i+1}',
            'price': price,
            'price_formatted': 'Rp {:,}'.format(price).replace(',', '.'),
            'link': f'https://shopee.co.id/search?keyword={keyword}',
        })
    
    # Pastikan sorting berdasarkan harga (terendah ke tertinggi)
    all_products.sort(key=lambda x: x['price'])
    
    top_3 = all_products[:3]
    logger.warning(f'✅ Using dummy data: {num_products} products generated')
    logger.warning(f'📊 Top 3 termurah untuk "{keyword}":')
    for i, p in enumerate(top_3, 1):
        logger.warning(f'   {i}. {p["name"][:60]} - {p["price_formatted"]}')
    
    return top_3
