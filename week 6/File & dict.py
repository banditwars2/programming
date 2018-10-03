def Ticker_company(company_name: str):
    file = open('company.txt', 'r')

    for Company in file.readlines():
        split_rule: list = Company.split(':')
        if split_rule[0] == company_name:
            return split_rule[1]
    return "Could not find a ticker."


def Ticker(ticker: str):
    file = open('company.txt', 'r')

    for Ticker in file.readlines():
        split_rule: list = Ticker.split(':')
        print(split_rule)
        if split_rule[1] == ticker:
            return split_rule[0]
    return "Could not find a company."

print(
    Ticker_company(
        input('Enter a company name: ')
    )
)

print(
    Ticker(
        input('Enter a ticker: ')
    )
)