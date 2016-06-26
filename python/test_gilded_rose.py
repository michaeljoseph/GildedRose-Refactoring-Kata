# -*- coding: utf-8 -*-

from gilded_rose import Item, GildedRose


def update_item_quality(item):
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    return gilded_rose.items[0]


def assert_items_equal(expected, item):
    assert str(expected) == str(item)


def assert_quality_changes(item, expected_quality, sell_in_change=-1):
    assert_items_equal(
        Item(item.name, item.sell_in+sell_in_change, expected_quality),
        update_item_quality(item)
    )


def test_sellby_and_quality_decrease():
    assert_quality_changes(Item('foo', 1, 1), 0)


def test_quality_decreases_twice_as_fast_after_sellby():
    assert_quality_changes(Item('foo', 0, 10), 8)


def test_brie_increases_in_quality():
    assert_quality_changes(Item('Aged Brie', 10, 10), 11)


def test_brie_increases_in_quality_pass_sellby():
    assert_quality_changes(Item('Aged Brie', -1, 10), 12)


def test_brie_quality_stays_at_fifty():
    assert_quality_changes(Item('Aged Brie', 10, 50), 50)


def test_sulfaras_never_changes():
    assert_quality_changes(Item('Sulfuras, Hand of Ragnaros', 10, 10), 10, 0)


def test_backstage_pass_under_ten_days_quality_plus_two():
    assert_quality_changes(
        Item('Backstage passes to a TAFKAL80ETC concert', 10, 10),
        12
    )


def test_backstage_pass_under_five_days_quality_plus_three():
    assert_quality_changes(
        Item('Backstage passes to a TAFKAL80ETC concert', 4, 10),
        13
    )


def test_backstage_pass_under_five_days_zero_quality():
    assert_quality_changes(
        Item('Backstage passes to a TAFKAL80ETC concert', 0, 10),
        0
    )


"""
    Item(name="Conjured Mana Cake", sell_in=3, quality=6),  # <-- :O
"""
def test_integration():
    items = [
        Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
        Item(name="Aged Brie", sell_in=2, quality=0),
        Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
        Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
        Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49),
        Item(name="Conjured Mana Cake", sell_in=3, quality=6),  # <-- :O
    ]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    # FIXME: test them all
    assert items[0].name.startswith('+5')
