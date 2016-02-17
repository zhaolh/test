#!/usr/bin/python

def char_freq(str):
    list_one = list(str)
    dict_s = {}
    for key in list_one:
        if key in dict_s:
            value = dict_s[key]
            dict_s[key] = value + 1
        else:
            dict_s[key] = 1

    for key in dict_s:
        print "dict[%s]:" %key, dict_s[key]

#print "call char_freq\n"
#char_freq("abababacdefdfe")


def word_len(list_words):
    list_len = []
    length = len(list_words)
    i = 0
    while i < length:
        value = list_words[i]
        #list_len[i] = len(value)
        list_len.append(len(value))
        i += 1

    i = 0
    while i < length:
        print "%s:" %list_words[i], list_len[i]
        i += 1

#print "call word_len\n"
#word = ['asdfs', '2902398', 'sadkjlfsldfowe', 'wosoiklsdfopiwe', '98126dhid873jke09']
#word_len(word)


def max(x, y):
    value = x
    if x < y:
        value = y
    return value

def max_in_list(list_num):
    value = reduce(max, list_num)
    print "%d" %value

#print "call max_in_list\n"
#list_num = [12, 234, 556, 928, 23, 49, 495, 182, 92]
#max_in_list(list_num)


def number_file(path):
    i = 0
    fi = open(path, "r")
    fo = open("number.file", "w")
    while True:
        i += 1
        line = fi.readline()
        if line:
            s = "%d %s" % (i, line)
            fo.write(s)
        else:
            break
    fo.close()
    fi.close()

#print "call number_file\n"
#number_file("a.txt")


def balanced(str):
    stack = []
    for character in str:
        if character == '[':
            stack.append(character)
        elif character == ']':
            if len(stack) > 0:
                stack.pop(-1)
            else:
                return False
        else:
            pass
    if len(stack) == 0:
        return True
    else:
        return False

str = "[][[[asleidk]]][[]][]"
flag = balanced(str)
if flag:
    print "%s is balanced" % str
else:
    print "%s is not balanced" % str

