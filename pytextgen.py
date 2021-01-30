#!/usr/bin/python

from sys    import argv
from random import choice

def gen(text, limit):
    vocab = {}
    result = ""
    
    for i in range(0, len(text)-1):
        if text[i] in vocab:
            vocab[text[i]] += text[i+1]
        else:
            vocab[text[i]] = text[i+1]

    end = text[-1]
    if end in vocab:
        vocab[end] += text[1]
    else:
        vocab[end] = text[1]
    
    last = choice(text)
    for k in range(0, limit):
        result += last
        last = choice(vocab[last])
    result += last

    return result

def main():
    infile = ""
    outfile = ""
    limit = 0
    
    argc = len(argv)
    if(argc == 4):
        infile = argv[1]
        outfile = argv[2]
        limit = int(argv[3])
    else:
        print("Usage: pytextgen infile outfile limit")

    f_in = open(infile, "r")
    text = f_in.read()
    f_in.close()

    f_out = open(outfile, "w")
    result = gen(text, limit)
    f_out.write(result)
    f_out.close()

if __name__ == "__main__":
    main()
