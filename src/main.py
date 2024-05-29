
def read_bill():
    pass

def read_gacha():
    pass

def write_bean():
    pass

def generate_bean():
    pass

def main():
    real_bill = read_bill(bill_list:List[Tuple[str,str]]=[("mybill.txt","alipay")])
    gacha_log = read_gacha(uigf_file_path:str)
    generate_bean(real_bill, gacha_log)
    write_bean()

if __name__ == "__main__":
    main()