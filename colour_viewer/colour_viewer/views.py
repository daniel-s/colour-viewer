"""
@Author: Daniel Stojanov
2021-02-03
"""
import json

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

import colour_viewer.pallettes

def home_page(request):
    return render(request, "colour_viewer/splash.html")

def get_all_converters():
    # Build the pallettes selector.
    all_converters = {}
    for converter in colour_viewer.pallettes.all_pallettes:
        all_converters[converter.get_label()] = converter
    return all_converters

def convert_single_colour(colour_data):
    converter = get_all_converters()[colour_data["pallette"]]
    rgb_values = converter.convert_colour(colour_data["fields"])
    return rgb_values

@csrf_exempt # Not secure
def convert_colours(request):
    # Convert to json.
    data = json.loads(request.body)
    all_converted_colours = []
    for colour in data:
        converted_colour = convert_single_colour(colour)
        all_converted_colours.append(converted_colour)
    # Data integrity check, use the no_of_fields given by the
    # corresponding pallette to check.
    return JsonResponse({"converted_colours": all_converted_colours})

@csrf_exempt
def pallettes_list(request):
    all_pallettes = colour_viewer.pallettes.all_pallettes
    all_pallettes_as_json = [{    
        "pallette": item.get_label(),
        "no_of_fields": item.get_no_of_fields()
    } for item in all_pallettes]
    return JsonResponse({"pallettes": all_pallettes_as_json})
