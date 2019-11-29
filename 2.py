try:
	n=int(input())
	b=int(input())
	a=input()
	c=n+b
	l=a+b
	n.append(3)
except ValueError:
	raise ValueError(' here value error occurred')
except TypeError:
	raise TypeError(' here Type error occurred')
except:
	raise AttributeError('here Attribute error occurred ')