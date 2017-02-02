list_input = ['jan','feb','mar','apr','may','june','july','aug','sept','oct','nov','dec']
inp = raw_input("enter which quarter you want")
inp = int(inp)
end = inp * 3
start = end - 3
print list_input[start:end]

