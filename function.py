import pandas as pd

class Eddies_Tools():

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

