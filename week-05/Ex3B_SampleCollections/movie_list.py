movies = ['Spiderman', 'Avengers', 'Ironman']

print(f"The list [movies] includes my top {len(movies)} favorite movies")
print(f"Completed list: {movies}")

print(sorted(movies))
print(movies)

# Sorted() lists it in an alphabetical order. Without it, it lists it based on how I defined it in my list
# However, it looks like sorted() didnt change the list, it printed a new version and left the original alone

movies.sort()
print(movies)

# Sort() rearranged the original list permanently into alphabetical order

movies.append("The Dark Knight")
print(movies)
print(f"The list [movies] includes my top {len(movies)} favorite movies")

# Yes, we achieved similar results among my group members