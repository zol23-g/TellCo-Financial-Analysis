# missing_values_handler.py

import pandas as pd
from sklearn.impute import SimpleImputer

def handle_missing_numerical(df, strategy='mean'):
    """
    Handle missing values for numerical columns.
    
    Parameters:
    df (pd.DataFrame): DataFrame containing the data
    strategy (str): Strategy to use for imputation ('mean', 'median', 'most_frequent', 'constant')
    
    Returns:
    pd.DataFrame: DataFrame with missing values handled
    """
    numerical_cols = df.select_dtypes(include=['number']).columns
    imputer = SimpleImputer(strategy=strategy)
    df[numerical_cols] = imputer.fit_transform(df[numerical_cols])
    return df

def handle_missing_categorical(df, strategy='most_frequent'):
    """
    Handle missing values for categorical columns.
    
    Parameters:
    df (pd.DataFrame): DataFrame containing the data
    strategy (str): Strategy to use for imputation ('most_frequent', 'constant')
    
    Returns:
    pd.DataFrame: DataFrame with missing values handled
    """
    categorical_cols = df.select_dtypes(include=['object', 'category']).columns
    imputer = SimpleImputer(strategy=strategy)
    df[categorical_cols] = imputer.fit_transform(df[categorical_cols])
    return df

def handle_missing_text(df, fill_value='Unknown'):
    """
    Handle missing values for text columns.
    
    Parameters:
    df (pd.DataFrame): DataFrame containing the data
    fill_value (str): Value to use for filling missing values
    
    Returns:
    pd.DataFrame: DataFrame with missing values handled
    """
    text_cols = df.select_dtypes(include=['object']).columns
    df[text_cols] = df[text_cols].fillna(fill_value)
    return df

def handle_missing_dates(df, strategy='mean'):
    """
    Handle missing values for date or datetime columns.
    
    Parameters:
    df (pd.DataFrame): DataFrame containing the data
    strategy (str): Strategy to use for imputation ('mean', 'median', 'most_frequent', 'constant')
    
    Returns:
    pd.DataFrame: DataFrame with missing values handled
    """
    date_cols = df.select_dtypes(include=['datetime64[ns]', 'datetime']).columns
    
    if strategy == 'mean':
        for col in date_cols:
            mean_date = df[col].mean()
            df[col] = df[col].fillna(mean_date)
    
    elif strategy == 'median':
        for col in date_cols:
            median_date = df[col].median()
            df[col] = df[col].fillna(median_date)
    
    elif strategy == 'most_frequent':
        for col in date_cols:
            most_frequent_date = df[col].mode()[0]
            df[col] = df[col].fillna(most_frequent_date)
    
    elif strategy == 'constant':
        for col in date_cols:
            constant_date = pd.Timestamp('1970-01-01')  # You can change this to any constant date
            df[col] = df[col].fillna(constant_date)
    
    return df
def handle_missing_others(df, fill_value=0):
    """
    Handle missing values for other types of columns.
    
    Parameters:
    df (pd.DataFrame): DataFrame containing the data
    fill_value (any): Value to use for filling missing values
    
    Returns:
    pd.DataFrame: DataFrame with missing values handled
    """
    other_cols = df.columns.difference(df.select_dtypes(include=['number', 'object', 'category']).columns)
    df[other_cols] = df[other_cols].fillna(fill_value)
    return df
