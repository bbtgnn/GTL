### FUNCTIONS - SHAPES

# do_nothing
# Does nothing - Used to leave blank space





# rectangle






# ellipse
# Draws an ellipse





# quarter
# Draws a quarter of circumference








# ### SYMBOL FUNCTION


# # Draws a symbol taken from a glyph
# # RGlyph, (float, float), (float, float), dict ->
# def symbol(gly, position, size, properties):

#     # Getting symbol properties
#     src = properties["source_glyph"]
#     scl = properties["scale"]
#     rot = properties["rotation"]
#     proportions_keep = properties["proportions_keep"]
#     proportions_mode = properties["proportions_mode"]

#     # Useful shortcut
#     w = size[0]
#     h = size[1]

#     # Getting source glyph size and position
#     src_x = src.box[0]
#     src_y = src.box[1]
#     src_wdt = abs(src.box[0] - src.box[2])
#     src_hgt = abs(src.box[1] - src.box[3])

#     # Calculating scaling factor
#     scl_x = w/src_wdt
#     scl_y = h/src_hgt


#     # Iterating over all contours in source glyph
#     for c in src:

#         # Copying contour
#         d = c.copy()

#         # Moving the contour to (0,0)
#         d.move((-src_x - src_wdt/2, -src_y - src_hgt/2))

#         # Scaling the glyph accordingly to properties
#         if proportions_keep == False:
#             d.scale((scl_x, scl_y))
#         else:
#             if   proportions_mode == "X":
#                 d.scale((scl_x, scl_x))
#             elif proportions_mode == "Y":
#                 d.scale((scl_y, scl_y))

#         # Contour operations
#         d.scale(scl)
#         d.rotate(rot)
#         d.move(position)
#         d.round()

#         # Getting pen on target glyph
#         pen = gly.getPen()
#         # Drawing contour on target glyph
#         d.draw(pen)


# # Draws a random symbol taken from a glyph list
# # RGlyph, (float, float), (float, float), dict ->
# def symbol_list(gly, position, size, properties):

#     # Getting glyph list
#     gly_list = properties["source_glyph_list"]

#     # Building symbol properties
#     p_symbol = {
#         "source_glyph"    : choice(gly_list),
#         "scale"           : properties["scale"],
#         "rotation"        : properties["rotation"],
#         "proportions_keep": properties["proportions_keep"],
#         "proportions_mode": properties["proportions_mode"]
#     }

#     symbol(gly, position, size, p_symbol)






# ### FUNCTIONS - COMPOSITION

# # random_function
# # This function accepts a list of tuples with this structure:
# # (function_name, function_properties)
# # It randomly chooses one of those and runs it

