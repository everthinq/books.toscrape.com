# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class BooksPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)

        for field_name in adapter.field_names():
            if field_name in ['price', 'price_exl_tax', 'price_incl_tax', 'tax']:
                adapter[field_name] = float(adapter.get(field_name).replace('£', ''))

            elif field_name == 'rating':
                word_to_number = {
                    'one': 1,
                    'two': 2,
                    'three': 3,
                    'four': 4,
                    'five': 5
                }

                field_value = adapter.get(field_name).lower()

                for word, number in word_to_number.items():
                    if word in field_value:
                        adapter[field_name] = number
                        break

        return item
