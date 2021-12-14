## python file for formatting Singlish data from talkingcock and wiktionary

import json

fh = open(r"singlish-wiktionary.json")
corpus = json.loads(fh.read())

example_list = []
print("length of corpus = " + str(len(corpus)))
for lex in corpus:
    entrydeets = corpus[lex]
# entrydeets = corpus["%27cher"]
    for insidedeets in entrydeets:
        definitions = insidedeets["definitions"]
        for definition in definitions:
            examples = definition["examples"]
            # print(len(examples))
            if len(examples) > 0:
                for sentence in examples:
        # examples = definitions["examples"]
                    # print(type(sentence))
                    example_list.append(sentence)
                # print(sentence)
                # break

enum_list = enumerate(example_list)
print(list(enum_list))
# import codecs
# f = codecs.open('wikienum.txt', 'w', encoding='utf8')
# for item in example_list:
#     f.write(item + "\n")
# with open('wikiexamples.txt', 'w') as f:
#     for item in example_list:
#         f.write(item + "\n")