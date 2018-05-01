#dimport pickle


def main():
    file = open('test.dat', 'wb')
    pickle.dump([1,2,3], file)
    file.close()


def countchar(buf):
    t_list = [0 for n in range(26)]
    buf = buf.lower()
    for i in range(len(buf)):
        if 'a' <= buf[i] <= 'z':
            t_list[ord(buf[i]) - ord('a')] += 1
    return t_list



def primes(n):
    if n == 2:
        return [2]
    elif n < 2:
        return []
    s = list(range(3, n + 1, 2))
    m_root = n ** 0.5
    half = ((n + 1) / 2) - 1
    i = 0
    m = 3
    while m <= m_root:
        if s[i]:
            j = int((m * m - 3) / 2)
            s[j] = 0
            while j < half:
                s[j] = 0
                j += m
        i += 1
        m = 2 * i + 3
    return [2] + [x for x in s if x]


import math

def is_prime(n):
    if n == 1:
        return False
    elif n < 4:
        return True
    if n % 2 == 0:
        return False
    elif n < 9:
        return True
    elif n % 3 == 0:
        return False
    else:
        r = float(math.sqrt(n))
        f = 5
        while f <= r:
            if n % f == 0:
                return False
            if n % (f + 2) == 0:
                return False
            f += 6
    return True

def monisen(no):
    m = 0
    n = 1
    while True:
        n += 1
        if is_prime(n):
            m = 2 ** n - 1
            if is_prime(m):
                no -= 1
        if no <= 0:
            break
    return m

if __name__ == '__main__':
    for n in range(10):
        print(monisen(n))
    #main()
