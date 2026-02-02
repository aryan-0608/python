# write a python program a translate a message into secert code language. like use rules to translate normal english into secret code language.
# use te rules below to translate normal english into secret code language


# coding
# if the word contains atleast 3 characters,remove the first letter
# and append it at the end

# now append three random characters at the starting and the end
# else:

# simply reverse the string

# Decoding

# if the  word contain less the 3 charcters, reverse it
# else:
#     remove 3 random charcters from start and end. now remove  the least
# letter and append it  to the begining of the word.

st = input("Enter message: ")
coding = True

if coding:
    words = st.split()   # missing line
    nwords = []
    for word in words:
        if len(word) >= 3:
            r1 = "dsf"
            r2 = "jkr"
            stnew = r1 + word[1:] + word[0] + r2
            nwords.append(stnew)
    print(" ".join(nwords))  # print outside loop
