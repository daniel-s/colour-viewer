An extensible colour palette viewer. New colour palettes are added by extending AbstractPalette in palettes.py. A palette describes the number of fields in the __no_of_fields__ class variable and by implementing the convert_colour(parameters) method. This method must map from the parameters describing a colour in its palette to the RGB colour model.