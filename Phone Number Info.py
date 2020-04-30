# importing geocoder, carrier from phonenumbers module
from phonenumbers import geocoder, carrier
import phonenumbers

# creating number variable to store phone number to get info for
number = input("Enter the number with country code : ")

# parsing phone number
ch_nmber = phonenumbers.parse(number, 'CH')
# finding country name of the number
country = geocoder.description_for_number(ch_nmber, "en")
print(country)

# finding service provider of the number
service_nmbr = phonenumbers.parse(number, "RO")
service_provider = carrier.name_for_number(service_nmbr, "en")
print(service_provider)