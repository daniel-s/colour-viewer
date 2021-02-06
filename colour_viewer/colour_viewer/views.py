"""
@Author: Daniel Stojanov
2021-02-03
"""
import json

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

import colour_viewer.palettes

def home_page(request):
    return render(request, "colour_viewer/splash.html")

def get_all_converters():
    # Build the palettes selector.
    all_converters = {}
    for converter in colour_viewer.palettes.all_palettes:
        all_converters[converter.get_label()] = converter
    return all_converters

def convert_single_colour(colour_data):
    converter = get_all_converters()[colour_data["palette"]]
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
    return JsonResponse({"converted_colours": all_converted_colours})

@csrf_exempt
def palettes_list(request):
    all_palettes = colour_viewer.palettes.all_palettes
    all_palettes_as_json = [{    
        "palette": item.get_label(),
        "no_of_fields": item.get_no_of_fields()
    } for item in all_palettes]
    return JsonResponse({"palettes": all_palettes_as_json})
