a = 50
b = 15

მოქმედებები = {
    (True, False): a + b,   
    (False, True): a - b,    
    (False, False): a * b   
}

print(მოქმედებები(a > b, a == b))