name: str = "Ahmed"
id: int = 14


def sum(
    name: int, id: int
):  ## here ":" mean we're fixing the data type of variable while defining it
    print(f"id is : {id}, name is : {name}")


sum(3, 4)

# Example:
from typing import Dict, List, Union, Tuple

listValues: List[int] = (3,1,77,99,)  ## it means we can fix the data type of variable while defining it
tupleValues: Tuple[int, str] = (3, "4")
dictValues: Dict[str, int] = {"Ahmed": 50, "Bilal": 30}
unionValues: Union[int, str] = "pepsi123"
unionValues = "ID111"  # also valid
