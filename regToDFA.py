
i=1
optable=[]

def table_star(a):
  global i
  res=[]
  

def table_concat(a,b):
  global i
  res=[]
  for tuple in a:
    res.append(tuple)
  res.append((a[-1][2],b[0][1],b[0][2]))
  return res

def table_union(a,b):
  global i
  res = []
  for tuple in a:
    res.append(tuple)
  res.append((a[0][0],b[0][1],a[-1][2]))
  return res

def table_single(a):
  global i
  s_state = 'q'+str(i)
  t_state = 'q'+str(i+1)
  s = [(s_state,a,t_state)]
  ##print s
  i+=2
  return s

def isOperator(op):
  if op in '*.+': 
    return True
  else:
    return False

def priority(op):
  if op=='*':
    return 5
  elif op == '.':
    return 4
  elif op=='+':
    return 3 
  elif op in '()':
    return -1
 
def pretopost(regex):
  post=[]
  opstack=[]
  for char in regex:
    if isOperator(char):
      if not opstack or priority(char) > priority(opstack[-1]):
        opstack.append(char)
      else:
        while opstack and (priority(char) <= priority(opstack[-1]) or opstack[-1] != '('):
          post.append(opstack.pop())
        opstack.append(char)
    elif(char=='('):
      opstack.append(char)
    elif(char==')'):
      while opstack[-1] != '(':
        post.append(opstack.pop())
      else:
        opstack.pop()
    else:
      post.append(char)
  while opstack:
    post.append(opstack.pop())
   
  return post

def evalpost(preregex):
  optable=[]
  postreg = pretopost(preregex)   ## postreg contains the regular expression in postfix form.
  for c in postreg:
    if c=='+':
      a = optable.pop()
      b = optable.pop()
      optable.append(table_union(b,a))
    elif c=='.':
      a=optable.pop()
      b=optable.pop()
      optable.append(table_concat(b,a))
    else:
      optable.append(table_single(c))     
  return optable  

def main():
  global i
  print 'ENTER THE REGEX:  '
  reg = raw_input()
  print evalpost(reg)
  

if __name__ == '__main__':
  main()
