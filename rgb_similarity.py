#Arrange işlemini yapalım
def arrange(item, dim, min_val, max_val):
    result = []
    for i in range(dim):
        if i < len(item):
            result.append(item[i] / ((max_val - min_val) / 100))
        else:
            result.append(50 / ((max_val - min_val) / 100))
    return result

def sqrt(X):
    return X**0.5

def power(X, level):
    return X**level

def vectorSimilarity(A, B):
    if len(A) != len(B):
        return -1
    total = sum(power((b - a), 2) for a, b in zip(A, B))
    distance = sqrt(total)
    max_distance = sqrt(3 * (255**2))
    return 1 - distance / max_distance

def rgbtxtnormalized(file_path):
    color_list = []
    with open(file_path, "r", encoding="utf-8") as file:
        for row in file:
            parts = row.strip().split()
            if len(parts) >= 4:
                r, g, b = int(parts[0]), int(parts[1]), int(parts[2])
                name = " ".join(parts[3:])
                color_list.append(([r, g, b], name))
    return color_list

# Kullanıcıdan RGB bilgilerini isteyelim.
print("Please enter RGB values.")
red = int(input("R: "))
green = int(input("G: "))
blue = int(input("B: "))

user_color = [red, green, blue]
normalized_user = arrange(user_color, 3, 0, 255)

# Renkleri okuyalım.
color_list = rgbtxtnormalized("rgb.txt")

# En yakın rengi bulalım.
max_similarity = float("-inf")
closest_color = ""

for clr_rgb, clr_name in color_list:
    normalized_clr = arrange(clr_rgb, 3, 0, 255)
    sim = vectorSimilarity(normalized_user, normalized_clr)
    if sim > max_similarity:
        max_similarity = sim
        closest_color = clr_name

print(f"En yakın renk: {closest_color} (benzerlik: {max_similarity:.2f})")
