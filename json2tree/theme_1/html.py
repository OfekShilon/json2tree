from . header import head
from .js import js
from .css import css


def list_handler(list_obj, indent, line_num=1):
    '''Write html code for lists in report dictionary'''
    html_string = ''
    for i, _ in enumerate(list_obj):
        if isinstance(list_obj[i], dict):
            if "name" in list_obj[i].keys():
                # Extract the name value
                name_value = str(list_obj[i]["name"])
                
                # Create display text that includes both index and name value
                display_text = str(i) + " : " + name_value
                
                html_string = html_string + '  '*indent + \
                    '<li><span class="line-num">' + str(line_num) + '</span>' + \
                    '<span class="caret">' + display_text + '</span> \n '
            else:
                html_string = html_string + '  '*indent + \
                    '<li><span class="line-num">' + str(line_num) + '</span>' + \
                    '<span class="caret">' + str(i) + ' : ' + '</span> \n '
            line_num += 1
            sub_html, line_num = dict_handler(list_obj[i], indent+1, line_num)
            html_string = html_string + sub_html
            html_string = html_string + '  '*indent + '</li> \n '
        elif isinstance(list_obj[i], list):
            html_string = html_string + '  '*indent + \
                '<li><span class="line-num">' + str(line_num) + '</span>' + \
                '<span class="caret">' + str(i) + ' : ' + '</span> \n '
            line_num += 1
            html_string = html_string + '  '*indent + \
                '<ul class ="nested"> \n '
            sub_html, line_num = list_handler(list_obj[i], indent+1, line_num)
            html_string = html_string + sub_html
            html_string = html_string + '  '*indent + '</ul> \n ' + \
                '  '*indent + '</li>\n '
        else:
            # Check if value is None and apply special class if so
            is_none = str(list_obj[i]) == 'None'
            none_class = ' none-value' if is_none else ''
            
            # Determine value type class for syntax highlighting
            type_class = get_value_type_class(list_obj[i])
            
            html_string = html_string + ' '*indent + \
                '<li class="' + none_class + '"><span class="line-num">' + str(line_num) + '</span>' + \
                '<span class="text-c ' + type_class + '">' + str(list_obj[i]) + \
                '</span>\n</li> \n '
            line_num += 1
    return html_string, line_num

# pylint: disable=too-many-branches
def dict_handler(dict_obj, indent, line_num=1):
    '''Writes html code for dictionary in report dictionary'''
    html_string = ''
    html_string = html_string + '  '*indent + '<ul class ="nested"> \n'
    for k, v in dict_obj.items():
        if isinstance(v, dict):
            # Check for the specific case where a dict has a "name" property
            # but we want to show the parent field name as well
            if "name" in v.keys():
                # Extract the name value
                name_value = str(v["name"])
                
                # Create display text that includes both parent key and name value
                display_text = str(k) + " : " + name_value
                
                html_string = html_string + '  '*indent + \
                    '<li><span class="line-num">' + str(line_num) + '</span>' + \
                    '<span class="caret">' + display_text + '</span> \n '
            else:
                html_string = html_string + '  '*indent + \
                    '<li><span class="line-num">' + str(line_num) + '</span>' + \
                    '<span class="caret">' + str(k) + ' : ' + '</span> \n '
            line_num += 1
            sub_html, line_num = dict_handler(v, indent+1, line_num)
            html_string = html_string + sub_html + \
                '  '*indent + '</li> \n '
        elif isinstance(v, list):
            html_string = html_string + '  '*indent + \
                '<li><span class="line-num">' + str(line_num) + '</span>' + \
                '<span class="caret">' + str(k) + ' : ' + \
                '[%d]' % (len(v)) + '</span> \n '
            line_num += 1
            html_string = html_string + '  '*indent + \
                '<ul class ="nested"> \n '
            sub_html, line_num = list_handler(v, indent+1, line_num)
            html_string = html_string + sub_html + \
                '  '*indent + '</ul> \n ' + '  '*indent + '</li> \n '
        else:
            # Check if value is None and apply special class if so
            is_none = str(v) == 'None'
            none_class = ' none-value' if is_none else ''
            
            # Determine value type class for syntax highlighting
            type_class = get_value_type_class(v)
            
            html_string = html_string + ' '*indent + \
                '<li class="' + none_class + '"><span class="line-num">' + str(line_num) + '</span>' + \
                '<span class="text-h">' + str(k) + ' : ' + \
                '</span><span class="text-c ' + type_class + '">' + str(v) + '</span></li>\n'
            line_num += 1
    html_string = html_string + '  '*indent + '</ul> \n '
    return html_string, line_num

def report_dict_to_html(dict_obj):
    '''Writes html code for report'''
    html_string = ''
    
    # Check if there's only a single root element
    if len(dict_obj) == 1:
        html_string = html_string + '<ul class="myUL"> \n'
        
        # Get the single root element's key and value
        root_key = list(dict_obj.keys())[0]
        root_value = dict_obj[root_key]
        
        # Create the single root node
        html_string = html_string + \
            f'<li><span class="line-num">1</span><span class="caret">{root_key}</span> \n'
        
        # Process the single root's content
        if isinstance(root_value, dict):
            dict_html, line_num = dict_handler(root_value, 0, 2)
            html_string = html_string + dict_html
        elif isinstance(root_value, list):
            html_string = html_string + '  <ul class="nested"> \n'
            list_html, _ = list_handler(root_value, 1, 2)
            html_string = html_string + list_html
            html_string = html_string + '  </ul> \n'
        else:
            # If the single root has a simple value, display it
            type_class = get_value_type_class(root_value)
            html_string = html_string + f'<span class="text-c {type_class}"> : {root_value}</span>\n'
        
        html_string = html_string + '</li></ul> \n'
    else:
        # Multiple root elements, use the REPORT wrapper
        html_string = html_string + '<ul class ="myUL"> \n'
        html_string = html_string + \
            '<li><span class="line-num">1</span><span class="caret">REPORT</span> \n'
        dict_html, _ = dict_handler(dict_obj, 0, 2)
        html_string = html_string + dict_html
        html_string = html_string + '</li></ul> \n'
    
    return html_string

def create_html_report(report_dict):
    '''Return the html report as a string'''
    # logger.debug("Creating HTML report...")
    report = ''
    report = report + '\n' + head % (css + line_number_css)
    report = report + '\n' + report_dict_to_html(report_dict)
    report = report + '\n' + js
    report = report + '\n' + '</body>\n</html>\n'
    return report

def get_report_dict(image_obj_list):
    '''Given an image object list, return a python dict of the report'''
    image_list = []
    for image in image_obj_list:
        image_list.append({'image': image.to_dict()})
    image_dict = {'images': image_list}
    return image_dict

def get_value_type_class(value):
    '''Return the appropriate CSS class for a given JSON value based on its type'''
    if value is None:
        return 'json-null'
    elif isinstance(value, bool):
        return 'json-boolean'
    elif isinstance(value, (int, float)):
        return 'json-number'
    elif isinstance(value, str):
        return 'json-string'
    else:
        return ''

# CSS for line numbers
line_number_css = '''
<style>
.line-num {
    display: inline-block;
    width: 40px;
    text-align: right;
    margin-right: 10px;
    padding-right: 4px;
    color: #94a3b8;
    font-family: 'JetBrains Mono', 'Fira Code', monospace;
    border-right: 1px solid #e2e8f0;
    user-select: none;
    font-size: 12px;
}

/* Style for None values that can be hidden */
.none-value.hidden {
    display: none;
}
</style>
'''