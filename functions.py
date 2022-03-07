# importing libraries
import pandas as pd
import numpy as np

# import for scoring and train_test_split
from sklearn.model_selection import train_test_split, cross_val_score


class TradeChat():

    def down_sample(self, df, label_name):
        # find the number of observations in the smallest group
        nmin = df[label_name].value_counts().min()
        return (df
                # split the dataframe per group
                .groupby(label_name)
                # sample nmin observations from each group
                .apply(lambda x: x.sample(nmin))
                # recombine the dataframes
                .reset_index(drop=True)
                )


    def run_model(self, X, y, model, t_size=0.25, r_state=5, cv=5):

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= t_size, random_state= r_state)

        model.fit(X_train,y_train)

        cv_acc = round(np.mean(cross_val_score(model, X_train, y_train, cv= cv, scoring='accuracy')),4)
        cv_rec = round(np.mean(cross_val_score(model, X_train, y_train, cv= cv, scoring='recall')),4)
        cv_pre = round(np.mean(cross_val_score(model, X_train, y_train, cv= cv, scoring='precision')),4)

        y_pred = model.predict(X_test)
    
        return cv_acc,cv_rec,cv_pre, y_pred, model




    def convert_to_df(self, filepath):

        chatlog = pd.read_csv(filepath, sep='\n', header=None)

        text = []
        date = []
        time = []

        for chat in chatlog[0]:
            if '[2. Trade]' in chat:
                split_chat = chat.split('  ', maxsplit=1)

                stamp = split_chat[0]
                text.append(split_chat[1])

                split_stamp = stamp.split(' ', maxsplit=1)

                date.append(split_stamp[0])
                time.append(split_stamp[1])
            else:
                continue

        trade_chat = pd.DataFrame()
        trade_chat['date'] = date
        trade_chat['time'] = time
        trade_chat['text'] = text

        tag_removed = []


        for chat in trade_chat['text']:
            split_chat = chat.split(':', maxsplit=1)
            
            tag_removed.append(split_chat[1])
            
        trade_chat['text'] = tag_removed

        return trade_chat



    def token_(self, text, tokenizer, stopwords):

        # Tokenize using `tokenizer`
        text = tokenizer.tokenize(text)
        
        # Remove stopwords
        text = [token for token in text if token not in stopwords]
        
        return text



    def token_lemmatizer(self, text, tokenizer, stopwords):
        """
        Takes in a sting, RegexpTokenizer instance, and stopwords
        to tokenize and lemmatize a string
        Parameters
        ----------
            text: str
                string to be tokenized and lemmatized
            tokenizer: nltk.tokenize.regexp.RegexpTokenizer
                instanced RegexpTokenizer to use for tokenizing
            stopwords: list
                list of frequent words to have removed from text.
        Returns
        -------
        Tokenized and stemmed string.
        """

        # importing stemmer and instancing the object
        from nltk.stem.wordnet import WordNetLemmatizer
        lemmatizer = WordNetLemmatizer()

        # Tokenize using `tokenizer`
        text = tokenizer.tokenize(text)
        
        # Remove stopwords
        text = [token for token in text if token not in stopwords]
        
        # Stem the tokenized text
        text = [lemmatizer.lemmatize(token) for token in text]

        return text



    def token_porter(self, text, tokenizer, stopwords):
        """
        Takes in a string, RegexpTokenizer instance, and stopwords
        to tokenize and stem a string
        Parameters
        ----------
            text: str
                string to be tokenized and stemmed
            tokenizer: nltk.tokenize.regexp.RegexpTokenizer
                instanced RegexpTokenizer to use for tokenizing
            stopwords: list
                list of frequent words to have removed from text.
        
        Returns
        -------
        Tokenized and stemmed string.
        """
        # importing stemmer and instancing the object
        from nltk.stem import PorterStemmer
        stemmer = PorterStemmer()

        # Tokenize using `tokenizer`
        text = tokenizer.tokenize(text)
        
        # Remove stopwords
        text = [token for token in text if token not in stopwords]
        
        # Stem the tokenized text
        text = [stemmer.stem(token) for token in text]

        return text



    def nlp_tokenizer(self, dataframe, tokenizer, stopwords, stem=None):

        df = dataframe.copy()

        df.text = df.text.str.lower()
    
        if stem == 'porter':
            df['text_tokenized'] = df['text'].apply(lambda x: self.token_porter(x, tokenizer, stopwords))
        elif stem == 'lemmatizer':
            df['text_tokenized'] = df['text'].apply(lambda x: self.token_lemmatizer(x, tokenizer, stopwords))
        else:
            df['text_tokenized'] = df['text'].apply(lambda x: self.token_(x, tokenizer, stopwords))


        text_list = df.text_tokenized.copy()

        for i, lists in enumerate(df.text_tokenized):
            if lists == []:
                if df.sentiment[i] == 'Negative':
                    text_list.iloc[i] = ['negative']
                else:
                    text_list.iloc[i] = ['other']

        df.text_tokenized = text_list

        df['joined_tokens'] = df['text_tokenized'].str.join(" ")

        return df

