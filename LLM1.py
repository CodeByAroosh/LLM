# Imports a library called Regular Expression (re), which provides regular expression operations 
import re

with open("/Users/arooshsalunkhe/Documents/Coding Folder/LLM Project/the-verdict.txt", encoding="utf-8") as input_file:
    raw_text = input_file.read()

# We tokenize the entire text and store it in 'preprocessing' which is a list
preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', raw_text)
preprocessed = [item.strip() for item in preprocessed if item.strip()]

# all_tokens contains all the tokens in preprocessed and sorts them alphabetically
# set() method removes all identical tokens or removes all the same words
# By .extend method, we add two more tokens: <|endoftext|> and <|unk|>
# <|unk|> is used anytime a word not stored in our database (in our case, the verdict story) is used
# <|endoftext|> is used when we have multiple documents and text files. Before the end of each file, we insert this token
#   in order to help the program understand this is a new sample of text and to not mix it up with the previous one
all_tokens = sorted(list(set(preprocessed)))
all_tokens.extend["<|endoftext|>", "<|unk|>"]

# Creates a dictionary; Assigns an integer for every token or 'word' in all_words
# Thus, we create a TokenID for every token
vocab = {token:integer for integer, token in enumerate(all_tokens)}

class SimpleTokenizerV1:

    # Im guessing without having to call it, these types of vars get set up
    def __init__(self, vocab):
        # Stores the token to ID dictionary in its respective format
        self.str_to_int = vocab

        # This stores all the IDs first, them associates them with token (Basically swaps dictionary order); 
        # Think s as the token and i as the ID
        self.int_to_str = {i:s for s, i in vocab.items()}

    #Returns the ids given text
    def encode(self, text):
        preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', text)
                                
        preprocessed = [item.strip() for item in preprocessed if item.strip()]
        ids = [self.str_to_int[s] for s in preprocessed]
        return ids

    #Returns the text given ids
    def decode(self, ids):
        text = " ".join([self.int_to_str[i] for i in ids])

        #Replace the spaces before each punctuation (with "" or removes the space), 
        # as now there are spaces b/w each punctuation and word
        text = re.sub(r'\s+([,.?!"()\'])', r'\1', text)

        return text

# Creates a new SimpleTokenizerV1 object called tokenizer 
tokenizer = SimpleTokenizerV1(vocab)
text = """"It's the last he painted, you know," Mrs. Gisburn said with pardonable pride."""


ids = tokenizer.encode(text)


print(ids)
print(tokenizer.decode(ids))

# print("Total number of character:", len(raw_text))
# print(raw_text[:99])