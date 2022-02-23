import pandas as pd

class Eddies_Tools():

    def convert_to_df(self, filepath):

        chatlog = pd.read_csv(filepath, sep='\n', header=None)

        time_stamp = []
        text = []

        for chat in chatlog[0]:
            if '[2. Trade]' in chat:
                split_chat = chat.split('  ', maxsplit=1)
                time_stamp.append(split_chat[0])
                text.append(split_chat[1])
            else:
                continue

        trade_chat = pd.DataFrame()
        trade_chat['time_stamp'] = time_stamp
        trade_chat['text'] = text

        tag_removed = []


        for chat in trade_chat['text']:
            split_chat = chat.split(':', maxsplit=1)
            
            tag_removed.append(split_chat[1])
            
        trade_chat['text'] = tag_removed

        return trade_chat

