PATTERN = re.compile(r'(11|1(00)+1|1(00)*01+((00)*1+)*(00)*01|0)+$')
#multiple instances are being checked as if doing long division
#first instance is 11 (3 in denary) being divided perfectly
#second instance is 1 followed by an even number of 0s and another 1
# and so on