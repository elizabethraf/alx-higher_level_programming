#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == 0:
        sentence = None
    if sentence:
        sen_len = len(sentence)
    else:
        sen_len = 0
    return (len(sentence), sentence[0] if len(sentence) > 0 else None)
