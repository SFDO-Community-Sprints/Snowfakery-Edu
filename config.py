from faker import Faker
from faker.generator import Generator
import faker.providers.address.en_US
import faker.providers.lorem.en_US
import faker.providers.company
import faker.providers.phone_number.en_US
import random

fake = Faker()
fakeAddress = faker.providers.address.en_US.Provider(Generator())
fakeLorem = faker.providers.lorem.en_US.Provider(Generator())
fakeCompany = faker.providers.company.Provider(Generator())
fakePhone = faker.providers.phone_number.en_US.Provider(Generator())

INSTITUTIONTYPES = {
    'University',
    'College',
    'Junior College',
    'State University'
}

TOPICS = {
    'Cloud',
    'ABC Computing',
    'Friendly',
    'Sunshine',
    'XYZ',
    'Rainbow',
    'Synergy',
    'Supernova',
    'Connected',
    'Credentials',
    'Snowflake',
    'Salesforce',
    'Worldview',
}

DEPARTMENTS = {
    'Accounting Division',
    'African American and African Diaspora Studies',
    'Africana Studies',
    'Anesthesiology',
    'Anthropology',
    'Applied Physics and Applied Mathematics',
    'Architecture',
    'Art History',
    'Archaeology',
    'Asian and Middle Eastern Cultures',
    'Astronomy and Astrophysics',
    'Biochemistry and Molecular Biophysics',
    'Biology',
    'Biomedical Engineering',
    'Cardiology',
    'Chemistry',
    'Civil Engineering',
    'Classics',
    'Classics and Ancient Studies',
    'Computer Science',
    'Dance',
    'Decision, Risk, and Operations Division',
    'Dermatology',
    'Digestive and Liver Diseases',
    'Earth and Environmental Sciences',
    'East Asian Languages and Cultures',
    'Ecology, Evolution and Environmental Biology',
    'Economics',
    'Electrical Engineering',
    'Endocrinology',
    'English and Comparative Literature',
    'Environmental Health Sciences',
    'Environmental Science',
    'Epidemiology',
    'Film',
    'Finance and Economics Division',
    'French',
    'French and Romance Philology',
    'General Medicine',
    'Genetics and Development',
    'Germanic Languages',
    'Global Support',
    'Health Policy and Management',
    'Hematology',
    'History',
    'Industrial Engineering & Operations Research',
    'Infectious Diseases',
    'Italian',
    'Latin American and Iberian Cultures',
    'Management Division',
    'Marketing Division',
    'Mathematics',
    'Mechanical Engineering',
    'Medicine',
    'Microbiology & Immunology',
    'Middle Eastern, South Asian, and African Studies',
    'Molecular Medicine',
    'Music',
    'Nephrology',
    'Neurology',
    'Neuroscience',
    'Pediatrics',
    'Pharmacology',
    'Philosophy',
    'Philosophy',
    'Physical Education & Recreation Program',
    'Physical Education',
    'Physics',
    'Physiology and Cellular Biophysics',
    'Political Science',
    'Population & Family Health',
    'Psychiatry',
    'Psychology',
    'Pulmonary, Allergy and Critical Care Medicine',
    'Radiation Oncology',
    'Radiology',
    'Rehabilitation and Regenerative Medicine',
    'Religion',
    'Religion',
    'Rheumatology',
    'Slavic Languages',
    'Sociology',
    'Sociomedical Sciences',
    'Spanish and Latin American Cultures',
    'Statistics',
    'Surgery',
    'Systems Biology',
    'Theatre',
    'Visual Arts',
    'Writing'
    }

FACULTYPOSITIONS = {
    'Associate Professor',
    'Professor',
    'Assistant Professor',
    'Professor Emeritus',
    'Adjunct Professor',
    'Lecturer',
    'TA',
    'Chair',
}
class Provider(faker.providers.BaseProvider):
    def institution_name(self):
        """Fake higher ed names."""
        topicsinclstate = set(fakeAddress.states)
        topicsinclstate.union(TOPICS)
        suffix = self.random_element(INSTITUTIONTYPES)
        topic = self.random_element(topicsinclstate)
        # topic = str.title(fakeCompany.catch_phrase())
        return " ".join([topic, suffix]).strip()

    def department_name(self):
        return self.random_element(DEPARTMENTS)
    
    def faculty_position(self):
        position = self.random_element(FACULTYPOSITIONS)
        return position

    def faculty_title(self):
        position = self.faculty_position()
        department = self.department_name() 
        return position+" of "+department

### Phone Numbers (could move to separate class)
    """Built around the North American Numbering Plan"""
    def phone_areacode(self):
        """Generates Area Codes from the of the North American Numbering Plan
        Allowed ranges: [2–9] for the first digit, and [0-9] for the second and third digits. 
        When the second and third digits of an area code are the same, 
        that code is called an easily recognizable code (ERC). 
        ERCs designate special services; e.g., 800 for toll-free service. 
        The NANP is not assigning area codes with 9 as the second digit.[34]"""
        firstdigit = random.randint(2,9)
        seconddigit = random.randint(0,9)
        thirddigit = random.randint(0,9)
        while seconddigit == thirddigit:
          thirddigit = random.randint(0,9)
        return str(firstdigit)+str(seconddigit)+str(thirddigit)
    
    def phone_exchange(self):
        """generally follows the same pattern as area code. While this doesn't capture
        every single option for phone numbers, it gets us pretty close."""
        return self.phone_areacode()
    
    def phone_lastfour(self):
        return fake.numerify(text='####')

    

"""Informal Testing"""      
prov1 = Provider(Generator())
print("I am the "+prov1.faculty_title()+" at "+prov1.institution_name())
print(('My phone number is {0}-{1}-{2}').format(prov1.phone_areacode(),prov1.phone_exchange(),prov1.phone_lastfour()))