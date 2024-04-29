import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import urlopen

base_url = "https://quotes.toscrape.com/page/{}"
num_pages = 10

quote_list = []
author_list = []
tags_list = []

for page_num in range(1, num_pages + 1):
    url = base_url.format(page_num)
    response = requests.get(url)
    
  
    soup = BeautifulSoup(response.content, "html.parser")
        
    #for each div class we need to get the quote, author, and the tags
    quotes = soup.find_all(class_="quote")
    for quote in quotes:
        text = quote.find(class_="text").get_text()
        author = quote.find(class_="author").get_text()
        tags = [tag.get_text() for tag in quote.find_all(class_="tag")]

        #Append Them to the list that we made outside the loop
        quote_list.append(text) 
        author_list.append(author)
        tags_list.append(tags) 

        #see if it is working  
        #print(f"Quote: {text}")
        #print(f"Author: {author}")
        #print(f"Tags: {tags}\n")

#Author Stats
#Number of Quotes by Each Author
author_count = {}
for author in author_list:
    if author in author_count:
        author_count[author] += 1
    else:
        author_count[author] = 1

#Author with the most and least quotes
most_quotes = max(author_count, key=lambda x: author_count[x])
least_quotes = min(author_count, key=lambda x: author_count[x])

print(f"Author with the most quotes: {most_quotes}, Number of quotes: {author_count[most_quotes]}")
print(f"Author with the least quotes: {least_quotes}, Number of quotes: {author_count[least_quotes]}\n")


#Quote Analysis
#Determine the average length of the quotes
quote_length = []
for q in quote_list:
    length = len(q)
    quote_length.append(length)
    count_of_quotes = len(quote_list)
    total_length = sum(quote_length)
    avg = round(float(total_length) / float(count_of_quotes),)
print(f"Average Length of Each Quote: {avg} Words \n")

#Find the shortest and longest
longest_quote = max(quote_list, key=len)
#print(f"Longest Quote is:\n {longest_quote}")
shortest_quote = min(quote_list,key=len)
#print(f"Shortest Quote is:\n {shortest_quote}")


#Tag Analysis
#Turn the list of list into one giant list
all_tags = [x for tags in tags_list for x in tags]

#Number of tags used in total
total_tags = len(all_tags)
print(f"Total Tags on all Quotes: {total_tags}")

#Tag Distribution
tag_count = {}
for tag in all_tags:
    if tag in tag_count:
        tag_count[tag] += 1
    else:
        tag_count[tag] = 1

most_pop_tag = max(tag_count, key=lambda x: tag_count[x])
print(f"Most popular tag: {most_pop_tag}, was used {tag_count[most_pop_tag]} times\n")

#Create the two grpahs
import plotly.graph_objects as plot


sorted_tags = sorted(tag_count.items(), key=lambda item: item[1], reverse=True)
top_ten_tags = sorted_tags[:10]

tags = [item[0] for item in top_ten_tags]
counts = [item[1] for item in top_ten_tags]

graph1 = plot.Figure(data=[plot.Bar(x=tags, y=counts)])

graph1.update_layout(title='Top 10 Tags by Popularity', xaxis_title='Tags', yaxis_title='Count')

sorted_author = sorted(author_count.items(), key=lambda item: item[1], reverse=True)
top_ten_authors = sorted_author[:10]

authors = [item[0] for item in top_ten_authors]
a_counts = [item[1] for item in top_ten_authors]

graph2 = plot.Figure(data=[plot.Bar(x=authors,y=a_counts)])
graph2.update_layout(title='Top 10 Authors by Quotes', xaxis_title='Author', yaxis_title='Count')

#Show The Graphs
graph1.show()
graph2.show()