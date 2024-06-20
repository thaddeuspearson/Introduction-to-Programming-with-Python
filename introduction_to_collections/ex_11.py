# Consider the data in the following table:

"""
Name        Country
Alice       USA
Francois    Canada
Inti        Peru
Monika      Germany
Sanyu       Uganda
Yoshitaka   Japan
"""

# You need to write some Python code to determine the country name associated
# with one of the listed names. Your code should include the data structure(s)
# you need and at least one test case to ensure the code works.

country_citizens_dict = {
    "USA": ["Alice"],
    "Canada": ["Francois"],
    "Peru": ["Inti"],
    "Germany": ["Monika"],
    "Uganda": ["Sanyu"],
    "Japan": ["Yoshitaka"],
}

def identify_country_citizen(citizen,
                             country_citizens_dict=country_citizens_dict):
    for country in country_citizens_dict.keys():
        if citizen in country_citizens_dict[country]:
            return country

if __name__ == "__main__":
    print(identify_country_citizen("Alice")) # Should print "USA"

