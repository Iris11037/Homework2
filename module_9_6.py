def all_variants(text):
    len(text)
    for i in range(len(text)):
        for a in range(len(text) - i):
            yield text[a:a + i + 1]

a = all_variants("abc")
for i in a:
    print(i)