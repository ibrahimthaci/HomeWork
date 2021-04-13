Vector1 = [1,2,3,4]
Vector2 = [3,3,4,5]

def subtract(Vector1, Vector2):
    assert len(Vector1) == len(Vector2), "Vectors must have same lenght"
    return [v_i+w_i for v_i, w_i in zip(Vector1,Vector2)]

print(subtract(Vector1,Vector2))
