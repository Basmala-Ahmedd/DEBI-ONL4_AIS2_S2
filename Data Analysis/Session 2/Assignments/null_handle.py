import pandas as pd
import numpy as np

def null_handling_strategy(df, strategy="fill_mean"):
    """
    Company Task: Clean a dataset by resolving missing (NaN) values.
    """
    # TODO: Implement using .isnull(), .dropna(), or .fillna() you can used Customer_Age for your test case
    
    null_count_before = df.isnull().sum().sum()
    
    if strategy == "drop_rows":
        cleaned_df = df.dropna()
        
    elif strategy == "fill_mean":
        cleaned_df = df.copy()
        numeric_cols = cleaned_df.select_dtypes(include=np.number).columns
        cleaned_df[numeric_cols] = cleaned_df[numeric_cols].fillna(
            cleaned_df[numeric_cols].mean()
        )
    
    elif strategy == "fill_median":
        cleaned_df = df.copy()
        numeric_cols = cleaned_df.select_dtypes(include=np.number).columns
        cleaned_df[numeric_cols] = cleaned_df[numeric_cols].fillna(
            cleaned_df[numeric_cols].median()
        )
    
    else:
        raise ValueError("Invalid strategy. Choose: 'drop_rows', 'fill_mean', or 'fill_median'")
    
    null_count_after = cleaned_df.isnull().sum().sum()
    
    print(f"Missing values before: {null_count_before}")
    print(f"Missing values after: {null_count_after}")
    
    return cleaned_df