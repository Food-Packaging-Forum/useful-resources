# useful-resources

## python functions
- `ExcelToEndNote_function.ipynb`   This Jupyter Notebook contains a Python function that takes a DataFrame with citation information and generates an EndNote-compatible .txt file. The function formats the provided data according to EndNote's requirements for importing references and writes the formatted entries to the specified output file.
- `CAS_verification.py`    This Python script provides tools for validating Chemical Abstracts Service (CAS) Registry Numbers. CAS numbers are unique numerical identifiers assigned to chemical substances. The script contains two main functions:    
    - validate_cas_number(): Validates a single CAS Registry Number by checking its checksum. This function ensures the integrity of the CAS number format, determining whether it conforms to the checksum validation rule.
    - find_invalid_cas(): Processes a pandas DataFrame that includes a column of CAS numbers, identifying any records with invalid CAS numbers. It returns a subset of the DataFrame containing only the invalid entries, or prints a message if all entries are valid.

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
