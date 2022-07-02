from prettytable import PrettyTable
from prettytable import DOUBLE_BORDER
from prettytable.colortable import ColorTable, Themes

#! Default Prettytable
#x = PrettyTable()
#! PrettyTable has the functionality of printing your table with ANSI color codes. This includes support for most Windows versions through Colorama. To get started, import the ColorTable class instead of PrettyTable.
x = ColorTable(theme=Themes.OCEAN)

#! field names first using the field_names attribute
# x.field_names = ["City name", "Area", "Population",
#                  "Annual Rainfall", "Highest Temperature", ]
#! add the rows one at a time using the add_row() method
# x.add_row(["Adelaide", 1295, 1158259, 600.5, 50])
# x.add_row(["Brisbane", 5905, 1857594, 1146.4, 45])
# x.add_row(["Darwin", 112, 120900, 1714.7, 52])
# x.add_row(["Hobart", 1357, 205556, 619.5, 41])
# x.add_row(["Sydney", 2058, 4336374, 1214.8, 30])
# x.add_row(["Melbourne", 1566, 3806092, 646.9, 40])
# x.add_row(["Perth", 5386, 1554769, 869.4, 29])
# #! add all list of rows in one go with add_rows()
# x.add_rows(
#     [
#         ["Adelaide", 1295, 1158259, 600.5, 50],
#         ["Brisbane", 5905, 1857594, 1146.4, 40],
#         ["Darwin", 112, 120900, 1714.7, 36],
#         ["Hobart", 1357, 205556, 619.5, 46],
#         ["Sydney", 2058, 4336374, 1214.8, 33],
#         ["Melbourne", 1566, 3806092, 646.9, 53],
#         ["Perth", 5386, 1554769, 869.4, 27],
#     ]
# )
# #! one column at a time with add_column()
x.add_column("City name",
             ["Adelaide", "Brisbane", "Darwin", "Hobart", "Sydney", "Melbourne", "Perth"])
x.add_column("Area", [1295, 5905, 112, 1357, 2058, 1566, 5386])
x.add_column("Population", [1158259, 1857594, 120900, 205556, 4336374, 3806092,
                            1554769])
x.add_column("Annual Rainfall", [600.5, 1146.4, 1714.7, 619.5, 1214.8, 646.9,
                                 869.4])
#! "l", "r" and "c" for left, right and centre alignment
x.align = "r"
x.align["City name"] = "l"
#! data sorted by one particular field by giving sortby keyword argument
#! reversesort=True to reverse a list
x.sortby = "Area"
# * Changing the appearance of your table - the easy way
#! set the style for your table using the set_style
# DEFAULT - The default look, used to undo any style changes you may have made
# PLAIN_COLUMNS - A borderless style that works well with command line programs for columnar data
# MARKDOWN - A style that follows Markdown syntax
# ORGMODE - A table style that fits Org mode syntax
# SINGLE_BORDER and DOUBLE_BORDER - Styles that use continuous single/double border lines with Box drawing characters for a fancier display on terminal
x.set_style(DOUBLE_BORDER)
# * Changing the appearance of your table - the hard way
#! border - A boolean option (must be True or False). Controls whether a border is drawn inside and around the table.
# preserve_internal_border - A boolean option(must be True or False). Controls whether borders are still drawn within the table even when border = False.
# header - A boolean option(must be True or False). Controls whether the first row of the table is a header showing the names of all the fields.
# hrules - Controls printing of horizontal rules after rows. Allowed values: FRAME, HEADER, ALL, NONE - note that these are variables defined inside the prettytable module so make sure you import them or use prettytable.FRAME etc.
# vrules - Controls printing of vertical rules between columns. Allowed values: FRAME, ALL, NONE.
# int_format - A string which controls the way integer data is printed. This works like: print("%<int_format>d" % data)
# float_format - A string which controls the way floating point data is printed. This works like: print("%<float_format>f" % data)
# custom_format - A Dictionary of field and callable. This allows you to set any format you want pf.custom_format["my_col_int"] = ()lambda f, v: f"{v:,}". The type of the callable if callable[[str, Any], str]
# padding_width - Number of spaces on either side of column data(only used if left and right paddings are None).
# left_padding_width - Number of spaces on left-hand side of column data.
# right_padding_width - Number of spaces on right-hand side of column data.
# vertical_char - Single character string used to draw vertical lines. Default is |.
# horizontal_char - Single character string used to draw horizontal lines. Default is -.
# _horizontal_align_char - single character string used to indicate column alignment in horizontal lines. Default is: for Markdown, otherwise None.
# junction_char - Single character string used to draw line junctions. Default is +.
# top_junction_char - single character string used to draw top line junctions. Default is junction_char.
# bottom_junction_char - single character string used to draw bottom line junctions. Default is junction_char.
# right_junction_char - single character string used to draw right line junctions. Default is junction_char.
# left_junction_char - single character string used to draw left line junctions. Default is junction_char.
# top_right_junction_char - single character string used to draw top-right line junctions. Default is junction_char.
# top_left_junction_char - single character string used to draw top-left line junctions. Default is junction_char.
# bottom_right_junction_char - single character string used to draw bottom-right line junctions. Default is junction_char
# bottom_left_junction_char - single character string used to draw bottom-left line junctions. Default is junction_char.
print(x)
