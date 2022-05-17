from transformers import BertTokenizer
from reigashi.tokenization_tools import convert_to_token_labels
import torch

tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")

# raw_text = "Hello Tommy22days!"
# labels = [[6, 11, 'PER'], [11, 13, 'NUM']]
# raw_text = "Hello Tom P, 22days!"
# labels = [[6, 11, 'PER'], [13, 15, 'NUM']]
# raw_text = "Hello Tom P222, I'm 李明!"
# labels = [[6, 11, 'PER'], [20, 22, 'PER']]
# raw_text = "Hi! I'm 田中、よろしく"
# labels = [[8, 10, 'PER']]
raw_text = "##田中##"
labels = [[2, 4, 'PER']]
tokens = tokenizer.tokenize(raw_text)

print(tokens)
print(convert_to_token_labels(tokens, labels, raw_text, '##'))
