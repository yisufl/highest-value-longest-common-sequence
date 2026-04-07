import random
import string

def generate_test(testname, K=5, lenA=5000, lenB=5000, value_range=(1, 50)):
    alphabet = random.sample(string.ascii_lowercase, K)
    
    values = {ch: random.randint(*value_range) for ch in alphabet}
    
    A = ''.join(random.choice(alphabet) for _ in range(lenA))
    B = ''.join(random.choice(alphabet) for _ in range(lenB))
    
    with open(testname, 'w') as test:
        print(K)
        test.write(str(K) + '\n')

        for ch in alphabet:
            print(ch, values[ch])
            test.write(ch + ' ' + str(values[ch]) + '\n')
        
        print(A)
        test.write(A + '\n')
        print(B)
        test.write(B)

        test.close()

generate_test("tests/test11.in")