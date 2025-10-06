class College:
    language = "JavaScript"
    gender = "male"


punjabCollege = College()
print(punjabCollege.language)
print(
    punjabCollege.gender
)  ## this will call it's parent "gender" attribute because it don't have it's own
punjabCollege.gender = "Female"
print(
    punjabCollege.gender
)  ## this will call it's own "gender" attribute because it have it's own same name attributea