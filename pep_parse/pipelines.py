import csv
from collections import defaultdict
from datetime import datetime as dt
from pathlib import Path


BASE_DIR = Path(__file__).parent.parent


class PepParsePipeline:
    def open_spider(self, spider):
        self.statuses = defaultdict(int)

    def process_item(self, item, spider):
        self.statuses[item['status']] += 1

        return item

    def close_spider(self, spider):
        path_file = BASE_DIR / 'results'
        file_name = (
            f'status_summary_{dt.now().isoformat(timespec="seconds")}.csv')

        with open(path_file / file_name, 'w') as csv_file:
            writer = csv.writer(csv_file)

            writer.writerow(('Статус', 'Количество'))
            writer.writerows(self.statuses.items())
            writer.writerow(('Total', sum(self.statuses.values())))
