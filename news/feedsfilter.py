import re


filters = {}


def linuxcn_summary_filter(summary):
    """
    filter linuxcn rss feeds' summary.
    select the text in <blockquote></blockquote> or in 2nd <p></p>
    """
    if summary.find('<blockquote>') == -1:
        tag_list = summary.split('\n')
        data = tag_list[1]
        summary_info = re.findall(r'<p>(.+)</p>', data)[0]
        summary_info = re.sub("。$", "...", summary_info)
        return summary_info

    summary_info = re.findall(r'<blockquote>\n<p>(.+)</p>\n</blockquote>', summary)[0]
    summary_info = re.sub("。$", "...", summary_info)
    return summary_info


filters['Linux中国'] = linuxcn_summary_filter
