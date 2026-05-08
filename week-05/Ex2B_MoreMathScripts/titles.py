import math

length = 10
width = 8

titles_needed = length * width
extra_titles = titles_needed * 0.10
total_titles_with_extra = titles_needed + extra_titles

boxes_needed = math.ceil(titles_needed / 12)
total_boxes_with_extra = math.ceil(total_titles_with_extra / 12)

print("Titles needed:", titles_needed)
print("Boxes needed without extra:", boxes_needed)
print("Boxes needed with 10% extra:", total_boxes_with_extra)