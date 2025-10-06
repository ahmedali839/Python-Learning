class Employer:
    language = "JavaScript"
    loginTime = 7

    def department(
        props,
    ):  ## props could be any name, like self, kk, Ahmed, but it should pass to run this function
        print(f"It's own language:  {props.language}")

    @staticmethod
    def Senior():  ## we can call staticmethod to call that function without giving any props
        print(f"By adding @staticmethod we can call function without props.")


punjabCollege = Employer()
print(
    punjabCollege.language
)  ## it will print language = Javascript as in it's parent class because it don't has it's own language
punjabCollege.language = "python"
print(
    punjabCollege.department()
)  ## it will print language = python instead of javascript because it priority it's own languages

print(
    punjabCollege.Senior()
)  ## it will print language = python instead of javascript because it priority it's own languages
