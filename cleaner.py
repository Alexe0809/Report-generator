import pandas as pd

def not_none_has_letter(column: str, df):
    has_letter = df[column].apply(lambda x: any(c.isalpha() for c in str(x)))
    mask = df[column].notna() & has_letter
    df = df[mask]
    return df

def qnt_price_validity(column: str, df):
    df[column] = pd.to_numeric(df[column], errors='coerce')
    mask = df[column] > 0
    df = df[mask]
    return df


def clean_data(default_data):
    df = default_data.copy()
    before = len(df)
    required = ['order_id', 'date', 'customer', 'product', 'quantity', 'price', 'status']
    missing = [col for col in required if col not in df.columns]
    if missing:
        raise ValueError(f'Not fount columns: {missing}')
    df = df.drop_duplicates(subset='order_id', keep='first')
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    df = df[df['date'].notna()]
    df = not_none_has_letter('customer', df)
    df = not_none_has_letter('product', df)
    df = qnt_price_validity('quantity', df)
    df = qnt_price_validity('price', df)
    mask = df['status'].isin(['completed', 'cancelled', 'pending'])
    df = df[mask]
    print (f'Was deleted {before - len(df)} lines')
    return df

