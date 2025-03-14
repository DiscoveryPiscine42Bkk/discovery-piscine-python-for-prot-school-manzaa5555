def array_of_names(persons):
    """สร้างอาร์เรย์ของชื่อเต็มจาก dictionary"""
    full_names = []
    for first_name, last_name in persons.items():
        full_name = first_name.capitalize() + " " + last_name.capitalize()
        full_names.append(full_name)
    return full_names

def main():
    persons = {
        "jean": "valjean",
        "grace": "hopper",
        "xavier": "niel",
        "fifi": "brindacier"
    }
    print(array_of_names(persons))

if __name__ == "__main__":
    main()