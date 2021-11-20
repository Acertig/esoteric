(lambda n,i=2:n>2and n%i>0and i*i>n or type(lambda:0)(__import__('sys')._getframe(0).f_code,globals())(n,i+1))(int(input()))
