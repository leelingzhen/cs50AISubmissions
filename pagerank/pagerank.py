import os
import random
import re
import sys
import numpy as np

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    transition_dictionary = {}
    if corpus[page] == set ():
        p = 1/len(corpus)
        for item in corpus:
            transition_dictionary[item] = p
        return transition_dictionary
    else:
        p = (1-damping_factor)/ len(corpus)
        links_set = corpus[page]
        for item in corpus:
            if item in links_set:
                transition_dictionary[item] = p + damping_factor/len(links_set)
            else:
                transition_dictionary[item] = p

                
        return transition_dictionary


def sample_pagerank(corpus, damping_factor, n):
    sample_dict = {item : 0 for item in corpus}
    start_page = random.choice(list(sample_dict.keys()))
    page = start_page
    for i in range (n):
        transistive_model = transition_model(corpus,page,damping_factor)
        new_page = random.choices(list(transistive_model.keys()), weights=list(transistive_model.values()), k=1)[0]
        sample_dict[new_page] += 1
        page = new_page
    for item in sample_dict:
        sample_dict[item] /= n
    return sample_dict

    


def iterate_pagerank(corpus, damping_factor):
    N = len(corpus)
    dict_x = {item : 1/N for item in corpus}
    dict_x_next = {}
    while True:
        for item in dict_x:
            page_link_probability = 0
            for page, link in corpus.items():
                if link == set():
                    link = corpus.keys()
                if item in link:
                    page_link_probability += dict_x[page] / len(link)
            dict_x_next[item] = ((1 - damping_factor) / N) + (damping_factor * page_link_probability)
        array_x ,array_x_next = np.array(list(dict_x.values())), np.array(list(dict_x_next.values()))
        array_subtract = abs(array_x - array_x_next)
        if any(i < 0.001 for i in array_subtract):
            return dict_x
        dict_x = dict_x_next


if __name__ == "__main__":
    main()
