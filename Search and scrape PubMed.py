"""
Script Summary:
This script provides a function for web scraping PubMed to extract the number of search results for chemical names, with optional custom search strings and a resume functionality for interrupted operations.

Functions:
1. PubMed_results_biomon_terms(
    search_url: str, df, NAME: str, search_string: Optional[str] = None, resume_from: int = 0
) -> List:
    - Scrapes PubMed for the number of results associated with chemical names provided in a DataFrame column.
    - Allows appending a custom search string to the chemical names.
    - Supports resuming from a specified index to handle interruptions or long processing times.

    Parameters:
    - search_url (str): Base URL for PubMed queries.
    - df (pandas.DataFrame): DataFrame containing chemical names.
    - NAME (str): Column name in the DataFrame with the chemical names.
    - search_string (str, optional): Additional search string for PubMed queries. Defaults to None.
    - resume_from (int, optional): Index to resume processing from. Defaults to 0.

    Returns:
    - List: Number of results for each chemical name or "TIMEOUT" for timeouts.

Notes:
- Uses `requests` for HTTP requests and `BeautifulSoup` for HTML parsing.
- Handles timeouts gracefully and returns "TIMEOUT" for entries where a timeout occurs.
- Progress tracking is supported with `tqdm`.
- Includes an optional code block for saving progress to a CSV file after each iteration.
"""


import os
import pandas as pd
import requests

from bs4 import BeautifulSoup

from typing import List, Optional
import certifi
from tqdm import tqdm


def PubMed_results_biomon_terms(
    search_url: str, df, NAME: str, search_string: Optional[str] = None, resume_from: int = 0
) -> List:
    """
    Scraping PubMed for number of results from a chemical name with an optional custom search string.
    Allows resuming from a specific index.

    Parameters:
    search_url (str): The base URL for the PubMed search.
    df (pandas.DataFrame): DataFrame that contains chemical names.
    NAME (str): The name of the column in the DataFrame that contains the chemical names.
    search_string (str, optional): An optional search string to append to the chemical name in the PubMed query.
                                   Defaults to None, which means only the chemical name will be searched.
    resume_from (int, optional): Index to resume processing from. Defaults to 0.
    
    Returns:
    List: A list containing the number of results for each chemical name or "TIMEOUT" if a timeout occurs.
    """
    # A list to store the number of results for each chemical name
    n_results = ['NA'] * len(df)  # Pre-fill with 'NA' for all rows
    
    # Iterate through each row in the DataFrame starting from resume_from
    for index, row in tqdm(df.iterrows(), total=len(df), initial=resume_from):
        if index < resume_from:
            continue  # Skip rows already processed
        
        # Get the chemical name from the specified column
        name = row[NAME]
        
        # Replace spaces with "+" for use in the URL
        name = name.replace(" ", "+")
        
        # Construct the search URL
        if search_string:
            url = f"{search_url}(\"{name}\"){search_string}"
        else:
            url = f"{search_url}(\"{name}\")"
        
        try:
            # Send a GET request to the URL and pass the CA certificate bundle
            response = requests.get(url, timeout=20, verify=certifi.where())
            
            # Parse the HTML content of the response
            soup = BeautifulSoup(response.content, "html.parser")
            
            # Attempt to find the number of results
            try:
                result = soup.find("span", {"class": "value"}).contents
                n_results[index] = result
            except:
                n_results[index] = 'NA'
        
        except requests.exceptions.Timeout:
            # If a timeout occurs, append "TIMEOUT"
            n_results[index] = "TIMEOUT"
        
        ## Optional: Save progress to a file after every iteration
        #progress_df = pd.DataFrame({NAME: df[NAME], 'Results': n_results})
        #progress_df.to_csv("progress.csv", index=False)
        
    return n_results


## example search_string
# '+AND+(human OR blood OR urine OR serum OR hair OR nail OR plasma OR biomon* OR "breast milk")'