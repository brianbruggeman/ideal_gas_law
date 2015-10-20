'''
Description:
    Calculates pressure, volume and temperature of the ideal gas equation

Usage:
    calculate_ideal_gas [options]

Options:
    -h --help                This message
    -p --pressure VALUE      Pressure
    -t --temperature VALUE   Temperature
    -v --volume VALUE        Volume

Example:
    calculate_ideal_gas -p 201.2 -t 25.6


'''

def validate_float(value):
    '''Validates that value is a float'''
    try:
        value = float(value)
    except ValueError as e:
        print('ERROR: {} is not a decimal number.'.format(value))
    return value


def calculate_ideal_gas(data, gas_constant=8.315):
    '''Calculates the ideal gas based on the missing value

    Formula:
        T = p * V / R
    '''
    # find the missing key
    fields = set(data.keys())
    missing_key = None
    for key in fields:
        if data[key] is None:
            missing_key = key
    fields.remove(missing_key)

    # find the missing value
    if sorted(fields) == ['pressure', 'volume']:
        # solve for temperature
        data['temperature'] = data['pressure'] * data['volume'] / gas_constant

    elif sorted(fields) == ['pressure', 'temperature']:
        # solve for volume
        data['volume'] = data['temperature'] * gas_constant / data['pressure']

    elif sorted(fields) == ['temperature', 'volume']:
        # solve for pressure
        data['pressure'] = data['temperature'] * gas_constant / data['volume']

    else:
        print sorted(fields)

    return data, missing_key


def display(data, missing_key):
    '''Displays data'''
    fields = sorted(data.keys())

    string_format = '{:>11}'
    numeric_format = '{:>11.2f}'

    # Display header
    print 'Calculated: {}'.format(missing_key)
    header = ' | '.join(string_format.format(field) for field in fields)
    print '-'*len(header)
    print header
    print '-'*len(header)

    # Display values
    values = ' | '.join(numeric_format.format(data[field]) for field in fields)
    print values


if __name__ == '__main__':
    import sys
    try:
        from docopt import docopt
    except ImportError as e:
        print >> sys.stderr, 'Package `docopt` not found. \n> pip install docopt'
        sys.exit()

    args = docopt(__doc__)
    data = {
        'pressure': args.get('--pressure'),
        'temperature': args.get('--temperature'),
        'volume': args.get('--volume'),
    }


    # Validate values


    # Check for a single None
    none_count = 0
    for key, value in data.iteritems():
        if value is not None:
            value = validate_float(value)
            data[key] = value
        else:
            none_count += 1
    if none_count > 1 or none_count == 0:
        print >> sys.stderr, 'Error:  Invalid entries.  Please enter two of:  Pressure, Temperature, Volume'
        sys.exit()

    # Calculate the ideal gas based on values provided
    data, missing_key = calculate_ideal_gas(data)

    # Display data
    display(data, missing_key)
