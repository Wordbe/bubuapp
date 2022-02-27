import openpyxl
from ingest.house import House


def write(house: House):
    workbook_path = "output/주택가치평가비교표"
    workbook = openpyxl.load_workbook(workbook_path + ".xlsx")
    sheet = workbook.get_sheet_by_name("주택가치평가비교표")
    row = 5

    address_split = house.address.split(" ")
    sheet[f'C{row}'] = address_split[1]
    sheet[f'D{row}'] = address_split[2]
    sheet[f'E{row}'] = address_split[3]
    sheet[f'F{row}'] = house.title
    sheet[f'G{row}'] = house.area.replace("평형", "")
    sheet[f'M{row}'] = f'({house.households_count})'
    yy = house.approval_date[2:4]
    sheet[f'R{row}'] = f'({yy}/{house.floor_area_ratio.replace("%", "")})'

    workbook.save(workbook_path + "v1.0.0.xlsx")

