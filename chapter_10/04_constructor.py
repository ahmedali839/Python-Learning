class Employer:
    language = "JavaScript"
    loginTime = 7

    def __init__(
        self,
    ):  ## it automatically call, even without call just need to create new Object
        print(
            "It's constructor always run beause it is constructor, it automatically calls when new Object created."
        )

    def department(
        props, language, name
    ):  ## props could be any name, like self, kk, Ahmed, but it should pass to run this function
        print(
            f"{name} Company has own language: {language} but it's parent class has language: {props.language}"
        )


punjabCollege = Employer()
print(
    punjabCollege.loginTime
)  ## it will print language = python instead of javascript because it priority it's own languages

SuperiorCollege = Employer()