import pytest
from hashmap_repeated_word import repeated_word
assert repeated_word("") is None
assert repeated_word("quick brown fox jumps over lazy dog.") is None
assert repeated_word("Hello world hello") == "hello"
assert repeated_word("The cat and the hat are on the mat.") == "the"
assert repeated_word("I saw a fox, and the fox saw me!") == "fox"
assert repeated_word("1 2 3 1 2 3 4") == "1"
assert repeated_word("@#$% hello @#$% world @#$% hello") == "hello"
assert repeated_word("Once upon a time, there was a brave princess who...") == "a"
assert repeated_word("It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only...")=='it'
assert repeated_word("It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York...") == "summer"