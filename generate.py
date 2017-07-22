from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter
from collections import defaultdict
import string
import vincent
feedback = 'The system doesnt work perfectly its not upto the mark!'

### reading content from a textfile
with open("sample.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]


### creating a word array from the lines
words = []
for line in content:
    wordlis = (word_tokenize(line))
    for word in wordlis:
        words.append(word)

### building stopword and punctuation list
punctuation = list(string.punctuation)
stop = stopwords.words('english')+punctuation

### removing stopwords
words = [term.lower() for term in words]
terms_stop = [term for term in words if term not in stop]

### counter for common words
count_all = Counter()
count_all.update(terms_stop)

### building co-occurrence matrix
com = defaultdict(lambda : defaultdict(int))
for i in range(len(terms_stop)-1):
    for j in range(i+1,len(terms_stop)):
        w2 = max(terms_stop[i],terms_stop[j])
        w1 = min(terms_stop[i],terms_stop[j])
        if(w1!=w2):
            com[w1][w2]+=1 ;

### building frequency graph
word_freq = count_all.most_common(20)
labels, freq = zip(*word_freq)
data = {'data': freq, 'x': labels}
bar = vincent.Bar(data, iter_idx='x')
bar.to_json('term_freq.json', html_out=True, html_path='chart.html')