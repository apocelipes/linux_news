import re


filters = {}


def linuxcn_summary_filter(title, summary):
    """
    filter linuxcn rss feeds' summary.
    select the text in <blockquote></blockquote> or in 2nd <p></p>
    when we can't find any summary, use the title
    """
    if summary.find('<blockquote>') == -1:
        tag_list = summary.split('\n')
        data = tag_list[1]
        summaries = re.findall(r'<p>(.+)</p>', data)
        if len(summaries) == 0:
            summary_info = title
        else:
            summary_info = summaries[0]

        summary_info = re.sub("。$", "...", summary_info)
        return summary_info

    summaries = re.findall(r'<blockquote>\n(?:<p>(.+)</p>\n)+?</blockquote>', summary)
    summary_info = ''.join(summaries)
    if summary_info == "":
        summary_info = title
    else:
        if summary_info.endswith("。"):
            summary_info = re.sub("。$", "...", summary_info)
        else:
            summary_info = summary_info + '...'

    return summary_info


filters['Linux中国'] = linuxcn_summary_filter
