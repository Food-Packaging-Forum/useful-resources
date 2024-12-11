![DALL·E 2024-04-18 14 53 49 - A detailed and artistic illustration for a GitHub repository header image  The image depicts a modern laboratory setting filled with scientific equipm](https://github.com/Food-Packaging-Forum/useful-resources/assets/15371952/2322e7f8-7e1f-4be8-a766-08cabafa5190)
# Useful resources for chemical studies


## python functions
- `ExcelToEndNote_function.ipynb`   This Jupyter Notebook contains a Python function that takes a DataFrame with citation information and generates an EndNote-compatible .txt file. The function formats the provided data according to EndNote's requirements for importing references and writes the formatted entries to the specified output file.
- `CAS_verification.py`    This Python script provides tools for validating Chemical Abstracts Service (CAS) Registry Numbers. CAS numbers are unique numerical identifiers assigned to chemical substances. The script contains two main functions:    
    - validate_cas_number(): Validates a single CAS Registry Number by checking its checksum. This function ensures the integrity of the CAS number format, determining whether it conforms to the checksum validation rule.
    - find_invalid_cas(): Processes a pandas DataFrame that includes a column of CAS numbers, identifying any records with invalid CAS numbers. It returns a subset of the DataFrame containing only the invalid entries, or prints a message if all entries are valid.
- `Search and scrape Human Metabolome Database.py`    This script provides functions to interact with the Human Metabolome Database (HMDB) by extracting HMDB IDs and statuses for chemical compounds based on their CAS registry numbers. It enhances pandas DataFrames with new information by adding HMDB-related columns.
    - extract_hmdb_id(CASid): Queries the HMDB database to retrieve the HMDB ID for a given CAS ID. Returns the HMDB ID or an error message.
    - add_HMDBid_to_df(df): Adds an 'HMDB_id' column to a pandas DataFrame by applying the extract_hmdb_id function to the 'casId_final' column.
    - fetch_HMDB_status(hmdb_id): Fetches the "Status" of a metabolite from the HMDB website using its HMDB ID. Returns the status or an error message.
    - add_status_to_df(df, HMDBid_column): Adds an 'HMDB_status' column to a pandas DataFrame by applying fetch_HMDB_status to a specified HMDB ID column.
- `Search and scrape PubMed.py`    This script provides a function for web scraping PubMed to extract the number of search results for chemical names, with optional custom search strings and a resume functionality for interrupted operations.


## web resources
### chemical identifiers
- [US EPA CompTox](https://comptox.epa.gov/dashboard/batch-search) to batch convert between CAS, InChIKey, and SMILES
- [PubChem identifier exchange](https://pubchem.ncbi.nlm.nih.gov/idexchange/idexchange.cgi)
- [Chemical Translation Service](http://cts.fiehnlab.ucdavis.edu/) (less verified but more identifiers)

### chemical lists
- [PFAS master list](https://comptox.epa.gov/dashboard/chemical-lists/PFASMASTER), US EPA
    > \>12,000 PFAS with identifiers 
- [Food Contact Chemicals of Concern](https://www.sciencedirect.com/science/article/pii/S0304389422009578?via%3Dihub#sec0145), table S2
    > 388 food contact chemicals listed for intentional use with known hazards counter to the EU Chemicals Strategy for Sustainability    
- [PlastChem](https://plastchem-project.org/)
    > Compiling a thorough overview of all known plastic chemicals.
    > Identifying plastic chemicals of concern and linking them to specific polymers.
    > Prioritizing plastic chemicals based on hazard, and other scientific, regulatory, and market data.
    > Synthesizing scientific evidence to guide informed policy development. 
