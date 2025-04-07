from . header import head
from .js import js
from .css import css


def list_handler(list_obj, indent, line_num=1):
    '''Write html code for lists in report dictionary'''
    html_string = ''
    for i, _ in enumerate(list_obj):
        if isinstance(list_obj[i], dict):
            if "name" in list_obj[i].keys():
                html_string = html_string + '  '*indent + \
                    '<li><span class="line-num">' + str(line_num) + '</span>' + \
                    '<span class="caret">' + str(list_obj[i]["name"]) + \
                    ' :         ' + '</span> \n '
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
            html_string = html_string + ' '*indent + \
                '<li><span class="line-num">' + str(line_num) + '</span>' + \
                '<span class="text-c">' + str(list_obj[i]) + \
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
            if "name" in v.keys():
                html_string = html_string + '  '*indent + \
                    '<li><span class="line-num">' + str(line_num) + '</span>' + \
                    '<span class="caret">' + str(v["name"]) + ' : ' + \
                    '</span> \n '
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
            html_string = html_string + ' '*indent + \
                '<li><span class="line-num">' + str(line_num) + '</span>' + \
                '<span class="text-h">' + str(k) + ' : ' + \
                '</span><span class="text-c">' + str(v) + '</span></li>\n'
            line_num += 1
    html_string = html_string + '  '*indent + '</ul> \n '
    return html_string, line_num


def report_dict_to_html(dict_obj):
    '''Writes html code for report'''
    html_string = ''
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


# CSS for line numbers
line_number_css = '''
<style>
.line-num {
    display: inline-block;
    width: 40px;
    text-align: right;
    margin-right: 8px;
    padding-right: 4px;
    color: #999;
    font-family: monospace;
    border-right: 1px solid #ddd;
    user-select: none;
}
</style>
'''

def generate(self, image_obj_list):
    '''Given a list of image objects, create a html report
    for the images'''
    report_dict = get_report_dict(image_obj_list)
    report = create_html_report(report_dict)
    return report