"""
EXP 04 - Basic Word Count MapReduce program
"""
# Input text data (replace with your own text)
text_data = '''
MapReduce is a programming paradigm for processing and generating large datasets with a parallel, distributed algorithm on a cluster.
The MapReduce algorithm contains two important tasks, namely Map and Reduce.
Map takes a set of data and converts it into another set of data, where individual elements are broken down into key-value pairs.
The Reduce task takes the output of the Map as an input and combines those data tuples into a smaller set of tuples.
'''


def mapper(text_data):
    words = text_data.strip().split()
    return [(word, 1) for word in words]


def reducer(mapped_data):
    word_count_dict = {}
    for word, count in mapped_data:
        if word in word_count_dict:
            word_count_dict[word] += count
        else:
            word_count_dict[word] = count
    return word_count_dict.items()


# Map phase
mapped_data = mapper(text_data)

# Reduce phase
reduced_data = reducer(mapped_data)

# Print the word counts
for word, count in reduced_data:
    print(f"{word}: {count}")
