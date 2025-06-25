from data_collection import merging_data
from thefuzz import  process
import json
import logging


with open('used_token.json', 'r', encoding='utf8') as file:
    used_tokens = json.load(file)


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
        with open("used_token.json", "w") as file:
            json.dump(used_tokens, file,indent=4)
        if not found:
           return found, merging_data(search)
            
        else: 
            return found ,search 
    except Exception as e:
        logging.ERROR(f'thier was an error as {e}')





