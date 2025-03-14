def find_the_redheads(family):
    """ค้นหาชื่อของคนที่มีผมสีแดงจาก dictionary"""
    redheads = list(filter(lambda name: family[name] == "red", family))
    return redheads

def main():
    dupont_family = {
        "florian": "red",
        "marie": "blond",
        "virginie": "brunette",
        "david": "red",
        "franck": "red"
    }
    print(find_the_redheads(dupont_family))

if __name__ == "__main__":
    main()