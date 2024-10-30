import spacy

nlp = spacy.load("tr_core_news_md")

sentence = "Ankara'daki turistik yerler nereler ?"

doc = nlp(sentence)

# Ögeler
for token in doc:
    # print(f"{token.text}: {token.dep_} -> {token.head.text}")
    print(token.cluster)  # bağlı olduğu kök kelime bilgisini göstermesidir
    # print(token.dep_) # etiketlerinin  cümledeki dilbilgisel ilişkileri yansıttığını gösterir
    # print(token.orth_)
# Token açıklamaları:
# nsubj (nominal subject): özne
# dobj (direct object): nesne
# ROOT: yüklem
# amod: bir ismi niteleyen sıfatı belirtir yeşil elmadaki yeşil 
# advmod: bir fiili, sıfatı veya diğer zarfları niteleyen zarfı belirtir hızlı koştu daki hızlı 



