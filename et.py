# Initialize references_pmid dictionary
references_pmid = {}

# Assuming `children.text` contains PubMed ID text and `i` is the index
i = 0  # Example index
references_pmid[f'reference_{i+1}_pmid'] = children.text

# After assignment, references_pmid may look like:
# {'reference_1_pmid': 'PubMedID_text_for_reference_1'}

# Incrementing index
i += 1
references_pmid[f'reference_{i+1}_pmid'] = children.text

# After another assignment, references_pmid may look like:
# {'reference_1_pmid': 'PubMedID_text_for_reference_1',
#  'reference_2_pmid': 'PubMedID_text_for_reference_2'}

# And so on, depending on how you iterate and assign values
