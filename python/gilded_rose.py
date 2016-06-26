# -*- coding: utf-8 -*-
BRIE = 'Aged Brie'
BACKSTAGE_PASS = 'Backstage passes to a TAFKAL80ETC concert'
SULFURAS = 'Sulfuras, Hand of Ragnaros'


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            # quality decreases
            if item.name != BRIE and item.name != BACKSTAGE_PASS:
                # quality cannot decrease beyond zero
                if item.quality > 0:
                    # sulfuras never changes
                    if item.name != SULFURAS:
                        item.quality = item.quality - 1
            # quality increases
            else:
                # quality cannot increase beyond 50
                if item.quality < 50:
                    item.quality = item.quality + 1
                    if item.name == BACKSTAGE_PASS:
                        if item.sell_in < 11:
                            if item.quality < 50:
                                item.quality = item.quality + 1
                        if item.sell_in < 6:
                            if item.quality < 50:
                                item.quality = item.quality + 1

            # sell by always decreases (except sulfuras)
            if item.name != SULFURAS:
                item.sell_in = item.sell_in - 1

            # past sell by
            if item.sell_in < 0:
                if item.name != BRIE:
                    if item.name != BACKSTAGE_PASS:
                        # normal item
                        if item.quality > 0:
                            if item.name != SULFURAS:
                                item.quality = item.quality - 1
                    # backstage is zero past sell by
                    else:
                        item.quality = item.quality - item.quality
                # brie quality increases past sell by
                else:
                    if item.quality < 50:
                        item.quality = item.quality + 1


class Item:

    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return '%s, %s, %s' % (self.name, self.sell_in, self.quality)
