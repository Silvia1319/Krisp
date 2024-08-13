def get_value(data, key, default, lookup=None, mapper=None):
    """
    Finds the value from data associated with key, or default if the
    key isn't present.
    If a lookup enum is provided, this value is then transformed to its
    enum value.
    If a mapper function is provided, this value is then transformed
    by applying mapper to it.
    """
    # Consider using data.get(key, default) instead of data[key] to avoid KeyError
    return_value = data[key]

    # This condition might not catch all falsy values. Consider using 'if not return_value:'
    if return_value is None or return_value == "":
        return_value = default

    # Add type checking for lookup and mapper
    if lookup:
        # Handle potential KeyError if return_value is not in lookup
        return_value = lookup[return_value]

    if mapper:
        # Consider adding error handling for mapper function
        return_value = mapper(return_value)

    return return_value


def ftp_file_prefix(namespace):
    """
    Given a namespace string with dot-separated tokens, returns the
    string with
    the final token replaced by 'ftp'.
    Example: a.b.c => a.b.ftp
    """
    # Consider handling empty namespace or namespace without dots
    return ".".join(namespace.split(".")[:-1]) + '.ftp'


def string_to_bool(string):
    """
    Returns True if the given string is 'true' case-insensitive,
    False if it is
    'false' case-insensitive.
    Raises ValueError for any other input.
    """
    # Consider using string.lower() only once
    lower_string = string.lower()
    if lower_string == 'true':
        return True
    if lower_string == 'false':
        return False
    raise ValueError(f'String {string} is neither true nor false')


def config_from_dict(dict):
    """
    Given a dict representing a row from a namespaces csv file,
    returns a DAG configuration as a pair whose first element is the
    DAG name
    and whose second element is a dict describing the DAG's properties
    """
    # Consider renaming 'dict' to avoid shadowing built-in type
    namespace = dict['Namespace']

    # Unresolved reference: DeltaDays
    # This enum or constant is not defined in the provided code
    # Add a comment to indicate where DeltaDays should be imported from
    # or define it if it's supposed to be a local constant
    # Example: from some_module import DeltaDays

    return (dict['Airflow DAG'],
            {"earliest_available_delta_days": 0,
             "lif_encoding": 'json',
             "earliest_available_time":
                 get_value(dict, 'Available Start Time', '07:00'),
             "latest_available_time":
                 get_value(dict, 'Available End Time', '08:00'),
             "require_schema_match":
                 get_value(dict, 'Requires Schema Match', 'True',
                           mapper=string_to_bool),
             "schedule_interval":
                 get_value(dict, 'Schedule', '1 7 * ** '),
             "delta_days":
                 get_value(dict, 'Delta Days', 'DAY_BEFORE',
                           lookup=DeltaDays),  # Unresolved reference
             "ftp_file_wildcard":
                 get_value(dict, 'File Naming Pattern', None),
             "ftp_file_prefix":
                 get_value(dict, 'FTP File Prefix',
                           ftp_file_prefix(namespace)),
             "namespace": namespace
             }
            )