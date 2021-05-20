import os
import random
import re
import sys
from pagerank import crawl
import numpy as np

corpus = crawl(sys.argv[1])
PAGE = "minesweeper.html"
DAMPING = 0.85

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






    # print(f'intiatlised dictionary {dict_x}\n')
    # while True:
    #     print(f'dict_x = {dict_x}\n')
    #     # print(f'emptying dict_x_next\n')
    #     dict_x_next = {}
    #     for page in corpus:
    #         numLinks = len(corpus[page])
    #         print(f'corpus[page] {corpus[page]}')
    #         # print(f'{[dict_x[i]/numLinks for i in corpus[page]]}')
    #         page_rank_link_sum = sum([dict_x[i]/numLinks for i in corpus[page]])
    #         # print(damping_factor* page_rank_link_sum)
    #         # print((1-damping_factor)/len(corpus))
    #         # print((1-damping_factor)/len(corpus) + damping_factor * page_rank_link_sum)
    #         dict_x_next[page] = (1-damping_factor)/len(corpus) + damping_factor * page_rank_link_sum
    #     print(f'parsed dict_x_next = {dict_x_next}\n')
    #     array_x ,array_x_next = np.array(list(dict_x.values())), np.array(list(dict_x_next.values()))
    #     array_subtract =  abs(array_x_next - array_x)
    #     print(f'{array_subtract} \n' )
    #     if any(i < 0.001 for i in array_subtract):
    #         return dict_x
    
    #     else:
    #         dict_x = dict_x_next

print(f'sample_pagerank : {sample_pagerank(corpus,DAMPING,10000)}')
print(iterate_pagerank(corpus,DAMPING))

        
