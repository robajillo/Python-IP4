import urllib.request,json
from .models import Quote

base_url = None

def configure_request(app):
    global base_url 
    base_url = app.config['QUOTES_API_BASE_URL']

def get_quotes(author):
    
    get_quotes_url = base_url.format(author)

    with urllib.request.urlopen(get_quotes_url) as url:
        get_quotes_data = url.read()
        get_quotes_response = json.loads(get_quotes_data)

        quotes_results = None

        if get_quotes_response['quotes']:
            quotes_results_list = get_quotes_response['quotes']
            quotes_results = process_quotes(quotes_results_list)

    return quotes_results


def process_quotes(quote_list):
    
    quote_results = []

    for quote_item in quote_list:
        id = quote_item.get('id')
        author = quote_item.get('author')
        quote = quote_item.get('quote')
        permalink = quote_item.get('permalink')
        
        quote_object = Quotes(id,author,quote,permalink)
        
        quote_results.append(quote_object)

    return quote_results