"""
Script Summary:
This script provides functions to interact with the Human Metabolome Database (HMDB) by extracting HMDB IDs and statuses for chemical compounds based on their CAS registry numbers. It enhances pandas DataFrames with new information by adding HMDB-related columns.

Functions:
1. extract_hmdb_id(CASid): Queries the HMDB database to retrieve the HMDB ID for a given CAS ID. Returns the HMDB ID or an error message.

2. add_HMDBid_to_df(df): Adds an 'HMDB_id' column to a pandas DataFrame by applying the extract_hmdb_id function to the 'casId_final' column.

3. fetch_HMDB_status(hmdb_id): Fetches the "Status" of a metabolite from the HMDB website using its HMDB ID. Returns the status or an error message.

4. add_status_to_df(df, HMDBid_column): Adds an 'HMDB_status' column to a pandas DataFrame by applying fetch_HMDB_status to a specified HMDB ID column.

Notes:
- The script uses web scraping via the `requests` and `BeautifulSoup` libraries.
- Includes delays to prevent rapid successive requests and potential server rate-limiting.
- Progress bars are displayed using `tqdm` for large DataFrames.
"""


import pandas as pd
import os
import numpy as np

import requests
from bs4 import BeautifulSoup
import time
from tqdm import tqdm


def extract_hmdb_id(CASid):
    """
    Extracts the Human Metabolome Database (HMDB) ID for a given CAS ID by querying
    the HMDB website. It constructs a search URL for the HMDB website, sends a GET request,
    and parses the HTML response to find the HMDB ID.

    Parameters:
    - CASid: A string representing the Chemical Abstracts Service (CAS) registry number
             of a compound. The CAS ID is used to query the HMDB database.

    Returns:
    - A string containing the HMDB ID if found. The function returns "HMDB ID not found"
      if no matching HMDB ID could be extracted from the query result. If there is an
      error during the request or parsing process, it returns a string describing the
      error prefixed with "Error:".

    Notes:
    - The function strips any leading or trailing single quotes from the CASid before
      constructing the search URL.
    - This function includes a delay (sleep) of 2 seconds at the end to prevent rapid
      successive requests that might overwhelm the server or trigger rate limiting.
    """
    
    CASid = CASid.strip("'")
    
    first_part_url = 'https://hmdb.ca/unearth/q?utf8=%E2%9C%93&query=' 
    second_part_url = '&searcher=metabolites&button='
    full_url = f'{first_part_url}\"{CASid}\"{second_part_url}'
    #print(full_url)
    
    try:
                # Send a GET request to the URL
        response = requests.get(full_url)
        # Raise an HTTPError exception for 4xx/5xx errors
        response.raise_for_status()
        
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find the element with the class 'result-link'
        result_link = soup.find(class_="result-link")
        
        if result_link and result_link.find('a'):
            # Extract the HMDB ID from the href attribute
            href = result_link.find('a').get('href')
            hmdb_id = href.split('/')[-1]
            return hmdb_id
        else:
            return "HMDB ID not found"
    except Exception as e:
        return f"Error: {str(e)}"
    finally:
        time.sleep(2)
    
def add_HMDBid_to_df(df):
    """
    Enhances a pandas DataFrame by adding a new column ('HMDB_id') that contains the HMDB ID
    for each compound identified by its CAS ID in the DataFrame. The function applies the
    `extract_hmdb_id` function to each CAS ID in the DataFrame to fetch the corresponding
    HMDB IDs.

    Parameters:
    - df: A pandas DataFrame that contains a column named 'casId_final'. Each row in this
          column should contain a CAS ID as a string.

    Returns:
    - The same pandas DataFrame passed as input but with an additional column ('HMDB_id').
      This column contains the HMDB IDs fetched for each CAS ID in the 'casId_final' column.
      If an HMDB ID cannot be found or an error occurs, the respective error message or
      "HMDB ID not found" is filled in for that row.

    Notes:
    - This function utilizes the `tqdm` library to provide a progress bar for the operation,
      which is useful for tracking progress when processing large DataFrames.
    - There is an implicit dependency on the `requests` and `BeautifulSoup` libraries in the
      `extract_hmdb_id` function, which is called by this function.
    - Because `extract_hmdb_id` includes a delay to prevent rapid requests, using this function
      on large DataFrames can be time-consuming.
    """
    tqdm.pandas(desc="Fetching status")
    df['HMDB_id'] = df['casId_final'].progress_apply(extract_hmdb_id)
    return df



def fetch_HMDB_status(hmdb_id):
    base_url = "https://hmdb.ca/metabolites/"
    full_url = f"{base_url}{hmdb_id}"
    try:
        response = requests.get(full_url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        status_container = soup.find("th", string="Status").find_next_sibling("td")
        if status_container:
            return status_container.text.strip()
        else:
            return "Not Found"
    except Exception as e:
        return f"Error: {str(e)}"
    finally:
        time.sleep(2)  # Pauses for __ seconds before making the next request

        
def add_status_to_df(df, HMDBid_column):
    # Define the inner function for checking HMDBid and fetching status
    def check_and_fetch_status(hmdb_id):
        if hmdb_id != "HMDB ID not found":
            return fetch_HMDB_status(hmdb_id)
        else:
            return None  # Or any default value you deem appropriate
    
    tqdm.pandas(desc="Fetching status")
    
    # Apply the inner function directly
    df['HMDB_status'] = df[HMDBid_column].progress_apply(check_and_fetch_status)
    
    return df        
        
# def add_status_to_df(df, HMDBid_column):
#     tqdm.pandas(desc="Fetching status")
#     df['HMDB_status'] = df[HMDBid_column].progress_apply(fetch_HMDB_status)
#     return df