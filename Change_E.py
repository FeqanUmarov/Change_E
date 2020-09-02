sentence = "Her alışqanlıq elimizi daha bacarıqlı, ağlımızı isə daha bacarıqslz hala getirir"
sentence = list(sentence)

for s in sentence:
    if s=="e":
        index = sentence.index(s)
        sentence[index]="ə"

for s in sentence:
    print(s,end="")