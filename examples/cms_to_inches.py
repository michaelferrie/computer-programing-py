# Convert imperial inches to metric cm's and mm's
cms_value = 60
inches_value = 7265432165
convert_inches_to_cms = inches_value * 2.54
convert_cms_to_inches = cms_value / 2.54
convert_cms_to_mms = cms_value * 10

print("The number of inches is: " ,convert_cms_to_inches)
print("The number of cms's is: " ,convert_inches_to_cms)
print("The number of mm's is: ",convert_cms_to_mms)
