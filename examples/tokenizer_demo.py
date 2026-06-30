from transformer.tokenizer import Tokenizer

texts = [
    "I love AI",
    "AI is amazing",
    "I love programming"
]

tokenizer = Tokenizer()

tokenizer.build_vocabulary(texts)

print("Vocabulary:")
print(tokenizer.word_to_index)

print()

encoded = tokenizer.encode("I love ChatGPT")

print("Encoded:")
print(encoded)

print()

decoded = tokenizer.decode(encoded)

print("Decoded:")
print(decoded)