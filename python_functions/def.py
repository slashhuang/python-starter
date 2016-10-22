def power(x):
	return x*x


def power1(x=None):
	if x is None:
		x=[]
	x.append('yes! x is immutable now ')
	return x	


print(power(1))

print(power1(['test']))

		

