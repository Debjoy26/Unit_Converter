from django.shortcuts import render, redirect

# Conversion factors
LENGTH_UNITS = {
    "millimeter": 0.001,
    "centimeter": 0.01,
    "meter": 1,
    "kilometer": 1000,
    "inch": 0.0254,
    "foot": 0.3048,
    "yard": 0.9144,
    "mile": 1609.34
}

WEIGHT_UNITS = {
    "milligram": 0.000001,
    "gram": 0.001,
    "kilogram": 1,
    "ounce": 0.0283495,
    "pound": 0.453592
}

def convert_units(value, from_unit, to_unit, unit_dict):
    try:
        if from_unit in unit_dict and to_unit in unit_dict:
            return value * (unit_dict[from_unit] / unit_dict[to_unit])
        return None
    except (ValueError, TypeError) as e:
        return f"Error in conversion: {e}"


def length_conversion(request):
    result = None
    if request.method == "POST":
        value = float(request.POST["value"])
        from_unit = request.POST["from_unit"]
        to_unit = request.POST["to_unit"]
        result = convert_units(value, from_unit, to_unit, LENGTH_UNITS)
        
    return render(request, "converter/length.html", {"result": result})

def weight_conversion(request):
    result = None
    if request.method == "POST":
        value = float(request.POST["value"])
        from_unit = request.POST["from_unit"]
        to_unit = request.POST["to_unit"]
        result = convert_units(value, from_unit, to_unit, WEIGHT_UNITS)
        
    return render(request, "converter/weight.html", {"result": result})

def temperature_conversion(request):
    result = None
    if request.method == "POST":
        value = float(request.POST["value"])
        from_unit = request.POST["from_unit"]
        to_unit = request.POST["to_unit"]
        
        if from_unit == "Celsius" and to_unit == "Fahrenheit":
            result = (value * 9/5) + 32
        elif from_unit == "Celsius" and to_unit == "Kelvin":
            result = value + 273.15
        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            result = (value - 32) * 5/9
        elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
            result = (value - 32) * 5/9 + 273.15
        elif from_unit == "Kelvin" and to_unit == "Celsius":
            result = value - 273.15
        elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
            result = (value - 273.15) * 9/5 + 32
        else:
            result = value  # Same unit conversion
        
    return render(request, "converter/temperature.html", {"result": result})


from django.shortcuts import render

def home(request):
    return render(request, 'converter/home.html')

