Sentence = "Mr. Miyagi bought cheapsite.com for 1.5 million dollars, i.e. he paid a lot for it. Did he mind? Adam Jones Jr. thinks he didn't. In any case, this isn't true... Well, with a probability of .9 it isn't."
Paragraph = []
counter1 = 0
Sentences = []
Titles = ["Mr.","Mrs.","Dr."]

for a in Sentence.split():
    counter1 += 1
    try:
        if a[-1] == "!" or a[-1] == "?":
            Sentences.append(a)
            x = " ".join(map(str, Sentences))
            Paragraph.append(x)
            Sentences = []
        elif a[-1] == "." and Sentence.split()[counter1][0].isupper() == True and a not in Titles:
            Sentences.append(a)
            x = " ".join(map(str,Sentences))
            Paragraph.append(x)
            Sentences = []
        else:
            Sentences.append(a)
    except IndexError:
        break
x = " ".join(map(str,Sentences))
Paragraph.append(x)
for b in Paragraph:
    print(b)