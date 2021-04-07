


# assignment 6 coursera data structure with python

text = "X-DSPAM-Confidence:    0.8475";

print(text)

pos=text.find("0")
print(pos)
print(float(text[pos:pos+6]))