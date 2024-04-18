import pandas as pd

def validate_cas_number(cas_number):
    """
    Validates a CAS Registry Number using the checksum method.
    
    Parameters:
    - cas_number (str): The CAS number as a string with or without hyphens.
    
    Returns:
    - bool: True if the CAS number is valid, False otherwise.
    """
    # Remove hyphens and extract the check digit
    digits = cas_number.replace("-", "")
    check_digit = int(digits[-1])
    digits = digits[:-1]  # All but the last digit

    # Calculate the checksum using the weight
    weighted_sum = sum(int(digit) * weight for digit, weight in zip(digits[::-1], range(1, len(digits) + 1)))
    calculated_check_digit = weighted_sum % 10

    # Return True if the calculated check digit matches the actual check digit
    return calculated_check_digit == check_digit

def find_invalid_cas(dataframe, column):
    """
    Identifies rows in a DataFrame with invalid CAS Registry Numbers.
    
    Parameters:
    - dataframe (pd.DataFrame): The DataFrame containing chemical data.
    - column (str): The name of the column in the DataFrame that contains the CAS numbers.
    
    Returns:
    - pd.DataFrame: A DataFrame containing only the rows with invalid CAS numbers.
      Prints a message if all CAS numbers are valid.
    """
    # Apply the validate_cas_number function to each CAS number in the specified column
    valid_mask = dataframe[column].apply(validate_cas_number)
    
    # Filter the dataframe to get only the rows with invalid CAS numbers
    invalid_cas_df = dataframe[~valid_mask]
    
    # Check if the resulting DataFrame is empty (i.e., all CAS numbers are valid)
    if invalid_cas_df.empty:
        print("All CASRNs are valid")
    else:
        return invalid_cas_df

# Example usage:
data = {
    'CAS Number': ['7732-18-5', '80-05-7', '123-45-6', '50-00-0'],
    'Chemical': ['Water', 'Bisphenol A', 'Fictional Compound', 'Formaldehyde']
}
df = pd.DataFrame(data)

# Check for invalid CAS numbers
invalid_cas_df = find_invalid_cas(df, 'CAS Number')
print(invalid_cas_df if invalid_cas_df is not None else "No invalid CAS numbers found.")
