# -*- coding: utf-8 -*-
BRIE = 'Aged Brie'
BACKSTAGE_PASS = 'Backstage passes to a TAFKAL80ETC concert'
SULFURAS = 'Sulfuras, Hand of Ragnaros'
CONJURED = 'Conjured Mana Cake'


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:

            if is_improving_item(item):
                # quality increases for abnormal items
                if item.name == BACKSTAGE_PASS:
                    if 6 <= item.sell_in < 11:
                        item.quality = increase_item_quality(item, increment=2)
                    elif item.sell_in < 6:
                        item.quality = increase_item_quality(item, increment=3)
                    else:
                        item.quality = increase_item_quality(item)
                else:
                    item.quality = increase_item_quality(item)
            else:
                # quality decreases for normal items
                item.quality = decrease_item_quality(item)
                if is_conjured_item(item):
                    item.quality = decrease_item_quality(item)

            # sell by always decreases (except sulfuras)
            if not is_immutable(item):
                item.sell_in -= 1

            # cumulative quality change if now past sell by
            if item.sell_in < 0:
                if is_improving_item(item):
                    # brie quality increases past sell by (cumulative=2) ?
                    if item.name == BRIE:
                        item.quality = increase_item_quality(item)

                    # backstage is zero past sell by
                    if item.name == BACKSTAGE_PASS:
                        item.quality = 0
                else:
                    # normal items decrease past sell by (cumulative=2)
                    item.quality = decrease_item_quality(item)
                    if is_conjured_item(item):
                        item.quality = decrease_item_quality(item)


def increase_item_quality(item, increment=1):
    if item.quality < 50:
        item.quality += increment
    return item.quality


def decrease_item_quality(item):
    if item.quality > 0:
        if not is_immutable(item):
            item.quality -= 1
    return item.quality


def item_can_change(item):
    """Sulfuras never changes"""
    return item.name not in [SULFURAS]


def is_immutable(item):
    """Sulfuras never changes"""
    return item.name in [SULFURAS]


def is_normal_item(item):
    """Normal items decrease in quality"""
    return item.name not in [BRIE, BACKSTAGE_PASS]


def is_improving_item(item):
    return item.name in [BRIE, BACKSTAGE_PASS]


def is_conjured_item(item):
    return item.name in [CONJURED]


class Item:

    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return '%s, %s, %s' % (self.name, self.sell_in, self.quality)
