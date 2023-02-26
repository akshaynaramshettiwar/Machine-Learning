import streamlit as st
import joblib
import string

from nltk.corpus import stopwords
import nltk
import sklearn
from nltk.stem.porter import PorterStemmer

ps = PorterStemmer()


def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)

tf= joblib.load('vectorizer.pkl')
model = joblib.load('model.pkl')

st.title("SMS classifier Analyisis App")
st.write(
    "A simple machine laerning app to predict weather person massage is SPAM or HAM"
)
form = st.form(key="my_form")
review = form.text_input(label="Enter the Massage")
submit = form.form_submit_button(label="Make Prediction")
if submit:

    # 1. preprocess
    transformed_sms = transform_text(review)
    # 2. vectorize
    vector_input = tf.transform([transformed_sms]).toarray()
    # 3. predict
    result = model.predict(vector_input)[0]
    # 4. Display
    if int(result)== 1:
        st.write("Spam")
    else:
        st.write("Not Spam")
