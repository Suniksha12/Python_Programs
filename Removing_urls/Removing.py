# Write a Program 

#1 Remove and Find URLS 

#2 Remove and Find Emails

#finding the urls
import spacy
model = spacy.load('en_core_web_sm')
urls = "This is my url https://suniksha.com and you can click on it "
doc = model(urls)

for token in doc:
  if token.like_url: #builtin of spacy is .like 
    print(token)

#remove 
splited_url = urls.split()

final_cleaned_text = " ".join([i for i in splited_url if "http" not in i])
print(final_cleaned_text)


#removing email
import spacy
model = spacy.load('en_core_web_sm')
email = "This is my email 611suniksha@gmail.com and you can contact me through it "
doc = model(email)

for token in doc:
  if token.like_email: #builtin of spacy is .like 
    print(token)

#remove
splited_text = email.split()

final_cleaned_text = " ".join([suniksha for suniksha in splited_text if "@" not in suniksha])
print(final_cleaned_text)