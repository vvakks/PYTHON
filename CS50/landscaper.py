words = ["There", "are", "a", "number", "of", "reasons", "you", "may", "need", "a", "block", "of", "text", "and", "when", "you", "do", "a", "random", "paragraph", "can", "be", "the", "perfect", "solution.", "If", "you", "happen", "to", "be", "a", "web", "designer", "and", "you", "need", "some", "random", "text", "to", "show", "in", "your", "layout,", "a", "random", "paragraph", "can", "be", "an", "excellent", "way", "to", "do", "this.", "If", "you're", "a", "programmer", "and", "you", "need", "random", "text", "to", "test", "the", "program,", "using", "these", "paragraphs", "can", "be", "the", "perfect", "way", "to", "do", "this.", "Anyone", "who's", "in", "search", "of", "realistic", "text", "for", "a", "project", "can", "use", "one", "or", "more", "of", "these", "random", "paragraphs", "to", "fill", "their", "need"]

lowercase_words = [word.lower() for word in words]

count = {}
for word in lowercase_words:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1

print(count)




        
    