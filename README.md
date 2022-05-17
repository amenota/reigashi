# reigashi
something
## Installation
    $ pip install reigashi
## Usage
    from reigashi.tokenization_tools import convert_to_token_labels
    from transformers import BertTokenizer
    
    raw_text = "Hello Tommy22days!"
    raw_labels = [[6, 11, 'PER'], [11, 13, 'NUM']]
    
    tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
    tokens = tokenizer.tokenize(raw_text)
    
    print(convert_to_token_labels(tokens, raw_labels, raw_text, '##'))
    # ['O', 'B-PER', 'B-NUM', 'O', 'O', 'O']
## Note
Support English/Chinese/Japanese