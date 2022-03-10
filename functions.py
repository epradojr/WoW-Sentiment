# importing libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# import for scoring and train_test_split
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score, confusion_matrix, recall_score, precision_score



class TradeChat():
    """
    A class to model, clean, tokenize, and down sample Trade Chat log data
    
    ...
    Methods
    -------
    multi_run_model(self, models, X_train, y_train, X_test, y_test, model_labels, 
                    score='accuracy')
    down_sample(self, df, label_name)
    convert_to_df(self, filepath)
    token_(self, text, tokenizer, stopwords):
    token_lemmatizer(self, text, tokenizer, stopwords):
    token_porter(self, text, tokenizer, stopwords):
    (self, dataframe, tokenizer, stopwords, stem=None):
    top_words


    """

    def multi_run_model(self, models, X_train, y_train, X_test, y_test, model_labels, score='accuracy'):
        # Dict to hold model performance
        model_perf = {}

        # Cycle through our models and output their performance and confusion matrix
        for key, model in models.items():

            # Fitting the model
            model.fit(X_train, y_train)

            # Grabbing our cross validated accuracy score
            cv_score = round(np.mean(cross_val_score(model, X_train, y_train, cv= 5, scoring= score)),4)

            # predicting with our model and grabiing the test accuracy
            y_pred = model.predict(X_test)

            if score == 'accuracy':
                test_acc = round(accuracy_score(y_pred, y_test), 4)

                # Placing the cv accuracy and test accuracy into a dict
                acc_dict = {'CV_Accuracy': cv_score, 'Test_Accuracy': test_acc}

                # updating the model_perf with performance metrics
                model_perf[key] = {'Model': model, 'Performace': acc_dict}

            elif score == 'recall':
                test_rec = round(recall_score(y_pred, y_test), 4)

                # Placing the cv recall and test recall into a dict
                rec_dict = {'CV_Recall': cv_score, 'Test_Recall': test_rec}

                # updating the model_perf with performance metrics
                model_perf[key] = {'Model': model, 'Performace': rec_dict}

            else:
                test_pre = round(precision_score(y_pred, y_test), 4)

                # Placing the cv precision and test precision into a dict
                pre_dict = {'CV_Precision': cv_score, 'Test_Precision': test_pre}

                # updating the model_perf with performance metrics
                model_perf[key] = {'Model': model, 'Performace': pre_dict}


            # Printing out results and confusion matrix
            print(f'Showing results for: {key}')
            print(model_perf[key])
            print()

            cm = confusion_matrix(y_test, y_pred)
            fig, ax = plt.subplots(figsize=(8,6))

            sns.heatmap(cm/np.sum(cm), annot=True, fmt='.2%', cmap='Blues', xticklabels= model_labels, yticklabels= model_labels)
            ax.set_title(key);

        return(model_perf)



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



    def convert_to_df(self, filepath):

        # loads in text file
        chatlog = pd.read_csv(filepath, sep='\n', header=None)

        # declaring variables for column creation
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

    def top_words(self, cluster_word_distribution, top_cluster, values):
        for cluster in top_cluster:
            sort_dicts = sorted(cluster_word_distribution[cluster].items(), key=lambda k: k[1], reverse=True)[:values]
            print("\nCluster %s : %s"%(cluster, sort_dicts))
