import arcpy
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

input_csv = arcpy.GetParameterAsText(0)
test_string = arcpy.GetParameterAsText(1)

df = pd.read_csv(input_csv)
target = df['is_there_an_emotion_directed_at_a_brand_or_product']
text = df['tweet_text']

fixed_text = text[pd.notnull(text)]
fixed_target = target[pd.notnull(text)]

count_vect = CountVectorizer()
count_vect.fit(fixed_text)

counts = count_vect.transform(fixed_text)

# NB has a bunch of parameters -- somewhat scary for those who haven't
# used it before. That said, Scikit-Learn mostly has sane defaults,
# and usually it's not necessary to modify them. Can also try to
# change a new algorithm, but usually it's not the best way to spend
# your time.
nb = MultinomialNB()
nb.fit(counts, fixed_target)

arcpy.AddMessage(nb.predict(count_vect.transform([test_string])))
