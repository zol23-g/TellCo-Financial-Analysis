def convert_bytes_to_mb(df, columns):
    # Conversion factor from bytes to megabytes
    bytes_to_mb = 1024 * 1024
    
    # Iterate over each column and apply the conversion
    for col in columns:
        df[col] = df[col] / bytes_to_mb
        # Rename the column to include '(MB)'
        df.rename(columns={col: f"{col.replace('Bytes', 'MB')}"}, inplace=True)
    
    return df
