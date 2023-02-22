import pandas as pd

def extract():

    path_to_file = 'D:/Coding_vacanta_de_vara/vacantadevara/python/etl_01/inputfile.txt'
    with open(path_to_file) as f:
        contents = f.read().split(" ")
    return contents


def transform(my_list):
    transformed_list = []
    for el in my_list:
        if int(el) % 3 == 0:
            transformed_list.append(1)
        else:
            transformed_list.append(0)
    return transformed_list

def load(tr_list):
    
    path_to_file = 'D:/Coding_vacanta_de_vara/vacantadevara/python/etl_01/outputfile.txt'
    """scriem in fisier"""
    df = pd.DataFrame(tr_list)
    # print(df * 100)
    df.to_csv(path_to_file, header=False, index=False, sep='\t', mode='w')
    # with open(path_to_file, 'a') as f:
    #     for el in tr_list:
    #         element = str(el) + "  "
    #         f.write(element)

def main():
    print("Extract ----->\n")
    lst = extract()

    print("Transform ----->\n")
    mglst = transform(lst)
    
    print("Load ----->\n")
    load(mglst)

    print("Done!")


if __name__ == "__main__":
    main()