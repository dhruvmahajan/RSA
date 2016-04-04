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

"""
fp = open("Public_key","r")
public_key_str = fp.read()
fp.close()
public_key = int(public_key_str)
"""

fp = open("Private_key","r")
private_key_str = fp.read()
fp.close()
private_key = int(private_key_str)

fp = open("N_common","r")
N_str = fp.read()
fp.close()
N = int(N_str)

fp = open("message","r")
message = fp.read()
fp.close()


message_list = [ord(c) for c in message]


encryptedMsg_list = [modular_pow(m,private_key,N) for m in message_list ]

fp = open("encrypted_msg","wb")

for i in encryptedMsg_list:
	fp.write(str(i)+'\n')

"""
encryptedMsg = "".join( str(i) for i in encryptedMsg_list )

decryptedMsg_list = [modular_pow(em,public_key,N) for em in encryptedMsg_list]
decryptedMsg = "".join( chr(i) for i in decryptedMsg_list )
"""
fp.close()