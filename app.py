from flask import Flask,url_for,render_template,request

import spacy
nlp = spacy.load('en_core_web_sm')



app = Flask(__name__)



# def analyze_text(text):
# 	return nlp(text)

def noun(doct):
    doc = nlp(doct)
    noun=[chunk.text for chunk in doc.noun_chunks]
    
    return noun

def verb(docts):
    doc = nlp(docts)
    noun=[chunk.text for chunk in doc.noun_chunks]
    verbs=[token.lemma_ for token in doc if token.pos_ == "VERB"]
    a=len(verbs)
    return verbs
    

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/analyze',methods=['GET','POST'])
def analyze():
    
    if request.method == 'POST':
        rawtext = request.form['rawtext']
        extracted_nouns= noun(rawtext)
        extracted_verbs = verb(rawtext)
    
    
    
        
    return render_template('result.html',ctext=rawtext,extracted_nouns=extracted_nouns,extracted_verbs=extracted_verbs)



    
    
if __name__ == '__main__':
	app.run(debug=True)