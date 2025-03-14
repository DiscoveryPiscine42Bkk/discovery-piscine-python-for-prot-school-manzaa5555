def famous_births(figures):
    """แสดงข้อมูลบุคคลสำคัญเรียงตามวันเกิด"""
    sorted_figures = sorted(figures.items(), key=lambda item: item[1]['date_of_birth'])
    for name, details in sorted_figures:
        print(f"{details['name']} is a great scientist born in {details['date_of_birth']}.")

def main():
    women_scientists = {
        "ada": {"name": "Ada Lovelace", "date_of_birth": "1815"},
        "cecilia": {"name": "Cecila Payne", "date_of_birth": "1900"},
        "lise": {"name": "Lise Meitner", "date_of_birth": "1878"},
        "grace": {"name": "Grace Hopper", "date_of_birth": "1906"}
    }
    famous_births(women_scientists)

if __name__ == "__main__":
    main()