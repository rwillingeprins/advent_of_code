import re


class Passport:

    def __init__(self, byr=None, iyr=None, eyr=None, hgt=None, hcl=None, ecl=None, pid=None, cid=None):
        self.byr = byr
        self.iyr = iyr
        self.eyr = eyr
        self.hgt = hgt
        self.hcl = hcl
        self.ecl = ecl
        self.pid = pid
        self.cid = cid

    @classmethod
    def from_string(cls, passport_string):
        kwargs = {}
        for key_value_string in passport_string.split():
            (key, value) = key_value_string.split(':')
            kwargs[key] = value
        return cls(**kwargs)

    @classmethod
    def is_valid_int_string(cls, int_string, minimum, maximum):
        return int_string is not None and bool(re.match(r'\d+$', int_string)) and minimum <= int(int_string) <= maximum

    def has_required_fields(self):
        return all(field is not None for field in (self.byr, self.iyr, self.hgt, self.hcl, self.ecl, self.pid))

    def has_valid_birth_year(self):
        birth_year = self.byr
        return self.is_valid_int_string(birth_year, 1920, 2002)

    def has_valid_issue_year(self):
        issue_year = self.iyr
        return self.is_valid_int_string(issue_year, 2010, 2020)

    def has_valid_expiration_year(self):
        expiration_year = self.eyr
        return self.is_valid_int_string(expiration_year, 2020, 2030)

    def has_valid_height(self):
        height = self.hgt
        if height is not None:
            match = re.match(r'(\d+)(cm|in)$', height)
            if match:
                (number, unit) = match.groups()
                return (
                        (unit == 'cm' and self.is_valid_int_string(number, 150, 193)) or
                        (unit == 'in' and self.is_valid_int_string(number, 59, 76))
                )
        return False

    def has_valid_hair_color(self):
        hair_color = self.hcl
        return hair_color is not None and bool(re.match(r'#[0-9a-f]{6}$', hair_color))

    def has_valid_eye_color(self):
        eye_color = self.ecl
        return eye_color is not None and eye_color in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')

    def has_valid_passport_id(self):
        passport_id = self.pid
        return passport_id is not None and bool(re.match(r'\d{9}$', passport_id))

    def is_valid(self):
        return (
                self.has_valid_birth_year() and
                self.has_valid_issue_year() and
                self.has_valid_expiration_year() and
                self.has_valid_height() and
                self.has_valid_hair_color() and
                self.has_valid_eye_color() and
                self.has_valid_passport_id()
        )


def parse_passports_from_batch_file(file_path):
    with open(file_path) as file:
        return [Passport.from_string(passport_string) for passport_string in file.read().split('\n\n')]


def day04a():
    passports = parse_passports_from_batch_file('input/day04.txt')
    return sum(passport.has_required_fields() for passport in passports)


def day04b():
    passports = parse_passports_from_batch_file('input/day04.txt')
    return sum(passport.is_valid() for passport in passports)


print(day04a())
print(day04b())
