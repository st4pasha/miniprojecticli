colons = "id|product_id\n"

def read_from_file(path: str) -> list[str]:
    with open(path, "r") as file:
        str_from_file = file.readlines()
        return str_from_file
    
def write_to_file(path: str, record_to_file: str):
    with open(path, "w") as file:
        file.write(record_to_file)

def parse_id(id: str):
    ids = id.split("|")
    return ids[1].strip()

def get_product_id_from_file(parse: str):

    ids = read_from_file(parse)[1::]
    id = "|".join(ids)

    return parse_id(id)


