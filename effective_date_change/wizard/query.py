class QueryList:
    update_stock_picking_by_name = "UPDATE stock_picking SET date_done = (%s) WHERE name = %s"
    update_stock_picking_by_origin = "UPDATE stock_picking SET date_done = (%s) WHERE origin = %s"
    update_sale_order = "UPDATE sale_order SET effective_date = (%s) WHERE name = %s"
    update_purchase_order = "UPDATE purchase_order SET effective_date = (%s) WHERE name = %s"
    update_stock_move = "UPDATE stock_move SET date = (%s) WHERE reference = %s"
    update_stock_move_by_ref_tuple = "UPDATE stock_move SET date = (%s) WHERE reference IN %s"
    update_stock_move_line = "UPDATE stock_move_line SET date = (%s) WHERE reference = %s"
    update_stock_move_line_by_ref_tuple = "UPDATE stock_move_line SET date = (%s) WHERE reference IN %s"
    find_name_from_stock_picking = "SELECT name FROM stock_picking WHERE origin = %s"
    update_journal_entry = "UPDATE account_move set date = (%s) WHERE ref SIMILAR TO %s"
    update_journal_entry_line = "UPDATE account_move_line SET date = (%s) WHERE ref SIMILAR TO %s"
    update_journal_entry_by_ref_tuple = "UPDATE account_move SET date = (%s) WHERE ref LIKE ANY (%s);"
    update_journal_entry_line_by_ref_tuple = "UPDATE account_move_line SET date = (%s) WHERE ref LIKE ANY (%s);"
    update_inventory_valuation_date = "UPDATE stock_valuation_layer SET create_date = (%s) WHERE stock_move_id = (%s)"

    # SilkSoft addition
    update_manufacturing_by_name = "UPDATE mrp_production SET date_planned_start = (%s) WHERE name = %s"
    update_inventory_valuation_date_desc = "UPDATE stock_valuation_layer " \
                                           "SET create_date = (%s) WHERE description = (%s)"
    update_scraps_by_id = "UPDATE stock_scrap SET date_done = (%s) WHERE id = %s"
