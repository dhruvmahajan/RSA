import random
from fractions import gcd

from largePrime import primeNumberGenerator

class key_generation:

	def multiplicativeInverse(self, a, mod):
		if a%mod ==0:
			return 0,1
		x,y = self.multiplicativeInverse(mod, a%mod)
		temp = x
		x = y
		y = temp - (a/mod)*y
		return x,y


	def publicKey(self, prime1, prime2,totient):

		e = random.randrange(max(prime1,prime2),max(prime1,prime2)*1000)

		while True:
			if gcd(e, totient) == 1:
				return e
			e+=1

	def generateKeys(self):

		primeNumber = primeNumberGenerator()

		numberOfBitPrime = 512

		primeNo1 = primeNumber.generateLargePrime(numberOfBitPrime)
		primeNo2 = primeNumber.generateLargePrime(numberOfBitPrime)

		N = primeNo1*primeNo2

		totient = (primeNo1-1) * (primeNo2-1)	

		public_key = self.publicKey(primeNo1, primeNo2, totient)
		private_key,extra = self.multiplicativeInverse(public_key, totient)

		if private_key<0:
			private_key = private_key + totient

		return public_key, private_key, N



if __name__ == "__main__":
	keyObject = key_generation()

	public_key, private_key, N = keyObject.generateKeys()

	print 'public_key key is ', public_key
	print 'private key is ', private_key
	print 'N is ', N

	fp = open("Public_key","wb")
	fp.write(str(public_key))
	fp.close()

	fp = open("Private_key","wb")
	fp.write(str(private_key))
	fp.close()

	fp = open("N_common","wb")
	fp.write(str(N))
	fp.close()