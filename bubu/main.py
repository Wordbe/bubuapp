from ingest.crawler import search
from ingest.writer import write

if __name__ == '__main__':
    house = search()
    print(vars(house))
    write(house)


