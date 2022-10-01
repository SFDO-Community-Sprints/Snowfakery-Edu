from pickle import FALSE, TRUE
from faker.generator import Generator
import faker.providers.address.en_US

INSTITUTIONTYPES = [
    'College',
    'Junior College',
    'State University',
    'University',
]

SECONDARYTYPES = [
    'High',
    'High School',
    'Prep',
    'Preparatory School',
    'School',
    'Unified High School',
]

TOPICS = [
    'Cloud',
    'Computing',
    'Connected',
    'Credentaliing',
    'Friendly',
    'Rainbow',
    'Salesforce',
    'Snowflake',
    'Sunshine',
    'Supernova',
    'Synergy',
    'Worldview',
]

DEPARTMENTS = [
    'Accounting Division',
    'African American and African Diaspora Studies',
    'Africana Studies',
    'Anesthesiology',
    'Anthropology',
    'Applied Physics and Applied Mathematics',
    'Archaeology',
    'Architecture',
    'Art History',
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
    'Physical Education',
    'Physical Education & Recreation Program',
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
    'Writing',
]

FACULTYPOSITIONS = [
    'Adjunct Professor',
    'Assistant Professor',
    'Associate Professor',
    'Chair',
    'Instructor',
    'Lecturer',
    'Professor',
    'Professor Emeritus',
    'Teaching Assistant',
]

SPORTS = [
    "Baseball",
    "Basketball",
    "Bowling",
    "Cricket",
    "Cross country",
    "Curling",
    "Fencing",
    "Field hockey",
    "Football",
    "Golf",
    "Gymnastics",
    "Ice hockey",
    "Lacrosse",
    "Rifle",
    "Rowing",
    "Rugby",
    "Skiing",
    "Soccer",
    "Softball",
    "Swimming & Diving",
    "Tennis",
    "Track & field (indoor)",
    "Track & field (outdoor)",
    "Volleyball (beach)",
    "Volleyball (indoor)",
    "Water polo",
    "Wrestling"
]

FACILITYTYPES = [
    'Building',
    'Center',
    'Hall',
    'Library',
    'Lab',
    'Tower'
]

ACADEMICDISCIPLINES = [
    'Agriculture',
    'Anthropology',
    'Applied science',
    'Archaeology',
    'Architecture and design',
    'Biology',
    'Business',
    'Chemistry',
    'Computer science',
    'Divinity',
    'Earth science',
    'Economics',
    'Education',
    'Engineering and technology',
    'Environmental studies and forestry',
    'Family and consumer science',
    'Formal science',
    'Geography',
    'History',
    'Human physical performance and recreation',
    'Humanities',
    'Journalism, media studies and communication',
    'Languages and literature',
    'Law',
    'Library and museum studies',
    'Mathematics',
    'Medicine and health',
    'Military sciences',
    'Natural science',
    'Performing arts',
    'Philosophy',
    'Physics',
    'Political science',
    'Psychology',
    'Public administration',
    'Public policy',
    'Religious Studies',
    'Social science',
    'Social work',
    'Sociology',
    'Space science',
    'Theology',
    'Transportation',
    'Visual arts'
]

class Provider(faker.providers.BaseProvider):
    def institution_name(self):
        """Fake higher education institution names."""
        fakeUsAddress = faker.providers.address.en_US.Provider(Generator())
        fullTopicList = set(TOPICS)
        usStates = set(fakeUsAddress.states)
        countryList = set(fakeUsAddress.countries)
        fullTopicList = fullTopicList.union(usStates)
        fullTopicList = fullTopicList.union(countryList)
        suffix = self.random_element(INSTITUTIONTYPES)
        topic = self.random_element(fullTopicList)
        return " ".join([topic, suffix]).strip()

    def highschool_name(self):
        """Generate name of a high school."""
        # Schools are named for people or places
        prefix = self.generator.city()
        if (self.random_element([TRUE, FALSE]) == TRUE):
            prefix = self.generator.name()

        suffix = self.random_element(SECONDARYTYPES)

        return " ".join([prefix, suffix]).strip()

    def department_name(self):
        return self.random_element(DEPARTMENTS)

    def faculty_position(self):
        position = self.random_element(FACULTYPOSITIONS)
        return position

    def faculty_title(self):
        position = self.faculty_position()
        department = self.department_name()
        return position+" of "+department

    def sport(self):
        genders = ["Men's", "Women's"]
        gender = self.random_element(genders)
        sport = self.random_element(SPORTS)
        return gender + ' ' + sport

    def facility_name(self):
        fakeName = faker.providers.person.en_US.provider(Generator())
        lasts = set(fakeName.last_names.keys())

        last_name = self.random_element(lasts)
        discipline = self.random_element(DEPARTMENTS)
        building = self.random_element(FACILITYTYPES)
        name = last_name + ' ' + discipline + ' ' + building
        return name

    def college_name(self):
        college = self.random_element(['College', 'School'])
        topic = self.random_element(ACADEMICDISCIPLINES)
        name = 'The '
        if (self.random_element([TRUE, FALSE]) == TRUE):
            fakeName = faker.providers.person.en_US.provider(Generator())
            lasts = set(fakeName.last_names.keys())
            last_name = self.random_element(lasts)
            """Deciding if the College name will have first and last name, or just last name"""
            if self.random_element([1, 2]) == 2:
                female_firsts = set(fakeName.first_names_female.keys())
                male_firsts = set(fakeName.first_names_male.keys())
                firsts = female_firsts.union(male_firsts)
                first_name = self.random_element(firsts)
                name += first_name + ' '
            name += last_name + ' '
        name += college + ' of ' + topic
        return name

    def academic_discipline(self):
        """Provides an academic discipline."""
        return self.random_element(ACADEMICDISCIPLINES)
