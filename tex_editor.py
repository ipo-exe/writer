import pandas as pd
import writer

def insert_tables(s_file, s_trigg='% insert table from:'):
    fle = open(s_file, 'r')
    lst_fle = fle.readlines()
    fle.close()
    print(lst_fle)
    lst_new = list()
    for line in lst_fle:
        if s_trigg in line:
            print(line)
            s_table_file = line.split(":")[-1].strip()
            s_label = s_table_file.split('/')[-1].split('.')[0]
            print(s_label)
            print(s_table_file)
            df_lcl = pd.read_csv(s_table_file, sep=';')
            print(df_lcl)
            print(df_lcl.to_string())
            lst_insert = writer.append_table(
                df_table=df_lcl,
                mode='tex',
                s_caption='Table caption',
                s_tex_label=s_label)
            for table_line in lst_insert:
                lst_new.append(table_line)
        else:
            lst_new.append(line)
    fle = open(s_file, 'w')
    fle.writelines(lst_new)
    fle.close()

insert_tables(s_file='./template.tex')
