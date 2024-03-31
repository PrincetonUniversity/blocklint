# multi-line doublequote docstring containing blocked words, not ignored
def process_data(data):
    """
    Process the given data and return a modified version to add to whitelist.
    
    Parameters:
    - data: The master data to be processed, can be a list or dict.
    
    Returns:
    - A modified version of the input data, where each element or value is doubled.
    """
    if isinstance(data, list):
        return [item * 2 for item in data]
    elif isinstance(data, dict):
        return {k: v * 2 for k, v in data.items()}
    return data

# multi-line singlequote docstring containing blocked words, full docstring ignored
def compile_allowlist_rules(rules):
    '''
    Compile whitelist rules into a usable format.
    
    Parameters:
    - rules: A list or dictionary of rules to compile.
    
    Returns:
    - A dictionary with each rule mapped to its compiled form. This is a placeholder for actual compilation logic.
    '''  # blocklint:  pragma
    compiled_rules = {rule: "compiled" for rule in rules}
    return compiled_rules

# single-line singlequote docstring containing blocked words, not ignored
def relay_to_slave_nodes(message):
    '''Relay a message to all slave nodes in the network.'''
    slave_nodes = ["Node 1", "Node 2", "Node 3"]
    for node in slave_nodes:
        print(f"Message '{message}' relayed to {node}")

# single-line doublequote docstring containing blocked words, ignored
def filter_blocklist_items(items, blocklist):
    """Filter out items that are in the blacklist."""  # blocklint:  pragma
    filtered_items = [item for item in items if item not in blocklist]
    return filtered_items


# multi-line doublequote raw docstring containing blocked words, full docstring ignored
def create_generic_function():
    r"""
    A generic function that performs a simple operation.
    
    Side Effects:
    - Prints a master message indicating a simple operation has been performed.
    """  # blocklint:  pragma
    print("Performing a simple operation...")

# multi-line singlequote raw docstring containing blocked words, not ignored
def synchronize_slave_database(database):
    r"""
    Synchronize the slave database with the master database.
    
    Parameters:
    - database: The slave database to be synchronized. This is a placeholder for the actual database object.
    
    Side Effects:
    - Assumes synchronization logic is implemented, updates the slave database to match the master database.
    """
    slave_database = database
    print("Slave database synchronized.")

# single-line doublequote raw docstring containing blocked words, ignored
def create_generic_function():
    r"""A generic function that performs a simple whitelist operation."""  # blocklint:  pragma
    print("Performing a simple whitelist operation...")  # blocklint:  pragma
