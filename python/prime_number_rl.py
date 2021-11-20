sp=int(input());print((lambda n,i=2:True if(n<=2) else(False if (n%i==0)else(True if(i*i>n)else type(lambda:0)((__import__("sys")._getframe(0).f_code),globals(),"death")(n,i+1))))(sp))
