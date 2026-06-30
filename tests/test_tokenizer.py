from transformer.tokenizer import Tokenizer


def test_tokenizer():

    tokenizer = Tokenizer()

    texts = [
        "I love AI",
        "AI is amazing",
        "I love programming"
    ]

    tokenizer.build_vocabulary(texts)

    encoded = tokenizer.encode("I love AI")

    decoded = tokenizer.decode(encoded)

    assert decoded == "i love ai"

    assert tokenizer.vocabulary_size == 7

    print("All tokenizer tests passed!")


if __name__ == "__main__":
    test_tokenizer()