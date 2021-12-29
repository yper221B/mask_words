import pandas as pd

def mask_NOTHOT(text_path):
    df_text = pd.read_excel(text_path, sheet_name=0)
    df_word = pd.read_excel(text_path, sheet_name=1, usecols=[0, 5], names=['word', 'NOTcount'])
    df_subset = pd.DataFrame()
    
    df_text.sample(frac=1).reset_index(drop=True , inplace=True)
    for _, word in df_word.iterrows():
        df_subset = df_text.query(
            
            'HOT == 0 and ' + word['word'] + ' == 1'
        
        ).loc[:, 'text'][:word['NOTcount']].replace(word['word'], '●', regex=True).copy()
        df_text.loc[df_subset.index, 'text'] = df_subset
    df_text.to_excel('./result.xlsx', index=False)