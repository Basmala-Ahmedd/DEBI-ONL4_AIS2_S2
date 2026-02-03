import pandas as pd

def automated_stat_analyzer(df, column_name):
    """
    Company Task: Provide a summary report of a specific data variable.
    
    Instructions:
    1. Check if the column is numerical or categorical.
    2. For numerical: Calculate Mean, Median, and Standard Deviation.
    3. For categorical: Calculate the Mode.
    4. Return a dictionary with these statistical measures.
    """
    # TODO: Implement using df[column_name].mean(), .median(), .std(), or .mode()  you can used Sales_Amount for your test case.
    column = df[column_name]    
    column_clean = column.dropna()
    
    result = {
        "Column": column_name,
        "Type": None
    }
    
    if pd.api.types.is_numeric_dtype(column_clean):
        mean_val = column_clean.mean()
        median_val = column_clean.median()
        std_val = column_clean.std()
        
        if mean_val > median_val:
            skewness = "Right Skewed"
        elif mean_val < median_val:
            skewness = "Left Skewed"
        else:
            skewness = "Symmetric"
        
        result.update({
            "Type": "Numerical",
            "Mean":float(round(mean_val, 2)) ,
            "Median": float(median_val),
            "Standard Deviation": float(round(std_val, 2)),
            "Skewness": skewness
        })  
        
    else:
        mode_val = column_clean.mode()[0]
        result.update({
            "Type": "Categorical",
            "Mode": mode_val
        })
    
    return result





