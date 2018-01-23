###
@api.model
def tracking_values(self, initial_value, new_value, col_name, col_info):
	item_tracked = True     
    item_values = {'field': col_name,
    			   'field_desc': col_info['string'],
    			   'field_type': col_info['type']
    }
    
    if col_info['type'] in ['many2many', 'one2many']:
        values.update({
            'old_value_char': initial_value and ',' .join(initial_value.mapped('name'))or '',
            'new_value_char': new_value and ',' .join(new_value.mapped('name')) or ''
        })
 	else:
 	    item_tracked = False
 	if item_tracked:
 		return item_values
 	return {}