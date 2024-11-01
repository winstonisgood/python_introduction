def annotation(a: int, b: str) -> float:
    print(a, b)
    return (3.5)

# annotation(1, 'string')
# annotation(3.4555, 'string') #not valid in typescript
# annotation(1, 1) not valid in typescript
# annotation('1', 1) not valid in typescript
# annotation('string', 1,0) not valid in typescript

def annotation2(a: int, b: str) -> int:
    print(a, b)
    return [3.5]

print(annotation(1, 'string'))