#Euler's constant, e
e = "2.718281828459045235360287471352662497757247093699959574966967627724076630353547594571382178525166427427466391932003059"
#Archimedes' constant, pi
pi = "3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066"
#Apery's constant, zeta of 3
zeta3 = "1.20205690315959428539973816151144999076498629234049888179227155534183820578631309018645587360933525814619915"
#Ramanujan-Soldner constant, mu
mu = "1.45136923488338105028396848589202744949303228364801586309300455766242559575451783565953135771108682884"
#Golden Ratio, phi
phi = "1.61803398874989484820458683436563811772030917980576286213544862270526046281890244970720720418939113748475408807538689175"
dict = {}
dict[e] ="Euler's constant"
dict[pi]="Archimedes' constant, pi"
dict[zeta3]="Apery's constant"
dict[mu] = "the Ramanujan-Soldner constant"
dict[phi] = "the Golden Ratio"

def isPrime(num):
    if num<=1:
        return False #obviously, numbers less than 2 cannot be prime
    else:
        i = 2
        while i <= num**(0.5):
            if (num%i) == 0:
                return False
            i+=1
    return True
def checker(const,dig): #input your selected constant and the length of the prime for which you are searching
    n = 2
    res = []
    while n < len(const)-dig:
        u = const[n:n+dig] #slicing the string
        check = long(u) # type casting
        if isPrime(check) and const[n]!=str(0): #if the current number is prime and doesn't start with a zero
            res = [check,n-1]
            return res
        n+=1
    res = [0,0]
    return res
def answer(const, dig):
    ans = checker(const,dig)
    if ans[0] == 0:
        return "The specified prime could not be found in the saved constant value." #use return instead of print to end function when prime is found/ end when cannot be found
    else:
        return  "The first "+str(dig)+"-digit prime present in "+dict[const]+" is "+str(ans[0])+",\nit can be found "+str(ans[1])+" place(s) after the decimal point."

print checker(e,10)
print answer(phi,5)