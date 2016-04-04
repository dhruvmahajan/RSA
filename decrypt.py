def modular_pow(base, exponent, mod):

	if exponent==0:
		return 1
	res=1
	while exponent > 0:
		if exponent & 1:
			res=(res*base)%mod
		exponent = exponent>>1
		base = (base*base)%mod
	return res


fp = open("Public_key","r")
public_key_str = fp.read()
fp.close()
public_key = int(public_key_str)


fp = open("N_common","r")
N_str = fp.read()
fp.close()
N = int(N_str)

fp = open("encrypted_msg","r")

encryptedMsg_list=[int(line) for line in fp]

fp.close()

decryptedMsg_list = [modular_pow(em,public_key,N) for em in encryptedMsg_list]
decryptedMsg = "".join( chr(i) for i in decryptedMsg_list )

print decryptedMsg
