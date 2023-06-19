from open_json import open_json

def data_converter():
    report_card = open_json("report_card")
    print(report_card)

data_converter()