# Imports a library called Regular Expression (re), which provides regular expression operations 
import re

# Imports the tiktoken library for Byte Pair Encoding (BPE)
import importlib
import tiktoken



# Similar to SimpleTokenizerV Method, but instead uses a method from a library.
tokenizer = tiktoken.get_encoding("gpt2")

text = (
    "Hello, do you like tea? <|endoftext|> In the sunlit terraces"
    "of someunknownPlace."
)

# tokenizer object has its own encode method
# uses the special string: <|endoftext|>
integers1 = tokenizer.encode(text, allowed_special={"<|endoftext|>"})

# Note: someunknownPlace is broken up into different words 
print(integers1)

# We can conver the token IDS back into the original string
message1 = tokenizer.decode(integers1)

print(message1)

# Now, lets take actual unknown words/gibberish and encode them to see the result
integers2  = tokenizer.encode("Akwirw ier")

# Understand how none of these as cast to the unknown ID, which is around the 50,000 mark according
# to the <|endoftext|> id. 
print(integers2)





