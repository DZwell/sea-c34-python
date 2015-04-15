from __future__ import print_function
import io


def lambda_args(*args):
    """Can I pass the args tuple to a lamba function?"""
    l = lambda *args: args
    print(l(*args))


lambda_args(10, 11, 12)
# result: Yes I can.


def filter_text():
    """Can I read a short text and filter to a set of certain words?"""
    f = io.open('test.txt', encoding='utf-8')
    text = f.read()
    f.close()

    words = set(text.split())
    filtered = filter(lambda x: len(x) > 5, words)
    print(
        'Showing the set of words longer than 5 characters.\n\n{filtered}'
        .format(filtered=filtered)
    )


filter_text()
# result: Yes! Here I returned the set of words longer than five characters.


def text_reverse():
    """Can I read a short text, reverse the words, and write back to file?"""
    f = io.open('test.txt', encoding='utf-8')
    text = f.read()
    f.close()

    words = text.split()
    reversed_words = map(lambda x: x[::-1], words)
    text = u" ".join(reversed_words)

    f = io.open('test.txt', 'w')
    f.write(text)
    f.close()
    print('\nReversed the text.')

text_reverse()
# result: Yes. It works as expected.

