class solution:
    def convert(first, s):
        roman={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        value=0
        for i in range(len(s)):
            if i>0 and roman[s[i]]>roman[s[i-1]]:
                value+=roman[s[i]]-2*roman[s[i-1]]
            else:
                value+=roman[s[i]]
        return value
Enter=input("Enter roman numeral: ").upper()
print(solution().convert(Enter))
