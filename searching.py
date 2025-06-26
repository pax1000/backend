from thefuzz import  process 
import json
import logging
from database import most_searched

with open('used_token.json', 'r', encoding='utf8') as f:
    used_tokens = json.load(f)


def update_token_and_terms(search):
    try :
        found = False
        search_tokens = search.split()
        for tokens in used_tokens:
            if (match := process.extractOne(tokens['token'], search_tokens)) and match[1] > 80:
                tokens['count'] = tokens['count'] + 1
                found = True
                break
            inputs = tokens['inputs']
            for input in inputs:
                if (match := process.extractOne(input['term'], search_tokens)) and match[1] > 80:
                    tokens['count'] = tokens['count'] + 1
                    input['count'] = input['count'] +1
                    found = True
        if  found:
            with open("used_token.json", "w") as f:
                json.dump(used_tokens, f,indent=4)
        else :    
            logging.info('reqire new scraping')
        most_searched(search)
        return  search 
    except Exception as e:
        logging.ERROR(f'thier was an error as {e}')




