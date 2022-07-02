

def boldface(s, mode='md'):
    s_lcl = ''
    if mode == 'md':
        s_lcl = '**{}**'.format(s)
    elif mode == 'html':
        s_lcl = '<b>{}</b>'.format(s)
    elif mode == 'tex':
        s_lcl = r'\textbf{' + s + '}'
    else:
        s_lcl = s_url
    return s_lcl


def table_heading(lst_fields, mode='md'):
    s_lcl = ''
    if mode == 'md':
        s_lcl = '\n|{}|\n|{}|'.format(' | '.join(lst_fields), ' | '.join(':---'))
    elif mode == 'html':
        s_lcl = '\n<a href="{}">{}</a>'.format(s_url, s_label)
    elif mode == 'tex':
        s_lcl = '\n\href{' + s_url + '}{' + s_label + '}'
    else:
        s_lcl = s_url
    return s_lcl


def hyperlink(s_url, s_label, mode='md'):
    s_lcl = ''
    if mode == 'md':
        s_lcl = '\n[{}]({})'.format(s_label, s_url)
    elif mode == 'html':
        s_lcl = '\n<a href="{}">{}</a>'.format(s_url, s_label)
    elif mode == 'tex':
         s_lcl = '\n\href{' + s_url + '}{' + s_label + '}'
    else:
        s_lcl = s_url
    return s_lcl


def blindtext():
    s_lcl = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce in sem elementum enim molestie cursus vitae' \
            ' in ante. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut ut lorem id augue tristique tempor ' \
            'eget faucibus nibh. Praesent eu lorem vel leo commodo eleifend. Sed orci erat, tempus ullamcorper cursus ' \
            'et, hendrerit at tortor. Vestibulum ornare neque a ipsum porta pulvinar. Morbi gravida consequat sem, ' \
            'viverra ullamcorper sapien convallis quis. Cras magna quam, fermentum at nisl et, tincidunt dignissim orci.' \
            ' Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Orci varius natoque' \
            ' penatibus et magnis dis parturient montes, nascetur ridiculus mus. Sed congue vel arcu id lacinia. '
    return s_lcl


def heading(s, n_level=1, mode='md'):
    """
    heading function
    :param s: string
    :param n_level: int level of heading
    :param mode: string mode code: md, html, tex
    :return:
    """
    s_lcl = ''
    if mode == 'md':
        s_lcl = '\n{} {}'.format('#' * n_level, s)
    elif mode == 'html':
        s_lcl = '\n<h{}>{}</h{}>'.format(n_level, s, n_level)
    elif mode == 'tex':
        if n_level == 1:
            s_aux = ''
        else:
            s_aux = 'sub' * (n_level - 1)
        s_lcl = '\n\{}'.format(s_aux) + 'section{' + '{}'.format(s) + '}'
    else:
        s_lcl = s
    return s_lcl


def paragraph(s, mode='md'):
    s_lcl = ''
    if mode == 'md':
        s_lcl = '\n\n{}\n\n'.format(s)
    elif mode == 'html':
        s_lcl = '\n<p>{}</p>\n'.format(s)
    elif mode == 'tex':
        s_lcl = '\n\par {}\n'.format(s)
    else:
        s_lcl = s
    return s_lcl


def list_item(s, mode='md', s_md_pre=' - '):
    s_lcl = ''
    if mode == 'md':
        s_lcl = '\n{} {}'.format(s_md_pre, s)
    elif mode == 'html':
        s_lcl = '\n<li>{}</li>'.format(s)
    elif mode == 'tex':
        s_lcl = '\n\item {}'.format(s)
    else:
        s_lcl = s
    return s_lcl


def append_unorder_list(lst_items, mode='md'):
    lst_lcl = list()
    if mode == 'md':
        for s in lst_items:
            lst_lcl.append(list_item(s, mode=mode))
            lst_lcl.append('\n')
    elif mode == 'html':
        lst_lcl.append('\n<ul>')
        for s in lst_items:
            lst_lcl.append(list_item(s, mode=mode))
        lst_lcl.append('\n</ul>')
    elif mode == 'tex':
        lst_lcl.append('\n')
        lst_lcl.append(r'\begin{itemize}')
        for s in lst_items:
            lst_lcl.append(list_item(s, mode=mode))
        lst_lcl.append('\n')
        lst_lcl.append(r'\end{itemize}')
    else:
        pass
    return lst_lcl


def append_ordered_list(lst_items, mode='md'):
    lst_lcl = list()
    if mode == 'md':
        n_count = 1
        for s in lst_items:
            lst_lcl.append(list_item(s, mode=mode, s_md_pre='{})'.format(n_count)))
            lst_lcl.append('\n')
            n_count = n_count + 1
    elif mode == 'html':
        lst_lcl.append('\n<ol>')
        for s in lst_items:
            lst_lcl.append(list_item(s, mode=mode))
        lst_lcl.append('\n</ol>')
    elif mode == 'tex':
        lst_lcl.append('\n')
        lst_lcl.append(r'\begin{enumerate}')
        for s in lst_items:
            lst_lcl.append(list_item(s, mode=mode))
        lst_lcl.append('\n')
        lst_lcl.append(r'\end{enumerate}')
    else:
        pass
    return lst_lcl


def append_table(df_table, mode='md', s_caption='', n_id=1):
    lst_lcl = list()
    df_table = df_table.astype(str)
    s_lcl = ''
    if mode == 'md':
        # caption:
        if s_caption == '':
            pass
        else:
            lst_lcl.append('\nTable {}. {}.\n'.format(n_id, s_caption))
        # heading
        lst_lcl.append('\n| {} |'.format(' | '.join(list(df_table.columns))))
        lst_lcl.append('\n| {}'.format(':--- | '*len(df_table.columns)))
        # rows:
        for i in range(len(df_table)):
            lst_lcl.append('\n|{}|'.format(' | '.join(list(df_table.values[i]))))
    elif mode == 'html':
        lst_lcl.append('\n<table>')
        lst_lcl.append('<style> '
                       'table, th, td {  border: 1px solid black;  border-collapse: collapse;}'
                       '</style>')
        if s_caption == '':
            pass
        else:
            lst_lcl.append('\n<caption>Table {}. {}.</caption>'.format(n_id, s_caption))
        # heading
        lst_lcl.append('\n<tr>')
        for i in range(len(df_table.columns)):
            lst_lcl.append('\n<th>{}</th>'.format(df_table.columns[i]))
        lst_lcl.append('\n</tr>')
        # rows
        for i in range(len(df_table)):
            lst_lcl.append('\n<tr>')
            for j in range(len(df_table.values[i])):
                lst_lcl.append('\n<td>{}</td>'.format(df_table.values[i][j]))
            lst_lcl.append('\n</tr>')
        lst_lcl.append('\n</table>')
    elif mode == 'tex':
        lst_lcl.append('')
        lst_lcl.append(r'\begin{table}[h!]')
        lst_lcl.append('\n\centering\n')
        if s_caption == '':
            pass
        else:
            lst_lcl.append('\n\caption{' + s_caption + '}')
        lst_lcl.append(r'\begin{tabular}{|' + ' c ' * len(df_table.columns) + '|} ')
        # heading
        lst_lcl_heads = list()
        for i in range(len(df_table.columns)):
            lst_lcl_heads.append(boldface(s=df_table.columns[i], mode=mode))
        lst_lcl.append('\n\hline\n')
        lst_lcl.append(r'{}\\ '.format(' & '.join(lst_lcl_heads)))
        lst_lcl.append('\n\hline\n')
        # rows
        for i in range(len(df_table)):
            lst_lcl.append(r'{}\\ '.format(' & '.join(list(df_table.values[i]))))
            lst_lcl.append('\n\hline\n')
        lst_lcl.append('\n\end{tabular}')
        lst_lcl.append('\n\label{' + 'table:' + str(n_id) + '}')
        lst_lcl.append('\n\end{table}')
    else:
        lst_lcl = ['ok', 'ok']
    return lst_lcl