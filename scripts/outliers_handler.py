import pandas as pd

def handle_outliers_numerical(df, method='iqr', factor=1.5):
    """
    Handle outliers for numerical columns using specified method.
    
    Parameters:
    df (pd.DataFrame): DataFrame containing the data
    method (str): Method for handling outliers ('iqr', 'zscore', or 'custom_range')
    factor (float): Factor for IQR outlier handling (default is 1.5, adjust as needed)
    
    Returns:
    pd.DataFrame: DataFrame with outliers handled
    """
    numerical_cols = df.select_dtypes(include=['number']).columns
    
    for col in numerical_cols:
        if method == 'iqr':
            # Calculate the IQR for outlier detection
            Q1 = df[col].quantile(0.25)
            Q3 = df[col].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - factor * IQR
            upper_bound = Q3 + factor * IQR
            
            # Cap the outliers
            df[col] = df[col].clip(lower=lower_bound, upper=upper_bound)
        
        elif method == 'zscore':
            # Calculate Z-scores for outlier detection (standard deviation-based)
            mean = df[col].mean()
            std = df[col].std()
            df[col] = df[col].clip(lower=mean - factor * std, upper=mean + factor * std)
        
        elif method == 'custom_range':
            # Replace this part with any custom logic for outliers
            lower_bound = df[col].min()  # Define your own lower bound
            upper_bound = df[col].max()  # Define your own upper bound
            df[col] = df[col].clip(lower=lower_bound, upper=upper_bound)
    
    return df

# def handle_outliers_categorical(df):
#     """
#     Handle 'outliers' for categorical columns (usually unnecessary but we can filter rare categories).
    
#     Parameters:
#     df (pd.DataFrame): DataFrame containing the data
    
#     Returns:
#     pd.DataFrame: DataFrame with potential categorical 'outliers' handled
#     """
#     categorical_cols = df.select_dtypes(include=['object', 'category']).columns
    
#     # For categorical data, 'outliers' could be rare categories
#     # You can handle rare categories by grouping them as 'Other'
#     for col in categorical_cols:
#         top_categories = df[col].value_counts().nlargest(10).index  # Keep top 10 categories
#         df[col] = df[col].apply(lambda x: x if x in top_categories else 'Other')
    
#     return df

def handle_outliers_text(df):
    """
    Handle 'outliers' for text columns. Outliers for text fields can be handled by trimming rare/invalid text values.
    
    Parameters:
    df (pd.DataFrame): DataFrame containing the data
    
    Returns:
    pd.DataFrame: DataFrame with outliers handled in text fields
    """
    text_cols = df.select_dtypes(include=['object']).columns
    
    # Here, text 'outliers' can be invalid or strange text, we can replace them with 'Unknown' or similar
    for col in text_cols:
        invalid_values = ['invalid', 'N/A', 'unknown']  # Define invalid values to handle
        df[col] = df[col].apply(lambda x: x if x not in invalid_values else 'Unknown')
    
    return df

def handle_outliers_dates(df, future_cap='now', past_cap='1970-01-01'):
    """
    Handle outliers for datetime columns by capping dates.
    
    Parameters:
    df (pd.DataFrame): DataFrame containing the data
    future_cap (str): How to cap future dates, 'now' or a specific date like '2025-01-01'
    past_cap (str): How to cap very old dates, specify a past limit like '1970-01-01'
    
    Returns:
    pd.DataFrame: DataFrame with datetime outliers handled
    """
    date_cols = df.select_dtypes(include=['datetime64[ns]', 'datetime']).columns

    # Define the future and past cap dates
    future_cap_date = pd.Timestamp(future_cap) if future_cap != 'now' else pd.Timestamp.now()
    past_cap_date = pd.Timestamp(past_cap)

    for col in date_cols:
        # Cap future dates
        df[col] = df[col].apply(lambda x: future_cap_date if x > future_cap_date else x)
        # Cap very old dates
        df[col] = df[col].apply(lambda x: past_cap_date if x < past_cap_date else x)

    return df
def handle_outliers_other(df):
    """
    Handle 'outliers' for other types of columns (e.g., datetime, boolean).
    
    Parameters:
    df (pd.DataFrame): DataFrame containing the data
    
    Returns:
    pd.DataFrame: DataFrame with outliers handled in other columns
    """
    other_cols = df.columns.difference(df.select_dtypes(include=['number', 'object', 'category']).columns)
    
    # Example: For datetime data, outliers can be very old or very future dates
    for col in other_cols:
        if pd.api.types.is_datetime64_any_dtype(df[col]):
            df[col] = df[col].apply(lambda x: pd.Timestamp('now') if x > pd.Timestamp('now') else x)  # Cap future dates
    
    return df
