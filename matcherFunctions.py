

import spacy

from spacy.matcher import Matcher
nlp = spacy.load("en_core_web_md")


def test(self, *args):
    for arg in args:
        print(arg)


def singlesearch(Matcher_1, rawdoc):
    test = rawdoc.lower()
    doc = nlp(test)
    matches = Matcher_1(doc)
    for match_id, start, end in matches:
        span = doc[start:end]
        newsent = span.sent
        for word in span:
            newsent = replace_word(str(newsent), str(word))

        markedContent = rawdoc.lower().replace(str(span.sent), newsent)
        return {"detected": True,
                "word1": span,
                "sent": str(span.sent),
                "markedSent": markedContent}
    return {"detected": False}


def doublesearch(Matcher_1, Matcher2, rawdoc):
    doc = nlp(rawdoc.lower())
    matches = Matcher_1(doc)
    for match_id, start, end in matches:
        span = doc[start:end]

        word = span
        sents = span.sent  # ADDED THIS LINE
        doc2 = nlp(str(sents))
        matches2 = Matcher2(doc2)
        for match, start2, end2 in matches2:
            span2 = doc2[start2:end2]
            newsent = span.sent
            words = []
            words.append(span)
            words.append(span2)
            for word in words:
                newsent = replace_word(str(newsent), str(word))
            markedContent = rawdoc.replace(str(span.sent), newsent)
            return {"detected": True,
                    "word1": span,
                    "word2": span2,
                    "sent": str(span.sent),
                    "markedSent": markedContent}

        return {"detected": False}
    return {"detected": False}


def MatcherAprover(control, result):
    if(control):
        if(control == result):
            return 'correclty classified interesting comments'
        else:
            return 'wrong classified interesting comments'
    if not(control):
        if(control == result):
            return 'correclty classified bad comments'
        else:
            return 'wrong classified bad comments'


# def replacestring(doc, test):
#     new_list = []
#     new_words = [token.text if token.text !=
#                  test else str('-----> '+test+' !!! ') for token in doc]
#     return(' '.join(new_words))


doc = "I have created a new home."
# print(replacestring(doc, 'I have designed'))


matches = ['i', 'have', 'created']

matcher = Matcher(nlp.vocab)


def replace_word(orig_text, replacement):
    matcher.add("Rule",  [[{"LOWER": replacement}]])
    tok = nlp(orig_text)
    text = ''
    buffer_start = 0
    for _, match_start, _ in matcher(tok):
        # If we've skipped over some tokens, let's add those in (with trailing whitespace if available)
        if match_start > buffer_start:
            text += tok[buffer_start: match_start].text + \
                tok[match_start - 1].whitespace_
        # Replace token, with trailing whitespace if available
        text += '-----> '+replacement + ' !!! '+tok[match_start].whitespace_
        buffer_start = match_start + 1
    text += tok[buffer_start:].text
    matcher.remove("Rule")
    return text


print(doc)


print(doc)

for match in matches:
    print(match)
    doc = replace_word(doc, match)
