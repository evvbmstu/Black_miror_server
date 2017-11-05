
def area(faces):
    areas = []
    for idx, (x, y, h, w) in enumerate(faces):
        areas.append(h*w)
    return areas.index(max(areas))
