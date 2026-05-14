class Phone(object):
    def __init__(self, phone_number):
        self._phone_number = phone_number
        self.validate()

    def validate(self):
        """Validate the phone number."""
        self.cleaned_number = []
        for i in self._phone_number:
            if not i.isdigit() and i not in ("@+. ()-"):
                raise ValueError("Invalid number, illegal characters")
            if i.isdigit():
                self.cleaned_number.append(i)
        self.cleaned_number = "".join(self.cleaned_number)
        if len(self.cleaned_number) < 10:
            raise ValueError("Invalid number, too short")
        if len(self.cleaned_number) > 11:
            raise ValueError("Invalid number, too long")
        if len(self.cleaned_number) == 11:
            if not self.cleaned_number.startswith("1"):
                raise ValueError("Invalid number, wrong country code")
            else:
                self.cleaned_number = self.cleaned_number[1:]
        if self.cleaned_number[0] in "01":
            raise ValueError("Invalid number, incorrect area code")
        if self.cleaned_number[3] in "01":
            raise ValueError("Invalid number, incorrect exchange code")

    def pretty(self):
        return f"({self.area_code}) {self.number[3:6]}-{self.number[6:]}"

    @property
    def number(self):
        return self.cleaned_number

    @property
    def area_code(self):
        return self.cleaned_number[:3]


