import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer

def clean_dataset(df):
    # 1. Clean column names
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

    # 2. Replace placeholders with NaN
    df.replace(['?', '', 'NA', 'N/A', 'nan', 'NaN'], np.nan, inplace=True)

    # 3. Standardize gender if exists
    if 'gender' in df.columns:
        df['gender'] = df['gender'].astype(str).str.lower().replace({
            'm': 'Male', 'male': 'Male',
            'f': 'Female', 'female': 'Female',
            'nan': np.nan
        })

    # 4. Strip all string columns
    for col in df.select_dtypes(include='object').columns:
        df[col] = df[col].astype(str).str.strip()

    # 5. Convert age/salary to float
    for col in ['age', 'salary']:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')

    # 6. Impute numeric
    num_cols = df.select_dtypes(include=[np.number]).columns
    if len(num_cols) > 0:
        num_imputer = SimpleImputer(strategy='mean')
        df[num_cols] = num_imputer.fit_transform(df[num_cols])

    # 7. Impute categorical (excluding name)
    cat_cols = [col for col in df.select_dtypes(include='object').columns if col != 'name']
    if len(cat_cols) > 0:
        cat_imputer = SimpleImputer(strategy='most_frequent')
        df[cat_cols] = cat_imputer.fit_transform(df[cat_cols])

    return df
