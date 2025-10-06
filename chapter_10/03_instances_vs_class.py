class Employer:
    language = "JavaScript"
    loginTime = 7

    def department(
        props, language, name
    ):  ## props could be any name, like self, kk, Ahmed, but it should pass to run this function
        print(f"{name} Company has own language: {language} but it's parent class has language: {props.language}")


punjabCollege = Employer()
print(
    punjabCollege.department("Java", "Software Company")
)  ## it will print language = python instead of javascript because it priority it's own languages
