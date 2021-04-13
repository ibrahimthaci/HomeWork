Vector1 = [1,2,3,4]
Vector2 = [2,3,4,5]

def subtract(v:Vector1, w:Vector2):
    assert len(v) == len(w), "Vectors must have same lenght"
    return [v_i+w_i for v_i, w_i in zip(v,w)]

print(subtract(Vector1,Vector2))