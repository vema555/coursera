if category_2 == 'IPAD':
    leaf_node_desc = row_asdict['LEAF_NODE_DESC']
    prod_desc = row_asdict['PROD_DESC']
    if category_3 == 'IPAD MINI':
        if  (('IPAD MINI 3' in leaf_node_desc) or ( 'IPAD MINI 3' in leaf_node_desc )):
            row_asdict[cls._column_name] = 3
        elif  (('IPAD MINI RETINA' in leaf_node_desc) ):
            row_asdict[cls._column_name] = 2
        else:
            row_asdict[cls._column_name] = 1
        return row_asdict
    elif category_3 == 'IPAD AIR':
        if  (('IPAD AIR 2' in leaf_node_desc)):
            row_asdict[cls._column_name] = 2
        else:         
            row_asdict[cls._column_name] = 1
        return row_asdict
    else:
        if leaf_node_desc in ['IPAD WIFI', 'IPAD 3G']:
            if 'IPAD 2 ' in row_asdict['PROD_DESC']:
                row_asdict[cls._column_name] = 2
            else:
                row_asdict[cls._column_name] = 1
        elif leaf_node_desc in ['IPAD 3 4G', 'IPAD 3 WIFI']:
            row_asdict[cls._column_name] = 3
        elif leaf_node_desc in ['IPAD RETINA CELLULAR', 'IPAD RETINA WIFI']:
            row_asdict[cls._column_name] = 4
        else:
            row_asdict[cls._column_name] = 0

