import random


def act():
    r = random.randint(1, 100)
    if r > 90:
        return random.randint(25, 30)
    return ""


def church():
    r = random.randint(1, 100)
    if r > 2:
        return ""
    return random.choice(["morrison heights baptist church", "fbc clinton"])


# def county():
#     r = random.randint(1, 100)
#     if r > 2:
#         return ""
#     return random.choice(
#         [
#             "attala",
#             "calhoun",
#             "choctaw",
#             "clinton",
#             "leake",
#             "marshall",
#             "simpson",
#             "chickasaw",
#             "pearl river",
#             "copiah county",
#         ]
#     )


def gender():
    r = random.randint(1, 100)
    if r > 10:
        return ""
    else:
        if r > 2:
            return "female"
        else:
            return "male"


def gpa():
    r = random.randint(1, 100)
    if r > 75:
        return round(random.uniform(3.00, 4.00) * 100) / 100
    return ""


def high_school():
    r = random.randint(1, 100)
    if r <= 98:
        return ""
    return random.choice(
        [
            "clinton high school",
            "clinton christian academy",
        ]
    )


def major():
    r = random.randint(1, 100)
    if r < 30:
        return "unrestricted"
    return random.choice(
        [
            "music",
            "biology",
            "business",
            "pre-med",
            "nursing",
            "english",
            "christian studies",
            "chemistry",
            "math",
            "journalism",
            "education",
            "science",
            "computer science",
            "art",
            "kinesiology",
            "history",
            "political science",
            "social science",
            "design",
            "social work",
            "engineering",
            "communication",
            "modern languages",
            "undecided",
        ]
    )


def married():
    r = random.randint(1, 100)
    if r == 1:
        return "yes"
    return ""


def ministry():
    r = random.randint(1, 100)
    if r <= 5:
        return "yes"
    return ""


def ministry_dependent():
    r = random.randint(1, 100)
    if r == 3:
        return "yes"
    return ""


def need():
    r = random.randint(1, 100)
    if r >= 70:
        return "yes"
    return "no"


def minority():
    r = random.randint(1, 100)
    if r >= 95:
        return "yes"
    return ""


def state():
    r = random.randint(1, 100)
    if r >= 90:
        return "ms"
    return ""


def create_scholarship(i):
    scholarships = []

    for i in range(i + 1):
        scholarships.append(
            [
                f"sch{i}",
                act(),
                church(),
                # county(),
                gender(),
                gpa(),
                high_school(),
                major(),
                married(),
                ministry(),
                ministry_dependent(),
                need(),
                minority(),
                state(),
            ]
        )

    return scholarships
