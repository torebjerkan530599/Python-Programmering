with open('Presidents.txt','r') as file:
    content = file.read().strip()
    reversed_content = content[::-1]
    
with open('Presidents.txt','w') as file:
    file.write(reversed_content)