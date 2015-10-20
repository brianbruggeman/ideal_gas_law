#!/usr/bin/env python

def calculate_ideal_gas(data, gas_constant=8.315):
    '''Calculates the ideal gas based on the missing value

    Formula:
        T = p * V / R
    '''
    # find the missing key
    fields = ['pressure', 'volume', 'temperature']
    missing_key = None
    for key in fields:
        if key not in data:
            missing_key = key
        elif data[key] == None:
            missing_key = key
    fields.remove(missing_key)
    data = {k: float(v) for k, v in data.iteritems()}

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

    return data, missing_key
